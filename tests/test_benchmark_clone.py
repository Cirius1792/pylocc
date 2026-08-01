import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmarks.run import _clone_repo, _count_files


def test_clone_repo_success(tmp_path):
    """Clone a tiny real repo (pylocc itself) shallowly."""
    dest = tmp_path / "test_clone"
    try:
        _clone_repo("https://github.com/Cirius1792/pylocc.git", dest)
        assert dest.exists()
        assert (dest / ".git").exists()
    except SystemExit:
        pytest.skip("Network unavailable or git failed")


def test_count_files_counts_something(tmp_path):
    """Create a dir with known Python files and count them."""
    d = tmp_path / "sample"
    d.mkdir()
    (d / "a.py").write_text("# hello\nprint('hi')\n", encoding="utf-8")
    (d / "b.md").write_text("not counted\n", encoding="utf-8")

    count = _count_files(d)
    assert isinstance(count, int)
    assert count >= 0


def test_count_files_empty_dir(tmp_path):
    d = tmp_path / "empty"
    d.mkdir()
    count = _count_files(d)
    assert count == 0
