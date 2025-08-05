import pytest
from pathlib import Path
import os

from pylocc.file_utils import get_all_file_paths

@pytest.fixture
def create_test_files(tmp_path):
    # Create a temporary directory structure for testing
    # tmp_path is a Path object provided by pytest
    test_dir = tmp_path / "test_project"
    test_dir.mkdir()
    (test_dir / "file1.py").touch()
    (test_dir / "file2.txt").touch()
    
    sub_dir = test_dir / "sub_dir"
    sub_dir.mkdir()
    (sub_dir / "file3.py").touch()
    (sub_dir / "file4.log").touch()

    empty_dir = tmp_path / "empty_dir"
    empty_dir.mkdir()

    return str(test_dir), str(empty_dir)

def test_get_all_file_paths_happy_path(create_test_files):
    test_dir, _ = create_test_files
    
    # Test without extension filter
    all_files = list(get_all_file_paths(test_dir))
    assert len(all_files) == 4
    
    expected_files = [
        os.path.join(test_dir, "file1.py"),
        os.path.join(test_dir, "file2.txt"),
        os.path.join(test_dir, "sub_dir", "file3.py"),
        os.path.join(test_dir, "sub_dir", "file4.log")
    ]
    assert sorted([str(p) for p in all_files]) == sorted([str(Path(p).resolve()) for p in expected_files])

def test_get_all_file_paths_with_extension_filter(create_test_files):
    test_dir, _ = create_test_files
    
    # Test with .py extension filter
    py_files = list(get_all_file_paths(test_dir, supported_extensions=["py"]))
    assert len(py_files) == 2
    
    expected_files = [
        os.path.join(test_dir, "file1.py"),
        os.path.join(test_dir, "sub_dir", "file3.py")
    ]
    assert sorted([str(p) for p in py_files]) == sorted([str(Path(p).resolve()) for p in expected_files])

def test_get_all_file_paths_with_multiple_extensions(create_test_files):
    test_dir, _ = create_test_files
    
    # Test with multiple extensions
    filtered_files = list(get_all_file_paths(test_dir, supported_extensions=["py", "txt"]))
    assert len(filtered_files) == 3
    
    expected_files = [
        os.path.join(test_dir, "file1.py"),
        os.path.join(test_dir, "file2.txt"),
        os.path.join(test_dir, "sub_dir", "file3.py")
    ]
    assert sorted([str(p) for p in filtered_files]) == sorted([str(Path(p).resolve()) for p in expected_files])

def test_get_all_file_paths_empty_directory(create_test_files):
    _, empty_dir = create_test_files
    
    # Test with an empty directory
    files = list(get_all_file_paths(empty_dir))
    assert len(files) == 0

def test_get_all_file_paths_nonexistent_path():
    # Test with a path that does not exist
    with pytest.raises(FileNotFoundError):
        list(get_all_file_paths("non_existent_dir"))

def test_get_all_file_paths_with_file_path(create_test_files):
    test_dir, _ = create_test_files
    file_path = os.path.join(test_dir, "file1.py")
    
    # Test with a path that is a file, not a directory
    with pytest.raises(NotADirectoryError):
        list(get_all_file_paths(file_path))

def test_get_all_file_paths_no_matching_extensions(create_test_files):
    test_dir, _ = create_test_files
    
    # Test with extensions that don't match any files
    files = list(get_all_file_paths(test_dir, supported_extensions=["java", "cpp"]))
    assert len(files) == 0
