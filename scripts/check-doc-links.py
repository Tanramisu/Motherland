#!/usr/bin/env python3
"""Report Markdown links a fresh clone cannot follow.

Scanning every Markdown file in every repository is noise: archived notes,
recorded session snapshots and vendored upstream docs are full of links that
were never meant to resolve here. What a reader actually walks is the entry
files at a repository root plus everything under ``docs/`` — that is the scope
this checks, and the only scope a break is worth reporting in.

Two targets fail. A relative one that points at nothing, and an absolute one:
``D:/...`` resolves on the machine that wrote it and nowhere else, so a local
existence check passes while every clone gets a 404. Research records are the
exception — they cite one checkout line by line, including profile files that
never enter git, so their absolute targets are evidence rather than navigation.

Repositories come from the registry — ``REPOS.local.md`` when present (the
maintainer's real table, never committed), else ``REPOS.md`` (the public
example): the local checkout column, first path in the cell. Missing
checkouts are skipped, not reported.

    python scripts/check-doc-links.py            # list every broken link
    python scripts/check-doc-links.py --check    # one line, exit 1 when broken
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRY_FILES = ("README.md", "AGENTS.md", "CODEMAP.md", "CLAUDE.md")
SKIP_DIRS = {
    "node_modules", ".git", "dist", "lib", "build", ".venv", "__pycache__", ".pytest_cache",
    ".dsh", ".dsh-dev", ".tmpbench", "templates", "archived", ".generated", "vendor",
    "snapshots",
}
def evidence_dirs() -> tuple[str, ...]:
    """Per-owner exceptions: record directories whose absolute targets are
    evidence rather than navigation. Set in check-doc-links.local.json at the
    repository root (never committed), e.g. {"evidence_dirs": ["docs/research/"]}."""
    config = ROOT / "check-doc-links.local.json"
    if config.is_file():
        try:
            return tuple(json.loads(config.read_text(encoding="utf-8")).get("evidence_dirs", []))
        except (ValueError, OSError):
            return ()
    return ()


EVIDENCE_DIRS = evidence_dirs()
LINK = re.compile(r"\[[^\]]*\]\(\s*(?:<([^>]*)>|([^)\s]+))")
DRIVE = re.compile(r"^[A-Za-z]:[\\/]")
FENCE = re.compile(r"^```.*?^```", re.S | re.M)
QUOTE = re.compile(r"^[ \t]*>.*$", re.M)
REASON = {"absolute": "（本机绝对路径，克隆后失效）"}


def checkouts() -> list[Path]:
    """Local checkout paths from the registry table, in table order."""
    local = ROOT / "REPOS.local.md"
    table = local if local.is_file() else ROOT / "REPOS.md"
    paths: list[Path] = []
    for line in table.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "`" not in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        first = cells[2]
        if not first.startswith("`"):
            continue
        candidate = Path(first.split("`")[1])
        if candidate.exists() and candidate not in paths:
            paths.append(candidate)
    return paths


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for name in ENTRY_FILES:
        entry = root / name
        if entry.is_file():
            files.append(entry)
    docs = root / "docs"
    if docs.is_dir():
        for path in sorted(docs.rglob("*.md")):
            if path.is_file() and not any(part in SKIP_DIRS for part in path.relative_to(root).parts):
                files.append(path)
    return files


def broken_links(root: Path, path: Path) -> list[tuple[str, str]]:
    """Every unusable target in one file, as (target, reason): ``missing`` or ``absolute``."""
    inside_evidence = path.relative_to(root).as_posix().startswith(EVIDENCE_DIRS)
    text = QUOTE.sub("", FENCE.sub("", path.read_text(encoding="utf-8", errors="replace")))
    broken: list[tuple[str, str]] = []
    for match in LINK.finditer(text):
        target = match[1] or match[2]
        if target.startswith(("http://", "https://", "mailto:", "#", "dsh-session:")):
            continue
        if "://" in target:
            continue
        if DRIVE.match(target):
            if not inside_evidence:
                broken.append((target, "absolute"))
            continue
        relative = target.split("#", 1)[0]
        if not relative:
            continue
        if not (path.parent / relative).exists():
            broken.append((target, "missing"))
    return broken


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="print one summary line and set the exit code")
    parser.add_argument("--examples", type=int, default=3, help="how many breaks to name (default 3)")
    args = parser.parse_args()

    roots = checkouts()
    total = 0
    scanned = 0
    report: list[str] = []
    for root in roots:
        files = markdown_files(root)
        scanned += len(files)
        breaks = [
            (path.name, target, reason)
            for path in files
            for target, reason in broken_links(root, path)
        ]
        if not breaks:
            continue
        total += len(breaks)
        report.append(f"{root.name}: {len(breaks)} 处")
        for name, target, reason in breaks[: args.examples]:
            report.append(f"  {root.name}/{name} -> {target}{REASON.get(reason, '')}")

    if args.check:
        if total == 0:
            print("ok")
            return 0
        print(f"文档断链 {total} 处（{len(roots)} 仓 {scanned} 篇）：{report[0]}", file=sys.stderr)
        return 1

    if total == 0:
        print(f"{len(roots)} 仓 {scanned} 篇 Markdown，断链 0 处")
        return 0
    print(f"{len(roots)} 仓 {scanned} 篇 Markdown，断链 {total} 处")
    print("\n".join(report))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
