---
title: "Efficient Video Instance Segmentation via Tracklet Query and Proposal"
aliases:
  - "Efficient Video Instance Segmentation via Tracklet Query and Proposal"
type: "cv-paper-note"
status: "summarized"
paper_id: "Efficient Video Instance Segmentation via Tracklet Query and Proposal"
venue: "CVPR"
year: "2022"
url: "https://openaccess.thecvf.com/content/CVPR2022/html/Wu_Efficient_Video_Instance_Segmentation_via_Tracklet_Query_and_Proposal_CVPR_2022_paper.html"
pdf: ""
code: ""
authors: ["Jialian Wu", "Sudhir Yarram", "Hui Liang", "Tian Lan", "Junsong Yuan", "Jayan Eledath", "Gerard Medioni"]
created: "2026-03-03"
updated: "2026-03-03"
tags:
  - "paper/cv"
  - "paper/review"
  - "status/summarized"
---

# Efficient Video Instance Segmentation via Tracklet Query and Proposal

## 핵심 요약
- EfficientVIS는 tracklet query/proposal을 이용해 VIS를 효율적으로 end-to-end 학습하는 프레임워크다.
- clip 내부뿐 아니라 clip 간 tracklet 연결까지 학습 가능한 correspondence learning을 도입한다.
- VisTR 대비 학습 비용을 크게 줄이면서 정확도를 유지/향상하는 것이 핵심 목표다.

## Problem
- 기존 clip-level VIS는 종종 비-end-to-end이며 clip 간 연결에 hand-crafted association이 필요하다.
- VisTR의 dense attention은 학습 수렴이 느려 연구/개발 주기를 길게 만든다.

## Method
- tracklet query/proposal이 시공간 RoI를 반복적으로 정렬하며 segmentation과 association을 동시에 수행한다.
- correspondence learning으로 연속 clip 간 연결을 네트워크 내부에서 학습한다.
- whole-video segmentation을 single end-to-end pass로 수행하는 경로를 제시한다.
- real-time 지향으로 학습/추론 비용을 함께 줄이는 데 초점을 둔다.

## Data / Benchmarks
- YouTube-VIS 2019/2021 validation에서 AP, AP50, AP75, AR 지표를 보고한다.
- VisTR, CrossVIS, SipMask 등 기존 실시간/clip-level 방법과 비교한다.

## Quantitative Results
- 논문 초록 기준 VisTR 대비 15배 적은 학습 epoch로 SOTA 정확도를 달성한다고 보고한다.
- YouTube-VIS 2019 val에서 EfficientVIS는 AP 39.8(멀티스케일), AP50 61.8, AP75 44.7을 보고한다.
- YouTube-VIS 2021 val에서 AP 34.0, AP50 57.5, AP75 37.3을 보고한다.

## Strengths
- 정확도 유지와 학습 효율 향상을 동시에 달성해 실무 적합성이 높다.
- clip 간 association을 학습화해 수작업 후처리 의존을 줄인다.

## Limitations
- 아주 긴 영상에서 메모리 기반 장기 추론 자체를 직접 모델링한 구조는 XMem류 대비 제한적이다.
- 최대 성능을 위해선 멀티스케일 학습/백본 선택 등 학습 설정 영향이 크다.

## MNSv2 관점 메모
- MNSv2에서는 tracklet를 memory token처럼 다루는 설계 실험에 직접 연결할 수 있다.
- association을 후처리에서 학습 내부로 옮기는 전략이 재현성 개선에 유리하다.

## References
- https://openaccess.thecvf.com/content/CVPR2022/html/Wu_Efficient_Video_Instance_Segmentation_via_Tracklet_Query_and_Proposal_CVPR_2022_paper.html
- https://openaccess.thecvf.com/content/CVPR2022/papers/Wu_Efficient_Video_Instance_Segmentation_via_Tracklet_Query_and_Proposal_CVPR_2022_paper.pdf
