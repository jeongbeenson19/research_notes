---
title: "MinVIS A Minimal Video Instance Segmentation Framework without Video-based Training"
aliases:
  - "MinVIS A Minimal Video Instance Segmentation Framework without Video-based Training"
type: "cv-paper-note"
status: "summarized"
paper_id: "MinVIS A Minimal Video Instance Segmentation Framework without Video-based Training"
venue: "NeurIPS"
year: "2022"
url: "https://arxiv.org/abs/2208.02245"
pdf: ""
code: "https://github.com/NVlabs/MinVIS"
authors: ["De-An Huang", "Zhiding Yu", "Anima Anandkumar"]
created: "2026-03-03"
updated: "2026-03-03"
tags:
  - "paper/cv"
  - "paper/review"
  - "status/summarized"
---

# MinVIS A Minimal Video Instance Segmentation Framework without Video-based Training

## 핵심 요약
- MinVIS는 비디오 전용 아키텍처/학습 없이, 이미지 인스턴스 분할 모델만으로 VIS를 수행한다.
- 학습 시 프레임을 독립 이미지로 다루고, 추론 시 query embedding의 시간적 일관성으로 추적한다.
- 추론은 온라인 bipartite matching 기반이며 수작업 heuristic tracking을 최소화한다.

## Problem
- 기존 VIS는 비디오 전용 설계와 긴 학습 파이프라인이 필요해 실험/적용 비용이 높다.
- 라벨링 프레임 수가 많을수록 비용이 급증해 데이터 효율성이 낮다.

## Method
- query-based image instance segmentation 모델을 그대로 학습한다.
- 비디오 추론 단계에서 프레임 간 query embedding을 bipartite matching으로 연결한다.
- 전체 비디오를 한 번에 로드하지 않아도 되는 online inference를 지원한다.
- 추적을 위해 별도 hand-crafted rules를 크게 늘리지 않는 것이 핵심 설계 철학이다.

## Data / Benchmarks
- OVIS, YouTube-VIS 2019/2021에서 평가한다.
- frame sub-sampling(1%, 5%, 10%) 조건으로 라벨 효율성 실험을 수행한다.

## Quantitative Results
- OVIS에서 기존 최고 성능 대비 10% AP 이상 향상을 보고한다.
- 추상/표 기준으로 1% 라벨 프레임에서도 full supervision 대비 유사하거나 경쟁력 있는 성능을 보고한다.
- YouTube-VIS 2019 표에서 MinVIS Swin-L Full 61.6 AP, 1% 설정 59.0 AP를 제시한다.

## Strengths
- 모델/학습 파이프라인이 단순해 재현과 확장이 쉽다.
- 라벨링 비용 절감 대비 성능 유지가 좋아 실무 적용성이 높다.

## Limitations
- 극단적 occlusion/장기 temporal reasoning은 명시적 메모리 모델 대비 한계가 있을 수 있다.
- query consistency 가정이 약한 도메인에서는 추적 안정성이 떨어질 수 있다.

## MNSv2 관점 메모
- MNSv2에서 최소 baseline으로 두고 메모리 모듈을 점진적으로 추가하는 ablation 시작점으로 적합하다.
- 라벨 프레임 비율별 성능 곡선을 함께 기록하면 데이터 효율 관점 비교가 명확해진다.

## References
- https://arxiv.org/abs/2208.02245
- https://github.com/NVlabs/MinVIS
