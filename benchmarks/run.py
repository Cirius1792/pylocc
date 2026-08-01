#!/usr/bin/env python3
"""CLI benchmark tool for pylocc.

Usage:
    python benchmarks/run.py [--config path]
"""
import argparse
import datetime
import json
import statistics
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

_DEFAULT_CONFIG = Path(__file__).parent / "scenarios.yaml"


@dataclass(frozen=True)
class Config:
    runs: int
    scenarios: list[dict[str, str]] = field(default_factory=list)


def _validate_scenario(raw: dict[str, Any]) -> None:
    """Validate a single scenario entry. Exits on missing fields."""
    if "name" not in raw or not isinstance(raw["name"], str) or not raw["name"].strip():
        print(f"Error: scenario is missing valid 'name' field", file=sys.stderr)
        sys.exit(1)
    if "repo_url" not in raw or not isinstance(raw["repo_url"], str) or not raw["repo_url"].strip():
        print("Error: scenario is missing valid 'repo_url' field", file=sys.stderr)
        sys.exit(1)


def _load_config(path: Path) -> Config:
    """Load and validate benchmark config from YAML file."""
    if not path.exists():
        print(f"Error: config file not found: {path}", file=sys.stderr)
        sys.exit(1)

    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    runs = raw.get("runs", 0)
    if not isinstance(runs, int) or runs < 2:
        print("Error: 'runs' must be an integer >= 2", file=sys.stderr)
        sys.exit(1)

    scenarios_raw = raw.get("scenarios")
    if not isinstance(scenarios_raw, list):
        print("Error: 'scenarios' key is required and must be a list", file=sys.stderr)
        sys.exit(1)

    validated: list[dict[str, str]] = []
    for item in scenarios_raw:
        _validate_scenario(item)
        validated.append({"name": item["name"], "repo_url": item["repo_url"]})

    return Config(runs=runs, scenarios=validated)


def _clone_repo(repo_url: str, dest: Path) -> None:
    """Shallow-clone a repository into dest directory."""
    try:
        result = subprocess.run(
            ["git", "clone", "--depth=1", repo_url, str(dest)],
            capture_output=True, text=True, timeout=120, check=False
        )
        if result.returncode != 0:
            print(f"Error: git clone failed for {repo_url}: {result.stderr.strip()}", file=sys.stderr)
            sys.exit(1)
    except subprocess.TimeoutExpired:
        print(f"Error: git clone timed out for {repo_url}", file=sys.stderr)
        sys.exit(1)


def _count_files(dir_path: Path) -> int:
    """Count how many files pylocc would scan in a directory.

    Loads the same language.json config that pylocc uses to determine
    supported extensions, then walks the directory counting matches.
    """
    lang_json = Path(__file__).parent.parent / "src" / "pylocc" / "language.json"
    if not lang_json.exists():
        print("Warning: cannot find pylocc language.json, using common extensions", file=sys.stderr)
        return 0

    with open(lang_json, encoding="utf-8") as f:
        configs = json.load(f)

    supported_exts = set()
    for lang_name, lang_info in configs.items():
        for ext in lang_info.get("extensions", []):
            supported_exts.add(ext.lower())

    count = 0
    for entry in dir_path.rglob("*"):
        if entry.is_file():
            fname = entry.name
            ext = fname.rsplit(".", 1)[-1].lower() if "." in fname else ""
            if ext in supported_exts:
                count += 1
    return count


@dataclass
class BenchmarkResult:
    scenario_name: str
    files_scanned: int = 0
    timings: list[float] = field(default_factory=list)


def _run_benchmark(dir_path: Path) -> float:
    """Run pylocc on dir_path and return wall-clock elapsed seconds."""
    start = time.perf_counter()
    try:
        result = subprocess.run(
            ["pylocc", str(dir_path)],
            capture_output=True, text=True, timeout=300, check=False
        )
    except FileNotFoundError:
        print("Error: pylocc binary not found in PATH", file=sys.stderr)
        sys.exit(1)
    elapsed = time.perf_counter() - start

    if result.returncode != 0:
        print(f"Error: pylocc returned {result.returncode}: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)

    return elapsed


def _compute_stats(timings: list[float]) -> tuple[float, float, float, float]:
    """Compute (median, stddev, min, max) for a list of timing values.

    Uses population standard deviation for deterministic results across runs.
    Single value returns 0.0 stddev.
    """
    if len(timings) == 1:
        return (timings[0], 0.0, timings[0], timings[0])

    mn = min(timings)
    mx = max(timings)

    median_val = float(statistics.median(timings))
    sd_val = float(statistics.pstdev(timings))

    return (median_val, sd_val, mn, mx)


def _interleave_and_run(config: Config, repos: dict[str, tuple[Path, int]]) -> dict[str, BenchmarkResult]:
    """Run benchmarks interleaved across scenarios to avoid cache bias.

    For N runs and K scenarios: A B C ... A B C ... (N*K total invocations).
    Returns a mapping of scenario_name -> BenchmarkResult with timings populated.
    """
    names = [s["name"] for s in config.scenarios]
    results: dict[str, BenchmarkResult] = {name: BenchmarkResult(scenario_name=name) for name in names}

    for run_num in range(config.runs):
        print(f"  Run {run_num + 1}/{config.runs}: ", end="", flush=True)
        for idx, name in enumerate(names):
            repo_dir = repos[name][0]
            timing = _run_benchmark(repo_dir)
            results[name].timings.append(timing)
            label = names[idx] if len(names) > 1 else f"A"
            print(f"{label}={timing:.3f}s ", end="", flush=True)
        print()

    return results


def _generate_report(results: dict[str, BenchmarkResult], runs: int) -> str:
    """Generate a Markdown table report with benchmark stats."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = []
    lines.append(f"# pylocc Benchmark — {now}")
    lines.append("")
    lines.append(f"Runs: {runs} | Date: {now}")
    lines.append("")
    lines.append("| Scenario   | Files Scanned | Median (s) | Stddev (s) | Min (s) | Max (s) |")
    lines.append("|------------|--------------|-----------|----------|--------|--------|")

    for name, result in results.items():
        median_val, sd_val, mn, mx = _compute_stats(result.timings)
        lines.append(
            f"| {result.scenario_name:<10} | {result.files_scanned:>12} "
            f"| {median_val:>9.4f} | {sd_val:>8.4f} | {mn:>6.4f} | {mx:>6.4f} |"
        )

    lines.append("")
    lines.append("*Wall-clock via time.perf_counter(). Scenarios interleaved across runs.*")
    return "\n".join(lines) + "\n"


def main() -> None:
    """CLI entrypoint for the benchmark tool."""
    parser = argparse.ArgumentParser(description="Benchmark pylocc performance against predefined repositories.")
    parser.add_argument("--config", type=Path, default=_DEFAULT_CONFIG, help="Path to scenarios YAML config")
    args = parser.parse_args()

    # 1. Load and validate config
    print(f"Loading config from {args.config}")
    config = _load_config(args.config)
    print(f"Scenario count: {len(config.scenarios)}, Runs per scenario: {config.runs}")

    # 2-3. Clone repos and count files
    with tempfile.TemporaryDirectory() as tmpdir:
        base_tmp = Path(tmpdir)
        repos: dict[str, tuple[Path, int]] = {}

        for scenario in config.scenarios:
            name = scenario["name"]
            repo_dir = base_tmp / f"bench_{name}"
            print(f"\nCloning {scenario['repo_url']} -> {repo_dir}")
            _clone_repo(scenario["repo_url"], repo_dir)
            file_count = _count_files(repo_dir)
            print(f"  Supported files: {file_count}")
            repos[name] = (repo_dir, file_count)

        # 4-5. Interleaved benchmark runs
        print("\nRunning benchmarks:")
        timed_results = _interleave_and_run(config, repos)

        # Merge file counts into interleaved results
        for name, (repo_dir, file_count) in repos.items():
            timed_results[name].files_scanned = file_count

        # 6. Generate report
        report_md = _generate_report(timed_results, config.runs)
        print("\n" + report_md)

        # 7. Write report to file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        results_dir = Path(__file__).parent / "results"
        results_dir.mkdir(exist_ok=True)
        report_path = results_dir / f"report_{timestamp}.md"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report_md)
        print(f"\nReport saved to {report_path}")


if __name__ == "__main__":
    main()
