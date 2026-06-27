# Plugins and Tooling

This project now includes a small plugin layer for structure, visuals, and distribution.

## Browser Plugins / Vendors

Vendored locally in `web/vendor/`:

- `fuse.min.js` — client-side fuzzy search for story nodes.
- `medium-zoom.min.js` — click/tap zoom for images and evidence cards.
- `howler.min.js` — future-ready support for author-provided voice logs or spoken-word clips.

Custom project plugins in `web/plugins/`:

- `search.js` — searchable visual novel nodes.
- `zoom.js` — initializes image zoom.
- `glass_horizon.js` — subtle pointer-reactive glass horizon glow.
- `audio_ready.js` — declares future audio support without inventing audio content.

## Distribution Tools

- `scripts/build_epub.py` builds the EPUB without external Python dependencies.
- `downloads/hello_my_name_is_steven.epub` is a public downloadable EPUB artifact for the GitHub Pages site.
- `.github/workflows/build.yml` builds and uploads EPUB artifacts on push.

## Author-Control Rule

Plugins may improve search, navigation, visual presentation, accessibility, and distribution.

Plugins may not invent facts, names, scenes, dialogue, evidence, diagnoses, legal conclusions, or story content.

## Map / Roadmap Tooling

Added:

- `web/vendor/leaflet/` — local Leaflet library for future approved-coordinate map display.
- `web/map.html` — public map/roadmap page.
- `web/map.js` — loads approved GeoJSON only.
- `scripts/build_map_exports.py` — creates Google My Maps CSV, KML, and GeoJSON.
- `maps/locations.csv` — author-approved location ledger.
- `timeline/master_timeline.csv` — canonical author-approved timeline.
- `scripts/extract_timeline_candidates.py` — extracts candidate dates/statements from text-readable files for review.

No Google Maps API key is committed to the repository. For Google My Maps, use the generated CSV or KML import files.
