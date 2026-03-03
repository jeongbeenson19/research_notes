---
title: "MeMOT Multi-Object Tracking with Memory"
aliases:
  - "MeMOT Multi-Object Tracking with Memory"
type: "cv-paper-note"
status: "summarized"
paper_id: "MeMOT Multi-Object Tracking with Memory"
venue: "CVPR"
year: "2022"
url: "https://arxiv.org/abs/2203.16761"
pdf: ""
code: ""
authors: ["Jiarui Cai", "Mingze Xu", "Wei Li", "Yuanjun Xiong", "Wei Xia", "Zhuowen Tu", "Stefano Soatto"]
created: "2026-03-03"
updated: "2026-03-03"
tags:
  - "paper/cv"
  - "paper/review"
  - "status/summarized"
---

# MeMOT Multi-Object Tracking with Memory

## 핵심 요약
- MeMOT은 detection과 association을 통합하고 장기 ID 연결을 위해 대규모 spatio-temporal memory를 사용한다.
- Transformer 기반의 Hypothesis Generation, Memory Encoding, Memory Decoding 3모듈로 구성된다.
- in-network association solver(IAS) 중심으로 온라인 MOT를 end-to-end에 가깝게 구성한다.

## Problem
- tracking-by-detection 파이프라인은 긴 시간 간격 재등장에서 ID switch가 잦다.
- 탐지와 연계를 분리하면 오류 전파가 커지고 장기 문맥 활용이 제한된다.

## Method
- 메모리에 track identity embedding을 보존하고 현재 프레임에서 필요한 정보만 적응적으로 참조/집계한다.
- Hypothesis Generation은 현재 프레임 object proposal을 생성한다.
- Memory Encoding은 track별 핵심 메모리 요약을 추출한다.
- Memory Decoding은 detection과 data association을 동시에 풀어 최종 tracking 결과를 출력한다.

## Data / Benchmarks
- MOT16/17/20에서 CLEAR MOT 및 HOTA 지표로 평가한다.
- ResNet50 + Deformable DETR 기반 설정과 memory buffer 크기(예: MOT16/17에서 최대 300 track)를 보고한다.

## Quantitative Results
- MOT17 표에서 MeMOT은 IAS 계열 기준 IDF1 69.0, MOTA 72.5, HOTA 56.9를 보고한다.
- MOT16에서는 IDF1 69.7, MOTA 72.6, HOTA 57.4를 보고한다.
- MOT20에서는 IDF1 66.1, MOTA 63.7, HOTA 54.1 성능을 제시한다.

## Strengths
- 장기 ID 유지에 필요한 메모리 기반 참조를 아키텍처 레벨에서 명시적으로 도입했다.
- 벤치마크별로 IAS 방식에서 경쟁력 있는 정확도-속도 균형을 달성한다.

## Limitations
- 메모리 버퍼 크기/길이 제한은 GPU 자원에 민감하며 초장기 시퀀스에선 추가 최적화가 필요하다.
- 복잡한 도심 장면에서 ID switch를 더 줄이려면 appearance/motion 결합 개선이 요구된다.

## MNSv2 관점 메모
- MNSv2에서 object permanence 추적 실험군으로 적합하며, memory query 전략 비교에 특히 유용하다.
- track 단위 memory encoding과 frame 단위 decoding 분리 구조는 모듈형 재사용이 쉽다.

## References
- https://arxiv.org/abs/2203.16761
- https://www.amazon.science/publications/memot-multi-object-tracking-with-memory
