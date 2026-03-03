---
name: cv-paper-template-builder
description: Create one filled Obsidian markdown note for a computer vision paper with YAML attributes, using a no-dash title filename. Use when the user asks to summarize a CV paper quickly into a single document (problem, method, results, strengths/limits, and follow-up notes).
---

# CV Paper Template Builder

## Overview

CV 논문 정보를 빠르게 수집해 단일 문서로 정리한다. 출력 파일명은 논문 제목 기반이며 대시(`-`)를 쓰지 않는다.

## Quick Start

1) 논문 정보를 수집해 섹션 내용을 채운다. 빈 템플릿만 만들지 않는다.  
2) 아래 스크립트로 단일 문서를 생성한다.

```bash
python skills/cv-paper-template-builder/scripts/create_cv_paper_note.py \
  --title "Learning to Track with Object Permanence" \
  --venue "<VENUE>" \
  --year "<YEAR>" \
  --url "<PAPER_URL>" \
  --pdf "<PDF_URL>" \
  --code "<CODE_URL>" \
  --authors "<AUTHOR1, AUTHOR2>" \
  --summary-item "<핵심 요약 1>" \
  --summary-item "<핵심 요약 2>" \
  --problem-item "<문제 정의>" \
  --method-item "<방법 핵심>" \
  --data-item "<데이터셋/벤치마크>" \
  --result-item "<주요 수치>" \
  --strength-item "<강점>" \
  --limitation-item "<한계>" \
  --note-item "<MNSv2 관점 메모>" \
  --reference-item "<참고 링크>"
```

## Workflow

1. 논문 title을 기준으로 메타데이터/핵심 기여/정량 결과를 확보한다.
2. 단일 문서 구조로 내용을 채운다.
3. `scripts/create_cv_paper_note.py`를 실행해 문서를 생성한다.
4. 경로를 보고하고, 핵심 수치/출처를 문서에 남긴다.

## Output Format

기본 생성 경로:
- `60_Library/Research/MNSv2/Reference/<Paper Title>.md`

필수 섹션:
- 핵심 요약
- Problem
- Method
- Data / Benchmarks
- Quantitative Results
- Strengths
- Limitations
- MNSv2 관점 메모
- References

## Rules

- Obsidian frontmatter 속성은 항상 포함한다.
- 제목/파일명은 공백 기반으로 유지하고 대시 슬러그를 만들지 않는다.
- 불확실한 내용은 추측하지 말고 `확인 필요`로 표기한다.
- 이미 파일이 있으면 덮어쓰기 전에 사용자 의도를 확인하거나 `--overwrite`를 사용한다.

템플릿/필드 규칙은 `references/template-spec.md`를 따른다.
