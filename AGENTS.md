# AGENTS.md
# Guidance for agentic coding assistants working in this repo.

## Quick commands
- Install deps (dev): `uv sync --locked --all-extras --dev`
- Run CLI locally: `uv run pylocc --help`
- Run tests (quiet): `uv run pytest -q`
- Run tests with coverage: `uv run pytest --cov=pylocc -q`
- Build wheel/sdist: `uv run hatchling build`
- Build Windows exe (script): `scripts/build_exe.sh --name pylocc-dev.exe --entry src/pylocc/cli.py`

## Single test workflows
- Single test file: `uv run pytest tests/test_file_utils.py`
- Single test function: `uv run pytest tests/test_file_utils.py::test_get_all_file_paths_happy_path`
- Match by name: `uv run pytest -k "file_utils and extension"`
- Run unittest-based tests (pytest still works): `uv run pytest tests/test_cli.py -k single_file`

## CI parity
- CI uses `uv sync --locked --all-extras --dev`
- CI runs `uv run pytest -q` and `--cov=pylocc` when coverage is collected
- Python versions tested in CI: 3.10, 3.11, 3.12, 3.13

## Lint/format/type checking
- No formatter or linter is configured in the repo.
- Type checking: pyright is configured via `pyrightconfig.json` (optional).
- If you add tooling, document it here and in `pyproject.toml`.

## Code style guidelines (Python)
### Imports
- Group imports in order: standard library, third-party, local.
- Separate groups with a single blank line.
- Prefer explicit imports over wildcard imports.

### Formatting
- 4-space indentation, no tabs.
- Keep lines reasonably short (prefer < 100 chars).
- Use blank lines to separate top-level classes/functions.
- Use double quotes or single quotes consistently within a file.

### Types and data models
- Add type hints for public functions and methods.
- Use `dataclass` for simple data containers (see `ProcessorConfiguration`).
- Use `Enum` for constrained value sets (see `Language`).
- Avoid mutable default arguments; use `None` and create inside.

### Naming conventions
- Modules: `snake_case.py`.
- Classes: `PascalCase`.
- Functions/variables: `snake_case`.
- Constants: `UPPER_CASE`.

### Error handling
- Raise specific exceptions for invalid inputs (see `file_utils.py`).
- Add context to errors when re-raising (use `raise ... from err`).
- Avoid swallowing exceptions unless output is user-facing (CLI).

### I/O and paths
- Prefer `pathlib.Path` for filesystem operations.
- Use explicit `encoding="utf-8"` for file reads/writes.
- For CLI output, use `click.echo` or `rich` tables.

### CLI patterns
- Use Click for argument parsing (`src/pylocc/cli.py`).
- Keep CLI logic thin; push computation into modules.
- Provide helpful errors; skip unsupported file types gracefully.

### Resource packaging
- `src/pylocc/language.json` is bundled via Hatch config.
- Use `importlib.resources` for package data.

## Tests
- Tests live in `tests/` and mirror module names.
- Mixed `pytest` and `unittest` styles are used; prefer pytest for new tests.
- Use fixtures for shared setup.
- Avoid slow filesystem operations unless needed.

## Generated files
- `src/pylocc/language.py` is auto-generated. Do not edit manually.
- If language data changes, update the generator or source JSON.

## Repository layout
- CLI entrypoint: `src/pylocc/cli.py`
- Core logic: `src/pylocc/processor.py`
- Reporting: `src/pylocc/reporter.py`
- File utilities: `src/pylocc/file_utils.py`
- Tests: `tests/`

## Build and release notes
- Hatch is used as the build backend (see `pyproject.toml`).
- Executable build script: `scripts/build_exe.sh`.
- CI workflows are in `.github/workflows/`.

## Cursor/Copilot rules
- No `.cursor/rules/`, `.cursorrules`, or `.github/copilot-instructions.md` found.

## When making changes
- Keep changes minimal and consistent with existing patterns.
- Update or add tests when touching logic.
- If you add new commands/tools, document them here.
