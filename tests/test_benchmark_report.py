import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmarks.run import _generate_report, BenchmarkResult


def test_generate_report_produces_table():
    results = {
        "pylocc-repo": BenchmarkResult(
            scenario_name="pylocc-repo",
            files_scanned=42,
            timings=[1.5, 1.3, 1.6]
        ),
        "redis-repo": BenchmarkResult(
            scenario_name="redis-repo",
            files_scanned=7890,
            timings=[12.1, 11.8, 12.0]
        )
    }

    markdown = _generate_report(results, runs=3)
    assert "pylocc Benchmark" in markdown
    assert "pylocc-repo" in markdown
    assert "redis-repo" in markdown
    assert "42" in markdown
    assert "7890" in markdown


def test_generate_report_single_scenario():
    results = {
        "solo": BenchmarkResult(
            scenario_name="solo",
            files_scanned=10,
            timings=[5.0]
        )
    }
    md = _generate_report(results, runs=1)
    assert "solo" in md
    assert "0.00" in md


def test_generate_report_wall_clock_footer():
    results = {
        "a": BenchmarkResult(scenario_name="a", files_scanned=5, timings=[1.0, 2.0])
    }
    md = _generate_report(results, runs=2)
    assert "Wall-clock via time.perf_counter()" in md
    assert "interleaved" in md
