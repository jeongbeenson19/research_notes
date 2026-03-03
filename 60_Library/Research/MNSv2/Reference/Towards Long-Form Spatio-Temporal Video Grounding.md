---
title: "Towards Long-Form Spatio-Temporal Video Grounding"
aliases:
  - "Towards Long-Form Spatio-Temporal Video Grounding"
type: "cv-paper-note"
status: "summarized"
paper_id: "Towards Long-Form Spatio-Temporal Video Grounding"
venue: "arXiv"
year: "2026"
url: "https://arxiv.org/abs/2602.23294"
pdf: ""
code: ""
authors: ["Xin Gu", "Bing Fan", "Jiali Yao", "Zhipeng Zhang", "Yan Huang", "Cheng Han", "Heng Fan", "Libo Zhang"]
created: "2026-03-03"
updated: "2026-03-03"
tags:
  - "paper/cv"
  - "paper/review"
  - "status/summarized"
---

# Towards Long-Form Spatio-Temporal Video Grounding

## 핵심 요약
- LF-STVG를 정의하고, 수 분~수 시간 길이 비디오에서 텍스트 질의 대상의 시공간 위치를 찾는 문제를 정식화한다.
- ART-STVG는 비디오를 스트리밍 입력으로 처리하는 autoregressive transformer로 설계된다.
- Spatial/Temporal memory bank와 memory selection 전략으로 긴 영상의 잡음 프레임 영향을 줄인다.

## Problem
- 기존 STVG는 주로 1분 이하 short-form 영상에 맞춰져 long-form에서 계산량과 irrelevant 정보 문제가 크다.
- 모든 프레임을 한 번에 처리하는 방식은 긴 시퀀스에서 시간/메모리 비용이 급격히 증가한다.

## Method
- 프레임을 순차적으로 처리하며 매 시점의 문맥을 memory bank에 누적한다.
- 현재 프레임과 관련도 높은 메모리만 선택해 decoder 입력으로 사용한다.
- Spatial decoder의 출력 단서를 temporal decoder로 전달하는 cascaded spatio-temporal 구조를 사용한다.
- Long-form 성능과 기존 short-form 성능을 동시에 비교해 확장성과 호환성을 검증한다.

## Data / Benchmarks
- 논문에서 확장한 LF-STVG 데이터셋에서 장시간 비디오 grounding 성능을 평가한다.
- 기존 short-form STVG 설정에서도 경쟁 모델과 비교 실험을 수행한다.

## Quantitative Results
- LF-STVG 설정에서 기존 SOTA 대비 유의미한 성능 향상을 보고한다(정량 수치는 원문 표 확인 권장).
- short-form setting에서는 경쟁력 있는 수준을 유지해 기존 파이프라인과의 호환성을 보인다.

## Strengths
- 스트리밍 추론과 메모리 선택 전략을 결합해 long-form에 맞는 현실적인 계산 구조를 제시한다.
- 공간-시간 디코더를 cascade로 연결해 세밀한 spatial cue를 temporal localization에 활용한다.

## Limitations
- 2026년 최신 arXiv 논문으로 후속 재현/벤치마크 비교가 아직 제한적이다.
- 데이터셋 확장 규격과 계산비 세부 수치는 추후 공식 리더보드 기준으로 재검증이 필요하다.

## MNSv2 관점 메모
- MNSv2 관점에서 memory bank 구성과 memory selection 정책은 직접 이식 가능한 설계 포인트다.
- cascaded decoder는 '공간 단서로 시간 추론 보조'라는 구조적 귀납편향으로 해석할 수 있다.

## References
- https://arxiv.org/abs/2602.23294
- https://openreview.net/forum?id=6a39c0b15779fd11e5a273a8299ddfd76d87326c
