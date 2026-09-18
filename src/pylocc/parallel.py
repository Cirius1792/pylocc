"""Process pool for counting lines of code across files in parallel.

Counting is CPU + I/O bound and files are independent, so a process pool
(avoiding the GIL) gives a near-linear speedup on large trees. The pool is
only worthwhile above a modest number of files because of process startup
cost, so the CLI decides when to use it.
"""
import os
from concurrent.futures import ProcessPoolExecutor
from typing import Dict, List, Optional, Tuple

from pylocc.processor import ProcessorConfiguration, Report

# Below this many files the pool's process startup cost exceeds the savings.
POOL_MIN_FILES = 512

# Cap the auto worker count; beyond ~8 cores the measured speedup plateaus
# and extra processes only add scheduling overhead.
MAX_AUTO_WORKERS = 8


def _init_worker(ext_to_config: Dict[str, ProcessorConfiguration]):
    """Process pool initializer: hand each worker the extension -> config map once."""
    global _EXT_TO_CONFIG
    _EXT_TO_CONFIG = ext_to_config


_EXT_TO_CONFIG: Dict[str, ProcessorConfiguration] = {}


def _count_one_file(item: Tuple[str, str]) -> Optional[Tuple[str, object]]:
    """Worker: count one file. Returns (path, Report), (path, error_message), or None
    when the extension has no configuration."""
    path, ext = item
    config = _EXT_TO_CONFIG.get(ext)
    if config is None:
        return None
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore', buffering=8192) as f_handle:
            return (path, count_locs_for_config(f_handle, config))
    except Exception as err:  # noqa: BLE001 - worker must not kill the pool
        return (path, str(err))


def count_locs_for_config(f_handle, config: ProcessorConfiguration) -> Report:
    """Indirection so the worker can be patched in tests without touching processor."""
    from pylocc.processor import count_locs
    return count_locs(f_handle, file_configuration=config)


def count_files_parallel(files: List[str],
                         ext_to_config: Dict[str, ProcessorConfiguration],
                         workers: int) -> Tuple[Dict[str, Report], List[Tuple[str, str]]]:
    """Count files in a process pool.

    Returns (per_file_reports in the original ``files`` order, errors) where
    ``errors`` is a list of (path, message) for files that could not be processed.
    """
    items = [(f, os.path.splitext(f)[1][1:]) for f in files]
    with ProcessPoolExecutor(max_workers=workers,
                             initializer=_init_worker,
                             initargs=(ext_to_config,)) as executor:
        results = list(executor.map(_count_one_file, items, chunksize=64))

    per_file_reports: Dict[str, Report] = {}
    errors: List[Tuple[str, str]] = []
    for result in results:
        if result is None:
            continue
        path, value = result
        if isinstance(value, str):
            errors.append((path, value))
        else:
            per_file_reports[path] = value
    # Preserve the original file order so output is deterministic.
    ordered = {f: per_file_reports[f] for f in files if f in per_file_reports}
    return ordered, errors


def suggested_worker_count() -> int:
    """A sensible default worker count for the current machine."""
    cpu = os.cpu_count() or 1
    return max(1, min(cpu, MAX_AUTO_WORKERS))


def should_use_pool(files_count: int, jobs: Optional[int]) -> bool:
    """Decide whether a process pool is worthwhile.

    ``jobs`` of 1 forces sequential; an explicit value > 1 forces the pool
    (the user asked for it); None (auto) uses the pool only when the tree is
    large enough to amortize process startup.
    """
    if jobs is None:
        return files_count >= POOL_MIN_FILES
    return jobs > 1
