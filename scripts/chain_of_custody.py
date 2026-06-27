#!/usr/bin/env python3
"""
Chain-of-Custody Logger — Hash and log every file added to source_ingest.

Creates SHA-256 hashes and logs:
- File path
- Hash
- Date/time received
- Who provided it
- Any transformations applied

Usage:
  python3 scripts/chain_of_custody.py [file_path] [provider]
  python3 scripts/chain_of_custody.py --scan
"""
from __future__ import annotations

import csv
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CUSTODY_LOG = ROOT / "source_ingest" / "chain_of_custody.csv"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def init_log():
    if not CUSTODY_LOG.exists():
        with open(CUSTODY_LOG, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp_utc",
                "timestamp_pacific",
                "file_path",
                "sha256",
                "file_size_bytes",
                "provider",
                "transformation",
                "notes",
            ])


def log_file(path: Path, provider: str = "Steven", transformation: str = "none", notes: str = ""):
    init_log()
    hash_val = sha256_file(path)
    size = path.stat().st_size
    now_utc = datetime.now(timezone.utc).isoformat()
    now_pacific = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S PT")

    with open(CUSTODY_LOG, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            now_utc,
            now_pacific,
            str(path.relative_to(ROOT)),
            hash_val,
            size,
            provider,
            transformation,
            notes,
        ])
    print(f"  Logged: {path.name} | SHA-256: {hash_val[:16]}... | {size} bytes")


def scan_ingest():
    """Scan all files in source_ingest and log any not yet in custody log."""
    init_log()

    # Read existing log
    logged_paths = set()
    if CUSTODY_LOG.exists():
        with open(CUSTODY_LOG, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                logged_paths.add(row.get("file_path", ""))

    # Scan
    ingest_dir = ROOT / "source_ingest"
    files = []
    for ext in ["*.md", "*.csv", "*.jpg", "*.jpeg", "*.png", "*.jpeg"]:
        files.extend(ingest_dir.rglob(ext))

    new_count = 0
    for f in sorted(files):
        rel = str(f.relative_to(ROOT))
        if rel not in logged_paths:
            log_file(f, provider="scan_auto", transformation="none", notes="Auto-detected during scan")
            new_count += 1

    if new_count == 0:
        print("  All source_ingest files already logged.")
    else:
        print(f"  Logged {new_count} new files.")


def main():
    if len(sys.argv) >= 3 and sys.argv[1] != "--scan":
        path = Path(sys.argv[1])
        provider = sys.argv[2] if len(sys.argv) >= 3 else "Steven"
        log_file(path, provider)
    elif len(sys.argv) >= 2 and sys.argv[1] == "--scan":
        scan_ingest()
    else:
        print("Chain-of-Custody Logger")
        print("Usage:")
        print("  python3 scripts/chain_of_custody.py <file_path> <provider>")
        print("  python3 scripts/chain_of_custody.py --scan")
        print()
        print("Running --scan by default...")
        scan_ingest()


if __name__ == "__main__":
    main()
