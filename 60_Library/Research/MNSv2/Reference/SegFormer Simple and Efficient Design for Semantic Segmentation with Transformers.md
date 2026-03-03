---
title: "SegFormer Simple and Efficient Design for Semantic Segmentation with Transformers"
aliases:
  - "SegFormer Simple and Efficient Design for Semantic Segmentation with Transformers"
type: "cv-paper-note"
status: "summarized"
paper_id: "SegFormer Simple and Efficient Design for Semantic Segmentation with Transformers"
venue: "NeurIPS"
year: "2021"
url: "https://arxiv.org/abs/2105.15203"
pdf: ""
code: "https://github.com/NVlabs/SegFormer"
authors: ["Enze Xie", "Wenhai Wang", "Zhiding Yu", "Anima Anandkumar", "Jose M. Alvarez", "Ping Luo"]
created: "2026-03-03"
updated: "2026-03-03"
tags:
  - "paper/cv"
  - "paper/review"
  - "status/summarized"
---

# SegFormer Simple and Efficient Design for Semantic Segmentation with Transformers

## 핵심 요약
- SegFormer는 계층형 Transformer encoder(MiT)와 경량 MLP decoder를 결합한 semantic segmentation 프레임워크다.
- positional encoding을 제거해 train/test 해상도 불일치에 따른 성능 저하를 줄인다.
- B0~B5 모델군으로 효율-정확도 스케일링을 제공한다.

## Problem
- 기존 Transformer segmentation은 복잡한 decoder와 위치 인코딩 보간 문제로 효율/일반화 한계가 있다.
- 해상도 변화가 큰 실제 환경에서 안정적으로 작동하는 단순 구조가 필요하다.

## Method
- MiT encoder가 멀티스케일 특징을 생성하고, MLP decoder가 stage별 특징을 통합한다.
- decoder를 단순화해 연산량을 줄이면서 local/global 문맥 결합 표현을 유지한다.
- ADE20K, Cityscapes, COCO-Stuff에서 동일 프레임워크로 전이 평가한다.
- 학습 시 OHEM/보조손실 같은 복잡한 trick 없이도 강한 성능을 보고한다.

## Data / Benchmarks
- ADE20K, Cityscapes, COCO-Stuff semantic segmentation 벤치마크를 사용한다.
- mIoU를 기본 성능 지표로 보고 single-scale/multi-scale 설정을 함께 제시한다.

## Quantitative Results
- 논문 초록 기준 SegFormer-B4는 ADE20K에서 50.3% mIoU, 64M 파라미터로 이전 최고 대비 +2.2를 보고한다.
- SegFormer-B5는 Cityscapes val 84.0% mIoU를 달성하고 Cityscapes-C zero-shot 강건성을 제시한다.

## Strengths
- 구조가 단순해 재현/적용이 쉽고, 다양한 해상도에서 안정적이다.
- 경량 decoder 설계로 정확도와 효율의 균형이 우수하다.

## Limitations
- 비디오 메모리 추론을 직접 다루는 모델이 아니므로 MOT/VIS 장기 연결은 별도 설계가 필요하다.
- 대형 B5 구성은 실시간 환경에서 여전히 비용이 높을 수 있다.

## MNSv2 관점 메모
- MNSv2에서는 segmentation backbone baseline으로 적합하며 memory module 결합 전 성능 기준선으로 유용하다.
- 특히 positional encoding 제거 전략은 해상도 변화가 큰 데이터셋에서 안정성 비교 포인트다.

## References
- https://arxiv.org/abs/2105.15203
- https://github.com/NVlabs/SegFormer
