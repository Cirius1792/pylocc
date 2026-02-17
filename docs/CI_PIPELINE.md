# CI/CD Pipeline Overview

This document explains how the GitHub Actions workflows in this repo fit together and how releases are triggered.

## Workflow inventory

- `tests.yml`: Runs the core test workflow on push/PR to `main` and generates the coverage badge.
- `test-workflow.yml`: Reusable test workflow (matrix across Python 3.10–3.13).
- `release.yml`: Publishes to PyPI, tags a release, builds the Windows exe, and creates a GitHub Release.
- `build_exe.yml`: Reusable workflow to build the Windows executable and upload it as an artifact.
- `deploy-docs.yml`: Builds and deploys Docusaurus docs to GitHub Pages on release publish.

## Tests and coverage badge

### `tests.yml` (entrypoint)

Triggers:
- `push` to `main`
- `pull_request` targeting `main`

Jobs:
- `test`: Reuses `test-workflow.yml`.
- `generate-badge`: Downloads coverage artifact, runs `coverage-badge`, and commits `coverage.svg` to the repo.

Notes:
- Coverage data is only uploaded from Python 3.13 in the reusable workflow.
- The badge update commit is `docs: update coverage badge` and writes `coverage.svg`.

### `test-workflow.yml` (reusable)

Inputs:
- `collect-coverage` (boolean, default true)
- `checkout-ref` (string, optional)

Steps:
1. Checkout requested ref.
2. Set up Python (matrix: 3.10, 3.11, 3.12, 3.13).
3. Install `uv`.
4. Install deps: `uv sync --locked --all-extras --dev`.
5. Run tests:
   - With coverage: `uv run pytest --cov=pylocc -q`
   - Without coverage: `uv run pytest -q`
6. Upload `.coverage` artifact only for Python 3.13 when `collect-coverage=true`.

## Release pipeline

### `release.yml` (Publish to PyPI)

Triggers:
- Manual: `workflow_dispatch` with input `logLevel` (major/minor/patch)
- Automatic: `workflow_run` after `Tests` workflow completes on `main`

High-level flow:
1. **check-release**
   - Resolves the commit SHA to release (either the workflow dispatch SHA or the tests workflow head SHA).
   - Reads the commit message.
   - Determines whether to release:
     - Manual dispatch: always releases using `logLevel`.
     - Automatic: only releases if the commit message matches `RELEASE - (major|minor|patch)`.
   - Outputs: `should-release`, `version-type`, `commit-sha`, `commit-message`.

2. **smoke-test** (gated by `should-release=true`)
   - Checks out the exact commit SHA.
   - Builds sdist/wheel with `uv build`.
   - Creates a venv and imports key modules from the wheel.
   - Repeats import test for the sdist.

3. **build-executable** (gated by `should-release=true`)
   - Reuses `build_exe.yml` to build a Windows executable and upload it as an artifact.

4. **publish** (gated by `should-release=true`)
   - Checks out the exact commit SHA.
   - Bumps version using `uv version --bump <type>`.
   - Commits version bump to `main` with message `Bump version to X.Y.Z [skip ci]`.
   - Tags `vX.Y.Z` and pushes the tag.
   - Builds package via `uv build`.
   - Publishes to PyPI using trusted publishing (`uv publish --trusted-publishing always`).
   - Downloads the Windows exe artifact from `build-executable`.
   - Creates a GitHub Release and uploads the exe zip as a release asset.

### Release trigger details

Automatic release (from tests):
- Push to `main` triggers `tests.yml`.
- `release.yml` listens to the completed `Tests` workflow.
- Release only proceeds if the triggering commit message starts with:
  - `RELEASE - patch`
  - `RELEASE - minor`
  - `RELEASE - major`

Manual release:
- Run `release.yml` from the GitHub Actions UI and choose the bump type.
- It will always proceed, using that selection.

## Windows executable build

### `build_exe.yml` (reusable)

Inputs:
- `source_ref`: ref/sha to build from

Flow:
1. **prepare** job resolves version and filenames (uses `uv tree` to read project version).
2. **tests** job reuses `test-workflow.yml` with coverage disabled.
3. **build-executable** job:
   - Runs on `windows-latest`.
   - Installs Python 3.11 and `uv`.
   - Runs `scripts/build_exe.sh` with a generated exe name.
   - Smoke tests the exe with `--help`.
   - Zips the exe and uploads it as an artifact.

## Docs deployment

### `deploy-docs.yml` (Docusaurus)

Triggers:
- `release` published
- manual `workflow_dispatch`

Flow:
1. Checkout source.
2. Install Node 18 and docs dependencies (`npm install` in `docs/`).
3. Set up Python and run `python generate_language_docs.py`.
4. Commit the generated `docs/docs/supported-languages.md`.
5. Build Docusaurus and deploy `docs/build` to GitHub Pages.

## Operational notes

- The release pipeline mutates `main` by committing the version bump.
- Coverage badge updates also commit to `main`.
- Trusted publishing assumes PyPI is configured for OIDC in the `pypi` environment.
- The Windows exe artifact name/zip filename are generated in `build_exe.yml` and passed through to release assets.

## Troubleshooting checklist

- Release didn’t run automatically:
  - Confirm the commit message uses `RELEASE - patch|minor|major`.
  - Ensure the `Tests` workflow succeeded on `main`.
- Publish failed:
  - Check the `pypi` environment permissions and OIDC configuration.
  - Verify `uv publish --trusted-publishing always` logs.
- Docs didn’t update:
  - Ensure a GitHub Release was published (not just tagged).
  - Check `generate_language_docs.py` output.
