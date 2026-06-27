# HELLO, MY NAME IS STEVEN

Author-controlled novel scaffolding, EPUB source, and visual novel web application framework.

## Project Purpose

This repository is designed to preserve and organize the novel **HELLO, MY NAME IS STEVEN** as an author-controlled, hyper-realistic, chronology-driven literary project.

The controlling rule of the project:

> Steven’s words are the source. Steven’s verbiage is the voice. Steven’s chronology is the spine. Steven’s perspective is the camera.

AI tools may assist with formatting, indexing, continuity checking, EPUB packaging, and web presentation. AI tools may **not** invent names, facts, motives, agencies, diagnoses, scenes, dialogue, or missing timeline material.

## Repository Structure

```text
hello-my-name-is-steven/
├── README.md
├── LICENSE.txt
├── book/
│   ├── metadata.yaml
│   ├── manuscript_order.txt
│   └── chapters/
│       ├── 00_front_matter.md
│       ├── 01_june_2025_waking.md
│       └── 02_body_does_not_match_archive.md
├── docs/
│   ├── author_control_scaffold_v0_2.md
│   ├── archive_scaffolding_v0_1.md
│   ├── ai_use_protocol.md
│   └── evidence_ledger_template.csv
├── scripts/
│   ├── build_epub.py
│   └── serve_local.py
└── web/
    ├── index.html
    ├── app.js
    ├── style.css
    └── story_data.js
```

## GitHub Pages / “Magic Link” Web App

The `web/` folder is a static visual novel application. It uses plain HTML, CSS, and JavaScript. No external CDN is required.

To publish with GitHub Pages:

1. Push this repository to GitHub.
2. Go to **Settings → Pages**.
3. Choose branch: `main`.
4. Choose folder: `/web` if GitHub offers it, or move the `web/` contents to `/docs` for GitHub Pages compatibility.
5. GitHub will provide a public URL.

If GitHub Pages does not allow `/web` directly, use one of these options:

- Rename `web/` to `docs/` for Pages.
- Or configure a GitHub Action later.

## EPUB Build

The project includes a dependency-free Python EPUB builder:

```bash
python3 scripts/build_epub.py
```

The generated EPUB will appear in:

```text
output/hello_my_name_is_steven.epub
```

## Local Web Preview

```bash
python3 scripts/serve_local.py
```

Then open:

```text
http://localhost:8000/web/
```

## Author-Control Rule

When adding manuscript content:

- Use Steven’s provided language first.
- Mark unknowns as `[UNKNOWN — STEVEN HAS NOT PROVIDED THIS]`.
- Mark verification needs as `[VERIFY]`.
- Do not smooth contradictions.
- Do not invent connective facts.
- Preserve the linear present timeline beginning in June 2025.
- Past material enters only through memory recursion, evidence review, or due diligence.


## Visual Direction: Glass Horizons

The current web interface uses author-provided visual material from `source_ingest/visuals/`, optimized into `web/assets/`.

Visual rule:

> Glass horizons. Something new. Personal artworks and pictures. The faces are the author's own face. The website should feel luminous, personal, forensic, digital, fragile, and forward-facing without losing the author-control rule.

The web app uses the images as evidence/memory/signal cards. They do not create plot facts by themselves.

## Source Ingest / Timeline / Map Roadmap

The project now includes an author-controlled ingest pipeline:

```text
source_ingest/raw/        # drop original documents, chats, logs, map exports
source_ingest/processed/  # generated timeline/statement candidates
timeline/master_timeline.csv
maps/locations.csv
maps/google_my_maps_import.csv
maps/locations.kml
maps/locations.geojson
web/map.html
```

### Extract timeline candidates

```bash
python3 scripts/extract_timeline_candidates.py
```

This does not decide truth. It only finds candidate lines for author review.

### Build Google Maps / My Maps exports

```bash
python3 scripts/build_map_exports.py
```

This generates CSV, KML, and GeoJSON from approved locations only.

### Timeline map page

```text
https://artistso2.github.io/Hmnis-/web/map.html
```

No Google API key is stored in the public repo. Use `maps/google_my_maps_import.csv` or `maps/locations.kml` to import approved locations into Google My Maps.

## NotebookLM / Gemini JSON Extraction Prompts

Prompt files for large source batches are stored in:

```text
docs/source_extraction_master_prompt.json
docs/source_extraction_compact_prompt.json
docs/notebooklm_source_extraction_prompt_pack.md
```

Use these to extract timeline events, statement banks, contradictions, locations, entities, chapter candidates, and visual novel nodes from AI chat exports or other source documents.

## Notion Editorial Pipeline

Notion can be used as the editorial CMS and approval board before GitHub publication.

See:

```text
docs/notion_github_editorial_pipeline.md
```

## Paper Writ / Overleaf-Inspired Prototype

A softer LaTeX/Overleaf-inspired visual direction has been added:

```text
web/paper.html
web/paper.css
latex/main.tex
latex/hmnis.sty
docs/latex_overleaf_visual_system.md
```

This direction uses soft ocean hush, pastel textured paper, legal/source boxes, marginal-note thinking, and title-page gravity:

```text
Hello, My Name is Steven
The Lived Experience of Habeas Corpus
Lex Duodecim Tabularum
```

## Governance / Legal / Timestamp Protocol

The project now includes a governance layer:

```text
governance/project_governance_protocol.md
governance/options_protocol.md
project_log/decision_log.csv
project_log/project_events.csv
legal/claim_ledger.csv
legal/entity_risk_ledger.csv
legal/publication_review_checklist.md
legal/attorney_packet_template.md
scripts/log_project_event.py
scripts/new_decision.py
scripts/build_attorney_packet.py
```

Default lived-time standard:

```text
Pacific Time / America/Los_Angeles
Ocean Shores, Washington 98569 context
```

Public/legal review principle:

```text
Private raw first-person Steven voice; public materials attorney-ready, source-grounded, transparent, and reviewed.
```

## Project Index / Breadcrumb System

The root `index.html` is now the single magic-link home base for the entire project:

```text
https://artistso2.github.io/Hmnis-/
```

Every major HTML page in `web/` loads:

```text
web/navigation.css
web/navigation.js
```

This injects a breadcrumb/top navigation bar back to the Project Index and key project pages.
