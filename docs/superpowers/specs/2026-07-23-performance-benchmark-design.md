# Performance Benchmark Design

## Overview

CLI benchmark tool that measures pylocc execution time against predefined repositories and produces a timestamped Markdown report with median and standard deviation statistics.

Local-first design; CI integration is out of scope (future).

## Structure

```
benchmarks/
├── run.py              # entrypoint: python benchmarks/run.py [--config path]
└── scenarios.yaml      # config file
```

Lives outside `src/pylocc/` and is excluded from the published package via hatch build exclusions.

**Dependencies**: stdlib + PyYAML (dev-only dep). No extra runtime dependencies for pylocc itself.

## Configuration

File: `benchmarks/scenarios.yaml`

```yaml
runs: 5                    # global iterations per scenario; must be >= 2

scenarios:
  - name: "pylocc-repo"
    repo_url: "https://github.com/Cirius1792/pylocc.git"

  - name: "redis-repo"
    repo_url: "https://github.com/redis/redis.git"
```

Each scenario has exactly two fields: a human-readable name and a git clone URL.

**Default config path**: `benchmarks/scenarios.yaml`. Overrideable via `--config` flag.

## Execution Flow

1. Load and validate config (fail if runs < 2)
2. For each scenario, shallow-clone the repo (`git --depth=1`) into a fresh temp directory
3. Count how many supported files pylocc will scan in each cloned repo
4. Interleave benchmark runs across scenarios — for N runs and K scenarios, execute `A B C A B C ...` to avoid cache bias (first run cold, subsequent warm affects all equally)
5. For each invocation, measure wall-clock time via `time.perf_counter()` around a subprocess call to the local pylocc CLI
6. Per scenario: compute median and standard deviation of timings
7. Write timestamped Markdown report to `benchmarks/results/report_<YYYY-MM-DD_HH-mm-ss>.md`
8. Clean up all temp directories (via `tempfile.TemporaryDirectory()`)

### Interleaved run example

With scenarios [A, B] and runs=3: A → B → A → B → A (5 invocations total)

## Metric

**Wall-clock time only**, measured with `time.perf_counter()` around the subprocess call. Single number, no parsing external tool output.

## Error Handling — Fail Fast

- Git clone fails → exit immediately with stderr message
- pylocc binary not in PATH or invocation fails → exit immediately
- Config validation fails (missing fields, runs < 2) → exit on startup

No fallbacks. If a prerequisite is missing the run stops.

## Report Format

```markdown
# pylocc Benchmark — YYYY-MM-DD HH:MM

Runs: 3 | Date: ...

| Scenario   | Files Scanned | Median (s) | Stddev (s) | Min (s) | Max (s) |
|------------|--------------|-----------|----------|--------|--------|
| pylocc-rep |      N       |    m      |     s    |    x   |    y   |
*Wall-clock via time.perf_counter(). Scenarios interleaved across runs.*
```

Written to `benchmarks/results/report_<YYYY-MM-DD_HH-mm-ss>.md`.
