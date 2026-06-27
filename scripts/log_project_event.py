#!/usr/bin/env python3
"""Append timestamped events to project_log/project_events.csv using Pacific Time and UTC."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "project_log" / "project_events.csv"
PACIFIC = ZoneInfo("America/Los_Angeles")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", default="PROJECT_EVENT", help="Event type")
    parser.add_argument("--title", required=True, help="Event title")
    parser.add_argument("--summary", default="", help="Event summary")
    parser.add_argument("--source", default="", help="Source/file reference")
    parser.add_argument("--actor", default="Arena Agent", help="Actor")
    parser.add_argument("--notes", default="", help="Notes")
    args = parser.parse_args()

    now_utc = datetime.now(timezone.utc)
    now_pt = now_utc.astimezone(PACIFIC)
    date_id = now_pt.strftime("%Y-%m-%d")

    rows = []
    if LOG.exists():
        with LOG.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    count_today = sum(1 for r in rows if r.get("event_id", "").startswith(f"EVTLOG-{date_id}")) + 1
    event_id = f"EVTLOG-{date_id}-{count_today:04d}"

    fieldnames = ["event_id", "created_at_pacific", "created_at_utc", "event_type", "title", "summary", "source_or_file", "actor", "notes"]
    write_header = not LOG.exists() or LOG.stat().st_size == 0
    with LOG.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow({
            "event_id": event_id,
            "created_at_pacific": now_pt.isoformat(timespec="seconds"),
            "created_at_utc": now_utc.isoformat(timespec="seconds"),
            "event_type": args.type,
            "title": args.title,
            "summary": args.summary,
            "source_or_file": args.source,
            "actor": args.actor,
            "notes": args.notes,
        })
    print(event_id)


if __name__ == "__main__":
    main()
