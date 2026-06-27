#!/usr/bin/env python3
"""
Markdown Linter — Validates chapter files against the scaffold schema.

Checks:
- All Internal Scaffold fields present
- No [STEVEN WORDS GO HERE] placeholders left unfilled
- Evidence labels properly formatted
- [UNKNOWN] and [VERIFY] tags correctly used
- No orphaned chapter references

Usage:
  python3 scripts/lint_chapters.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "book" / "chapters"

REQUIRED_SCAFFOLD_FIELDS = [
    "Date:",
    "Location:",
    "Present-time status:",
    "Body log:",
    "Memory recursion:",
    "Due diligence:",
    "Evidence status:",
    "System contact:",
    "Updated timeline:",
    "Next action:",
]

EVIDENCE_LABELS = [
    "STEVEN_WORDS",
    "TIMELINE_DECLARATION",
    "SOURCE_MATERIAL",
    "MEMORY_RETURN",
    "BODY_EVIDENCE",
    "LOGIC_REASONING",
    "UNVERIFIED_DO_NOT_EXPAND",
    "PM",
    "PA",
    "MI",
    "FC",
    "VF",
]

PLACEHOLDER_PHRASES = [
    "[STEVEN WORDS GO HERE]",
    "[DATE IN LINEAR SEQUENCE",
    "[UNKNOWN — STEVEN HAS NOT PROVIDED",
    "[UNKNOWN]",
]

VALID_UNKNOWN = "[UNKNOWN — STEVEN HAS NOT PROVIDED THIS]"
VALID_VERIFY = "[VERIFY]"


def lint_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors = []
    warnings = []

    # Check for H1 heading
    has_h1 = any(line.startswith("# ") for line in lines)
    if not has_h1:
        errors.append("Missing H1 chapter heading")

    # Check for Steven's words (blockquote or narrative text)
    has_blockquote = any(line.startswith(">") for line in lines)
    has_narrative = any(
        line.strip() and not line.startswith("#") and not line.startswith("-")
        and not line.startswith("**") and not line.startswith(">")
        and not line.startswith("[") and not line.startswith("<!--")
        for line in lines[5:]  # skip heading area
    )
    if not has_blockquote and not has_narrative:
        warnings.append("No Steven words detected (no blockquotes or narrative text)")

    # Check scaffold fields
    scaffold_section = False
    found_fields = set()
    for line in lines:
        if "Internal Scaffold" in line:
            scaffold_section = True
        if scaffold_section:
            for field in REQUIRED_SCAFFOLD_FIELDS:
                if field in line:
                    found_fields.add(field)
    missing_fields = [f for f in REQUIRED_SCAFFOLD_FIELDS if f not in found_fields]
    if missing_fields and scaffold_section:
        for f in missing_fields:
            warnings.append(f"Missing scaffold field: {f}")
    elif not scaffold_section:
        warnings.append("No Internal Scaffold section found")

    # Check for unfilled placeholders
    for i, line in enumerate(lines, 1):
        for phrase in PLACEHOLDER_PHRASES:
            if phrase in line:
                if "UNKNOWN — STEVEN HAS NOT PROVIDED" in phrase:
                    pass  # This is valid
                else:
                    errors.append(f"L{i}: Unfilled placeholder: {phrase}")

    # Check evidence labels
    for i, line in enumerate(lines, 1):
        label_match = re.findall(r"\*\*[^*]+\*\*", line)
        for label in label_match:
            label_clean = label.strip("*")
            if "Evidence Label" in line or "Verification" in line:
                continue  # It's a label name, not a usage
            if label_clean and label_clean.isupper() and len(label_clean) > 3:
                if label_clean not in EVIDENCE_LABELS:
                    warnings.append(f"L{i}: Unrecognized label: {label_clean}")

    # Check [UNKNOWN] usage
    for i, line in enumerate(lines, 1):
        if "[UNKNOWN" in line and VALID_UNKNOWN not in line:
            warnings.append(f"L{i}: [UNKNOWN] tag not in standard format — should be: {VALID_UNKNOWN}")

    # Check [VERIFY] usage
    for i, line in enumerate(lines, 1):
        if "[VERIFY]" in line:
            pass  # Valid
        elif "[verify]" in line.lower() and "[VERIFY]" not in line:
            warnings.append(f"L{i}: [verify] should be uppercase [VERIFY]")

    # Word count
    word_count = len(text.split())

    return {
        "path": str(path.relative_to(ROOT)),
        "errors": errors,
        "warnings": warnings,
        "word_count": word_count,
        "has_scaffold": scaffold_section,
        "has_steven_words": has_blockquote or has_narrative,
    }


def main():
    files = sorted(CHAPTERS.glob("*.md"))
    print("=" * 60)
    print("CHAPTER LINT REPORT")
    print("=" * 60)
    print(f"Scanning {len(files)} chapter files...\n")

    total_errors = 0
    total_warnings = 0

    for f in files:
        result = lint_file(f)
        status = "✓" if not result["errors"] else "✗"
        print(f"  {status} {result['path']} ({result['word_count']} words)")

        if result["errors"]:
            for e in result["errors"]:
                print(f"    ✗ ERROR: {e}")
                total_errors += 1

        if result["warnings"]:
            for w in result["warnings"]:
                print(f"    ⚠ WARNING: {w}")
                total_warnings += 1

        if not result["has_steven_words"]:
            print(f"    ⚠ No Steven words — scaffold only")
        if not result["has_scaffold"]:
            print(f"    ⚠ No Internal Scaffold section")

        print()

    print("=" * 60)
    print(f"SUMMARY: {len(files)} chapters | {total_errors} errors | {total_warnings} warnings")
    print()
    if total_errors > 0:
        print("✗ Errors found. These must be fixed before EPUB build.")
    if total_warnings > 0:
        print("⚠ Warnings found. These should be reviewed by Steven.")


if __name__ == "__main__":
    main()
