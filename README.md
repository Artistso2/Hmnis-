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
