#!/usr/bin/env python3
"""Append a timestamped decision to project_log/decision_log.csv."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "project_log" / "decision_log.csv"
PACIFIC = ZoneInfo("America/Los_Angeles")

FIELDNAMES = [
    "decision_id", "created_at_pacific", "created_at_utc", "decision_area", "question",
    "options_presented", "selected_option", "selected_by", "rationale", "impact_level",
    "requires_attorney_review", "notes"
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--area", required=True)
    parser.add_argument("--question", required=True)
    parser.add_argument("--options", default="")
    parser.add_argument("--selected", required=True)
    parser.add_argument("--selected-by", default="Steven Owens")
    parser.add_argument("--rationale", default="")
    parser.add_argument("--impact", choices=["low", "medium", "high"], default="medium")
    parser.add_argument("--attorney-review", choices=["yes", "no"], default="no")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    now_utc = datetime.now(timezone.utc)
    now_pt = now_utc.astimezone(PACIFIC)
    date_id = now_pt.strftime("%Y-%m-%d")

    rows = []
    if LOG.exists():
        with LOG.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    count_today = sum(1 for r in rows if r.get("decision_id", "").startswith(f"DEC-{date_id}")) + 1
    decision_id = f"DEC-{date_id}-{count_today:04d}"

    write_header = not LOG.exists() or LOG.stat().st_size == 0
    with LOG.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow({
            "decision_id": decision_id,
            "created_at_pacific": now_pt.isoformat(timespec="seconds"),
            "created_at_utc": now_utc.isoformat(timespec="seconds"),
            "decision_area": args.area,
            "question": args.question,
            "options_presented": args.options,
            "selected_option": args.selected,
            "selected_by": args.selected_by,
            "rationale": args.rationale,
            "impact_level": args.impact,
            "requires_attorney_review": args.attorney_review,
            "notes": args.notes,
        })
    print(decision_id)


if __name__ == "__main__":
    main()
