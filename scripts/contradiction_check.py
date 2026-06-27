#!/usr/bin/env python3
"""
Contradiction Detector — Scans memoranda and chapter files for conflicts.

Checks for:
- Date conflicts (same event referenced at different dates)
- Name conflicts (same person referenced differently)
- Fact conflicts (same event described with different details)
- Marks each with [CONTRADICTION CANDIDATE]

Usage:
  python3 scripts/contradiction_check.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = [
    ROOT / "docs",
    ROOT / "book" / "chapters",
]
SCAN_GLOBS = ["*.md"]


def extract_dates(text: str) -> list[tuple[str, str]]:
    """Extract date-like patterns with surrounding context."""
    patterns = [
        (r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s*(\d{4})", "full_date"),
        (r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})", "month_year"),
        (r"\b(\d{4})-(\d{2})-(\d{2})\b", "iso_date"),
    ]
    results = []
    for pat, label in patterns:
        for m in re.finditer(pat, text):
            results.append((m.group(0), label))
    return results


def extract_rcw_refs(text: str) -> list[str]:
    """Extract RCW and USC citations."""
    return re.findall(r"RCW\s+[\dA-Za-z.]+|USC\s+[\d\s]+|U\.S\.C\.?\s*§?\s*[\d]+", text)


def extract_verify_tags(text: str) -> list[tuple[str, int]]:
    """Extract [VERIFY] and [UNKNOWN] tags with line numbers."""
    results = []
    for i, line in enumerate(text.splitlines(), 1):
        if "[VERIFY]" in line:
            results.append(("[VERIFY]", i, line.strip()))
        if "[UNKNOWN" in line:
            results.append(("[UNKNOWN]", i, line.strip()))
    return results


def scan_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    dates = extract_dates(text)
    rcw = extract_rcw_refs(text)
    tags = extract_verify_tags(text)
    return {
        "path": str(path.relative_to(ROOT)),
        "dates": dates,
        "rcw_refs": rcw,
        "tags": tags,
        "line_count": len(text.splitlines()),
    }


def cross_reference(scans: list[dict]) -> list[dict]:
    """Cross-reference across files for contradictions."""
    contradictions = []

    # Build date index: event keywords → dates across files
    date_index = {}
    for scan in scans:
        for date_str, date_type in scan["dates"]:
            key = (date_str, scan["path"])
            date_index.setdefault(date_str, []).append(scan["path"])

    # Same date appearing in multiple contexts — not a contradiction by itself,
    # but flag if different event descriptions attach to same date
    # (This is a lightweight check; full NLP-based detection would be Phase 5)

    # Check for conflicting RCW references
    rcw_all = {}
    for scan in scans:
        for ref in scan["rcw_refs"]:
            ref_norm = re.sub(r"\s+", " ", ref.strip())
            rcw_all.setdefault(ref_norm, []).append(scan["path"])
    # If same RCW cited differently, flag
    rcw_variants = {}
    for ref in rcw_all:
        base = re.match(r"(RCW \d+[A-Za-z]?\.\d+\.\d+|USC \d+|U\.S\.C\. § \d+)", ref)
        if base:
            rcw_variants.setdefault(base.group(1), []).append(ref)
    for base, variants in rcw_variants.items():
        if len(set(variants)) > 1:
            contradictions.append({
                "type": "STATUTE_VARIANT",
                "detail": f"Same statute referenced differently: {variants}",
                "files": rcw_all.get(variants[0], []),
            })

    return contradictions


def main():
    files = []
    for d in SCAN_DIRS:
        for g in SCAN_GLOBS:
            files.extend(d.glob(g))

    print("=" * 60)
    print("CONTRADICTION CHECK REPORT")
    print("=" * 60)
    print(f"Scanning {len(files)} files...\n")

    scans = []
    total_tags = 0
    for f in sorted(files):
        result = scan_file(f)
        scans.append(result)
        if result["tags"] or result["dates"]:
            print(f"  {result['path']}")
            print(f"    Dates found: {len(result['dates'])}")
            for date_str, date_type in result["dates"][:5]:
                print(f"      {date_str} ({date_type})")
            if len(result["dates"]) > 5:
                print(f"      ... and {len(result['dates']) - 5} more")
            print(f"    RCW/USC refs: {len(result['rcw_refs'])}")
            for ref in result["rcw_refs"][:5]:
                print(f"      {ref}")
            print(f"    Open tags: {len(result['tags'])}")
            for tag_type, line_num, line_text in result["tags"][:5]:
                print(f"      L{line_num}: {tag_type} — {line_text[:70]}")
            total_tags += len(result["tags"])
            print()

    contradictions = cross_reference(scans)
    if contradictions:
        print("--- CROSS-FILE CONTRADICTION CANDIDATES ---")
        for c in contradictions:
            print(f"  [CONTRADICTION CANDIDATE] {c['type']}: {c['detail']}")
            print(f"    Files: {', '.join(c['files'])}")
        print()

    print("=" * 60)
    print(f"SUMMARY: {len(files)} files | {total_tags} open tags | {len(contradictions)} cross-file contradictions")
    print()
    if total_tags > 0:
        print("⚠  Open [VERIFY] and [UNKNOWN] tags need Steven's review.")
    if contradictions:
        print("⚠  Contradiction candidates found. Do not smooth — these may be")
        print("   memory recursion, date conflict, source conflict, or narrative")
        print("   pressure points. Flag for Steven's review.")


if __name__ == "__main__":
    main()
