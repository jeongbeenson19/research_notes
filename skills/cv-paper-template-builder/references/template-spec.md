# Template Spec

## 목표
- 컴퓨터 비전 논문 정보를 하나의 Obsidian 문서로 빠르게 정리한다.
- 섹션별 핵심 정보(문제/방법/실험/한계)를 즉시 검색 가능하게 만든다.

## 출력 파일 규칙
- 파일 개수: 1개
- 기본 경로: `60_Library/Research/MNSv2/Reference`
- 파일명: 논문 제목 기반, 공백 사용, 대시 슬러그 미사용
- 확장자: `.md`

## 필수 frontmatter 속성
- `title`
- `aliases`
- `type`
- `status`
- `paper_id`
- `venue`
- `year`
- `url`
- `pdf`
- `code`
- `authors`
- `created`
- `updated`
- `tags`

## 본문 필수 섹션
- `핵심 요약`
- `Problem`
- `Method`
- `Data / Benchmarks`
- `Quantitative Results`
- `Strengths`
- `Limitations`
- `MNSv2 관점 메모`
- `References`

## Placeholder 규칙
- 템플릿 변수는 `{{placeholder}}` 형식으로 유지한다.
- 비어 있는 섹션은 `확인 필요`로 채운다.

## 관련 파일
- 템플릿: `assets/template-single-note.md`
- 생성 스크립트: `scripts/create_cv_paper_note.py`
