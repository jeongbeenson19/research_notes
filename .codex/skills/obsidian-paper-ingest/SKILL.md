---
name: obsidian-paper-ingest
description: When the user provides a paper title and asks to generate an Obsidian summary + tags + prerequisite docs, run the ingest script to create/update files in the vault.
---

Run:
- python .codex/skills/obsidian-paper-ingest/scripts/ingest_paper.py --title "<TITLE>"

Behavior:
1) Resolve metadata (Semantic Scholar first; arXiv fallback if needed).
2) Auto-tag tasks/methods/datasets (rule-based; avoid guessing).
3) Create paper note file under Research/VideoUnderstanding/20_Papers/<VENUE+YEAR>/...
4) For each inferred prerequisite topic:
   - if prerequisite doc does not exist, create it under Research/VideoUnderstanding/05_Prereqs/
5) Print only a short summary (paths created/updated).