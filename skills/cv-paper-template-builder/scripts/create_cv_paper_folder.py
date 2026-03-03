#!/usr/bin/env python3
"""Create CV paper note folders and Obsidian markdown files from templates."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

DOC_LAYOUT = [
    ("00_paper.md", "template-00-paper.md"),
    ("01_problem-method.md", "template-01-problem-method.md"),
    ("02_experiments-results.md", "template-02-experiments-results.md"),
    ("03_critique-followup.md", "template-03-critique-followup.md"),
]

DEFAULT_TAGS = [
    "paper/cv",
    "paper/review",
    "status/inbox",
]

PLACEHOLDER_PATTERN = re.compile(r"{{\s*([a-zA-Z0-9_]+)\s*}}")
NON_WORD_PATTERN = re.compile(r"[^\w\s-]", flags=re.UNICODE)
MULTI_SPACE_PATTERN = re.compile(r"\s+")
MULTI_DASH_PATTERN = re.compile(r"-{2,}")


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def slugify(title: str) -> str:
    cleaned = NON_WORD_PATTERN.sub("", title).strip().lower()
    cleaned = MULTI_SPACE_PATTERN.sub("-", cleaned)
    cleaned = MULTI_DASH_PATTERN.sub("-", cleaned).strip("-")
    return cleaned or "untitled-paper"


def resolve_folder_name(title: str, year: str, folder_name: str) -> str:
    if folder_name.strip():
        return folder_name.strip()
    year_token = year.strip() if year.strip() else "yyyy"
    return f"{year_token}-{slugify(title)}"


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


def build_context(args: argparse.Namespace, folder_name: str) -> dict[str, str]:
    today = date.today().isoformat()
    tags = args.tags if args.tags else DEFAULT_TAGS
    tags_yaml = "\n".join(f"  - {yaml_quote(tag)}" for tag in tags)

    return {
        "title": args.title.strip(),
        "title_yaml": yaml_quote(args.title.strip()),
        "venue": args.venue.strip(),
        "venue_yaml": yaml_quote(args.venue.strip()),
        "year": args.year.strip(),
        "year_yaml": yaml_quote(args.year.strip()),
        "url": args.url.strip(),
        "url_yaml": yaml_quote(args.url.strip()),
        "authors": args.authors.strip(),
        "authors_yaml": yaml_quote(args.authors.strip()),
        "paper_id_yaml": yaml_quote(folder_name),
        "created_date": today,
        "created_date_yaml": yaml_quote(today),
        "tags_yaml": tags_yaml,
    }


def create_documents(
    assets_dir: Path,
    output_dir: Path,
    context: dict[str, str],
    allow_existing: bool,
) -> tuple[list[Path], list[Path]]:
    created: list[Path] = []
    skipped: list[Path] = []

    for output_name, template_name in DOC_LAYOUT:
        template_path = assets_dir / template_name
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")

        output_path = output_dir / output_name
        if output_path.exists():
            if allow_existing:
                skipped.append(output_path)
                continue
            raise FileExistsError(
                f"Output file already exists: {output_path}. "
                "Use --allow-existing to skip existing files."
            )

        template_text = template_path.read_text(encoding="utf-8")
        rendered = render_template(template_text, context)
        output_path.write_text(rendered, encoding="utf-8")
        created.append(output_path)

    return created, skipped


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a CV paper note folder with Obsidian markdown templates and YAML attributes."
        )
    )
    parser.add_argument("--title", required=True, help="Paper title")
    parser.add_argument("--venue", default="", help="Conference or journal name")
    parser.add_argument("--year", default="", help="Publication year")
    parser.add_argument("--url", default="", help="Paper URL (arXiv, OpenReview, etc.)")
    parser.add_argument("--authors", default="", help="Comma-separated author list")
    parser.add_argument(
        "--root",
        default="40_Papers/CV",
        help="Root directory where paper folders are created",
    )
    parser.add_argument(
        "--folder-name",
        default="",
        help="Folder name override (default: <year-or-yyyy>-<title-slug>)",
    )
    parser.add_argument(
        "--tags",
        nargs="*",
        default=None,
        help="Obsidian tags (space-separated). Default: paper/cv paper/review status/inbox",
    )
    parser.add_argument(
        "--allow-existing",
        action="store_true",
        help="Allow existing target folder and skip files that already exist",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    skill_dir = Path(__file__).resolve().parents[1]
    assets_dir = skill_dir / "assets"
    if not assets_dir.exists():
        print(f"[ERROR] Assets directory not found: {assets_dir}", file=sys.stderr)
        return 1

    folder_name = resolve_folder_name(args.title, args.year, args.folder_name)
    target_root = Path(args.root).expanduser()
    target_dir = target_root / folder_name

    if target_dir.exists() and not args.allow_existing:
        print(
            f"[ERROR] Target folder already exists: {target_dir}\n"
            "Use --allow-existing to skip existing files.",
            file=sys.stderr,
        )
        return 1

    target_dir.mkdir(parents=True, exist_ok=True)

    context = build_context(args, folder_name)
    created, skipped = create_documents(
        assets_dir=assets_dir,
        output_dir=target_dir,
        context=context,
        allow_existing=args.allow_existing,
    )

    print(f"[OK] Folder: {target_dir}")
    for path in created:
        print(f"[CREATED] {path}")
    for path in skipped:
        print(f"[SKIPPED] {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
