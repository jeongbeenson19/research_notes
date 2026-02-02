---
type: paper
title: "MOTChallenge: A Benchmark for Single-Camera Multiple Target Tracking"
venue: CVPR
year: 2020
authors:
  - Patrick Dendorfer
  - Aljo˘sa O˘sep
  - Anton Milan
  - Konrad Schindler
  -  Daniel Cremers
  - Ian Reid
  - Stefan Roth
  - Laura Leal-Taix
url: https://www.alphaxiv.org/abs/2010.07548
tasks:
  - benchmark
  - tracking
methods: []
datasets:
  - MOT
metrics: []
trends: []
status: to-read
date_read: ""
---
# 요약
---
MOTChallenge는 단일 카메라 다중 목표 추적을 위한 표준화된 벤치마크를 구축하여 다양한 데이터셋, 일관된 주석 프로토콜 및 포괄적인 평가 지표 세트를 제공합니다. 이 이니셔티브는 딥러닝을 활용하여 MOT17과 같은 도전적인 데이터셋에서 50% 이상의 MOTA를 달성하고 다양한 감지 품질에 대한 향상된 견고성을 입증하는 최고의 방법론으로 연구를 크게 가속화했습니다.

---

# 문제
---
- 단일 카메라 다중 객체 추적(MOT) 분야는 표준화된 평가의 부족으로 인해 방법론 간의 공정한 비교가 어려웠습니다.
- 기존 데이터셋은 규모, 다양성 및 복잡성 면에서 제한적이어서 방법론의 과적합과 실제 성능에 대한 불분명한 이해로 이어졌습니다.
- 일관성 없는 진실 정의와 다양한 평가 지표의 확산은 연구 노력을 더욱 파편화시켰습니다.

---

# 방법
---
- MOTChallenge 벤치마크는 점진적으로 도전적이고 세심하게 주석 처리된 데이터셋(MOT15, MOT16, MOT17)을 포함하는 웹 기반 플랫폼을 도입했습니다.
- MOTA 및 IDF1을 포함한 통합 평가 지표 세트를 수립하고, 추적 구성 요소에 대한 평가에 집중하기 위해 공개 객체 감지를 제공했습니다.
- 가시성 수준 및 미묘한 가려짐 처리 등 고품질 및 일관된 진실을 보장하기 위해 엄격한 주석 프로토콜이 개발되었습니다.

---

# 결과
---
- MOTChallenge는 MOT 평가를 위한 사실상의 표준이 되었으며, 2020년 말까지 1,000개 이상의 공개적으로 테스트된 방법과 1,800명 이상의 등록 사용자를 유치했습니다.
- 벤치마크에서 최첨단 추적 정확도(MOTA)는 약 20-30%(딥러닝 이전)에서 MPNTrack과 같은 방법으로 58% 이상으로 향상되었습니다.
- 제출된 추적기 분석은 딥러닝으로의 명확한 전환을 보여주었으며, 방법론은 향상된 견고성과 효율성을 보였고 평균 약 5 Hz의 처리 속도를 나타냈습니다.
---

# 핵심사항
---
- 딥러닝 기술, 특히 외관 모델링, 온라인 적응 및 회귀 기반 추적(tracking-by-regression)은 MOT 성능 향상에 핵심적인 역할을 했습니다.
- 다중 감지기(MOT17)에 걸쳐 추적기를 평가한 결과, 실제 적용을 위해 다양한 감지 품질에 대한 견고성의 중요성이 강조되었습니다.
- 최고 성능의 추적기는 종종 이미지 컨텍스트를 활용하여 감지 격차를 메우고 가려짐을 처리함으로써 오탐지(false positives) 및 미탐지(false negatives)를 효과적으로 줄입니다.

---

# Contents
---
