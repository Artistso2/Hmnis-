#!/usr/bin/env python3
"""
Timeline Differ — Compares two versions of a timeline CSV and outputs changes.

Usage:
  python3 scripts/timeline_diff.py [old.csv] [new.csv]

If only one file given, compares against git HEAD version.
If no files given, compares timeline_candidates.csv against last committed version.
"""
from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_csv(path: Path) -> dict[str, dict]:
    """Read a timeline CSV keyed by candidate_id or event_id."""
    rows = {}
    if not path.exists():
        return rows
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row.get("candidate_id") or row.get("event_id") or ""
            if key:
                rows[key] = row
    return rows


def diff(old: dict[str, dict], new: dict[str, dict]) -> dict:
    added = {k: new[k] for k in new if k not in old}
    removed = {k: old[k] for k in old if k not in new}
    modified = {}
    for k in old:
        if k in new and old[k] != new[k]:
            changed_fields = {}
            for field in old[k]:
                if old[k].get(field) != new[k].get(field):
                    changed_fields[field] = {
                        "old": old[k].get(field, ""),
                        "new": new[k].get(field, ""),
                    }
            if changed_fields:
                modified[k] = changed_fields
    contradictions = []
    for k in modified:
        fields = modified[k]
        if "date_matches" in fields or "start_date" in fields:
            contradictions.append({
                "id": k,
                "type": "DATE_CONFLICT",
                "fields": list(fields.keys()),
                "detail": fields,
            })
        if "event_title" in fields or "candidate_text" in fields:
            contradictions.append({
                "id": k,
                "type": "FACT_CONFLICT",
                "fields": list(fields.keys()),
                "detail": fields,
            })
    return {
        "added": added,
        "removed": removed,
        "modified": modified,
        "contradiction_candidates": contradictions,
        "summary": {
            "added_count": len(added),
            "removed_count": len(removed),
            "modified_count": len(modified),
            "contradiction_count": len(contradictions),
        },
    }


def print_report(result: dict):
    s = result["summary"]
    print("=" * 60)
    print("TIMELINE DIFF REPORT")
    print("=" * 60)
    print(f"  Added:      {s['added_count']}")
    print(f"  Removed:    {s['removed_count']}")
    print(f"  Modified:   {s['modified_count']}")
    print(f"  Contradictions: {s['contradiction_count']}")
    print()

    if result["added"]:
        print("--- ADDED ---")
        for k, row in result["added"].items():
            date = row.get("date_matches") or row.get("start_date") or "?"
            text = row.get("candidate_text") or row.get("event_title") or ""
            print(f"  {k} | {date} | {text[:80]}")
        print()

    if result["removed"]:
        print("--- REMOVED ---")
        for k, row in result["removed"].items():
            date = row.get("date_matches") or row.get("start_date") or "?"
            text = row.get("candidate_text") or row.get("event_title") or ""
            print(f"  {k} | {date} | {text[:80]}")
        print()

    if result["modified"]:
        print("--- MODIFIED ---")
        for k, fields in result["modified"].items():
            print(f"  {k}:")
            for field, vals in fields.items():
                print(f"    {field}: '{vals['old'][:60]}' → '{vals['new'][:60]}'")
        print()

    if result["contradiction_candidates"]:
        print("--- CONTRADICTION CANDIDATES ---")
        for c in result["contradiction_candidates"]:
            print(f"  [CONTRADICTION CANDIDATE] {c['id']} | {c['type']}")
            for field, vals in c["detail"].items():
                print(f"    {field}: '{vals['old'][:60]}' vs '{vals['new'][:60]}'")
        print()


def main():
    if len(sys.argv) >= 3:
        old_path = Path(sys.argv[1])
        new_path = Path(sys.argv[2])
    elif len(sys.argv) == 2:
        new_path = Path(sys.argv[1])
        old_path = new_path
    else:
        new_path = ROOT / "source_ingest/processed/timeline_candidates/timeline_candidates.csv"
        old_path = new_path

    # Try to get the committed version via git
    try:
        git_output = subprocess.run(
            ["git", "show", f"HEAD:{old_path.relative_to(ROOT)}"],
            capture_output=True, text=True, cwd=ROOT,
        )
        if git_output.returncode == 0:
            tmp = ROOT / ".tmp_old_timeline.csv"
            tmp.write_text(git_output.stdout, encoding="utf-8")
            old = read_csv(tmp)
            tmp.unlink(missing_ok=True)
        else:
            old = {}
    except Exception:
        old = {}

    new = read_csv(new_path)
    result = diff(old, new)
    print_report(result)

    if result["summary"]["contradiction_count"] > 0:
        print("⚠  Contradiction candidates found. Do not smooth — these may be")
        print("   memory recursion, date conflict, source conflict, or narrative")
        print("   pressure points. Flag for Steven's review.")


if __name__ == "__main__":
    main()
