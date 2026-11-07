# Portfolio expansion plan

## Status (updated 2026-09-19)

The README redesign in [PR #6](https://github.com/alianisreyesr/alianisreyesr/pull/6) already delivers most of what the original "Pinning strategy" section below was planning toward: all 8 public repos are now surfaced from the profile in a curated hierarchy (3 flagship project cards + 5 supporting project cards), with visual design, a live stats card, and consistent badges. See `docs/README_REDESIGN_LOG.md` for the full audit and rationale behind that change.

What is **not** done yet: the case-study depth described in Phase 2/3 below (screenshots, dashboards, walkthroughs) and the "Service Operations Command Center" project, which was planned here but never built — no repo, no README reference, no assets exist for it. Treat every mention of it below as aspirational, not shipped.

## Positioning

**Primary identity:** Data, AI & Quality Systems Engineer building trustworthy, testable systems.

**Differentiator:** Experience applying traceability, data quality, explainable rules, and evidence-oriented engineering in regulated environments — now paired with AI evaluation work (retrieval, groundedness, evaluation harnesses) to support a broader AI Engineering search.

This positioning supports a broader search without discarding the GxP/CSV specialization.

## Portfolio tracks

| Track | Proof project | Status | Target roles |
|---|---|---|---|
| Data & Analytics Engineering | Retail Operations Data Platform | Shipped — supporting project in README | Data Engineer, Analytics Engineer, BI Developer |
| Backend & Product Engineering | Service Operations Command Center | Not started — no repo exists | Backend Engineer, Software Engineer, Platform Engineer |
| Applied AI & Evaluation | AI Document Intelligence Evaluator | Shipped — promoted to flagship in README | AI Application Engineer, AI Quality Engineer, Data Scientist |
| Regulated Quality Systems | GxP/CSV flagships (Quality Deviation Risk Monitor, GxP Change Control, CSV Evidence Tracker, GxP Batch Data Pipeline, CSA Assurance Planner, Data Integrity Case File) | Shipped — all 6 surfaced in README | Quality Data Engineer, CSV/CSA, GxP Systems Engineer |

## Delivery phases

### Phase 1 — executable foundations

- Publish synthetic datasets and working domain logic. ✅ done for all 8 shipped repos.
- Document the business problem, architecture, and limitations. ✅ done for all 8 shipped repos.
- Add automated tests, dependency management, security policy, and contribution guidance. ✅ done for the 5 repos with test badges (Quality Deviation Risk Monitor, GxP Change Control, CSA Assurance Planner, Data Integrity Case File); not yet confirmed for CSV Evidence Tracker, GxP Batch Data Pipeline, Retail Operations Data Platform, AI Document Intelligence Evaluator.

### Phase 2 — recruiter-ready product evidence

- Add CI and CodeQL evidence. Partially done — CI badges exist per-project; CodeQL status not tracked in the profile README.
- Build visual interfaces or decision dashboards. Done in the underlying repos (FastAPI + React stacks); not yet surfaced as screenshots in the profile.
- Capture two to four screenshots per project. **Not started.**
- Publish short case-study walkthroughs. **Not started.**

### Phase 3 — production-minded depth

- Retail: orchestration, dbt models, incremental loads, and BI semantic layer. Status lives in that repo, not tracked here.
- Service operations: PostgreSQL, OIDC/RBAC, React UI, background escalation jobs, and telemetry. **Blocked — project not started.**
- AI evaluator: retrieval adapter, versioned experiment runs, semantic graders, and evaluation dashboard. Status lives in that repo, not tracked here.

### Phase 4 — portfolio promotion

- Replace lower-priority pins only when new projects have green CI, visual evidence, and complete case studies.
- Align resume project bullets with measurable repository evidence.
- Publish one technical article or 60–90 second walkthrough for each portfolio track. **Not started.**

## README project hierarchy (supersedes the old "Pinning strategy")

The profile README now curates all 8 shipped repos into two tiers instead of picking 6 pins:

**Flagship (lead cards, full visual treatment):**
1. Quality Deviation Risk Monitor
2. GxP Change Control
3. AI Document Intelligence Evaluator

**Supporting (secondary card grid):**
4. CSV Evidence Tracker
5. GxP Batch Data Pipeline
6. CSA Assurance Planner
7. Data Integrity Case File
8. Retail Operations Data Platform

Service Operations Command Center is intentionally absent — it doesn't exist yet. Do not add it to the README until a repo exists with at least Phase 1 complete (per the quality gate below).

## Quality gate for promotion

A project becomes flagship-ready only when it has:

- a clear business outcome and target user;
- synthetic data and an explicit safety boundary;
- reproducible installation and execution;
- automated tests and green CI;
- CodeQL and dependency updates;
- architecture and case-study documentation;
- screenshots, a dashboard, or a short walkthrough;
- no unsupported claims, broken links, or stale badges.

A project that ships but doesn't yet clear every item goes in "Supporting projects," not flagship — that's the bar QDRM, GxP Change Control, and the AI evaluator cleared to lead the README.
