#!/usr/bin/env python3
"""CLI benchmark tool for pylocc.

Usage:
    python benchmarks/run.py [--config path]
"""
import argparse
import datetime
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


def _validate_scenario(raw: Any) -> None:
    """Validate a single scenario entry. Exits on missing/invalid fields."""
    if not isinstance(raw, dict):
        print(f"Error: each scenario must be a mapping, got: {raw!r}", file=sys.stderr)
        sys.exit(1)
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

    Reuses pylocc's own language config and file enumeration so the count
    exactly matches what the pylocc CLI will scan.
    """
    try:
        from pylocc.file_utils import get_all_file_paths
        from pylocc.processor import load_default_language_config
    except ImportError as err:
        print("Error: pylocc is not importable; install it first (e.g. `uv sync --locked --all-extras --dev`)",
              file=sys.stderr)
        sys.exit(1)

    configs = load_default_language_config()
    supported_extensions = [
        ext for config in configs for ext in config.file_extensions
    ]
    return sum(1 for _ in get_all_file_paths(str(dir_path), supported_extensions=supported_extensions))


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
