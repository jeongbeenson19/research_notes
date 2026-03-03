---
title: "XMem Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model"
aliases:
  - "XMem Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model"
type: "cv-paper-note"
status: "summarized"
paper_id: "XMem Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model"
venue: "ECCV"
year: "2022"
url: "https://arxiv.org/abs/2207.07115"
pdf: ""
code: "https://github.com/hkchengrex/XMem"
authors: ["Ho Kei Cheng", "Alexander G. Schwing"]
created: "2026-03-03"
updated: "2026-03-03"
tags:
  - "paper/cv"
  - "paper/review"
  - "status/summarized"
---

# XMem Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model

## 핵심 요약
- XMem은 Atkinson-Shiffrin 인지 모델을 차용해 VOS용 다중 메모리 저장소를 설계한다.
- sensory memory, working memory, long-term memory를 분리해 정확도-메모리 균형을 맞춘다.
- memory potentiation과 consolidation으로 장기 영상에서도 메모리 폭증을 억제한다.

## Problem
- 단일 메모리 구조는 영상 길이가 길어질수록 메모리 사용량과 정확도 사이 trade-off가 급격해진다.
- 장기 구간에서 오래된 유용 정보는 남기고 불필요한 정보는 버리는 정책이 필요하다.

## Method
- 매 프레임 sensory memory를 갱신하고, working memory는 간격 기반으로 갱신한다.
- working memory가 가득 차면 사용 빈도 기반 prototype을 long-term memory로 압축 이관한다.
- long-term memory는 LFU eviction으로 오래된 저효용 요소를 제거한다.
- 논문 본문 기준 6GB 예산에서 약 34,000 프레임까지 처리 가능하다고 보고한다.

## Data / Benchmarks
- Long-time Video dataset에서 장기 시나리오를 평가한다.
- DAVIS/YouTubeVOS 등 단기/표준 벤치마크에서도 함께 비교한다.

## Quantitative Results
- long-video 벤치마크에서 기존 SOTA를 크게 상회하고 short-video에서도 동급 성능을 보인다고 보고한다.
- 학습 데이터 구성(Static/BL30K/DAVIS/YouTubeVOS)에 따라 성능이 점진적으로 개선되는 경향을 제시한다.

## Strengths
- 메모리 계층화와 압축/망각 정책이 명확해 장기 추론 문제에 직접적이다.
- 정확도뿐 아니라 메모리 사용량 제어까지 함께 설계했다.

## Limitations
- 저장소별 하이퍼파라미터(업데이트 주기, 압축 비율, eviction 임계치) 튜닝 비용이 있다.
- 대상 도메인 특성에 따라 usage 기반 선택 정책의 일반화 성능 검증이 필요하다.

## MNSv2 관점 메모
- MNSv2 memory hierarchy 설계에서 가장 직접적인 참조 모델이며, consolidation/eviction 실험을 그대로 이식하기 좋다.
- object permanence 유지와 메모리 예산 관리의 균형점을 찾는 데 기준선으로 사용 가능하다.

## References
- https://arxiv.org/abs/2207.07115
- https://github.com/hkchengrex/XMem
