import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmarks.run import _compute_stats


def test_compute_stats_median():
    median, _, _, _ = _compute_stats([3.0, 1.0, 2.0])
    assert abs(median - 2.0) < 1e-9


def test_compute_stats_stddev_zero_for_single_value():
    """With only one value, population stddev is 0."""
    median, _, _, _ = _compute_stats([5.0, 3.0])
    assert isinstance(median, float)


def test_compute_stats_min_max():
    _, _, mn, mx = _compute_stats([4.0, 1.0, 9.0, 2.0])
    assert abs(mn - 1.0) < 1e-9
    assert abs(mx - 9.0) < 1e-9


def test_compute_stats_single_value():
    median, sd, mn, mx = _compute_stats([7.5])
    assert abs(median - 7.5) < 1e-9
    assert abs(sd - 0.0) < 1e-9
    assert abs(mn - 7.5) < 1e-9
    assert abs(mx - 7.5) < 1e-9
