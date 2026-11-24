#!/usr/bin/env bash
# Sets the description and topics of every portfolio repository in one pass.
# Requires the GitHub CLI (`gh`) authenticated as the repository owner:
#   gh auth login
#   bash scripts/set_repo_metadata.sh
# Re-running is safe: descriptions are overwritten and topics are only added.
set -euo pipefail

OWNER="alianisreyesr"

set_meta() {
  local repo="$1" description="$2"; shift 2
  local args=(--description "$description")
  for topic in "$@"; do args+=(--add-topic "$topic"); done
  echo "→ $OWNER/$repo"
  gh repo edit "$OWNER/$repo" "${args[@]}"
}

set_meta alianisreyesr \
  "Profile README for Alianis Reyes Reyes: data, AI and quality systems engineering with Python, SQL, FastAPI, React, GxP/CSV and AI evaluation." \
  github-profile portfolio

set_meta gxp-change-control \
  "GxP change control workflow engine for impact assessment, multi-step approvals, and post-change verification. Built with Python, FastAPI, and React (synthetic data)." \
  gxp change-control fastapi react python audit-trail

set_meta quality-deviation-risk-monitor \
  "Quality deviation risk scoring and monitoring API using Python, SQL, and FastAPI to surface recurring operational bottlenecks (synthetic data)." \
  quality deviation capa fastapi python sql

set_meta gxp-batch-data-pipeline \
  "Pharmaceutical batch telemetry pipeline with DuckDB, dbt, and automated SQL quality gates aligned with ALCOA+ data integrity checks (synthetic data)." \
  duckdb dbt data-engineering alcoa gxp python

set_meta csv-evidence-tracker \
  "Computer System Validation (CSV) workspace for requirements traceability, IQ/OQ/PQ execution logs, and 21 CFR Part 11-aligned audit trails in FastAPI and React." \
  csv validation 21-cfr-part-11 fastapi react traceability

set_meta data-integrity-case-file \
  "Data integrity investigation tracker for ALCOA+ gap analysis, structured evidence linking, and CAPA readiness using Python, FastAPI, and React." \
  alcoa data-integrity capa fastapi react python

set_meta csa-assurance-planner \
  "Risk-based Computer Software Assurance (CSA) planner mapping test rigor to FDA CSA guidance with FastAPI and React (synthetic data)." \
  csa gamp5 fda risk-based fastapi react

set_meta ai-security-analyst \
  "Explainable security operations platform: normalizes logs, applies deterministic detection and 0-100 risk scoring with MITRE ATT&CK mapping, and uses AI only for bounded, validated summaries." \
  python ai-security mitre-attack fastapi react postgresql llm-evaluation

set_meta ai-document-intelligence-evaluator \
  "Provider-neutral AI evaluation harness for document Q&A: citation validity, evidence coverage, groundedness, recall@k, latency and cost, with human-review routing (synthetic data)." \
  llm-evaluation rag ai-quality python fastapi streamlit

set_meta retail-operations-data-platform \
  "Retail analytics pipeline with DuckDB, tested SQL quality gates, dimensional metrics and decision-ready inventory evidence (synthetic data)." \
  duckdb analytics-engineering data-quality sql python

set_meta service-operations-command-center \
  "Service operations API for incident intake, severity-based SLA targets, controlled status transitions, owner assignment and audit events, with a Streamlit dashboard (synthetic data)." \
  fastapi streamlit sla incident-management python

echo "Done."
