#!/usr/bin/env python3
"""Refresh the profile README + REPOSITORY_INDEX.md from live GitHub data.

Zero third-party dependencies (stdlib only). Runs in GitHub Actions on a
schedule; the README never carries a number a human had to remember to update.

Refreshes three things:
1. the STATS block (markers <!-- STATS:START/END -->)
2. badge counts in the README header (Repos / per-language)
3. REPOSITORY_INDEX.md — the full per-language repo listing
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
INDEX = "REPOSITORY_INDEX.md"
START = "<!-- STATS:START -->"
END = "<!-- STATS:END -->"

# badge slug -> shield color/logo fragment, matched against live language counts
LANG_BADGES = {
    "Python": "3776AB?logo=python",
    "HTML": "E34F26?logo=html5",
    "JavaScript": "F7DF1E?logo=javascript",
    "TypeScript": "3178C6?logo=typescript",
}

SECTION_TITLES = {
    "Python": "Python · 算法系统与基准",
    "HTML": "HTML · 单文件零依赖实验室（浏览器可跑）",
    "JavaScript": "JavaScript · 零依赖内核与工具",
    "TypeScript": "TypeScript · 平台与全栈",
}
SECTION_ORDER = ["Python", "HTML", "JavaScript", "TypeScript"]

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

    # CI presence needs one extra call per repo; counted over every active repo
    ci_count = 0
    for r in active:
        try:
            wf = api(f"/repos/{USER}/{r['name']}/contents/.github/workflows")
            if isinstance(wf, list) and wf:
                ci_count += 1
        except Exception:
            pass

    # the profile repo itself is just bookkeeping, not a deliverable
    recent = [r for r in repos if r["name"].lower() != USER.lower()]
    recent = sorted(recent, key=lambda r: r.get("pushed_at", ""), reverse=True)[:6]

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
        f"| 活跃仓库 CI 覆盖 | **{ci_count}/{len(active)}**（{ci_count * 100 // max(len(active), 1)}%） |",
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

    # keep header badges and the index heading in sync with live counts
    new = re.sub(r"Repos-\d+-blue", f"Repos-{len(repos)}-blue", new)
    for lang, frag in LANG_BADGES.items():
        if lang in langs:
            new = re.sub(
                rf"{lang}-\d+-{re.escape(frag)}",
                f"{lang}-{langs[lang]}-{frag}",
                new,
            )
    new = re.sub(r"全部 \d+ 个仓库", f"全部 {len(repos)} 个仓库", new)

    changed = []
    if new != src:
        open(README, "w", encoding="utf-8").write(new)
        changed.append(README)

    index_text = render_index(repos)
    old_index = ""
    if os.path.exists(INDEX):
        old_index = open(INDEX, encoding="utf-8").read()
    if index_text != old_index:
        open(INDEX, "w", encoding="utf-8").write(index_text)
        changed.append(INDEX)

    if changed:
        print(f"updated {changed}: {len(repos)} repos, {stars} stars, {ci_count} with CI")
    else:
        print("no change")
    return 0


def truncate(text: str, limit: int = 50) -> str:
    text = (text or "").replace("|", "\\|").replace("\n", " ").strip()
    return text[:limit] + ("…" if len(text) > limit else "")


def render_index(repos: list) -> str:
    """Full repo listing grouped by language, alphabetically, global numbering."""
    repos = sorted(repos, key=lambda r: r["name"].lower())
    number = {r["name"]: i + 1 for i, r in enumerate(repos)}

    groups: dict[str, list] = {}
    for r in repos:
        groups.setdefault(r.get("language") or "其他", []).append(r)

    total = len(repos)
    out = [
        "# 📇 全量仓库索引 · Repository Index",
        "",
        f"> 本文件由主页 README 拆分而来，包含 **{total} 个公开仓库**的完整清单。",
        "> 主页只放精选；这里是全部。按语言分组，表格内为「仓库 / 一句话 / 状态」。",
        "",
        "## 全量仓库索引",
        "",
        f"**{total} 个仓库，零遗漏。** 按形态分组，字母序。归档项目保留但不推荐 —— 它们是历史迭代的诚实痕迹。",
        "",
    ]
    ordered = [k for k in SECTION_ORDER if k in groups]
    ordered += [k for k in groups if k not in SECTION_ORDER]
    for lang in ordered:
        items = groups[lang]
        active_n = sum(1 for r in items if not r.get("archived"))
        title = SECTION_TITLES.get(lang, f"{lang} · 其他")
        out.append(f"### {title} · {len(items)}（活跃 {active_n}）")
        out.append("")
        out.append("<details>")
        out.append(f"<summary>展开 {len(items)} 个仓库</summary>")
        out.append("")
        out.append("| # | 仓库 | 一句话 | 状态 |")
        out.append("| ---: | --- | --- | --- |")
        for r in items:
            status = "归档" if r.get("archived") else "活跃"
            out.append(
                f"| {number[r['name']]} | [{r['name']}](https://github.com/{USER}/{r['name']}) "
                f"| {truncate(r.get('description'))} | {status} |"
            )
        out.append("")
        out.append("</details>")
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    sys.exit(main())
