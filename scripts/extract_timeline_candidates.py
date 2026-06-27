#!/usr/bin/env python3
"""
Extract timeline and statement candidates from text-readable source files.

This script does not decide what is true.
It only finds lines that may contain dates or timeline language.
Steven/author review is required before anything enters master_timeline.csv.
"""
from __future__ import annotations

import csv
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "source_ingest" / "raw"
OUT_DIR = ROOT / "source_ingest" / "processed" / "timeline_candidates"
OUT = OUT_DIR / "timeline_candidates.csv"

TEXT_EXTS = {".txt", ".md", ".csv", ".json", ".html", ".xml", ".kml", ".srt", ".vtt"}

DATE_PATTERNS = [
    r"\b\d{4}-\d{1,2}-\d{1,2}\b",
    r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",
    r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},?\s+\d{4}\b",
    r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{4}\b",
    r"\b\d{4}\b",
]
DATE_RE = re.compile("|".join(f"({p})" for p in DATE_PATTERNS), re.IGNORECASE)
KEYWORD_RE = re.compile(r"\b(wake|woke|amnesia|kidnap|kidnapp|traffick|hospital|clinic|police|FBI|food|lock|door|AI|Google|map|moved|lived|worked|assault|threat|memory|recursion|CPTSD|neuropathy|walk|talk)\b", re.IGNORECASE)


def safe_read(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="latin-1")
        except Exception:
            return None
    except Exception:
        return None


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in sorted(RAW.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTS:
            continue
        text = safe_read(path)
        if text is None:
            continue
        for idx, line in enumerate(text.splitlines(), start=1):
            clean = " ".join(line.strip().split())
            if not clean:
                continue
            date_matches = [m.group(0) for m in DATE_RE.finditer(clean)]
            keyword = bool(KEYWORD_RE.search(clean))
            if date_matches or keyword:
                rows.append({
                    "candidate_id": f"CAND-{len(rows)+1:05d}",
                    "extracted_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
                    "file_path": str(path.relative_to(ROOT)),
                    "line_number": idx,
                    "date_matches": "; ".join(date_matches),
                    "keyword_match": "yes" if keyword else "no",
                    "candidate_text": clean[:1200],
                    "review_status": "NEEDS_AUTHOR_REVIEW",
                    "promote_to_event_id": "",
                    "notes": ""
                })
    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "candidate_id", "extracted_at", "file_path", "line_number", "date_matches", "keyword_match",
            "candidate_text", "review_status", "promote_to_event_id", "notes"
        ])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} candidates to {OUT}")


if __name__ == "__main__":
    main()
