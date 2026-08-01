#!/usr/bin/env python3
"""CLI benchmark tool for pylocc.

Usage:
    python benchmarks/run.py [--config path]
"""
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
