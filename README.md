<div align="center">

<img src="https://raw.githubusercontent.com/alianisreyesr/alianisreyesr/main/assets/profile-header.svg" width="100%" alt="Alianis Reyes-Reyes - Quality Data Engineer, GxP Systems and CSV" />

<p align="center">
  <a href="https://www.linkedin.com/in/alianis-reyes-reyes/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://github.com/alianisreyesr?tab=repositories"><img src="https://img.shields.io/badge/Repositories-12192f?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://poplme.co/hash/aJvjFE0Z/1/es"><img src="https://img.shields.io/badge/Digital_Portfolio-2aa8ad?style=for-the-badge&logo=linktree&logoColor=white" alt="Portfolio" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Education-B.S.B.A._Information_Systems_(Dec_2026)-0A66C2?style=flat-square" alt="Education" />
  <img src="https://img.shields.io/badge/Focus-Quality_Data_Engineering_%26_CSV-2E7D32?style=flat-square" alt="Focus" />
  <img src="https://img.shields.io/badge/Relocation-Open_to_Relocate-7842df?style=flat-square" alt="Relocation" />
</p>

[Flagship Systems](#flagship-quality--data-systems) · [Recent Hardening](#recent-hardening) · [Beyond Pharma](#beyond-pharma) · [Engineering Pillars](#engineering-pillars) · [Technologies](#technologies--tools) · [Quality Principles](#validation--assurance-principles)

</div>

## Engineering focus

I build end-to-end data and workflow systems for environments where **traceability, explainability and validation matter**. My public repositories focus on regulated quality engineering: connecting SQL and Python pipelines, FastAPI services, modern React frontends, and containerized deployments with GAMP 5, ALCOA+ data integrity, and automated CI/CD quality gates.

Information Systems senior graduating **December 2026** — pursuing entry-level roles in Quality Data Engineering, CSV, Data Engineering, Analytics Engineering, IT Compliance/GRC, and BI Automation. Experience informed by work at **TechLilly** and **OcyonBio**.

<table>
  <tr>
    <td align="center" width="25%"><h3>6+</h3><sub>Flagship quality systems</sub></td>
    <td align="center" width="25%"><h3>300+</h3><sub>Automated tests in CI</sub></td>
    <td align="center" width="25%"><h3>CI/CD</h3><sub>GitHub Actions · CodeQL · Docker</sub></td>
    <td align="center" width="25%"><h3>GxP &amp; CSV</h3><sub>Traceability &amp; audit trails</sub></td>
  </tr>
</table>

<p align="center">
  <img src="https://raw.githubusercontent.com/alianisreyesr/alianisreyesr/main/assets/stats-card.svg" alt="Live GitHub stats for @alianisreyesr — public repos, portfolio systems, followers, and language footprint" />
</p>
<p align="center"><sub>Regenerated weekly straight from the GitHub API by <a href="scripts/generate_stats_card.py"><code>scripts/generate_stats_card.py</code></a> — <a href="https://claude.ai/code/artifact/7a6d6d96-2d4e-4b9d-81bd-1efcc4805f4f">full interactive version →</a></sub></p>

<img src="https://raw.githubusercontent.com/alianisreyesr/alianisreyesr/main/assets/section-divider.svg" width="100%" height="26" alt="" />

## Recent hardening

Every flagship system below just went through a self-run audit — bugs, security, and quality issues found and fixed, verified with live smoke tests, then merged:

- Closed a **TOCTOU race** in deviation status transitions (`quality-deviation-risk-monitor`) using a `BEGIN IMMEDIATE` transaction; verified with a 10-thread concurrent stress test.
- Fixed **broken end-to-end auth** in the one project with real login (`csv-evidence-tracker`): an unprotected write endpoint, a frontend that never sent its JWT, and plaintext password comparisons — now bcrypt-hashed with timing-safe checks.
- Wired an **unused explainable risk-scoring function** into the actual deviation-creation path (`csa-assurance-planner`) so `risk_score`/`risk_classification` are computed and persisted, not just defined.
- Fixed a **DuckDB `executemany()` empty-list crash** and a cross-store inventory blending bug in the retail analytics pipeline.
- Rewrote a README that documented an entirely different API than the one shipping.

See each repo's merged PR for the full audit trail.

<img src="https://raw.githubusercontent.com/alianisreyesr/alianisreyesr/main/assets/section-divider.svg" width="100%" height="26" alt="" />

## Flagship quality &amp; data systems

<table>
  <tr>
    <td width="33%" valign="top">
      <div align="center">
        <h3><a href="https://github.com/alianisreyesr/csv-evidence-tracker">CSV Evidence Tracker</a></h3>
        <p>
          <img src="https://img.shields.io/badge/Status-Live-2E7D32?style=flat-square" alt="Status Live" />
          <img src="https://img.shields.io/badge/ALCOA+-Attributable_Audit_Trail-2E7D32?style=flat-square" alt="ALCOA+ Attributable Audit Trail" />
        </p>
      </div>
      <p>Computer System Validation tracking system covering Requirements Traceability Matrices (RTM), IQ/OQ/PQ execution patterns, deviation logs, and a 21 CFR Part 11-aligned audit trail.</p>
      <p><b>Architecture:</b> FastAPI · React · SQLite · Docker · Nginx</p>
      <div align="center">
        <a href="https://github.com/alianisreyesr/csv-evidence-tracker"><b>View repository →</b></a>
      </div>
    </td>
    <td width="33%" valign="top">
      <div align="center">
        <h3><a href="https://github.com/alianisreyesr/gxp-change-control">GxP Change Control</a></h3>
        <p>
          <img src="https://img.shields.io/badge/Release-v1.0.0-2E7D32?style=flat-square" alt="Release v1.0.0" />
          <img src="https://img.shields.io/badge/Tests-68_passing-2E7D32?style=flat-square" alt="68 Tests" />
        </p>
      </div>
      <p>Controlled change lifecycle application with impact assessment, multi-role approval gates, immutable UTC audit trail, and release verification.</p>
      <p><b>Architecture:</b> FastAPI · React 19 · TypeScript · SQLite · Docker</p>
      <div align="center">
        <a href="https://github.com/alianisreyesr/gxp-change-control"><b>View repository →</b></a>
      </div>
    </td>
    <td width="33%" valign="top">
      <div align="center">
        <h3><a href="https://github.com/alianisreyesr/quality-deviation-risk-monitor">Deviation Risk Monitor</a></h3>
        <p>
          <img src="https://img.shields.io/badge/Status-Active-2E7D32?style=flat-square" alt="Status Active" />
          <img src="https://img.shields.io/badge/Tests-112_passing-2E7D32?style=flat-square" alt="112 Tests" />
        </p>
      </div>
      <p>Proactive deviation monitoring system with explainable risk scoring, reviewer triage workflow, append-only audit trail, and synthetic data pipeline.</p>
      <p><b>Architecture:</b> Python · FastAPI · React · SQLite · Docker</p>
      <div align="center">
        <a href="https://github.com/alianisreyesr/quality-deviation-risk-monitor"><b>View repository →</b></a>
      </div>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width="33%" valign="top">
      <div align="center">
        <h3><a href="https://github.com/alianisreyesr/gxp-batch-data-pipeline">GxP Batch Data Pipeline</a></h3>
        <p>
          <img src="https://img.shields.io/badge/Status-Active-2E7D32?style=flat-square" alt="Status Active" />
          <img src="https://img.shields.io/badge/dbt-Quality_Gates-2E7D32?style=flat-square" alt="dbt" />
        </p>
      </div>
      <p>Synthetic pharmaceutical batch-manufacturing pipeline with DuckDB, dbt, SQL quality gates, and GxP process telemetry for decision-ready evidence.</p>
      <p><b>Architecture:</b> Python · SQL · DuckDB · dbt · ETL</p>
      <div align="center">
        <a href="https://github.com/alianisreyesr/gxp-batch-data-pipeline"><b>View repository →</b></a>
      </div>
    </td>
    <td width="33%" valign="top">
      <div align="center">
        <h3><a href="https://github.com/alianisreyesr/csa-assurance-planner">CSA Assurance Planner</a></h3>
        <p>
          <img src="https://img.shields.io/badge/Status-Active-0A66C2?style=flat-square" alt="Status Active" />
          <img src="https://img.shields.io/badge/Tests-11_passing-0A66C2?style=flat-square" alt="11 Tests" />
        </p>
      </div>
      <p>Risk-based Computer Software Assurance planning system aligned with FDA CSA guidance, risk classification, and unscripted testing strategies.</p>
      <p><b>Architecture:</b> Python · FastAPI · React · Structured assurance workflows</p>
      <div align="center">
        <a href="https://github.com/alianisreyesr/csa-assurance-planner"><b>View repository →</b></a>
      </div>
    </td>
    <td width="33%" valign="top">
      <div align="center">
        <h3><a href="https://github.com/alianisreyesr/data-integrity-case-file">Data Integrity Case File</a></h3>
        <p>
          <img src="https://img.shields.io/badge/Status-Active-0A66C2?style=flat-square" alt="Status Active" />
          <img src="https://img.shields.io/badge/Tests-36_passing-0A66C2?style=flat-square" alt="36 Tests" />
        </p>
      </div>
      <p>ALCOA+ investigation workspace and evidence ledger for deviation root-cause analysis, audit trail review, and CAPA readiness.</p>
      <p><b>Architecture:</b> FastAPI · SQLite · Audit trail evidence ledger</p>
      <div align="center">
        <a href="https://github.com/alianisreyesr/data-integrity-case-file"><b>View repository →</b></a>
      </div>
    </td>
  </tr>
</table>

> Public portfolio projects use synthetic data to demonstrate engineering architectures and regulated quality patterns.

<img src="https://raw.githubusercontent.com/alianisreyesr/alianisreyesr/main/assets/section-divider.svg" width="100%" height="26" alt="" />

## Beyond pharma

<table>
  <tr>
    <td width="50%" valign="top">
      <div align="center">
        <h3><a href="https://github.com/alianisreyesr/retail-operations-data-platform">Retail Operations Data Platform</a></h3>
        <p><img src="https://img.shields.io/badge/Status-Active-2E7D32?style=flat-square" alt="Status Active" /></p>
      </div>
      <p>Analytics engineering pipeline with DuckDB, tested quality gates, dimensional metrics, and decision-ready inventory evidence.</p>
      <p><b>Stack:</b> Python · DuckDB · SQL · Analytics Engineering</p>
      <div align="center">
        <a href="https://github.com/alianisreyesr/retail-operations-data-platform"><b>View repository →</b></a>
      </div>
    </td>
    <td width="50%" valign="top">
      <div align="center">
        <h3><a href="https://github.com/alianisreyesr/ai-document-intelligence-evaluator">AI Document Intelligence Evaluator</a></h3>
        <p><img src="https://img.shields.io/badge/Status-Active-2E7D32?style=flat-square" alt="Status Active" /></p>
      </div>
      <p>Provider-neutral AI evaluation harness for citations, evidence coverage, groundedness, latency, cost, and human review workflows.</p>
      <p><b>Stack:</b> Python · FastAPI · LLM Evaluation · RAG</p>
      <div align="center">
        <a href="https://github.com/alianisreyesr/ai-document-intelligence-evaluator"><b>View repository →</b></a>
      </div>
    </td>
  </tr>
</table>

<img src="https://raw.githubusercontent.com/alianisreyesr/alianisreyesr/main/assets/section-divider.svg" width="100%" height="26" alt="" />

## Engineering pillars

<table>
  <tr>
    <td width="33%" valign="top">
      <div align="center">
        <h4>Data &amp; Pipelines</h4>
      </div>
      <p>SQL &amp; Python ETL pipelines, data lineage modeling, DuckDB, dbt, and decision-ready Power BI reporting.</p>
    </td>
    <td width="33%" valign="top">
      <div align="center">
        <h4>GxP &amp; CSV Compliance</h4>
      </div>
      <p>ALCOA+ data integrity, 21 CFR Part 11, GAMP 5 risk assessments, IQ/OQ execution patterns, and audit trail architecture.</p>
    </td>
    <td width="33%" valign="top">
      <div align="center">
        <h4>Full-Stack &amp; DevOps</h4>
      </div>
      <p>FastAPI microservices, modern React interfaces, Docker containerization, and GitHub Actions automated quality gates.</p>
    </td>
  </tr>
</table>

<img src="https://raw.githubusercontent.com/alianisreyesr/alianisreyesr/main/assets/section-divider.svg" width="100%" height="26" alt="" />

## Technologies &amp; tools

<div align="center">

**Data engineering &amp; analytics**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat-square&logo=duckdb&logoColor=black)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=flat-square&logo=dbt&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)

**Software engineering &amp; APIs**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

**Cloud, containers &amp; CI/CD**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

**Regulated quality &amp; compliance**

![GAMP 5](https://img.shields.io/badge/GAMP_5-CSV-2E7D32?style=flat-square)
![21 CFR Part 11](https://img.shields.io/badge/21_CFR-Part_11_%2F_820-2E7D32?style=flat-square)
![ALCOA+](https://img.shields.io/badge/ALCOA%2B-Data_Integrity-2E7D32?style=flat-square)
![CAPA](https://img.shields.io/badge/Deviation_%26_CAPA-2E7D32?style=flat-square)
![Change Control](https://img.shields.io/badge/Change_Control-2E7D32?style=flat-square)

</div>

<img src="https://raw.githubusercontent.com/alianisreyesr/alianisreyesr/main/assets/section-divider.svg" width="100%" height="26" alt="" />

## Validation &amp; assurance principles

Every system in this portfolio is built with verification and auditability at the center:

<table>
  <tr>
    <td width="25%" valign="top">
      <div align="center"><h4>Traceability</h4></div>
      <p>Where did the data originate and how was it transformed?</p>
    </td>
    <td width="25%" valign="top">
      <div align="center"><h4>Accountability</h4></div>
      <p>What changed, who approved it, and when (UTC)?</p>
    </td>
    <td width="25%" valign="top">
      <div align="center"><h4>Explainability</h4></div>
      <p>Can calculations and risk scores be audited and reproduced?</p>
    </td>
    <td width="25%" valign="top">
      <div align="center"><h4>Assurance</h4></div>
      <p>Are requirements, automated tests, and deployment gates aligned?</p>
    </td>
  </tr>
</table>

<img src="https://raw.githubusercontent.com/alianisreyesr/alianisreyesr/main/assets/section-divider.svg" width="100%" height="26" alt="" />

<div align="center">

### Building auditable systems from data to decision

Open to roles in **Indiana, Puerto Rico, and global new-grad programs**.

For full professional background and career history, visit [LinkedIn](https://www.linkedin.com/in/alianis-reyes-reyes/) · [Digital portfolio](https://poplme.co/hash/aJvjFE0Z/1/es) · [All repositories](https://github.com/alianisreyesr?tab=repositories)

</div>
