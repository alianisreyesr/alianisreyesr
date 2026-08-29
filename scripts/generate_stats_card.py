#!/usr/bin/env python3
"""Regenerate the "Reyes-Reyes Ledger" GitHub profile stats card.

Fetches real, live data from the public GitHub REST API for a given user
(profile info, public repos, per-repo language byte counts, repo topics)
and renders it into a single self-contained HTML file styled to match the
card published at https://claude.ai/code/artifact/7a6d6d96-2d4e-4b9d-81bd-1efcc4805f4f

No third-party packages required — only the Python standard library.

Usage:
    python generate_stats_card.py                       # defaults to alianisreyesr
    python generate_stats_card.py octocat
    python generate_stats_card.py alianisreyesr --output card.html
    GITHUB_TOKEN=ghp_xxx python generate_stats_card.py   # higher rate limit

Notes:
- Unauthenticated requests are capped at 60/hour by GitHub. This script
  makes roughly (2 + number of non-fork public repos) calls, so it's fine
  unauthenticated for most profiles run a few times an hour. Set
  GITHUB_TOKEN (a plain "repo"-less, public-read PAT is enough) to raise
  the cap to 5,000/hour if you run it more often.
- This will NOT run inside a sandboxed Claude Code remote session — that
  sandbox blocks direct calls to api.github.com. It runs fine locally, in
  a normal CI runner, or in a GitHub Actions workflow.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

API_BASE = "https://api.github.com"
DEFAULT_USERNAME = "alianisreyesr"
TOP_TOPICS_SHOWN = 6


def _request(url: str, token: str | None) -> dict | list:
    headers = {
        "User-Agent": "reyes-reyes-ledger-card-generator",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API request failed ({exc.code}) for {url}: {body}") from exc


def fetch_user(username: str, token: str | None) -> dict:
    return _request(f"{API_BASE}/users/{username}", token)


def fetch_public_repos(username: str, token: str | None) -> list[dict]:
    repos: list[dict] = []
    page = 1
    while True:
        batch = _request(
            f"{API_BASE}/users/{username}/repos?per_page=100&page={page}&type=owner",
            token,
        )
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def fetch_languages(owner: str, repo: str, token: str | None) -> dict[str, int]:
    """Byte counts per language for one repo — the real basis for a
    weighted 'language footprint', rather than just each repo's single
    primary-language label."""
    try:
        return _request(f"{API_BASE}/repos/{owner}/{repo}/languages", token)
    except RuntimeError:
        return {}


def fetch_avatar_data_uri(avatar_url: str) -> str:
    req = urllib.request.Request(avatar_url, headers={"User-Agent": "reyes-reyes-ledger-card-generator"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        content_type = resp.headers.get("Content-Type", "image/jpeg")
        data = resp.read()
    return f"data:{content_type};base64,{base64.b64encode(data).decode()}"


def humanize_age(created_at: str) -> str:
    created = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    days = (now - created).days
    years, remainder_days = divmod(days, 365)
    months = remainder_days // 30
    if years and months:
        return f"{years}y {months}m"
    if years:
        return f"{years}y"
    return f"{months}m"


LANG_COLORS = {
    "Python": "var(--accent-teal)",
    "JavaScript": "var(--accent-blue)",
    "TypeScript": "#3E7BD6",
    "HTML": "#D97757",
    "CSS": "#7C6FE0",
    "SQL": "#C4941F",
    "Shell": "#6B8E5A",
    "Dockerfile": "#4C9AC9",
}
FALLBACK_COLORS = ["var(--accent-teal)", "var(--accent-blue)", "#C4941F", "#7C6FE0", "#D97757", "#6B8E5A"]


def build_language_rows(repos: list[dict], token: str | None) -> list[dict]:
    totals: dict[str, int] = {}
    for repo in repos:
        if repo.get("fork"):
            continue
        for lang, byte_count in fetch_languages(repo["owner"]["login"], repo["name"], token).items():
            totals[lang] = totals.get(lang, 0) + byte_count

    grand_total = sum(totals.values()) or 1
    ranked = sorted(totals.items(), key=lambda item: item[1], reverse=True)[:6]
    rows = []
    for index, (lang, byte_count) in enumerate(ranked):
        pct = round(100 * byte_count / grand_total)
        color = LANG_COLORS.get(lang, FALLBACK_COLORS[index % len(FALLBACK_COLORS)])
        rows.append({"name": lang, "pct": pct, "color": color})
    return rows


def build_topic_rows(repos: list[dict]) -> list[dict]:
    counts: dict[str, int] = {}
    for repo in repos:
        if repo.get("fork"):
            continue
        for topic in repo.get("topics") or []:
            counts[topic] = counts.get(topic, 0) + 1
    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:TOP_TOPICS_SHOWN]
    return [{"name": name, "count": count} for name, count in ranked]


def esc(value: str) -> str:
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_html(user: dict, repos: list[dict], lang_rows: list[dict], topic_rows: list[dict], avatar_data_uri: str) -> str:
    non_fork = [r for r in repos if not r.get("fork")]
    portfolio_repos = sum(1 for r in non_fork if "portfolio" in (r.get("topics") or []))
    location = user.get("location")
    bio = user.get("bio") or ""
    generated_on = datetime.now(timezone.utc).strftime("%b %d, %Y")

    lang_bars = "\n".join(
        f"""      <div class="lang-row">
        <div class="lang-name"><span class="swatch" style="background:{row['color']}"></span>{esc(row['name'])}</div>
        <div class="lang-track"><div class="lang-fill" style="width:{row['pct']}%;background:{row['color']}"></div></div>
        <div class="lang-pct mono">{row['pct']}%</div>
      </div>"""
        for row in lang_rows
    )

    topic_lines = "\n".join(
        f'      <div class="tag-row"><span class="tag-name">{esc(row["name"])}</span>'
        f'<span class="tag-count mono">{row["count"]}</span></div>'
        for row in topic_rows
    )

    meta_lines = []
    if location:
        meta_lines.append(f'<li><span class="dot"></span>{esc(location)}</li>')
    meta_lines.append(
        f'<li><span class="dot"></span>Joined GitHub {user["created_at"][:7]} '
        f'<span class="mono" style="color:var(--faint)">· {humanize_age(user["created_at"])}</span></li>'
    )
    meta_html = "\n        ".join(meta_lines)

    footnote = (
        f"Share of bytes across {len(non_fork)} non-fork public repos, weighted by language "
        f"(GitHub's linguist byte counts, not just each repo's single primary label)."
    )

    return f"""<title>Reyes-Reyes Ledger</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
  :root {{
    --page-bg: #F6F4EE;
    --card-bg: #FFFFFF;
    --card-bg-raised: #FBFAF6;
    --ink: #10202E;
    --muted: #5B6B7C;
    --faint: #93A0AC;
    --line: #E3DFD3;
    --line-strong: #D3CDBC;
    --accent-teal: #1F7A4D;
    --accent-blue: #0A66C2;
    --bar-track: #ECE9DF;
    --shadow: 0 1px 2px rgba(16, 32, 46, 0.04), 0 12px 32px rgba(16, 32, 46, 0.07);
  }}

  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      --page-bg: #0A121C;
      --card-bg: #101B28;
      --card-bg-raised: #14212F;
      --ink: #E9EEF3;
      --muted: #8FA0AF;
      --faint: #5E6E7C;
      --line: rgba(255, 255, 255, 0.08);
      --line-strong: rgba(255, 255, 255, 0.14);
      --accent-teal: #3FBE84;
      --accent-blue: #5B9FE8;
      --bar-track: rgba(255, 255, 255, 0.07);
      --shadow: 0 1px 2px rgba(0, 0, 0, 0.3), 0 20px 44px rgba(0, 0, 0, 0.38);
    }}
  }}

  :root[data-theme="dark"] {{
    --page-bg: #0A121C;
    --card-bg: #101B28;
    --card-bg-raised: #14212F;
    --ink: #E9EEF3;
    --muted: #8FA0AF;
    --faint: #5E6E7C;
    --line: rgba(255, 255, 255, 0.08);
    --line-strong: rgba(255, 255, 255, 0.14);
    --accent-teal: #3FBE84;
    --accent-blue: #5B9FE8;
    --bar-track: rgba(255, 255, 255, 0.07);
    --shadow: 0 1px 2px rgba(0, 0, 0, 0.3), 0 20px 44px rgba(0, 0, 0, 0.38);
  }}

  * {{ box-sizing: border-box; }}

  body {{
    margin: 0;
    min-height: 100vh;
    background: var(--page-bg);
    color: var(--ink);
    font-family: "IBM Plex Sans", system-ui, -apple-system, sans-serif;
    display: flex;
    justify-content: center;
    padding: 48px 20px;
  }}

  .mono {{ font-family: "IBM Plex Mono", ui-monospace, "SF Mono", monospace; font-variant-numeric: tabular-nums; }}

  .card {{
    width: 100%;
    max-width: 860px;
    background: var(--card-bg);
    border: 1px solid var(--line);
    border-radius: 18px;
    box-shadow: var(--shadow);
    overflow: hidden;
  }}

  .card-header {{
    padding: 34px 38px 28px;
    border-bottom: 1px solid var(--line);
    display: flex;
    justify-content: space-between;
    gap: 24px;
    align-items: flex-start;
  }}

  .eyebrow {{
    font-family: "IBM Plex Mono", monospace;
    font-size: 11px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--accent-teal);
    font-weight: 600;
    margin: 0 0 10px;
  }}

  h1 {{ font-size: 26px; font-weight: 700; margin: 0 0 6px; letter-spacing: -0.01em; text-wrap: balance; }}
  .handle {{ color: var(--muted); font-family: "IBM Plex Mono", monospace; font-size: 14px; margin: 0 0 14px; }}
  .handle a {{ color: inherit; text-decoration: none; border-bottom: 1px solid var(--line-strong); }}
  .handle a:hover {{ color: var(--accent-teal); border-color: var(--accent-teal); }}
  .bio {{ color: var(--muted); font-size: 14.5px; line-height: 1.55; max-width: 46ch; margin: 0; }}

  .meta-list {{ list-style: none; margin: 14px 0 0; padding: 0; display: flex; flex-direction: column; gap: 6px; font-size: 13px; color: var(--muted); }}
  .meta-list li {{ display: flex; align-items: center; gap: 8px; }}
  .meta-list .dot {{ width: 5px; height: 5px; border-radius: 50%; background: var(--faint); flex: none; }}

  .avatar-ring {{
    flex: none; width: 84px; height: 84px; border-radius: 20px; padding: 3px;
    background: linear-gradient(135deg, var(--accent-teal), var(--accent-blue));
  }}
  .avatar-ring img {{ width: 100%; height: 100%; border-radius: 17px; display: block; object-fit: cover; background: var(--card-bg-raised); }}

  .stat-strip {{ display: grid; grid-template-columns: repeat(4, 1fr); border-bottom: 1px solid var(--line); }}
  .stat {{ padding: 22px 20px; border-right: 1px solid var(--line); }}
  .stat:last-child {{ border-right: none; }}
  .stat-value {{ font-size: 25px; font-weight: 600; line-height: 1; letter-spacing: -0.01em; }}
  .stat-label {{ margin-top: 8px; font-size: 10.5px; letter-spacing: 0.09em; text-transform: uppercase; color: var(--faint); }}

  .body-grid {{ display: grid; grid-template-columns: 1fr 1fr; }}
  .panel {{ padding: 28px 38px 32px; }}
  .panel + .panel {{ border-left: 1px solid var(--line); }}
  .panel h2 {{ font-size: 12px; letter-spacing: 0.09em; text-transform: uppercase; color: var(--muted); font-weight: 600; margin: 0 0 18px; }}

  .lang-row {{ display: grid; grid-template-columns: 88px 1fr 34px; align-items: center; gap: 10px; margin-bottom: 12px; font-size: 13px; }}
  .lang-row:last-child {{ margin-bottom: 0; }}
  .lang-name {{ display: flex; align-items: center; gap: 7px; color: var(--ink); font-weight: 500; }}
  .swatch {{ width: 9px; height: 9px; border-radius: 3px; flex: none; }}
  .lang-track {{ height: 7px; border-radius: 4px; background: var(--bar-track); overflow: hidden; }}
  .lang-fill {{ height: 100%; border-radius: 4px; }}
  .lang-pct {{ text-align: right; color: var(--muted); font-size: 12px; }}
  .lang-footnote {{ margin: 16px 0 0; font-size: 11.5px; color: var(--faint); line-height: 1.5; }}

  .tag-row {{ display: flex; align-items: baseline; justify-content: space-between; padding: 9px 0; border-bottom: 1px dashed var(--line); font-size: 13.5px; }}
  .tag-row:last-of-type {{ border-bottom: none; }}
  .tag-name {{ color: var(--ink); font-weight: 500; }}
  .tag-count {{ color: var(--accent-teal); font-weight: 600; }}

  .card-footer {{
    display: flex; justify-content: space-between; align-items: center; gap: 16px; flex-wrap: wrap;
    padding: 18px 38px; border-top: 1px solid var(--line); background: var(--card-bg-raised);
    font-size: 12px; color: var(--faint);
  }}
  .card-footer a {{ color: var(--accent-blue); text-decoration: none; font-weight: 500; }}
  .card-footer a:hover {{ text-decoration: underline; }}
  .snapshot-note {{ display: flex; align-items: center; gap: 7px; }}
  .pulse {{ width: 7px; height: 7px; border-radius: 50%; background: var(--accent-teal); flex: none; }}

  @media (max-width: 620px) {{
    .stat-strip {{ grid-template-columns: repeat(2, 1fr); }}
    .stat:nth-child(2) {{ border-right: none; }}
    .body-grid {{ grid-template-columns: 1fr; }}
    .panel + .panel {{ border-left: none; border-top: 1px solid var(--line); }}
    .card-header {{ flex-direction: column-reverse; }}
  }}
</style>

<div class="card">
  <div class="card-header">
    <div>
      <p class="eyebrow">GitHub Ledger</p>
      <h1>{esc(user.get('name') or user['login'])}</h1>
      <p class="handle"><a href="{esc(user['html_url'])}" target="_blank" rel="noopener">@{esc(user['login'])}</a></p>
      <p class="bio">{esc(bio)}</p>
      <ul class="meta-list">
        {meta_html}
      </ul>
    </div>
    <div class="avatar-ring">
      <img src="{avatar_data_uri}" alt="{esc(user['login'])} avatar" />
    </div>
  </div>

  <div class="stat-strip">
    <div class="stat">
      <div class="stat-value mono">{user.get('public_repos', 0)}</div>
      <div class="stat-label">Public repos</div>
    </div>
    <div class="stat">
      <div class="stat-value mono">{portfolio_repos}</div>
      <div class="stat-label">Portfolio systems</div>
    </div>
    <div class="stat">
      <div class="stat-value mono">{user.get('followers', 0)}</div>
      <div class="stat-label">Followers</div>
    </div>
    <div class="stat">
      <div class="stat-value mono">{user.get('following', 0)}</div>
      <div class="stat-label">Following</div>
    </div>
  </div>

  <div class="body-grid">
    <div class="panel">
      <h2>Language footprint</h2>
{lang_bars}
      <p class="lang-footnote">{footnote}</p>
    </div>

    <div class="panel">
      <h2>Focus areas <span style="color:var(--faint); font-weight:400;">— by repo topic</span></h2>
{topic_lines}
    </div>
  </div>

  <div class="card-footer">
    <div class="snapshot-note">
      <span class="pulse"></span>
      Snapshot from the public GitHub API · {generated_on}
    </div>
    <a href="{esc(user['html_url'])}?tab=repositories" target="_blank" rel="noopener">View all repositories →</a>
  </div>
</div>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("username", nargs="?", default=DEFAULT_USERNAME, help=f"GitHub username (default: {DEFAULT_USERNAME})")
    parser.add_argument("--output", default="stats-card.html", help="Output HTML file path (default: stats-card.html)")
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"), help="GitHub token (or set GITHUB_TOKEN env var); optional but raises the rate limit")
    args = parser.parse_args()

    print(f"Fetching GitHub data for @{args.username}...", file=sys.stderr)
    user = fetch_user(args.username, args.token)
    repos = fetch_public_repos(args.username, args.token)
    print(f"  {len(repos)} public repos found; fetching per-repo language stats...", file=sys.stderr)
    lang_rows = build_language_rows(repos, args.token)
    topic_rows = build_topic_rows(repos)
    print("  downloading avatar...", file=sys.stderr)
    avatar_data_uri = fetch_avatar_data_uri(user["avatar_url"])

    html = render_html(user, repos, lang_rows, topic_rows, avatar_data_uri)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
