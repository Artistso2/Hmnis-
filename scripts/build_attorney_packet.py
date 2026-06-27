#!/usr/bin/env python3
"""Create a timestamped attorney-ready packet from the template."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "legal" / "attorney_packet_template.md"
OUTDIR = ROOT / "attorney_packets"
PACIFIC = ZoneInfo("America/Los_Angeles")


def slug(text: str) -> str:
    return "".join(c.lower() if c.isalnum() else "-" for c in text).strip("-").replace("--", "-")[:80]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--purpose", default="Attorney/editorial review")
    args = parser.parse_args()

    now_utc = datetime.now(timezone.utc)
    now_pt = now_utc.astimezone(PACIFIC)
    packet_id = f"ATTY-{now_pt.strftime('%Y-%m-%d-%H%M%S')}-{slug(args.title)}"
    content = TEMPLATE.read_text(encoding="utf-8")
    content = content.replace("- Packet ID:", f"- Packet ID: {packet_id}")
    content = content.replace("- Created at Pacific:", f"- Created at Pacific: {now_pt.isoformat(timespec='seconds')}")
    content = content.replace("- Created at UTC:", f"- Created at UTC: {now_utc.isoformat(timespec='seconds')}")
    content = content.replace("- Review purpose:", f"- Review purpose: {args.purpose}")
    content = f"# {args.title}\n\n" + content

    OUTDIR.mkdir(exist_ok=True)
    path = OUTDIR / f"{packet_id}.md"
    path.write_text(content, encoding="utf-8")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
