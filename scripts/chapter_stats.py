#!/usr/bin/env python3
"""
Chapter Statistics — Word counts, scaffold fill %, and open tags.

Usage:
  python3 scripts/chapter_stats.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "book" / "chapters"


def count_placeholder_fields(text: str) -> tuple[int, int]:
    """Count total scaffold fields vs filled fields."""
    scaffold_start = False
    total = 0
    filled = 0
    for line in text.splitlines():
        if "Internal Scaffold" in line:
            scaffold_start = True
            continue
        if scaffold_start:
            if line.startswith("- **"):
                total += 1
                # Check if the value after the colon is more than just a placeholder
                if ":" in line:
                    value = line.split(":", 1)[1].strip()
                    if value and "[STEVEN WORDS GO HERE]" not in value:
                        filled += 1
            elif line.startswith("#") and scaffold_start:
                break  # End of scaffold
    return total, filled


def count_tags(text: str) -> dict:
    unknown = len(re.findall(r"\[UNKNOWN", text))
    verify = len(re.findall(r"\[VERIFY\]", text))
    contradiction = len(re.findall(r"\[CONTRADICTION", text))
    return {"UNKNOWN": unknown, "VERIFY": verify, "CONTRADICTION": contradiction}


def main():
    files = sorted(CHAPTERS.glob("*.md"))
    print("=" * 70)
    print("CHAPTER STATISTICS")
    print("=" * 70)
    print(f"{'Chapter':<40} {'Words':>6} {'Scaffold':>10} {'Tags':>10}")
    print("-" * 70)

    total_words = 0
    total_filled = 0
    total_scaffold = 0
    total_tags_all = {"UNKNOWN": 0, "VERIFY": 0, "CONTRADICTION": 0}

    for f in files:
        text = f.read_text(encoding="utf-8")
        words = len(text.split())
        scaffold_total, scaffold_filled = count_placeholder_fields(text)
        tags = count_tags(text)

        fill_pct = f"{scaffold_filled}/{scaffold_total}" if scaffold_total else "n/a"
        tag_str = "/".join(str(v) for v in tags.values()) if any(tags.values()) else "0"

        # Short chapter name
        name = f.stem.replace("_", " ").title()
        if len(name) > 38:
            name = name[:36] + ".."

        print(f"  {name:<38} {words:>6} {fill_pct:>10} {tag_str:>10}")

        total_words += words
        total_filled += scaffold_filled
        total_scaffold += scaffold_total
        for k in total_tags_all:
            total_tags_all[k] += tags[k]

    print("-" * 70)
    fill_total = f"{total_filled}/{total_scaffold}" if total_scaffold else "n/a"
    tag_total = "/".join(str(v) for v in total_tags_all.values())
    print(f"  {'TOTAL':<38} {total_words:>6} {fill_total:>10} {tag_total:>10}")
    print()

    if total_scaffold > 0:
        pct = (total_filled / total_scaffold) * 100
        print(f"  Scaffold fill rate: {pct:.0f}%")
    print(f"  Open [UNKNOWN] tags: {total_tags_all['UNKNOWN']}")
    print(f"  Open [VERIFY] tags:  {total_tags_all['VERIFY']}")
    print()


if __name__ == "__main__":
    main()
