---
title: "Learning to Track with Object Permanence"
aliases:
  - "Learning to Track with Object Permanence"
type: "cv-paper-note"
status: "summarized"
paper_id: "Learning to Track with Object Permanence"
venue: "ICCV"
year: "2021"
url: "https://openaccess.thecvf.com/content/ICCV2021/html/Tokmakov_Learning_To_Track_With_Object_Permanence_ICCV_2021_paper.html"
pdf: "https://openaccess.thecvf.com/content/ICCV2021/papers/Tokmakov_Learning_To_Track_With_Object_Permanence_ICCV_2021_paper.pdf"
code: "https://github.com/TRI-ML/permatrack"
authors: ["Pavel Tokmakov", "Jie Li", "Wolfram Burgard", "Adrien Gaidon"]
created: "2026-03-03"
updated: "2026-03-03"
tags:
  - "paper/cv"
  - "paper/review"
  - "status/summarized"
---

# Learning to Track with Object Permanence

## 핵심 요약
- PermaTrack은 object permanence 귀납편향을 적용해 완전 가림에서도 trajectory를 유지하는 온라인 MOT를 제안한다.
- CenterTrack를 임의 길이 비디오로 확장하고 ConvGRU 기반 spatio-temporal recurrent memory를 결합한다.
- 합성 Parallel Domain 데이터의 invisible object GT로 가림 구간 supervision을 학습한다.

## Problem
- tracking-by-detection은 현재 프레임 관측 품질 의존이 커서 full occlusion에서 track가 쉽게 끊긴다.
- 실제 MOT 데이터셋은 invisible object 정답 라벨이 부족해 직접 supervision이 어렵다.

## Method
- 프레임 pair 입력 CenterTrack를 sequence 입력으로 확장해 과거 전체 히스토리를 활용한다.
- recurrent memory가 현재 프레임에서 보이지 않는 객체의 위치/ID를 추론하도록 학습된다.
- synthetic+real joint training으로 domain gap을 완화하고 invisible supervision은 합성에서만 제공한다.
- occluded target supervision을 위해 GT/pseudo-GT 기반 전략을 비교한다.

## Data / Benchmarks
- Parallel Domain synthetic 데이터와 KITTI, MOT17 real benchmark를 사용한다.
- KITTI test와 MOT17 val(public/private, Track Rebirth on/off) 설정으로 비교한다.

## Quantitative Results
- KITTI(Table 4)에서 Car HOTA/MOTA 78.0/91.3, Person HOTA/MOTA 48.6/66.0으로 CenterTrack(73.0/88.8, 40.4/53.8) 대비 개선한다.
- MOT17(Table 5, Public, no T.R.)에서 IDF1/MOTA 67.0/67.8로 CenterTrack 63.2/63.1 대비 향상한다.
- MOT17(Table 5, Private, no T.R.)에서도 IDF1/MOTA 68.2/69.4로 CenterTrack 64.2/66.1 대비 향상한다.

## Strengths
- 가림 구간 object permanence를 모델 내부 메모리로 직접 학습해 ID 단절을 줄인다.
- 합성-실데이터 혼합 학습으로 invisible supervision 부재 문제를 실용적으로 해결한다.

## Limitations
- 합성 데이터 품질/도메인 갭에 성능이 민감할 수 있다.
- 메모리 모듈 도입으로 학습/튜닝 복잡도가 증가한다.

## MNSv2 관점 메모
- MNSv2의 핵심 가설인 '보이지 않아도 존재를 유지'를 정량적으로 검증하는 직접 레퍼런스다.
- 향후 memory unit(ConvGRU vs SSM/Transformer) 교체 ablation의 기준 모델로 적합하다.

## References
- https://openaccess.thecvf.com/content/ICCV2021/html/Tokmakov_Learning_To_Track_With_Object_Permanence_ICCV_2021_paper.html
- https://github.com/TRI-ML/permatrack
