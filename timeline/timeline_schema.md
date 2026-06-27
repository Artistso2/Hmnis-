# Master Timeline Schema

| Field | Meaning |
|---|---|
| `event_id` | Unique event ID. Example: `EVT-2025-06-0001`. |
| `start_date` | Date or approximate date. Use ISO format when exact. |
| `end_date` | Optional. |
| `time_text` | Exact wording when date/time is approximate, e.g. `June 2025`. |
| `timeline_layer` | `PRESENT_LINEAR`, `MEMORY_RECURSION`, `DUE_DILIGENCE`, `BODY_LOG`, `SYSTEM_CONTACT`, `DIGITAL_LOG`, `MAP_POINT`. |
| `location_id` | Link to `maps/locations.csv` when applicable. |
| `event_title` | Short title. |
| `steven_words` | Steven's actual words or a tightly quoted phrase. |
| `summary_no_new_facts` | Organizational summary only; no invented details. |
| `source_id` | Link to `source_ingest/source_manifest.csv`. |
| `evidence_label` | `STEVEN_WORDS`, `TIMELINE_DECLARATION`, `SOURCE_MATERIAL`, `MEMORY_RETURN`, `BODY_EVIDENCE`, `LOGIC_REASONING`, `UNVERIFIED_DO_NOT_EXPAND`. |
| `verification_status` | `AUTHOR_DECLARED`, `SOURCE_EXTRACTED`, `NEEDS_REVIEW`, `VERIFIED`, `CONFLICT`, `FICTIONALIZED`. |
| `map_relevant` | `yes` or `no`. |
| `notes` | Internal notes. |

## Evidence Labels

- **STEVEN_WORDS** — direct author/protagonist wording.
- **TIMELINE_DECLARATION** — author-declared date/event.
- **SOURCE_MATERIAL** — drawn from attached file, transcript, message, record, or artifact.
- **MEMORY_RETURN** — recovered memory as Steven experiences it.
- **BODY_EVIDENCE** — body symptoms, movement, hunger, sensory status, pain.
- **LOGIC_REASONING** — Steven's deductions, calculations, due diligence.
- **UNVERIFIED_DO_NOT_EXPAND** — do not embellish.
