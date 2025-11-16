#!/usr/bin/bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: build_executable.sh --name <exe-name> --entry <script-path> [extra PyInstaller args]

Options:
  --name <exe-name>     Name to use for the generated executable (required).
  --entry <script-path> Python entry-point script to package (required).
  --help                Show this help message and exit.

Any additional arguments (including flags such as --upx-dir) are passed
verbatim to PyInstaller after the required options.
EOF
}

exe_name=""
entry_path=""
extra_args=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --help|-h)
      usage
      exit 0
      ;;
    --name)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for --name" >&2
        usage
        exit 1
      fi
      exe_name="$2"
      shift 2
      ;;
    --entry)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for --entry" >&2
        usage
        exit 1
      fi
      entry_path="$2"
      shift 2
      ;;
    --)
      shift
      while [[ $# -gt 0 ]]; do
        extra_args+=("$1")
        shift
      done
      ;;
    *)
      extra_args+=("$1")
      shift
      ;;
  esac

done

if [[ -z "$exe_name" || -z "$entry_path" ]]; then
  echo "Both --name and --entry options are required." >&2
  usage
  exit 1
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
cd "$repo_root"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv command not found. Please install uv before running this script." >&2
  exit 1
fi

if [[ ! -f "$entry_path" ]]; then
  echo "Entry script not found: $entry_path" >&2
  exit 1
fi

printf 'Packaging %s from %s\n' "$exe_name" "$entry_path"

cmd=(
  uv
  run
  pyinstaller
  --onefile
  --name
  "$exe_name"
)

if [[ "${OSTYPE:-}" == msys* || "${OSTYPE:-}" == cygwin* || "${OS:-}" == "Windows_NT" ]]; then
  data_sep=';'
else
  data_sep=':'
fi
cmd+=(
  --add-data
  "src/pylocc/language.json${data_sep}pylocc"
)

cmd+=("${extra_args[@]}")
cmd+=("$entry_path")

"${cmd[@]}"

