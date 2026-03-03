---
title: "VideoMamba State Space Model for Efficient Video Understanding"
aliases:
  - "VideoMamba State Space Model for Efficient Video Understanding"
type: "cv-paper-note"
status: "summarized"
paper_id: "VideoMamba State Space Model for Efficient Video Understanding"
venue: "ECCV"
year: "2024"
url: "https://arxiv.org/abs/2403.06977"
pdf: ""
code: "https://github.com/OpenGVLab/VideoMamba"
authors: ["Kunchang Li", "Xinhao Li", "Yi Wang", "Yinan He", "Yali Wang", "Limin Wang", "Yu Qiao"]
created: "2026-03-03"
updated: "2026-03-03"
tags:
  - "paper/cv"
  - "paper/review"
  - "status/summarized"
---

# VideoMamba State Space Model for Efficient Video Understanding

## 핵심 요약
- VideoMamba는 비디오 도메인에 특화된 Mamba(SSM) 설계로 긴 시퀀스 처리 효율을 높인 모델이다.
- 핵심은 linear-complexity operator를 이용해 장기 문맥 모델링 비용을 줄이는 데 있다.
- 논문은 scalability, short-term sensitivity, long-term superiority, multimodal compatibility의 4가지 능력을 제시한다.

## Problem
- 3D CNN/Video Transformer는 고해상도 장기 비디오에서 메모리/연산 비용이 크다.
- 짧은 동작 인식과 긴 문맥 추론을 동시에 만족하는 효율적 구조가 필요하다.

## Method
- 비디오 시퀀스를 위한 SSM 기반 블록을 도입해 local redundancy와 global dependency를 함께 다룬다.
- self-distillation을 추가해 대규모 사전학습 의존도를 줄이고 학습 안정성을 높인다.
- short-term/long-term/multi-modal 과제를 하나의 백본 계열로 확장 가능하도록 설계한다.
- Figure 1에서 기존 대비 throughput/메모리 측면의 우위를 제시한다.

## Data / Benchmarks
- 단기 비디오 이해, 장기 비디오 이해, 비디오-텍스트 과제를 포함한 광범위 벤치마크를 평가한다.
- 공개 코드에서 image/video single-modality와 video multimodality 실험 구성을 제공한다.

## Quantitative Results
- 논문은 VideoMamba가 short-term과 long-term 모두에서 better/faster/cheaper 특성을 보인다고 보고한다.
- self-distillation 실험에서 과적합 완화와 성능 개선 효과를 확인한다.

## Strengths
- 선형 복잡도 기반으로 긴 비디오에서 확장성이 높다.
- 단기/장기/멀티모달을 하나의 패밀리로 연결해 재사용성이 높다.

## Limitations
- Transformer 대비 우위는 태스크/설정에 따라 달라질 수 있어 정밀 튜닝이 필요하다.
- 최대 성능 달성을 위해서는 self-distillation 및 학습 스케줄 설정 민감도가 존재한다.

## MNSv2 관점 메모
- MNSv2에서는 memory backbone을 ConvGRU 외 SSM으로 바꿔볼 때 1순위 비교군으로 적합하다.
- 특히 장기 구간에서 메모리 사용량 대비 성능 곡선을 비교하는 실험 설계가 중요하다.

## References
- https://arxiv.org/abs/2403.06977
- https://github.com/OpenGVLab/VideoMamba
