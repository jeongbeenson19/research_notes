# AGENT

## 목적
- 문서 생성 요청에 대해 Obsidian 스타일 문서를 일관되게 작성한다.
- GitHub 링크를 받았을 때 모델 아키텍처를 반복적으로 탐색해 성실하게 정리한다.

## 기본 출력 규칙
- Output language: Korean
- Format: Markdown
- Must include: (1) model architecture, (2) data flow, (3) training/inference entrypoints, (4) config files, (5) dependencies, (6) extension points
- When claiming behavior, cite exact file path + function/class name.
- If uncertain, explicitly mark "확인 필요" and point to where to verify.

## Obsidian 작성 규칙
- 제목은 H1으로 시작하고, 필요 시 H2/H3를 사용한다.
- 내부 링크는 `[[문서명]]` 형식을 사용한다.
- 참고 문헌/외부 링크는 섹션 말미에 모아 둔다.
- 코드/명령은 fenced code block으로 감싼다.
- 문서의 맥락을 잃지 않도록 섹션 간 연결 문장을 1~2문장 포함한다.
- 모든 문서의 처음에는 obsidian format에 기반한 attribute를 포함한다.

## 문서 생성 워크플로우
- 요구사항을 빠르게 확인하고, 누락된 필수 항목이 있으면 명시적으로 요청한다.
- 구조는 다음 순서를 기본으로 한다: 개요 → 아키텍처 → 데이터 흐름 → 학습/추론 엔트리포인트 → 설정 파일 → 의존성 → 확장 포인트 → 참고
- 각 섹션에서 근거가 되는 코드 위치를 `경로 + 함수/클래스` 형태로 표기한다.

## GitHub 링크 기반 아키텍처 정리
- 레포 구조를 먼저 파악하고 핵심 디렉터리를 추린다.
- 주요 모듈(모델, 데이터, 학습 루프, 추론, 설정)을 반복적으로 브라우징하며 구조를 확인한다.
- 단일 파일에 의존하지 말고, 관련 파일을 교차 확인해 아키텍처를 정리한다.
- 아키텍처 다이어그램이 필요할 때는 텍스트 기반(목록/흐름)으로 먼저 정리한다.
- 확실하지 않은 부분은 "확인 필요"로 표시하고 검증 위치를 제시한다.

## 리뷰 기준
- Treat documentation typos as P1.
- Flag any mismatch between docs and code as P0.xxs.

## Goal
- Given a paper title, create:
  1) an Obsidian paper note (Markdown) in Research/VideoUnderstanding/20_Papers/...
  2) prerequisite knowledge notes in Research/VideoUnderstanding/05_Prereqs/ (if missing)

## Constraints
- Never guess unknown metadata. If not found, leave fields empty.
- Paper note must follow the fixed template:
  - YAML keys fixed
  - Main Contribution exactly 3 lines (What/Why/Impact)
  - Method <= 5 bullets
  - Assumptions/Limits <= 2 each
  - Failure Modes <= 3

## Paths
- Papers: Research/VideoUnderstanding/20_Papers/
- Prereqs: Research/VideoUnderstanding/05_Prereqs/