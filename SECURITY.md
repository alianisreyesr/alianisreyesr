# Security Policy

## Scope

AI Security Analyst processes untrusted security telemetry, uploaded files, network identifiers, and AI-generated analysis. Security issues should be treated as first-class engineering work.

## Supported versions

Before v1.0, only the current development branch is supported.

## Reporting

Do not publish real credentials, API keys, tokens, private infrastructure details, sensitive production logs, or exploitable private-system information in public issues.

For ordinary bugs, use the Bug Report template with sanitized evidence.

## Data handling rules

- Use synthetic or sanitized sample logs in the repository.
- Never commit secrets.
- Treat uploaded log content as untrusted input.
- Treat LLM output as untrusted and non-authoritative.
- Deterministic evidence and detection logic remain the source of truth.
- Human approval is required before any future blocking/enforcement action.
- Avoid storing unnecessary sensitive data.

## AI-specific security

The project should defend against:
- Prompt injection embedded in log content
- Unsupported or hallucinated threat claims
- AI output being mistaken for deterministic evidence
- Leakage of secrets into model prompts
- Unbounded input sizes or resource usage

## Dependency security

Dependencies should be pinned or constrained appropriately and checked with automated dependency/security scanning before v1.0.
