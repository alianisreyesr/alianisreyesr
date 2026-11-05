# Portfolio Repository Standard

Common baseline for every project repository under [@alianisreyesr](https://github.com/alianisreyesr). It is a target standard: individual repositories may still deviate, and `VERIFICATION_NOTES.md` records what was and was not checked.

## 1. Required files

| File | Requirement |
|---|---|
| `README.md` | Purpose, quick start, architecture, test/CI badges (workflow badges, no hard-coded test counts), synthetic-data boundary, "Portfolio Ecosystem" table linking the other portfolio repos |
| `LICENSE` | MIT, holder `Alianis Reyes-Reyes` (hyphenated, identical in every repo) |
| `SECURITY.md` | Project-specific scope, how to report, supported versions, data-handling rules |
| `CONTRIBUTING.md` | Branching and commit conventions that match how the repo is actually maintained |
| `CHANGELOG.md` | Keep a Changelog format with `[Unreleased]` and one entry per released version; versions must match `pyproject`/app version and git tags |
| `.github/CODEOWNERS` | `* @alianisreyesr` |
| `.github/dependabot.yml` | pip/npm ecosystems used by the repo plus `github-actions` |
| `.github/pull_request_template.md` and `ISSUE_TEMPLATE/` | Specific to the project, not copied from another one |
| `.gitignore` and `.dockerignore` | Exclude virtualenvs, caches (`.mypy_cache`, `.ruff_cache`, `.pytest_cache`), coverage files, local databases and `.env*` (keep `.env.example`) |

## 2. Continuous integration

- Workflow `ci.yml` on push and pull request to `main`, with an explicit least-privilege `permissions:` block (`contents: read` by default).
- `codeql.yml` for static analysis; `secret-scan.yml` (gitleaks) for secret scanning with `fetch-depth: 0` so history is covered.
- Python versions: **3.11 and 3.12** (matrix) for libraries and services; Docker images use a `python:3.11-slim` or `3.12-slim` base. Do not develop on a newer minor than CI runs.
- Lint and typing: `ruff check` and `ruff format --check`, and `mypy`, run in CI as blocking steps (not `continue-on-error`). Configuration lives in `pyproject.toml` (or `ruff.toml`), with an explicit `line-length`.
- Tests: `pytest` with a coverage gate (`--cov-fail-under`, currently 70 as the floor).
- Security checks where the stack allows: `pip-audit`, `bandit`, container scan (Trivy) for repos that publish images.
- Frontends use `npm ci` (never `npm install`) with a committed lockfile.
- One test workflow per repo; avoid overlapping `ci.yml`/`tests.yml`.

## 3. Pinning

- GitHub Actions use a verified major tag. Verify a tag exists before using it:
  `git ls-remote --tags https://github.com/<owner>/<action> | grep -E 'refs/tags/v[0-9]+$'`.
  Current baseline: `actions/checkout@v7`, `actions/setup-python@v7`, `github/codeql-action@v4`, `gitleaks/gitleaks-action@v2`, `actions/upload-artifact@v7`.
- Python dependencies are pinned (`==`) or bounded (`>=,<`) in `requirements.txt`; development tools live in `requirements-dev.txt`; production images must not install test tooling.
- Docker base images are pinned to a minor version tag (digest pinning is a later improvement).
- Dependabot keeps pins current.

## 4. Documentation hygiene

- Do not hard-code test counts, coverage percentages or release versions in prose; use workflow badges or omit the number.
- Version in CHANGELOG, app metadata and README badges must agree.
- Release badges are added only after the matching tag/release exists on GitHub.
- Every public example uses synthetic data; demo credentials are labelled as such.

## 5. Releases

Tags and GitHub Releases are created by the repository owner in the GitHub UI after the CHANGELOG entry is final. Automation and assistants do not create tags or releases.
