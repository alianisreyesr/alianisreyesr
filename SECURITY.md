# Security Policy

This repository is a GitHub profile README and portfolio index. It contains no running service and no user data. Each project repository under [@alianisreyesr](https://github.com/alianisreyesr) maintains its own `SECURITY.md`; where a repository has none, this policy applies.

## Scope

- Portfolio projects use **synthetic data only** and are demonstrations of engineering patterns, not production systems.
- Credentials found in documentation or UI code of the demo projects are demo placeholders. They must never be reused outside a local demo.
- Please do not publish real credentials, tokens, private infrastructure details, or exploitable details of private systems in public issues.

## Reporting a vulnerability

1. Preferred: open a private report through the repository's **Security > Report a vulnerability** tab (GitHub private vulnerability reporting), when enabled.
2. Otherwise, open an issue with sanitized details only and ask for a private channel. Do not include exploit code, secrets, or personal data.

I aim to acknowledge reports within 7 days. These are personal portfolio projects maintained on a best-effort basis, so no formal SLA applies.

## Supported versions

Only the latest commit on `main` of each repository is supported. Tagged releases, if any, are listed in each repository's `CHANGELOG.md`.

## Baseline controls across the portfolio

- Secret scanning in CI (gitleaks) and CodeQL analysis where configured.
- Dependabot for dependency and GitHub Actions updates.
- Synthetic or sanitized sample data only.

See [`docs/PORTFOLIO_REPO_STANDARD.md`](docs/PORTFOLIO_REPO_STANDARD.md) for the common repository standard.
