---

title: Problem Space

tags: [tracking, out-of-view, memory]

---
# 연구 문제(최상위)
- 관측 단절(occlusion / out-of-view / miss) 동안에도 객체 상태를 유지하고,
- 재관측 시 re-activation/association을 안정화하여 ID switch를 감소시키는 문제

## 현재 고정한 표현
- Partially Observable MOT with Object State Memory
- Persistent Perception / Visual Working Memory 관점

## 범위 제한(필수)
- Downstream 1개를 메인으로 고정: **MOT association / re-activation**
- 나머지 video task(grounding/QA/event)는 확장 가능성으로만 유지