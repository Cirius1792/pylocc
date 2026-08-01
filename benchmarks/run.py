#!/usr/bin/env python3
"""CLI benchmark tool for pylocc.

Usage:
    python benchmarks/run.py [--config path]
"""
import json
import subprocess
import sys
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
