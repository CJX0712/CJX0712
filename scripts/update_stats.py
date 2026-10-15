#!/usr/bin/env python3
"""Refresh the STATS block in the profile README from live GitHub data.

Zero third-party dependencies (stdlib only). Runs in GitHub Actions on a
schedule; the README never carries a number a human had to remember to update.
"""
from __future__ import annotations

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

USER = "CJX0712"
README = "README.md"
START = "<!-- STATS:START -->"
END = "<!-- STATS:END -->"

TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "profile-stats",
    "X-GitHub-Api-Version": "2022-11-28",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def api(path: str):
    req = urllib.request.Request(f"https://api.github.com{path}", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def paginate(path: str) -> list:
    out: list = []
    page = 1
    while page <= 20:
        sep = "&" if "?" in path else "?"
        chunk = api(f"{path}{sep}per_page=100&page={page}")
        if not chunk:
            break
        out.extend(chunk)
        if len(chunk) < 100:
            break
        page += 1
    return out


def human_size(kb: int) -> str:
    mb = kb / 1024.0
    return f"{mb:.1f} MB" if mb < 1024 else f"{mb / 1024.0:.2f} GB"


def days_ago(iso: str) -> str:
    then = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    delta = (datetime.now(timezone.utc) - then).days
    return "今天" if delta == 0 else (f"{delta} 天前" if delta < 30 else f"{delta // 30} 个月前")


def main() -> int:
    user = api(f"/users/{USER}")
    repos = paginate(f"/users/{USER}/repos?affiliation=owner")
    repos = [r for r in repos if not r.get("private")]

    archived = [r for r in repos if r.get("archived")]
    active = [r for r in repos if not r.get("archived")]
    forks = [r for r in repos if r.get("fork")]

    stars = sum(r.get("stargazers_count", 0) for r in repos)
    size_kb = sum(r.get("size", 0) for r in repos)

    langs: dict[str, int] = {}
    for r in repos:
        lang = r.get("language") or "其他"
        langs[lang] = langs.get(lang, 0) + 1
    top_langs = sorted(langs.items(), key=lambda kv: -kv[1])

    with_ci = sum(1 for r in repos if r.get("has_issues") is not None)
    # CI presence needs a second call per repo; approximate via workflow files
    ci_count = 0
    for r in active[:200]:
        try:
            wf = api(f"/repos/{USER}/{r['name']}/contents/.github/workflows")
            if isinstance(wf, list) and wf:
                ci_count += 1
        except Exception:
            pass

    recent = sorted(repos, key=lambda r: r.get("pushed_at", ""), reverse=True)[:6]

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lang_str = " · ".join(f"{k} {v}" for k, v in top_langs[:5])

    lines = [
        f"> 由 GitHub Actions 自动刷新 · 最后更新 {stamp} · 数字由 API 实拉，不靠手改",
        "",
        "| 指标 | 数值 |",
        "| --- | --- |",
        f"| 公开仓库 | **{len(repos)}**（活跃 {len(active)} · 归档 {len(archived)}） |",
        f"| Stars / Followers | **{stars}** / **{user.get('followers', 0)}** |",
        f"| 代码体量 | ≈ {human_size(size_kb)}（GitHub 计 {sum(r.get('size', 0) for r in repos):,} KB） |",
        f"| 语言分布 | {lang_str} |",
        f"| 活跃仓库 CI 覆盖 | **{ci_count}/{len(active[:200])}**（抽样前 200） |",
        f"| Fork | {len(forks)} |",
        "",
        "**最近推送**",
        "",
    ]
    for r in recent:
        desc = (r.get("description") or "").replace("|", "/").strip()
        desc = desc[:58] + ("…" if len(desc) > 58 else "")
        lines.append(
            f"- [{r['name']}](https://github.com/{USER}/{r['name']}) — {desc} "
            f"（{days_ago(r['pushed_at'])}）"
        )

    block = "\n".join([START, *lines, END])

    src = open(README, encoding="utf-8").read()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(src):
        print(f"ERROR: markers {START} / {END} not found in {README}", file=sys.stderr)
        return 1
    new = pattern.sub(lambda _: block, src)
    if new == src:
        print("no change")
        return 0
    open(README, "w", encoding="utf-8").write(new)
    print(f"updated: {len(repos)} repos, {stars} stars, {ci_count} with CI")
    return 0


if __name__ == "__main__":
    sys.exit(main())
