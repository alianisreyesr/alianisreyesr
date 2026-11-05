# Verification Notes

Scope: portfolio consistency pass (medium and low priority items) across the profile repo and the 10 project repos. Date: 2026-11-05.

## Verified

- Action tags exist upstream (checked with `git ls-remote --tags`): `actions/checkout` v7, `actions/setup-python` v7, `github/codeql-action` v4, `actions/upload-artifact` v7, `gitleaks/gitleaks-action` v2 (and v2.3.9).
- All 11 local clones were on `main` and up to date with `origin/main` before changes.
- Workflow YAML added or edited in the profile repo parses correctly.
- `LICENSE` holder is now `Alianis Reyes-Reyes` in all 11 repos (profile gained a new LICENSE).
- The profile `SECURITY.md`, `docs/GITHUB_PROJECT_STRUCTURE.md` and pull request template no longer contain AI Security Analyst-specific content.
- The "Portfolio Ecosystem" tables in the project READMEs link all 10 projects (excluding the repo itself) and contain no hard-coded test counts.

## Not verified

- The new `secret-scan.yml` workflows have not run on GitHub; the first run on `main` will confirm they pass. gitleaks may flag the documented demo credentials (for example in `csv-evidence-tracker/frontend/src/pages/LoginPage.jsx`); if so, add a `.gitleaks.toml` allowlist or an inline `gitleaks:allow` comment rather than removing the finding silently.
- `gitleaks-action` is free for personal-account repositories; it needs a `GITLEAKS_LICENSE` secret if a repo is moved to an organization.
- Test suites, ruff, mypy and Docker builds were not run for this pass (documentation, licence and workflow-file changes only).
- Whether `.dockerignore` additions break any Docker build was not tested; they only exclude VCS, caches, virtualenvs, local databases and env files.
- GitHub-side settings (topics, private vulnerability reporting, branch protection, Pages, demos) cannot be seen from a local clone.

## Pending for the repository owner

- **Tags and GitHub Releases are not created.** No repository has git tags locally, and README release badges (for example `release-v1.0.0`) and CHANGELOG `[1.0.0]` entries cannot be confirmed. The owner should create tags and releases in GitHub for each repository (or remove the badges), then keep CHANGELOG, app version and tags aligned.
- `csv-evidence-tracker` and `quality-deviation-risk-monitor` have only `[Unreleased]` in their CHANGELOG; decide on a version to cut.
- Screenshots, GIFs and hosted demo URLs are still missing from most READMEs.
- The graduation date shown in the profile README (December 2026) should be re-checked against the current plan.
- Items outside this pass (identity attribution, default secrets, root containers, functional defects) are tracked in the main improvement report.
