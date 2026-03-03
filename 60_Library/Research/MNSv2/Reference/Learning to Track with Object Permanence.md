---
title: Learning to Track with Object Permanence
aliases:
  - Learning to Track with Object Permanence
type: cv-paper-note
status: summarized
venue: ICCV
year: "2021"
authors:
  - Pavel Tokmakov
  - Jie Li
  - Wolfram Burgard
  - Adrien Gaidon
url: https://openaccess.thecvf.com/content/ICCV2021/html/Tokmakov_Learning_To_Track_With_Object_Permanence_ICCV_2021_paper.html
pdf: https://openaccess.thecvf.com/content/ICCV2021/papers/Tokmakov_Learning_To_Track_With_Object_Permanence_ICCV_2021_paper.pdf
code: https://github.com/TRI-ML/permatrack
paper id: Learning to Track with Object Permanence
created: 2026-03-03
updated: 2026-03-03
tags:
  - paper/cv
  - topic/occlusion
  - benchmark/KITTI
  - benchmark/MOT17
---

# Learning to Track with Object Permanence

## 핵심 요약
- 기존 tracking-by-detection은 현재 프레임 관측 품질에 크게 의존해 완전 가림(full occlusion)에서 track가 자주 끊긴다.
- 이 논문은 CenterTrack를 video-level recurrent 모델로 확장해, 과거 히스토리를 이용해 가려진 객체 위치를 추론하는 PermaTrack을 제안한다.
- 합성 데이터(Parallel Domain)와 실제 데이터(KITTI/MOT17)를 joint training하여 occlusion handling을 학습하고, KITTI/MOT17에서 SOTA 성능을 보인다.

## Problem
- 목표: 온라인 다중 객체 추적(MOT)에서 완전 가림 구간에서도 ID를 유지하며 trajectory를 이어가기.
- 한계: 실제 데이터셋은 보이지 않는(invisible) 객체에 대한 일관된 라벨이 부족해서 직접 supervised learning이 어렵다.

## Method
### 1) 아키텍처
- 기반 모델: CenterTrack.
- 확장 포인트:
  - 프레임 쌍 기반 처리에서 벗어나 임의 길이 비디오 시퀀스를 처리.
  - Backbone feature를 ConvGRU memory에 누적해 장기 시공간 히스토리를 보존.
  - 기존 head(중심/크기/변위) + visibility head 추가.
- 효과:
  - 현재 프레임에서 객체가 완전히 가려져도 메모리 상태를 기반으로 위치를 hallucinate하고, 재등장 시 ID를 안정적으로 재연결.

### 2) 가림 구간 supervision 전략
- 단순히 모든 invisible 객체를 GT로 넣으면(naive all GT) 학습 신호가 모호해 성능 저하.
- 제안한 핵심:
  - annotation filtering으로 학습 불가능/모호한 invisible target을 제거.
  - pseudo label 생성: 3D constant velocity 기반으로 가림 중 center를 추정해 deterministic supervision 제공.

### 3) Sim-to-Real 학습
- 합성(PD)과 실제(KITTI/MOT17)를 joint training.
- 합성은 긴 시퀀스에서 invisible supervision 제공, 실제는 domain gap 완화 역할.
- 실제 데이터만 fine-tune하면 occlusion hallucination 능력이 약해지는 문제를 joint training으로 완화.

## Data / Benchmarks
- Synthetic: Parallel Domain (invisible object annotation 확보용)
- Real: KITTI, MOT17
- 주요 평가지표: HOTA, MOTA, IDF1, MT, PT, ML

## Quantitative Results
### KITTI Test (Table 4)
- Car HOTA: CenterTrack 73.0 -> PermaTrack 78.0 (+5.0)
- Person HOTA: CenterTrack 40.4 -> PermaTrack 48.6 (+8.2)
- Car MOTA: 88.8 -> 91.3
- Person MOTA: 53.8 -> 66.0

### MOT17 Validation (Table 5)
- Public detection, no T.R.:
  - IDF1: 63.2 -> 67.0
  - MOTA: 63.1 -> 67.8
- Private detection, no T.R.:
  - IDF1: 64.2 -> 68.2
  - MOTA: 66.1 -> 69.4

### Ablation 핵심 포인트
- video-level recurrent 학습이 frame-pair 대비 우수.
- invisible supervision에서 filtered/pseudo label 전략이 naive 방식보다 유리.
- 데이터 규모가 충분히 커야(합성 대규모) occlusion hallucination 성능 차이가 명확히 나타남.

## Strengths
- 완전 가림 상황에서 track continuity를 학습 기반으로 개선.
- heuristic post-processing 의존도를 줄이고 모델 내부 표현으로 해결.
- synthetic+real joint training으로 현실 도메인 성능까지 확보.

## Limitations
- 합성 데이터 품질/도메인 격차에 여전히 의존.
- 메모리 기반 장기 추론은 계산량/튜닝 복잡도를 증가시킴.
- invisible GT가 없는 실제 벤치마크에서 완전한 직접 검증이 제한적.

## MNSv2 관점 메모
- "보이지 않아도 존재를 유지"하는 object permanence prior를 명시적으로 학습시킨 점이 핵심.
- memory state를 통해 occlusion interval을 bridge하는 구조는 MNS류 메모리 모델 설계와 직접 연결 가능.
- 후속 실험 아이디어:
  - memory unit(ConvGRU vs Transformer memory) 비교
  - pseudo label 생성기(3D const-vel vs learned motion prior) 비교
  - 긴 occlusion 길이 구간별 성능 분해 분석

## References
- ICCV 2021 page: https://openaccess.thecvf.com/content/ICCV2021/html/Tokmakov_Learning_To_Track_With_Object_Permanence_ICCV_2021_paper.html
- Paper PDF: https://openaccess.thecvf.com/content/ICCV2021/papers/Tokmakov_Learning_To_Track_With_Object_Permanence_ICCV_2021_paper.pdf
- Code: https://github.com/TRI-ML/permatrack
