---
title: 빠른 문헌 독해로 아이디어 구체화 워크플로우
tags:
  - literature-review
  - video
  - tracking
  - memory
  - out-of-view
created: 2026-02-02
---

# 목표
- 논문을 “이해”가 아니라 **설계 결정을 내리기 위한 증거 수집**으로 읽는다.
- 산출물:  
  1) [[결정 로그]](Design Decisions)  
  2) [[문헌 DB]](Paper Matrix)  
  3) [[평가 프로토콜 초안]](Event-based Evaluation)

---

# 0) 내 아이디어를 “판별 가능한 주장”으로 분해
아래 4문항은 문헌을 읽으면서 업데이트한다.

- [ ] **Task 범위**: MOT association(reactivation/stitching)인가? (Yes/No)
- [ ] **State 정의**: location / appearance / semantic / uncertainty 중 필수는?
- [ ] **결합 방식**: feature injection vs gating/late fusion 중 무엇을 고정할까?
- [ ] **평가 프로토콜**: gap-length bucket / view-shift event 기반 평가를 쓸까?

---

# 1) 검색 축(4개)으로 나눠 후보 10편씩 모으기
> 한 번에 다 찾지 말고 “축별로” 모은다.

## A. Out-of-view / Long-gap / Reactivation
- 키워드: out-of-view tracking, reappearance, long-term tracking, absent target, tracklet stitching, reactivation

## B. Memory / Belief / Partial Observability
- 키워드: object memory, belief state tracking, partial observability, persistent perception, object permanence

## C. MOT Association + Context
- 키워드: uncertainty-aware association, context prior gating, visibility-aware tracking, entry/exit prior, re-ranking tracklets

## D. PTZ / Moving camera / View-shift
- 키워드: PTZ tracking reacquisition, active camera tracking, moving camera MOT, view shift tracking

---

# 2) 1차 선별(2분 컷) 체크리스트
논문마다 **읽는 순서 고정**.

1. Figure 1 / pipeline
2. Contributions(3줄)
3. Assumptions(전제 조건)
4. Evaluation protocol(평가 설계)
5. Ablation(모듈 기여 검증)

## 2분 컷 판정
- [ ] 내 문제(관측 단절/재활성화/ID 안정성)와 직접 연결되는가?
- [ ] 내가 가져갈 수 있는 “결정 규칙/모듈/프로토콜”이 1개 이상 있는가?
- [ ] 가정이 현실(단일 RGB 비디오, PTZ 로그 유무)에 맞는가?

**결과**
- ✅ Keep(2차 독해로) / ❌ Drop / 🔁 Later(보류)

---

# 3) 2차 독해(10분 컷) — 템플릿만 채우기
> 요약 금지. 아래 항목만 뽑는다.

## [[문헌 DB]]에 넣을 필드(복붙용)
- Task:
- Unobserved interval 정의: (out-of-view/occlusion/miss)
- Memory unit: (frame / tracklet / object slot)
- State 구성: (location / appearance / semantic / uncertainty)
- Update rule: (update/freeze/decay 조건)
- Reactivation: (candidate generation / final assignment)
- Fusion: (gating / late fusion / injection)
- Assumptions: (PTZ 로그/3D/GT 필요 여부)
- Evaluation: (IDF1/IDS/HOTA, gap-bucket, event-based)
- Failure modes: (false merge, drift, long gap collapse)
- 내 설계에 주는 결론(1줄):

---

# 4) 결정 로그(Design Decisions) 운영
문헌 5편 읽으면 반드시 결정 3개를 만든다.

## D1. Fusion 고정
- 후보: gating / late fusion / injection
- 결정:
- 근거 논문:
- 반례(실패 케이스) 논문:

## D2. Location은 분포(belief)로 유지할지
- 결정:
- 근거:
- 반례:

## D3. Semantic을 어디까지 넣을지(범위 제한)
- 후보: category / attribute / action / group relation
- 결정(최대 1~2개만 선택):
- 근거:
- 반례:

> 규칙: “결정 1개 = 근거 1 + 반례 1”을 항상 붙인다.

---

# 5) 논문을 “역할”로 분류해서 읽기
각 논문은 한 가지 역할만 맡긴다.

- 문제 정의용: 왜 관측 단절이 핵심인가(서론 근거)
- 방법 차용용: memory/state/decay/uncertainty 설계
- 평가 설계용: gap-bucket / event-based / view-shift 분석
- 반박 대비용: injection 붕괴, PTZ 가정, 일반화 한계

---

# 6) out-of-view 희소성 대응: “사건 중심 프로토콜”로 만든다
## 핵심 아이디어
- out-of-view 라벨이 없어도 **관측 단절 사건**은 추출 가능하다.
- 평균 IDF1/IDS만 보지 말고, **재활성화 이벤트 구간만** 본다.

## 이벤트 정의(초안)
- tracklet A 종료 시점: t_end
- tracklet B 시작 시점: t_start
- gap = t_start - t_end - 1
- 같은 GT ID(가능한 데이터셋에서)면 “재등장 이벤트”로 카운트

### Gap-length bucket 예시
- S: 0–15 frames
- M: 16–60 frames
- L: 61–180 frames
- XL: 181+ frames

### Reactivation window
- 재등장 시점 기준 ±K frames 구간에서 IDS/매칭 오류를 집중 측정

---

# 7) 최소 문헌 세트(권장)
- memory/object-oriented 2편
- MOT association 3~5편
- long-term/absent target 2편
- PTZ/view-shift 1~2편

---

# 8) 아이디어 구체화 완료 조건(4문장 테스트)
아래를 한 번에 말할 수 있어야 한다.

1) 우리의 state는 무엇인가? (location/appearance/semantic/uncertainty)
2) 관측 단절 시 어떻게 유지/감쇠되는가?
3) 재관측 시 어떻게 prior로 작동해 association을 안정화하는가?
4) gap/event-based 평가에서 어느 구간에서 IDS가 얼마나 줄어드는가?

---

# 부록: [[문헌 DB]] 노트 템플릿
> 새 논문마다 아래 템플릿으로 노트 1개 생성

## Paper
- Title:
- Venue/Year:
- Link:
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