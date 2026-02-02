---
description: Generate an Obsidian paper note using the fixed template (YAML + sections).
argument-hint: TITLE="..." VENUE="..." YEAR=2025 URL="..." AUTHORS="a; b; c" TASKS="long-video; temporal-grounding" METHODS="retrieval; memory" DATASETS="MLVU; ActivityNet" TRENDS="Trend__LongVideo; Trend__TemporalGrounding"
---

You will produce a SINGLE Markdown note for Obsidian.

Hard constraints:
- Output Markdown only. No commentary.
- Must start with YAML frontmatter exactly using these keys:
  type, title, venue, year, authors, url, tasks, methods, datasets, metrics, trends, status, date_read
- Do NOT guess unknown values. Use "" for strings, [] for lists.
- Main Contribution section must have EXACTLY 3 numbered lines:
  1) **What**:
  2) **Why**:
  3) **Impact**:
- Method section: <= 5 bullets.
- Evidence: include Benchmarks / Key numbers / Key ablations (2) with bullets.
- Assumptions / Limitations: max 2 items each.
- Failure Modes: max 3 bullets.
- One-liner takeaway: 1 bullet.
- Next experiment idea: 1 bullet.

Inputs (use as provided; do not normalize unless requested):
- TITLE: $TITLE
- VENUE: $VENUE
- YEAR: $YEAR
- URL: $URL
- AUTHORS: $AUTHORS (split by ';' into a list)
- TASKS: $TASKS (split by ';' into a list)
- METHODS: $METHODS (split by ';' into a list)
- DATASETS: $DATASETS (split by ';' into a list)
- TRENDS: $TRENDS (convert each into Obsidian link format [[...]])

Now generate the note using the template below:

---
type: paper
title: "$TITLE"
venue: "$VENUE"
year: $YEAR
authors: []
url: "$URL"
tasks: []
methods: []
datasets: []
metrics: []
trends: []
status: to-read
date_read: ""
---

# Main Contribution (3 lines)
1) **What**:
2) **Why**:
3) **Impact**:

## Method (<=5 bullets)
- 

## Evidence
- Benchmarks:
- Key numbers:
- Key ablations (2):
  - 
  - 

## Assumptions / Limitations (2 each)
- Assumptions:
  - 
- Limitations:
  - 

## Failure Modes (3)
- 
- 
- 

## One-liner takeaway
- 

## Next experiment idea (1)
- 