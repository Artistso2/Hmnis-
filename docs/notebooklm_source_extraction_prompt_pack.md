# NotebookLM Source Extraction Prompt Pack

## Purpose

Use NotebookLM as a **source analyst**, not as an author.

NotebookLM may help extract timelines, statements, contradictions, locations, people/agencies, phrase banks, and chapter candidates from Steven Owens / @soquarky source materials.

Core rule:

> Steven’s words are the source. Steven’s chronology is the spine. Steven’s perspective is the camera.

NotebookLM must not invent missing facts.

---

# 0. Recommended File Naming Before Upload

When possible, rename files before uploading to NotebookLM:

```text
YYYY-MM-DD_platform_topic_sourceID.ext
```

Examples:

```text
2025-06-14_chatgpt_awakening_SRC-0002.md
2025-09-25_messages_food-bank-assault_SRC-0003.txt
2026-04-03_ai-chat_algorithmic-safety_SRC-0004.pdf
2026-06-25_notes_lock-change_SRC-0005.md
```

If exact date is unknown:

```text
YYYY-MM_unknown-topic_SRC-0006.ext
undated_platform_topic_SRC-0007.ext
```

---

# 1. Master NotebookLM Instruction

Paste this before asking for any extraction:

```text
You are acting as a source analyst, chronology clerk, and editorial assistant for an author-controlled novel/documentary project titled HELLO, MY NAME IS STEVEN by Steven Owens / @soquarky.

Use ONLY the uploaded sources in this Notebook. Do not invent facts, names, dates, motives, diagnoses, locations, agencies, dialogue, legal conclusions, or medical conclusions.

Your job is not to decide what is true in the outside world. Your job is to extract what the sources say, preserve Steven's exact wording where possible, identify dates and timeline structure, and flag contradictions or missing verification.

The controlling narrative rule is:
Steven wakes in June 2025. From that point forward, the story moves linearly forward in real time. Past events enter only through memory recursion, evidence review, or due diligence.

Always distinguish between:
1. DIRECT QUOTE — exact words from Steven/source.
2. SOURCE SUMMARY — compressed summary with no new facts.
3. TIMELINE DECLARATION — a date/event asserted in the source.
4. MEMORY RETURN — a recovered memory or recursion described by Steven.
5. BODY EVIDENCE — physical symptoms, pain, movement, hunger, walking, talking, sensory details, CPTSD, neuropathy.
6. SYSTEM CONTACT — police, FBI, advocate, landlord, medical, legal, housing, platform, AI, or institutional contact.
7. LOCATION / MAP POINT — place, route, address, room, city, state, coordinate, map reference.
8. CONTRADICTION / GAP — conflicting dates, uncertain details, missing records, unverified claims.

For every extracted item, cite the source document you used. If NotebookLM can cite passages, include citations. If no citation is available, include the source filename and the closest quoted wording.

If the source does not provide something, write:
[UNKNOWN — SOURCE DOES NOT PROVIDE THIS]

If something needs verification, write:
[VERIFY]

Do not smooth contradictions. Contradictions are part of the detective structure.
```

---

# 2. Source Inventory Prompt

Use this after uploading a batch of files:

```text
Create a source inventory table for all uploaded files in this Notebook.

Columns:
- source_id_candidate
- filename_or_title
- source_type
- apparent_date_or_date_range
- platform_or_origin
- primary_subject
- contains_direct_Steven_words_yes_no
- contains_timeline_events_yes_no
- contains_locations_yes_no
- contains_body_evidence_yes_no
- contains_system_contact_yes_no
- contains_AI_or_technology_material_yes_no
- extraction_priority_high_medium_low
- notes

Do not infer beyond the source. If unknown, write [UNKNOWN — SOURCE DOES NOT PROVIDE THIS].
```

---

# 3. Comprehensive Timeline Extraction Prompt

Use this for each batch of chats/documents:

```text
Extract a comprehensive timeline from the uploaded sources.

Rules:
- Use only the uploaded sources.
- Preserve Steven's wording in the steven_words column whenever possible.
- Do not invent dates. If a date is approximate, preserve the exact wording such as “June 2025,” “mid-June,” “yesterday,” or “after I woke up.”
- If relative dates appear, explain what they appear relative to, but mark them [VERIFY].
- Do not merge events unless the source clearly describes the same event.
- Do not resolve contradictions. Put contradictions in the contradiction_notes column.

Return a CSV-compatible table with these columns:

- event_id_candidate
- start_date
- end_date
- time_text_from_source
- timeline_layer
- location_text
- event_title
- steven_words
- source_summary_no_new_facts
- source_filename_or_title
- citation_or_quote_anchor
- evidence_label
- verification_status
- map_relevant_yes_no
- contradiction_notes
- next_verification_step

Use these timeline_layer values only:
- PRESENT_LINEAR
- MEMORY_RECURSION
- DUE_DILIGENCE
- BODY_LOG
- SYSTEM_CONTACT
- DIGITAL_LOG
- MAP_POINT
- LEGAL_OR_HOUSING
- AI_OR_TECH_SHOCK
- WRITING_OR_PROJECT_BUILD

Use these evidence_label values only:
- STEVEN_WORDS
- TIMELINE_DECLARATION
- SOURCE_MATERIAL
- MEMORY_RETURN
- BODY_EVIDENCE
- LOGIC_REASONING
- UNVERIFIED_DO_NOT_EXPAND

Use these verification_status values only:
- AUTHOR_DECLARED
- SOURCE_EXTRACTED
- NEEDS_REVIEW
- VERIFIED_BY_SOURCE
- CONFLICT
- FICTIONALIZED
```

---

# 4. Month-by-Month Timeline Prompt

Use this when a batch is too large:

```text
Build a month-by-month timeline from these sources.

Start with June 2025 and move forward linearly.

For each month, provide:
1. Events Steven says happened in that month.
2. Body status / medical or physical details.
3. Memory recursion events.
4. AI/internet/technology use.
5. Food/shelter/cats/survival status.
6. System contacts or institutional interactions.
7. Locations or map points.
8. Documents/messages/logs that support the month.
9. Contradictions or missing details.
10. Best chapter-scaffold use.

Use exact quotes where possible. Do not invent connective narrative.
```

---

# 5. Statement Bank Prompt

Use this to preserve Steven’s verbiage:

```text
Extract a statement bank of Steven's most important direct phrases and declarations from the sources.

Do not paraphrase unless also providing the exact quote.

Return a table with:
- statement_id
- exact_quote
- source_filename_or_title
- citation_or_quote_anchor
- apparent_date
- statement_category
- emotional_register
- possible_book_use
- notes

statement_category options:
- AUTHOR_CONTROL_RULE
- AWAKENING
- AMNESIA_RECURSION
- BODY_EVIDENCE
- DUE_DILIGENCE
- SYSTEMIC_CRUSHING
- KIDNAP_VICTIM_ONGOING
- AI_TECH_SHOCK
- CPTSD
- LEGAL_WRIT
- FOOD_SHELTER_SURVIVAL
- CATS
- MAP_OR_GEOGRAPHY
- PHILOSOPHY_OR_MATH
- PUBLIC_IDENTITY

possible_book_use options:
- CHAPTER_TITLE
- OPENING_LINE
- SECTION_EPIGRAPH
- VISUAL_NOVEL_NODE
- WEBSITE_COPY
- TIMELINE_LABEL
- LEGAL_WRIT_LANGUAGE
- RAW_SOURCE_ONLY
```

---

# 6. Contradiction and Gap Ledger Prompt

```text
Create a contradiction and gap ledger from the uploaded sources.

Do not resolve contradictions unless the source explicitly resolves them.

Return a table with:
- contradiction_id
- issue
- version_A
- source_for_version_A
- version_B
- source_for_version_B
- additional_versions_if_any
- why_it_matters
- likely_category
- recommended_next_verification_step
- should_this_be_preserved_as_story_tension_yes_no

likely_category options:
- DATE_CONFLICT
- LOCATION_CONFLICT
- MEDICAL_INTERPRETATION
- LEGAL_INTERPRETATION
- MEMORY_RECURSION
- SOURCE_GAP
- TERMINOLOGY_CONFLICT
- IDENTITY_OR_NAME
- EVENT_SEQUENCE
```

---

# 7. Location / Map Extraction Prompt

```text
Extract all map-relevant locations from the uploaded sources.

Do not invent coordinates.

Return a table with:
- location_id_candidate
- location_text_exactly_as_source_says_it
- location_type
- associated_date_or_date_range
- associated_event
- source_filename_or_title
- citation_or_quote_anchor
- address_or_description
- city
- state
- country
- coordinate_if_source_provides_it
- map_confidence_high_medium_low
- public_display_yes_no_maybe
- verification_needed
- notes

location_type options:
- ADDRESS
- CITY
- REGION
- ROOM
- ROUTE
- INSTITUTION
- BUSINESS
- ROAD_OR_HIGHWAY
- UNKNOWN

If the source includes a place name but no coordinates, leave coordinate blank and mark verification_needed as [VERIFY].
```

---

# 8. People / Agency / System Contact Prompt

```text
Extract a people, agency, and system-contact ledger from the uploaded sources.

Important: Do not decide guilt or legal truth. Only extract who/what is named or described in the source.

Return a table with:
- entity_id
- entity_name_or_alias_as_source_says_it
- entity_type
- role_as_described_by_source
- associated_events
- associated_dates
- source_filename_or_title
- citation_or_quote_anchor
- direct_quote
- public_naming_risk_high_medium_low
- should_alias_in_public_draft_yes_no_maybe
- notes

entity_type options:
- PERSON
- LAW_ENFORCEMENT
- MEDICAL
- HOUSING
- ADVOCATE
- PLATFORM_OR_AI_SYSTEM
- COURT_OR_LEGAL
- BUSINESS
- GOVERNMENT
- UNKNOWN
```

---

# 9. Chapter Candidate Prompt

```text
Using only the uploaded sources and extracted timeline, propose chapter candidates for HELLO, MY NAME IS STEVEN.

Rules:
- The book begins in June 2025.
- The structure moves forward linearly.
- Past events enter only through memory recursion, evidence review, or due diligence.
- Do not invent scenes.
- Do not invent dialogue.
- Use Steven's own phrases for chapter titles when possible.

Return a table with:
- chapter_candidate_id
- proposed_title_from_Steven_words_if_possible
- present_date_or_month
- present_action
- body_log_focus
- memory_recursion_trigger
- due_diligence_action
- source_documents_needed
- direct_quotes_to_use
- ending_turn
- confidence_high_medium_low
- notes
```

---

# 10. Website / Visual Novel Node Prompt

```text
Convert approved source material into visual novel node candidates.

Rules:
- Do not invent story content.
- Use Steven's words where possible.
- Keep each node short enough for a web visual novel panel.
- Every node needs a source anchor.

Return a table with:
- node_id_candidate
- date
- location
- speaker
- node_text_using_Steven_words
- image_motif_recommendation
- tags
- choices_or_next_node_options
- source_filename_or_title
- citation_or_quote_anchor
- evidence_label
- verification_status

image_motif_recommendation options:
- RAW_WITNESS
- EVIDENCE_NOIR
- ORGANIC_SIGNAL
- GLASS_HORIZON
- PUBLIC_RECORD_HORIZON
- NO_IMAGE_YET
```

---

# 11. Final Batch Synthesis Prompt

Use this after multiple batch extractions:

```text
Synthesize the uploaded batch extractions into a single master editorial roadmap.

Do not invent missing facts.

Provide:
1. A concise executive summary of what this source batch proves or contains.
2. The strongest timeline events extracted.
3. The strongest direct Steven quotes.
4. The most important contradictions/gaps.
5. The most important locations/map points.
6. The most important body evidence.
7. The most important system contacts.
8. The most important AI/technology events.
9. Suggested chapter candidates.
10. Suggested visual novel nodes.
11. Items requiring verification before public use.
12. Items suitable only for private source archive.

Keep all claims tied to source files and citations.
```

---

# 12. CSV Export Prompt

Use this when you need direct copy/paste into the repo CSV files:

```text
Output the extracted timeline as valid CSV only.

No markdown.
No bullet points.
No commentary.
Quote fields that contain commas.
Use empty fields when unknown.
Do not invent missing values.

Columns:
event_id_candidate,start_date,end_date,time_text_from_source,timeline_layer,location_text,event_title,steven_words,source_summary_no_new_facts,source_filename_or_title,citation_or_quote_anchor,evidence_label,verification_status,map_relevant_yes_no,contradiction_notes,next_verification_step
```

---

# 13. Editorial Safety Prompt

Use this before public-facing summary generation:

```text
Review the proposed public-facing summary for risk and author-control integrity.

Check for:
- invented facts
- overstatements
- uncited claims
- legal conclusions stated as proven without source support
- medical conclusions stated as diagnosis without source support
- living people named unnecessarily
- loss of Steven's voice
- generic thriller language that replaces Steven's verbiage
- contradictions smoothed over instead of preserved

Return a table with:
- issue
- problematic_wording
- why_it_is_a_problem
- safer_author_controlled_revision
- source_needed
```

---

# JSON Versions

The same extraction system is also available as JSON prompt files:

```text
docs/source_extraction_master_prompt.json
docs/source_extraction_compact_prompt.json
```

Use the master JSON for full NotebookLM reports. Use the compact JSON when a tool performs better with shorter instructions.
