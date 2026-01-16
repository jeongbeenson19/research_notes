---
type: trend
name: ""
scope: ""        # 무엇을 포함/배제하는지
constraints: []  # e.g. [token-budget, evidence, latency]
eval_axes: []    # e.g. [accuracy, evidence-match, latency]
failure_modes: [] 
---

# Trend 정의(1문장)
- 

## 왜 어려운가(3)
- 
- 
- 

## 대표 접근 유형(2~3)
- Type A:
- Type B:
- Type C:

## 이 트렌드에 속한 논문(자동)
```dataview
LIST FROM "Research/VideoUnderstanding/20_Papers"
WHERE type = "paper" AND contains(trends, this.file.link)
SORT year desc
```
