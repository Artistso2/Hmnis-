# Notion + GitHub Editorial Pipeline

## Objective

Use Notion AI / Notion databases as the human editorial command center, and use GitHub as the public build/distribution system.

## Clean Division of Labor

| Tool | Best Job |
|---|---|
| NotebookLM | Batch source extraction from many documents. |
| Gemini / other LLMs | Alternate extraction, critique, rewriting after source lock. |
| Notion | Editorial CMS, review board, status tracker, chapter board, approval layer. |
| GitHub | Version control, public website, EPUB build, map exports, CI/CD. |
| GitHub Actions | Automated build/check pipeline. |

## Important Distinction

Notion itself is not the CI/CD engine. GitHub Actions should remain the CI/CD engine.

Notion can be used as:

- source tracker,
- timeline review board,
- chapter kanban,
- statement bank,
- locations database,
- contradiction ledger,
- public/private approval dashboard.

Then GitHub Actions can pull approved data from Notion or receive exported CSV/JSON files and rebuild the site/EPUB/map exports.

## Recommended Notion Databases

### 1. Sources

Properties:

- `source_id`
- `title`
- `file/link`
- `source_type`
- `date_range`
- `platform`
- `processing_status`
- `priority`
- `public/private`
- `notes`

### 2. Timeline Events

Properties:

- `event_id`
- `start_date`
- `time_text`
- `timeline_layer`
- `title`
- `steven_words`
- `source_id`
- `verification_status`
- `map_relevant`
- `approved_for_public`

### 3. Statement Bank

Properties:

- `statement_id`
- `exact_quote`
- `category`
- `emotional_register`
- `possible_book_use`
- `source_id`
- `approval_status`

### 4. Locations

Properties:

- `location_id`
- `label`
- `address_or_description`
- `city`
- `state`
- `latitude`
- `longitude`
- `source_id`
- `verification_status`
- `public_display`

### 5. Contradictions

Properties:

- `contradiction_id`
- `issue`
- `version_A`
- `version_B`
- `sources`
- `why_it_matters`
- `next_verification_step`
- `preserve_as_story_tension`

### 6. Chapters

Properties:

- `chapter_id`
- `title`
- `present_month`
- `body_focus`
- `memory_trigger`
- `due_diligence_action`
- `source_documents`
- `draft_status`
- `approved_for_epub`

### 7. Visual Novel Nodes

Properties:

- `node_id`
- `date`
- `location`
- `speaker`
- `node_text`
- `image_motif`
- `tags`
- `choices`
- `source_id`
- `verification_status`
- `approved_for_web`

## CI/CD Pattern

### Manual/Low-Risk Pattern

1. Upload files to NotebookLM.
2. Run JSON extraction prompt.
3. Paste extracted tables into Notion databases.
4. Steven approves rows in Notion.
5. Export approved tables as CSV.
6. Commit CSV to GitHub.
7. GitHub Actions rebuilds EPUB/map/site.

### Automated Pattern

1. Store Notion database IDs and integration token in GitHub repository secrets.
2. GitHub Action pulls approved rows from Notion.
3. Action writes:
   - `timeline/master_timeline.csv`
   - `maps/locations.csv`
   - `web/story_data.js` or `web/data/story_nodes.json`
4. Action rebuilds EPUB/map/site.

Required repository secrets would likely be:

```text
NOTION_TOKEN
NOTION_SOURCES_DB_ID
NOTION_TIMELINE_DB_ID
NOTION_STATEMENTS_DB_ID
NOTION_LOCATIONS_DB_ID
NOTION_CHAPTERS_DB_ID
NOTION_VISUAL_NODES_DB_ID
```

## Why Not Automate Too Early

Automation is useful only after the data model stabilizes.

For now, the safest path is:

```text
NotebookLM extraction → Notion review → approved CSV/JSON → GitHub build
```

Once the approval fields are stable, we can build the Notion-to-GitHub sync.

## Author-Control Rule

Notion AI can suggest, group, summarize, or extract.

It cannot become the author.

Every public item must be traceable to:

- Steven's words,
- a source file,
- a timeline event,
- or an author-approved editorial decision.
