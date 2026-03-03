# Template Spec

## 목표
- 컴퓨터 비전 논문 리뷰에 필요한 정보를 빠르게 수집하고 문서화한다.
- 문서 간 분리를 통해 요약, 방법, 실험, 비판 관점을 독립적으로 관리한다.

## 공통 Obsidian 속성(frontmatter)
- `title`: 문서 제목
- `type`: 문서 타입
- `paper_id`: 논문 폴더 식별자
- `paper_title`: 논문 원제
- `created`, `updated`: 생성/수정 날짜(ISO)
- `tags`: Obsidian 태그 배열

## 파일별 역할
- `00_paper.md`: 메타데이터, 핵심 기여, 전체 체크리스트
- `01_problem-method.md`: 문제정의, 방법, 아키텍처, 학습 설정
- `02_experiments-results.md`: 실험 세팅, 메트릭, 정량/정성 결과
- `03_critique-followup.md`: 장단점, 실패 모드, 후속 실험

## 커스터마이징 규칙
- 템플릿 필드는 `{{placeholder}}` 형식을 유지한다.
- 공통 필드는 모든 파일에서 같은 이름으로 유지한다.
- 새 템플릿을 추가할 때 `scripts/create_cv_paper_folder.py`의 `DOC_LAYOUT`도 함께 수정한다.
