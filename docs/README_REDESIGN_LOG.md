# README redesign log — 2026-09-19

## Why

The profile README had accumulated a rich visual design over many iterations (badges, animated SVGs, a live GitHub stats card, project cards) that made the profile stand out. On 2026-09-13, commit `54209a9` ("docs: focus profile on three flagship projects") stripped ~90% of that visual layer in a single pass to produce a minimal, text-only README — cutting the file from 296 to 48 lines. This was a legitimate attempt to sharpen the narrative, but it went further than intended: it also orphaned working automation and quietly dropped a third of the public repos from the profile.

## Audit findings (before the fix)

- **Orphaned visual assets** — `assets/career-flow.svg`, `assets/architecture-pattern.svg`, `assets/section-divider.svg`, and `assets/stats-card.svg` all still existed in the repo but were referenced nowhere in the README.
- **Wasted CI** — `.github/workflows/update-stats-card.yml` was still running every Monday, regenerating `assets/stats-card.svg` from the live GitHub API and committing it, even though nothing displayed that image anymore.
- **Repos dropped from the profile** — `csa-assurance-planner`, `data-integrity-case-file`, and `retail-operations-data-platform` (3 of 8 public repos) had no link anywhere in the simplified README, making them undiscoverable from the profile.
- **Dropped content with no replacement** — the "Recent hardening" section (concrete bug-fix evidence per repo) and the "Validation & assurance principles" 4-pillar table were removed entirely, not folded into the new copy.
- **Stale/unverifiable metrics** — earlier versions claimed "300+ tests" and "6+ flagship systems" without a way to re-derive those numbers from what's actually in the repo.

## What changed ([PR #6](https://github.com/alianisreyesr/alianisreyesr/pull/6), merged 2026-09-19)

Rebuilt `README.md` by merging the pre-simplification visual system with the sharper post-simplification positioning and copy:

- Restored the badge row (LinkedIn / Repositories / Portfolio), status badges, and a quick-nav line matching the real section headers.
- Re-embedded `career-flow.svg`, `architecture-pattern.svg`, `section-divider.svg`, and the live `stats-card.svg` — the weekly-refresh Action is no longer wasted work.
- Rebuilt the 3 flagship projects (Quality Deviation Risk Monitor, GxP Change Control, AI Document Intelligence Evaluator) as icon + badge cards instead of a plain markdown table.
- Added a new "Supporting projects" section restoring the 5 repos that had been dropped, so all 8 public repos are linked from the profile again.
- Reinstated the "Validation & assurance principles" table.
- Rebuilt the Technology section as a grouped badge wall instead of a single plain-text line.
- Replaced unverifiable aggregate metrics with a stat table built only from numbers already backed by badges elsewhere in the file (8 public repos, CI/CD, stack, domain) rather than reusing stale totals.
- Did **not** restore the "Recent hardening" section — that content ages quickly (it described specific fixes from one point in time) and re-adding it wasn't part of the agreed scope; revisit if there's a current batch of hardening work worth documenting the same way.

## Follow-up

`docs/PORTFOLIO_EXPANSION_PLAN.md` was updated the same day to reflect this: its old "Pinning strategy" (picking 6 of a hypothetical larger set) is superseded by the README's actual two-tier hierarchy (3 flagship + 5 supporting), and its reference to "Service Operations Command Center" is now explicitly marked as unstarted — no repo exists for it, so it should not be added to the README until it clears Phase 1 of that plan.
