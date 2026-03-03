---
title: "MambaVision A Hybrid Mamba-Transformer Vision Backbone"
aliases:
  - "MambaVision A Hybrid Mamba-Transformer Vision Backbone"
type: "cv-paper-note"
status: "summarized"
paper_id: "MambaVision A Hybrid Mamba-Transformer Vision Backbone"
venue: "CVPR"
year: "2025"
url: "https://arxiv.org/abs/2407.08083"
pdf: ""
code: "https://github.com/NVlabs/MambaVision"
authors: ["Ali Hatamizadeh", "Jan Kautz"]
created: "2026-03-03"
updated: "2026-03-03"
tags:
  - "paper/cv"
  - "paper/review"
  - "status/summarized"
---

# MambaVision A Hybrid Mamba-Transformer Vision Backbone

## 핵심 요약
- MambaVision은 Mamba와 Transformer를 결합한 하이브리드 비전 백본으로 분류/검출/분할을 모두 겨냥한다.
- 비전 친화적으로 재설계한 MambaVision mixer와 후반 self-attention 블록 조합이 핵심이다.
- 모델군은 T/S/B/L/L2로 제공되며 정확도-처리량 Pareto를 목표로 설계되었다.

## Problem
- 순수 ViT는 attention의 quadratic 복잡도로 고해상도에서 비용이 높다.
- 순수 Mamba 계열은 전역 문맥 포착에서 한계가 있어 공간 의존성 모델링이 약해질 수 있다.

## Method
- 4-stage 계층 구조에서 고해상도 stage(1,2)는 CNN residual block으로 빠르게 특징을 추출한다.
- 저해상도 stage(3,4)는 MambaVision block과 Transformer block을 함께 사용해 전역 문맥을 보강한다.
- 기존 causal conv를 regular conv로 교체하고, SSM이 없는 symmetric path를 추가해 token mixing을 강화한다.
- ablation에서 final layers에 self-attention을 배치할 때 성능/효율 균형이 가장 좋음을 보고한다.

## Data / Benchmarks
- ImageNet-1K에서 분류 성능과 이미지 처리량을 함께 비교한다.
- MS COCO(검출/인스턴스 분할), ADE20K(의미 분할) 백본 전이 성능을 평가한다.

## Quantitative Results
- ImageNet-1K에서 Top-1 정확도와 처리량 기준 SOTA Pareto front를 보고한다.
- COCO/ADE20K에서 동급 백본 대비 우수하거나 동등한 정확도-효율 trade-off를 달성한다.

## Strengths
- CNN의 효율성과 attention의 전역 문맥 장점을 하이브리드로 결합했다.
- 백본 하나로 분류/검출/분할 전 과제를 일관되게 지원한다.

## Limitations
- 비디오 전용 모델은 아니므로 장기 시계열 메모리 추론은 별도 모듈이 필요하다.
- 최대 성능 구성(L/L2)은 여전히 대형 모델 학습 자원이 필요하다.

## MNSv2 관점 메모
- MNSv2에서는 SSM 블록과 attention 블록의 stage별 혼합 비율 설계 참고점으로 적합하다.
- 고해상도는 CNN, 저해상도는 memory/attention 중심으로 분담하는 전략이 유효함을 시사한다.

## References
- https://arxiv.org/abs/2407.08083
- https://github.com/NVlabs/MambaVision
