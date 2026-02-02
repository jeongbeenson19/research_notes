#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ingest a paper title -> create Obsidian paper note + prerequisite notes (if missing).
- Deterministic tagging (rule-based).
- Never guess unknown metadata; leave blanks if unresolved.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import os
import re
import sys
import textwrap
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    import requests  # type: ignore
except Exception:
    print("ERROR: requests is required. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)


# ---------------------------
# Config: paths (vault-relative)
# ---------------------------
PAPERS_ROOT = Path("Research/VideoUnderstanding/20_Papers")
PREREQ_ROOT = Path("Research/VideoUnderstanding/05_Prereqs")

PAPER_TEMPLATE = """---
type: paper
title: "{title}"
venue: {venue}
year: {year}
authors: {authors}
url: "{url}"
tasks: {tasks}
methods: {methods}
datasets: {datasets}
metrics: {metrics}
trends: {trends}
status: {status}
date_read: "{date_read}"
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
"""

PREREQ_TEMPLATE = """---
type: prereq
topic: "{topic}"
aliases: {aliases}
related_tasks: {related_tasks}
related_methods: {related_methods}
---

# {topic}

## Definition (1–2 lines)
-

## Why it matters for video understanding
-

## Core concepts / formulas
-

## Typical failure modes / pitfalls
-

## Minimal reading list (optional)
-
"""


# ---------------------------
# Data structures
# ---------------------------
@dataclasses.dataclass
class PaperMeta:
    title: str = ""
    venue: str = ""
    year: int | None = None
    authors: list[str] = dataclasses.field(default_factory=list)
    url: str = ""
    abstract: str = ""
    external_ids: dict = dataclasses.field(default_factory=dict)


# ---------------------------
# Helpers
# ---------------------------
def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:80] if len(s) > 80 else s


def yaml_list_str(items: list[str]) -> str:
    # YAML inline list
    esc = [i.replace('"', '\\"') for i in items]
    return "[" + ", ".join(f'"{x}"' for x in esc) + "]"


def safe_mkdir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


# ---------------------------
# Metadata resolvers
# ---------------------------
def resolve_semantic_scholar(title: str) -> PaperMeta:
    """
    Use Semantic Scholar Graph API paper search.
    """
    base = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": title,
        "limit": 1,
        "fields": "title,authors,year,venue,abstract,url,externalIds",
    }
    url = base + "?" + urllib.parse.urlencode(params)
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    data = r.json()
    if not data.get("data"):
        return PaperMeta(title=title)

    p = data["data"][0]
    meta = PaperMeta()
    meta.title = p.get("title") or title
    meta.venue = p.get("venue") or ""
    meta.year = p.get("year")
    meta.abstract = p.get("abstract") or ""
    meta.url = p.get("url") or ""
    meta.external_ids = p.get("externalIds") or {}
    meta.authors = [a.get("name", "") for a in (p.get("authors") or []) if a.get("name")]
    return meta


def resolve_arxiv(title: str) -> PaperMeta:
    """
    Fallback: arXiv API (Atom).
    Uses search_query=ti:"...".
    """
    base = "http://export.arxiv.org/api/query"
    q = f'ti:"{title}"'
    params = {"search_query": q, "start": 0, "max_results": 1}
    url = base + "?" + urllib.parse.urlencode(params)

    r = requests.get(url, timeout=20)
    r.raise_for_status()

    root = ET.fromstring(r.text)
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
    }
    entry = root.find("atom:entry", ns)
    if entry is None:
        return PaperMeta(title=title)

    meta = PaperMeta()
    meta.title = (entry.findtext("atom:title", default="", namespaces=ns) or "").strip() or title
    meta.abstract = (entry.findtext("atom:summary", default="", namespaces=ns) or "").strip()
    # authors
    authors = []
    for a in entry.findall("atom:author", ns):
        name = (a.findtext("atom:name", default="", namespaces=ns) or "").strip()
        if name:
            authors.append(name)
    meta.authors = authors
    # year
    published = (entry.findtext("atom:published", default="", namespaces=ns) or "").strip()
    if published:
        try:
            meta.year = int(published[:4])
        except Exception:
            pass
    # url (alternate)
    for link in entry.findall("atom:link", ns):
        if link.attrib.get("rel") == "alternate" and link.attrib.get("href"):
            meta.url = link.attrib["href"]
            break
    meta.venue = ""  # arXiv alone doesn't map to venue reliably
    return meta


def resolve_metadata(title: str) -> PaperMeta:
    # Try Semantic Scholar, then arXiv fallback
    try:
        meta = resolve_semantic_scholar(title)
        if meta.title or meta.abstract or meta.url:
            return meta
    except Exception:
        pass

    try:
        return resolve_arxiv(title)
    except Exception:
        return PaperMeta(title=title)


# ---------------------------
# Tagging (rule-based)
# ---------------------------
TASK_RULES = [
    ("long-video", [r"long[- ]form", r"extra[- ]long", r"hour[- ]scale", r"hour[- ]long", r"long video"]),
    ("temporal-grounding", [r"temporal grounding", r"moment retrieval", r"temporal evidence", r"evidence distillation"]),
    ("videoqa", [r"videoqa", r"video question answering", r"video question", r"question answering"]),
    ("tal", [r"temporal action localization", r"\bTAL\b"]),
    ("tad", [r"temporal action detection", r"\bTAD\b"]),
    ("streaming", [r"streaming", r"online video", r"online understanding"]),
    ("hallucination", [r"hallucination", r"faithfulness"]),
    ("benchmark", [r"benchmark", r"\bbench\b", r"dataset"]),
]

METHOD_RULES = [
    ("retrieval", [r"retrieval", r"search", r"rag", r"index"]),
    ("memory", [r"memory", r"cache"]),
    ("compression", [r"compression", r"token", r"keyframe", r"frame selection", r"sampling"]),
    ("distillation", [r"distill", r"distillation"]),
    ("prompting", [r"prompt", r"prompting"]),
    ("agent", [r"agent"]),
]

DATASET_HINTS = [
    "ActivityNet",
    "THUMOS14",
    "Charades",
    "Kinetics",
    "Ego4D",
    "Something-Something",
    "MLVU",
    "Video-MME",
]


def infer_tags(meta: PaperMeta) -> tuple[list[str], list[str], list[str]]:
    text = f"{meta.title}\n{meta.abstract}".lower()

    tasks: list[str] = []
    methods: list[str] = []
    datasets: list[str] = []

    for tag, pats in TASK_RULES:
        if any(re.search(p, text, re.I) for p in pats):
            tasks.append(tag)

    for tag, pats in METHOD_RULES:
        if any(re.search(p, text, re.I) for p in pats):
            methods.append(tag)

    # dataset: keyword match (case-sensitive scan on original title/abstract)
    raw = f"{meta.title}\n{meta.abstract}"
    for d in DATASET_HINTS:
        if d in raw:
            datasets.append(d)

    # de-dup
    tasks = sorted(set(tasks))
    methods = sorted(set(methods))
    datasets = sorted(set(datasets))
    return tasks, methods, datasets


# ---------------------------
# Prereq mapping
# ---------------------------
PREREQ_BY_TASK = {
    "long-video": [
        "Transformer Attention Scaling (O(n^2))",
        "KV Cache / Memory in Transformer Inference",
        "Keyframe / Token Sampling Basics",
        "Retrieval-Augmented Generation (RAG) Basics",
    ],
    "temporal-grounding": [
        "Temporal Grounding / Moment Retrieval Basics",
        "Evidence Retrieval & Alignment for Video",
        "Evaluation: timestamp IoU / Recall@K",
    ],
    "videoqa": [
        "VQA Basics (Question types, biases)",
        "Multimodal Fusion / Tokenization Basics",
    ],
    "tal": [
        "Temporal Action Localization (TAL) Basics",
        "Temporal IoU, mAP, Proposal-based vs DETR-style",
    ],
    "tad": [
        "Temporal Action Detection (TAD) Basics",
        "Proposal generation & boundary regression",
    ],
    "streaming": [
        "Causal/Online Inference Constraints",
        "Streaming memory update patterns",
    ],
    "hallucination": [
        "Faithfulness/Hallucination in MLLMs (Definition & tests)",
        "Evidence-based evaluation protocols",
    ],
}


def prereq_filename(topic: str) -> str:
    # Stable filename
    return "Prereq__" + slugify(topic) + ".md"


# ---------------------------
# File generation
# ---------------------------
def write_text(path: Path, content: str) -> None:
    safe_mkdir(path.parent)
    path.write_text(content, encoding="utf-8")


def create_prereq_if_missing(topic: str, related_tasks: list[str], related_methods: list[str]) -> Path:
    out = PREREQ_ROOT / prereq_filename(topic)
    if out.exists():
        return out

    content = PREREQ_TEMPLATE.format(
        topic=topic,
        aliases=yaml_list_str([topic]),
        related_tasks=yaml_list_str(related_tasks),
        related_methods=yaml_list_str(related_methods),
    )
    write_text(out, content)
    return out


def paper_out_path(meta: PaperMeta) -> Path:
    year = f"{meta.year}_" if meta.year else ""
    venue = f"{meta.venue}_" if meta.venue else ""
    folder = PAPERS_ROOT / f"{year}_{slugify(str(venue))}"
    fname = f"{year}{slugify(str(venue))}{slugify(meta.title or 'unknown-title')}.md"
    return folder / fname


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--status", default="to-read")
    ap.add_argument("--date_read", default="")
    args = ap.parse_args()

    title_in = args.title.strip()
    meta = resolve_metadata(title_in)

    tasks, methods, datasets = infer_tags(meta)

    # prerequisites
    prereq_topics: list[str] = []
    for t in tasks:
        prereq_topics.extend(PREREQ_BY_TASK.get(t, []))
    prereq_topics = sorted(set(prereq_topics))

    # Create prereq docs if missing
    prereq_paths: list[Path] = []
    for topic in prereq_topics:
        prereq_paths.append(create_prereq_if_missing(topic, tasks, methods))

    # Paper note
    out_path = paper_out_path(meta)
    content = PAPER_TEMPLATE.format(
        title=meta.title.replace('"', '\\"'),
        venue=json.dumps(meta.venue) if meta.venue else '""',
        year=meta.year if meta.year else "null",
        authors=yaml_list_str(meta.authors),
        url=meta.url,
        tasks=yaml_list_str(tasks),
        methods=yaml_list_str(methods),
        datasets=yaml_list_str(datasets),
        metrics=yaml_list_str([]),
        trends=yaml_list_str([]),  # you can post-edit to [[Trend__...]] style if you want
        status=args.status,
        date_read=args.date_read,
    )
    write_text(out_path, content)

    # Print short summary
    print("OK")
    print(f"- Paper: {out_path}")
    if prereq_paths:
        created = [p for p in prereq_paths if p.exists()]
        print(f"- Prereqs checked: {len(prereq_paths)} (created if missing)")
        # show up to 8
        for p in created[:8]:
            print(f"  - {p}")
        if len(created) > 8:
            print("  - ...")
    else:
        print("- Prereqs: none inferred")
    print(f"- Tags: tasks={tasks} methods={methods} datasets={datasets}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())