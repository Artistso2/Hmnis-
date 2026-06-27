# Source Ingest

This folder is for Steven's raw source material.

## Core Rule

Raw source files are not rewritten here.

They are preserved as the author provides them so every timeline event, statement, map point, chapter node, EPUB passage, or visual novel scene can be traced back to Steven's actual words and actual files.

## Folder Layout

```text
source_ingest/
├── raw/
│   ├── documents/        # PDFs, DOCX exports, letters, notes, reports
│   ├── text_messages/    # exported chats, screenshots OCR, message logs
│   ├── voice_logs/       # transcripts or audio metadata
│   ├── medical/          # medical records or author notes about medical records
│   ├── legal/            # legal filings, complaints, police records, tenant docs
│   ├── digital_exports/  # account logs, AI chats, GitHub exports, Google exports
│   └── map_exports/      # KML, KMZ, CSV, Google My Maps exports
├── visuals/              # author-provided images/artwork already preserved here
└── processed/
    ├── timeline_candidates/
    └── statement_candidates/
```

## Ingest Protocol

When Steven provides a file:

1. Put the original file in the appropriate `source_ingest/raw/` folder.
2. Add one row to `source_manifest.csv`.
3. Run `scripts/extract_timeline_candidates.py` if the file is text-readable.
4. Review the extracted candidates manually.
5. Promote only approved items into `timeline/master_timeline.csv`.
6. Promote only approved map items into `maps/locations.csv`.

## No Hallucination Rule

If a date, address, location, person, agency, diagnosis, or event is not in Steven's source material, do not add it.

If it appears in the source but needs verification, mark it:

```text
[VERIFY]
```

If it is unknown, mark it:

```text
[UNKNOWN — STEVEN HAS NOT PROVIDED THIS]
```
