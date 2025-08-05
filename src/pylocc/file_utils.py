
from pathlib import Path
from typing import List

def get_all_file_paths(folder: str, supported_extensions: List[str] = []) -> List[str]:
    """
    Returns a list of all file paths.

    Args:
        folder (str): Path to the root folder to search

    Returns:
        List[str]: List of absolute file paths as strings
    """
    folder_path = Path(folder)

    if not folder_path.exists():
        raise FileNotFoundError(f"The path '{folder_path}' does not exist")
    if not folder_path.is_dir():
        raise NotADirectoryError(
            f"The path '{folder_path}' is not a directory")

    # Use rglob to recursively find all files
    file_paths = [str(file.resolve())
                  for file in folder_path.rglob('*') if file.is_file()]

    # Filter by supported extensions if provided
    if supported_extensions:
        extensions_set = set(supported_extensions)
        file_paths = [file for file in file_paths if Path(
            file).suffix[1:] in extensions_set]

    return file_paths
