---
name: cv-paper-template-builder
description: Create a standardized Obsidian folder and markdown notes for computer vision papers using reusable templates with YAML attributes. Use when a user asks to quickly collect CV paper information, organize paper review fields, or generate per-paper note documents from title/metadata.
---

# CV Paper Template Builder

## Overview

빠른 CV 논문 리딩을 위해 폴더 구조와 문서 템플릿을 자동 생성한다. 모든 생성 문서는 Obsidian YAML frontmatter(속성)를 포함한다.

## Quick Start

필수 입력을 확보한다.
- `title`

가능하면 함께 확보한다.
- `venue`
- `year`
- `url`
- `authors`

스크립트를 실행한다.

```bash
python skills/cv-paper-template-builder/scripts/create_cv_paper_folder.py \
  --title "<PAPER TITLE>" \
  --venue "<VENUE>" \
  --year "<YEAR>" \
  --url "<URL>" \
  --authors "<AUTHORS>"
```

## Workflow

1. 사용자 입력에서 논문 메타데이터를 정리한다. 없는 값은 빈 문자열로 둔다.
2. `scripts/create_cv_paper_folder.py`를 실행해 폴더와 문서를 생성한다.
3. 생성된 파일 경로를 사용자에게 보고한다.
4. 문서 내부 placeholder를 채워 논문 정보 수집을 진행한다.

## Output Layout

기본 생성 경로:
- `40_Papers/CV/<year-or-yyyy>-<slug>/`

생성 파일:
- `00_paper.md` - 논문 메타데이터, 핵심 기여, 빠른 체크리스트
- `01_problem-method.md` - 문제정의, 방법, 아키텍처, 학습 전략
- `02_experiments-results.md` - 데이터셋, 메트릭, 정량/정성 결과
- `03_critique-followup.md` - 강점/약점, 실패 모드, 후속 실험

## Customization

템플릿 수정이 필요하면 `assets/`의 템플릿 파일을 직접 편집한다.
- `assets/template-00-paper.md`
- `assets/template-01-problem-method.md`
- `assets/template-02-experiments-results.md`
- `assets/template-03-critique-followup.md`

속성(field) 의미와 유지 규칙은 `references/template-spec.md`를 참고한다.
