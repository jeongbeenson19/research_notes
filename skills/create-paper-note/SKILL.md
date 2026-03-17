---
name: create-paper-note
description: MNS(Workflow).md'에 정의된 템플릿에 따라, 논문 제목을 입력받아 '60_Library/Research/MNSv2/Reference' 디렉토리에 요약 노트를 생성합니다.
---

# Paper Note Creation Skill

This skill automates the creation of a new paper summary note in the `60_Library/Research/MNSv2/Reference/` directory, based on the template found in `60_Library/Research/MNS/MNS(Workflow).md`.

## Workflow

1.  **Get Paper Title**: The user will provide a paper title.
2.  **Find Paper Details**: Use the `google_web_search` tool to find the paper's official title, venue, year, and a public URL (prefer arXiv).
    - **Query**: Use a query like `"[paper_title]" paper arxiv`.
3.  **Construct File Content**: Use the paper details to fill out the template below. The "Extract" and "Takeaway" sections should be left as placeholders for the user to fill in, as they require in-depth analysis.
4.  **Determine Filename**: The filename should be the paper's official title.
5.  **Create File**: Use the `write_file` tool to create the new markdown file in the `60_Library/Research/MNSv2/Reference/` directory.

## Note Template

Use the following markdown template for the file content.

```markdown
## Paper
- Title: {{title}}
- Venue/Year: {{venue_year}}
- Link: {{url}}
- 역할(문제정의/방법/평가/반박):

## Extract
- Task:
- Unobserved interval:
- Memory unit:
- State:
- Update rule:
- Reactivation:
- Fusion:
- Assumptions:
- Evaluation:
- Failure modes:

## Takeaway
- 내 설계에 적용(1줄):
- D1/D2/D3에 미치는 영향:
```
