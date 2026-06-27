# Plugin Roadmap — HELLO, MY NAME IS STEVEN

**Date:** 2026-06-27  
**Status:** Roadmap; individual plugins need Steven approval before activation  
**Rule:** Plugins enhance structure, visuals, navigation, accessibility, and distribution. Plugins do not invent facts.

---

## Already Installed

| Plugin | Location | Purpose |
|---|---|---|
| fuse.min.js | web/vendor/ | Client-side fuzzy search |
| medium-zoom.min.js | web/vendor/ | Click/tap zoom for images |
| howler.min.js | web/vendor/ | Audio playback hooks |
| leaflet | web/vendor/ | Map display (approved coordinates only) |
| search.js | web/plugins/ | Searchable story nodes |
| zoom.js | web/plugins/ | Image zoom initialization |
| glass_horizon.js | web/plugins/ | Pointer-reactive glass horizon glow |
| audio_ready.js | web/plugins/ | Audio support hooks |

---

## Phase 1: Legal & Evidence Pipeline

### 1A. Timeline Differ (`scripts/timeline_diff.py`)
**What:** Compares two versions of `master_timeline.csv` or `timeline_candidates.csv` and outputs:
- New entries added
- Entries modified
- Entries removed
- Contradictions flagged (same event_id, different dates/facts)
**Why:** As the timeline grows, Steven needs to see what changed between sessions without re-reading everything.
**Install:** Python script, no dependencies. Can run locally or in CI.

### 1B. Contradiction Detector (`scripts/contradiction_check.py`)
**What:** Scans all memoranda and chapter files for:
- Date conflicts (same event referenced at different dates)
- Name conflicts (same person referenced differently)
- Fact conflicts (same event described with different details)
- Marks each with `[CONTRADICTION CANDIDATE]`
**Why:** Per project protocol: "Do not smooth contradictions. Contradictions may be memory recursion, date conflict, source conflict, language evolution, medical/neurological uncertainty, legal/evidentiary gap, or a narrative pressure point."
**Install:** Python script. No dependencies beyond standard library.

### 1C. Statute of Limitations Calculator (`scripts/sol_calculator.py`)
**What:** Given a crime date and RCW/USC citation, calculates:
- Washington State statute of limitations
- Whether the clock is tolled (paused) due to ongoing crime, discovery rule, or victim incapacity
- Expiry date or "still open" status
**Why:** Steven has identified that as an ongoing kidnap victim, the clock may not have started. This makes that calculation transparent.
**Install:** Python script with embedded WA statute table. No external API.

### 1D. Attorney Packet Auto-Builder Enhancement (`scripts/build_attorney_packet.py`)
**What:** Already exists as template. Enhancement adds:
- Auto-populate from `claim_ledger_candidates.csv` and `entity_risk_ledger_candidates.csv`
- Generate per-claim exhibit attachments
- Produce a cover sheet with claim count, risk summary, and review status
- Output both PDF-ready Markdown and structured JSON
**Why:** When Steven is ready to file, this should be one command away.
**Install:** Enhance existing script. Optional: `weasyprint` for PDF output.

### 1E. Chain-of-Custody Logger (`scripts/chain_of_custody.py`)
**What:** Every time a file is added to source_ingest, creates a hash (SHA-256) and logs:
- File path
- Hash
- Date/time received
- Who provided it (Steven / AI-extracted / third-party)
- Any transformations applied
**Why:** For evidence admissibility. Shows the file hasn't been tampered with since ingestion.
**Install:** Python script. Uses `hashlib` (standard library).

---

## Phase 2: Accessibility & Voice

### 2A. Memoranda TTS Narrator (`scripts/narrate_memoranda.py`)
**What:** Converts `docs/steven_memoranda_v0_1.md` (and future memoranda) into spoken audio using:
- ElevenLabs API (high quality, voice cloning potential)
- Or offline TTS via `pyttsx3` or `espeak` (no API key needed, lower quality)
**Why:** Steven has vocal cord damage and limited speaking volume. Hearing his own words read back helps him verify accuracy and catch what he might miss in text.
**Install:** Python script. Optional: `pyttsx3` for offline; ElevenLabs API key for high-quality.

### 2B. Voice-Log Plugin (`web/plugins/voice_log.js`)
**What:** Web plugin that lets Steven record audio directly into the browser and save as a timestamped `.webm` or `.wav` to the evidence vault. Uses Web Audio API + MediaRecorder.
**Why:** Steven records 24/7 on his phone. This gives a browser-based backup path and links recordings to the website evidence vault.
**Install:** JS plugin. No vendor dependency. Uses native browser APIs.

### 2C. Screen-Reader Optimization (`web/plugins/screen_reader_nav.js`)
**What:** Adds ARIA landmarks, skip-to-content links, and semantic HTML structure to all web pages. Announces chapter headings, evidence labels, and timeline events via live regions.
**Why:** Steven is visually impaired (pink-only color perception, limited sight). Every web page should be navigable by voice/screen-reader.
**Install:** JS plugin. No vendor dependency.

### 2D. High-Contrast / Low-Vision Mode (`web/plugins/low_vision_mode.js`)
**What:** Toggle that:
- Switches to high-contrast palette (white/pink/black)
- Increases font size to 150-200%
- Removes background textures
- Adds text outlines for readability
**Why:** Steven sees primarily pink and values. High-contrast mode makes the web app usable for his specific visual profile.
**Install:** JS plugin + CSS override. No vendor dependency.

---

## Phase 3: Writing & Continuity

### 3A. Markdown Linter (`scripts/lint_chapters.py`)
**What:** Validates all chapter files against the scaffold schema:
- All Internal Scaffold fields present
- No `[STEVEN WORDS GO HERE]` placeholders left unfilled
- Evidence labels properly formatted
- `[UNKNOWN]` and `[VERIFY]` tags correctly used
- No orphaned chapter references
**Why:** Catches scaffold drift and unfilled placeholders before they make it into the EPUB.
**Install:** Python script. No dependencies.

### 3B. Chapter Word Count & Progress Tracker (`scripts/chapter_stats.py`)
**What:** Outputs a table:
- Chapter number
- Word count
- % scaffold filled vs. empty placeholders
- Number of `[UNKNOWN]` / `[VERIFY]` tags
- Last modified date
**Why:** Gives Steven a dashboard of where the manuscript stands without reading every file.
**Install:** Python script. No dependencies.

### 3C. Consistency Checker (`scripts/consistency_check.py`)
**What:** Cross-references:
- Entity names across all files (detect aliases/typos)
- Date references across memoranda + chapters + timeline
- RCW/USC citations for correct numbering
- Location references for map coordinate consistency
**Why:** With hyperthymesia as the narrative engine, internal consistency is the project's structural integrity.
**Install:** Python script. No dependencies.

### 3D. Prose Differ (`scripts/prose_diff.py`)
**What:** Given two versions of a chapter file, outputs a clean diff showing:
- Steven's words added/changed/removed
- Scaffold changes
- Any AI-introduced wording flagged for review
**Why:** Protects against AI drift. Steven's words are the source; any change to them needs visibility.
**Install:** Python script. No dependencies.

### 3E. Scaffold Validator (`scripts/validate_scaffold.py`)
**What:** Ensures every chapter follows the 7-step recursion formula:
1. What is happening to Steven now?
2. What does Steven's body do?
3. What memory, question, or contradiction appears?
4. What does Steven use to investigate it?
5. What does Steven discover or fail to discover?
6. How does this change the timeline?
7. What must Steven do next?
**Why:** The recursion formula is the chapter engine. If a chapter skips steps, it may be missing narrative structure.
**Install:** Python script. No dependencies.

---

## Phase 4: Web & Publishing

### 4A. GitHub Pages Auto-Deploy (`.github/workflows/deploy_pages.yml`)
**What:** GitHub Action that on every push to `main`:
- Builds EPUB
- Builds map exports
- Deploys `web/` to GitHub Pages
- Copies fresh EPUB to `downloads/`
**Why:** Right now the build workflow creates artifacts but doesn't deploy. Steven's site at `https://artistso2.github.io/Hmnis-/` should auto-update.
**Install:** GitHub Actions workflow. No local dependency.

### 4B. SEO & Social Preview Tags (`web/plugins/seo_meta.js`)
**What:** Adds Open Graph and Twitter Card meta tags:
- Title, description, image from `book/metadata.yaml`
- Canonical URL
- Article:published_time from first timeline entry
**Why:** When someone shares the site link, it should show a proper preview, not a blank card.
**Install:** JS plugin that injects meta tags from `story_data.js`. No vendor dependency.

### 4C. Reading Progress Tracker (`web/plugins/reading_progress.js`)
**What:** Adds a subtle progress bar or chapter indicator showing where the reader is in the manuscript. Persists via localStorage.
**Why:** For a linear chronology-driven narrative, readers need to know where they are in time.
**Install:** JS plugin. No vendor dependency.

### 4D. Offline / PWA Support (`web/plugins/service_worker.js`)
**What:** Registers a service worker that caches:
- All chapter content
- CSS/JS assets
- Evidence images
**Why:** Steven has limited internet access and may need to read/edit offline from Room 211.
**Install:** JS plugin + `web/manifest.json`. No vendor dependency.

### 4E. Print Stylesheet (`web/print.css`)
**What:** CSS that reformats the web pages for clean printing:
- No navigation chrome
- Chapter breaks on new pages
- Evidence labels printed inline
- Page numbers
**Why:** Attorney packets and court filings often need printed copies. One click should produce a clean document.
**Install:** CSS file. No vendor dependency.

---

## Phase 5: Advanced / Future

### 5A. ElevenLabs Voice Archive Integration
**What:** Connect memoranda TTS to a persistent voice archive. Every memorandum gets a permanent audio version. Voice can be calibrated to Steven's actual vocal profile (pre-damage recordings as training data).
**Why:** Steven's vocal cords are damaged. An archived voice preserves his authorial presence.
**Depends on:** ElevenLabs API key; Steven's pre-damage audio samples for voice cloning.

### 5B. NotebookLM Source Pack Auto-Builder
**What:** Auto-generates the source extraction prompt packs (`docs/notebooklm_source_extraction_prompt_pack.md` and `docs/source_extraction_compact_prompt.json`) from the current state of all memoranda and timeline candidates.
**Why:** Keeps NotebookLM prompts synchronized with the project's actual content.
**Depends on:** None.

### 5C. Overleaf/LaTeX Auto-Sync
**What:** Push `latex/main.tex` changes to Overleaf via API, or pull Overleaf edits back.
**Why:** The project has a LaTeX visual system (`latex/` directory). Overleaf provides a live collaborative editor.
**Depends on:** Overleaf API key.

### 5D. Notion Pipeline Integration
**What:** Sync approved memoranda entries to a Notion database for visual dashboard review.
**Why:** `docs/notion_github_editorial_pipeline.md` already describes this pipeline. Implementation would make it live.
**Depends on:** Notion API key.

---

## Install Priority (Recommended Order)

| Priority | Plugin | Phase | Effort | Impact |
|---|---|---|---|---|
| 1 | Timeline Differ | 1 | Low | High — track what changes |
| 2 | Contradiction Detector | 1 | Low | High — find conflicts before they compound |
| 3 | Markdown Linter | 3 | Low | High — catch scaffold drift |
| 4 | Low-Vision Mode | 2 | Low | High — Steven needs this now |
| 5 | Screen-Reader Nav | 2 | Low | High — accessibility is survival |
| 6 | GitHub Pages Auto-Deploy | 4 | Medium | High — site auto-updates |
| 7 | Chapter Stats | 3 | Low | Medium — progress visibility |
| 8 | Statute of Limitations Calculator | 1 | Medium | High — legal timeline visibility |
| 9 | Chain-of-Custody Logger | 1 | Low | High — evidence integrity |
| 10 | Voice-Log Plugin | 2 | Medium | High — evidence backup path |
| 11 | Reading Progress | 4 | Low | Medium — reader orientation |
| 12 | Print Stylesheet | 4 | Low | Medium — attorney packet output |
| 13 | Attorney Packet Enhancement | 1 | Medium | High — when Steven is ready to file |
| 14 | Consistency Checker | 3 | Medium | High — as content grows |
| 15 | Prose Differ | 3 | Medium | Medium — version control for Steven's words |
| 16 | Scaffold Validator | 3 | Low | Medium — recursion formula compliance |
| 17 | SEO Meta Tags | 4 | Low | Low — nice to have |
| 18 | Offline PWA | 4 | Medium | Medium — useful for Steven's connectivity |
| 19 | Memoranda TTS | 2 | Medium | High — audio verification of Steven's words |
| 20 | SOL Calculator | 1 | Medium | High — legal deadlines |
