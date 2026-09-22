# Contributing

## Workflow

1. Start from an issue with acceptance criteria.
2. Use a short-lived branch:
   - `feature/<issue>-name`
   - `fix/<issue>-name`
   - `docs/<issue>-name`
   - `security/<issue>-name`
3. Keep changes focused.
4. Add/update tests for behavior changes.
5. Open a pull request and link the issue.
6. Merge only after required checks pass.

## Engineering standards

- Prefer explainable deterministic detections over opaque behavior.
- Keep parsers and rules independently testable.
- Validate untrusted input.
- Never commit secrets or sensitive real-world logs.
- Use synthetic fixtures.
- Keep raw and normalized events distinguishable.
- AI explanations must not overwrite or fabricate evidence.
- Architecture diagrams must be Mermaid source with styles/colors.

## Commit style

Prefer Conventional Commit-style messages, for example:

- `feat: add SSH auth parser`
- `fix: prevent duplicate threat creation`
- `test: add brute-force rule fixtures`
- `docs: document risk scoring`
- `security: validate uploaded log size`

## Pull requests

A good PR explains:
- What changed
- Why it changed
- How it was tested
- Security impact
- Documentation impact
