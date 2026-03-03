#!/usr/bin/env python3
"""Create a single, content-ready CV paper Obsidian note."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

PLACEHOLDER_PATTERN = re.compile(r"{{\s*([a-zA-Z0-9_]+)\s*}}")
INVALID_FILE_CHARS = re.compile(r'[<>:"/\\|?*]')
MULTI_SPACE_PATTERN = re.compile(r"\s+")

DEFAULT_TAGS = [
    "paper/cv",
    "paper/review",
    "status/summarized",
]


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def to_bullet_block(items: list[str], empty_text: str = "확인 필요") -> str:
    values = [item.strip() for item in items if item and item.strip()]
    if not values:
        values = [empty_text]
    return "\n".join(f"- {item}" for item in values)


def sanitize_note_title(raw_title: str) -> str:
    cleaned = INVALID_FILE_CHARS.sub(" ", raw_title).strip()
    cleaned = MULTI_SPACE_PATTERN.sub(" ", cleaned)
    return cleaned or "Untitled Paper"


def parse_csv_values(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def authors_yaml_inline(authors: list[str]) -> str:
    if not authors:
        return "[]"
    return "[" + ", ".join(yaml_quote(author) for author in authors) + "]"


def tags_yaml_block(tags: list[str]) -> str:
    values = [tag.strip() for tag in tags if tag and tag.strip()]
    if not values:
        values = DEFAULT_TAGS
    return "\n".join(f"  - {yaml_quote(tag)}" for tag in values)


def render_template(template_text: str, context: dict[str, str]) -> str:
    missing_keys: set[str] = set()

    def repl(match: re.Match[str]) -> str:
        key = match.group(1)
        if key not in context:
            missing_keys.add(key)
            return ""
        return context[key]

    rendered = PLACEHOLDER_PATTERN.sub(repl, template_text)
    if missing_keys:
        missing = ", ".join(sorted(missing_keys))
        raise KeyError(f"Template placeholder missing in context: {missing}")
    return rendered


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate one Obsidian markdown note for a CV paper with filled sections. "
            "Filename keeps spaces and does not use dashes."
        )
    )
    parser.add_argument("--title", required=True, help="Paper title")
    parser.add_argument("--venue", default="", help="Venue (conference/journal)")
    parser.add_argument("--year", default="", help="Publication year")
    parser.add_argument("--url", default="", help="Paper landing page URL")
    parser.add_argument("--pdf", default="", help="Paper PDF URL")
    parser.add_argument("--code", default="", help="Code repository URL")
    parser.add_argument(
        "--authors",
        default="",
        help="Comma-separated author list (example: 'A, B, C')",
    )
    parser.add_argument(
        "--root",
        default="60_Library/Research/MNSv2/Reference",
        help="Directory to create the markdown note in",
    )
    parser.add_argument(
        "--filename",
        default="",
        help="Optional filename override without extension",
    )
    parser.add_argument(
        "--tag",
        action="append",
        default=[],
        help="Tag entry (repeatable). Default tags are used when omitted.",
    )
    parser.add_argument(
        "--summary-item",
        action="append",
        default=[],
        help="One bullet for 핵심 요약 (repeatable).",
    )
    parser.add_argument(
        "--problem-item",
        action="append",
        default=[],
        help="One bullet for Problem (repeatable).",
    )
    parser.add_argument(
        "--method-item",
        action="append",
        default=[],
        help="One bullet for Method (repeatable).",
    )
    parser.add_argument(
        "--data-item",
        action="append",
        default=[],
        help="One bullet for Data/Benchmarks (repeatable).",
    )
    parser.add_argument(
        "--result-item",
        action="append",
        default=[],
        help="One bullet for Quantitative Results (repeatable).",
    )
    parser.add_argument(
        "--strength-item",
        action="append",
        default=[],
        help="One bullet for Strengths (repeatable).",
    )
    parser.add_argument(
        "--limitation-item",
        action="append",
        default=[],
        help="One bullet for Limitations (repeatable).",
    )
    parser.add_argument(
        "--note-item",
        action="append",
        default=[],
        help="One bullet for MNSv2 관점 메모 (repeatable).",
    )
    parser.add_argument(
        "--reference-item",
        action="append",
        default=[],
        help="One bullet for References (repeatable).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing note file if present.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    skill_dir = Path(__file__).resolve().parents[1]
    template_path = skill_dir / "assets" / "template-single-note.md"
    if not template_path.exists():
        print(f"[ERROR] Template not found: {template_path}", file=sys.stderr)
        return 1

    title = sanitize_note_title(args.title)
    file_stem = sanitize_note_title(args.filename) if args.filename.strip() else title
    output_path = Path(args.root).expanduser() / f"{file_stem}.md"

    if output_path.exists() and not args.overwrite:
        print(
            f"[ERROR] File already exists: {output_path}\n"
            "Use --overwrite to replace it.",
            file=sys.stderr,
        )
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)

    today = date.today().isoformat()
    authors = parse_csv_values(args.authors)
    tags = args.tag if args.tag else DEFAULT_TAGS

    context = {
        "title": title,
        "title_yaml": yaml_quote(title),
        "paper_id_yaml": yaml_quote(title),
        "venue_yaml": yaml_quote(args.venue.strip()),
        "year_yaml": yaml_quote(args.year.strip()),
        "url_yaml": yaml_quote(args.url.strip()),
        "pdf_yaml": yaml_quote(args.pdf.strip()),
        "code_yaml": yaml_quote(args.code.strip()),
        "authors_yaml_inline": authors_yaml_inline(authors),
        "created_date_yaml": yaml_quote(today),
        "updated_date_yaml": yaml_quote(today),
        "tags_yaml": tags_yaml_block(tags),
        "summary_block": to_bullet_block(args.summary_item),
        "problem_block": to_bullet_block(args.problem_item),
        "method_block": to_bullet_block(args.method_item),
        "data_block": to_bullet_block(args.data_item),
        "result_block": to_bullet_block(args.result_item),
        "strength_block": to_bullet_block(args.strength_item),
        "limitation_block": to_bullet_block(args.limitation_item),
        "note_block": to_bullet_block(args.note_item),
        "reference_block": to_bullet_block(args.reference_item),
    }

    template_text = template_path.read_text(encoding="utf-8")
    rendered = render_template(template_text, context)
    output_path.write_text(rendered, encoding="utf-8")

    print(f"[OK] Note created: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
