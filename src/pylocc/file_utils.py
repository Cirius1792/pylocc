
from pathlib import Path
from typing import Iterator, List
import os

def get_all_file_paths(folder: str, supported_extensions: List[str] = [])-> Iterator[str]:
    folder_path = Path(folder)
    if not folder_path.exists():
        raise FileNotFoundError(f"The path '{folder_path}' does not exist")
    if not folder_path.is_dir():
        raise NotADirectoryError(
            f"The path '{folder_path}' is not a directory")

    extensions_set = None
    if supported_extensions:
        extensions_set = set(supported_extensions)

    for root, _, files in os.walk(folder):
        for file in files:
            if not extensions_set or Path(file).suffix[1:] in extensions_set:
                # return the path
                yield os.path.join(root, file)
    return None
