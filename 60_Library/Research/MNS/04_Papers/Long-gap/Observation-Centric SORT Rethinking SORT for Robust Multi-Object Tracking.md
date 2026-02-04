---
aliases:
  - OC-SORT
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
  - SORT
  - Long-gap
  - OTnContext
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking"
authors:
  - Jinkun Cao
  - Xinshuo Weng
  - Rui Khirodkar
  - Jianing Pang
  - Kris Kitani
year: 2022
venue: arXiv
paper_url: https://arxiv.org/pdf/2203.14360.pdf
topics:
  - Multi-Object Tracking
  - Kalman Filter
  - Occlusion Handling
  - Non-linear Motion
Keyword:
  - ORU
  - OCM
  - Occlusion Robusteness
  - Non-linear Motion Robustness
---

## **📄 Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking 개요**

- **발표 논문**: Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking by Jinkun Cao et al., arXiv 2022.
- **핵심 아이디어**:
    기존 [[Kalman Filter (KF)]] 기반의 [[Multi-Object Tracking (MOT)]] 방법론인 [[SORT]]의 한계점(선형 운동 가정, 추정 중심적 접근, 오차 누적)을 해결하기 위해 "관측 중심(observation-centric)" 접근 방식을 제안한다. 특히, 폐색(occlusion) 및 비선형 움직임(non-linear motion) 상황에서 추적의 강건성(robustness)을 향상시키는 데 중점을 둔다. 이를 위해 [[Observation-centric Re-Update (ORU)]]와 [[Observation-Centric Momentum (OCM)]]이라는 두 가지 주요 혁신 기법을 도입한다.
- **주요 성과**:
    - 기존 [[SORT]]의 "Simple, Online, Real-Time" 특성을 유지한다.
    - 단일 CPU에서 700+ FPS (초당 프레임 수) 이상의 빠른 속도로 동작한다. 
    - MOT17, MOT20, KITTI, DanceTrack 등 다양한 데이터셋에서 최첨단(state-of-the-art) 성능을 달성했으며, 특히 객체 움직임이 매우 비선형적인 DanceTrack에서 뛰어난 성능을 보인다.
    - MOT17에서 63.2 HOTA, MOT20에서 62.1 HOTA를 기록하여 기존 발표된 방법론들을 능가한다. [7]

---

## **🏗 아키텍처 개요**

OC-SORT는 기존 [[SORT]] 프레임워크를 기반으로 하며, 특히 폐색 기간 동안의 오차 처리 방식을 개선하는 관측 중심 메커니즘을 통합한다. [2, 6, 8]

### **0. 기호/차원**
- 일반적으로 [[Kalman Filter]]는 객체의 위치($x, y$), 크기($h, w$), 속도($v_x, v_y$) 등을 포함하는 상태 벡터($\mathbf{x}$)와 공분산 행렬($\mathbf{P}$)을 사용합니다.

### **1. 주요 파트 (관측 중심 메커니즘)**
OC-SORT는 전통적인 인코더/디코더 구조보다는 추적 파이프라인 내에서 [[Kalman Filter]]의 동작을 개선하는 데 초점을 맞춘다.

- **[[Observation-centric Re-Update (ORU)]]**
    - **구성**: 트랙이 손실된 후 재연관(re-association)될 때 활성화된다. [3, 6]
    - **특이 사항**: 과거 추정치 대신 가상 관측치(virtual observations)를 사용하여 오차 누적을 방지한다. 이 가상 관측치는 트랙이 손실되기 전 마지막으로 관측된 데이터와 트랙을 재활성화하는 최신 관측치를 앵커(anchor)로 사용하여 생성된 궤적에서 파생된다. [6]

- **[[Observation-Centric Momentum (OCM)]]**
    - **구성**: 연관성(association)을 위한 비용 행렬에 트랙의 방향 일관성(direction consistency)을 통합한다. [2, 6]
    - **특이 사항**: [[SORT]]에서 방향 추정의 높은 노이즈로 인해 방향 정보를 활용하기 어려웠던 문제를 관측 중심 방식으로 해결한다. [6]

- **[[Observation-Centric Recovery (OCR)]]**
    - **구성**: 주 트랙/탐지 연관 이후에 발생하는 IOU(Intersection Over Union) 기반의 보조 연관 단계이다. [3]
    - **특이 사항**: 손실된 트랙을 마지막으로 알려진 관측치를 사용하여 복구하는 휴리스틱 기법으로, 일시적인 폐색으로 인한 트랙 손실을 방지하는 데 도움을 준다. [3, 8]

### **3. 주요 수식 요약**
- 본 요약에 사용된 자료에서는 핵심 수식이 명시적으로 제공되지 않았습니다.

---

## **🎯 주요 구성 요소**

### **1. [[Observation-centric Re-Update (ORU)]]**
- **입력/출력 및 작동 원리**: 트랙이 손실되었다가 재활성화될 때, 과거의 추정치(estimations)를 더 정확한 관측치(observations) 기반의 데이터로 대체하여 누적된 오차를 줄인다. 이는 가상 궤적(virtual trajectory)을 생성하여 과거 시간 단계의 [[Kalman Filter]] 파라미터를 재업데이트하는 방식으로 이루어진다. [3, 6]
- **핵심 수식**: (제공되지 않음)

### **2. [[Observation-Centric Momentum (OCM)]]**
- **입력/출력 및 작동 원리**: 선형 운동 가정 하에서 객체의 움직임 방향 일관성(direction consistency)을 활용한다. 기존 [[SORT]]에서 방향 추정의 높은 노이즈로 인해 활용하기 어려웠던 이 정보를 관측 중심 방식으로 연관성 비용 행렬에 통합하여 추적의 강건성을 높인다. [2, 6]
- **핵심 수식**: (제공되지 않음)

### **3. [[Observation-Centric Recovery (OCR)]]**
- **입력/출력 및 작동 원리**: 주 연관성 단계 이후에 수행되는 휴리스틱 기법으로, 일치하지 않는 트랙과 관측치 간의 IOU 기반 연관을 통해 손실된 트랙을 복구한다. 이는 특히 단기 폐색(short-term occlusions) 및 정지 객체(stationary objects) 처리 능력을 향상시킨다. [3, 8]

---

## **⚖️ OC-SORT vs SORT**

| **비교 항목** | **OC-SORT** | **SORT** |
| :--- | :--- | :--- |
| **핵심 아이디어** | 관측 중심(Observation-Centric) [2, 4] | 추정 중심(Estimation-Centric) [2, 4] |
| **강점** | 폐색 및 비선형 움직임에 대한 강건성 향상 [1, 2, 6] | 단순성, 온라인, 실시간 처리 [1] |
| **제한 사항** | (SORT의 한계점 개선) | 상태 추정 노이즈에 민감, 오차 누적, 추정 중심적 [2, 5, 6] |
| **복잡도** | Simple, Online, Real-Time 유지, 단일 CPU 700+ FPS [1, 6, 8] | Simple, Online, Real-Time [1] |

- OC-SORT는 [[SORT]]의 기본적인 프레임워크를 유지하면서도, [[Kalman Filter]] 기반 추적의 고질적인 문제점인 폐색 시 오차 누적과 비선형 움직임에 대한 취약성을 관측 중심의 접근 방식으로 효과적으로 개선한다. 

---

## **🧠 추론/디코딩/생성 과정**
- **방식**: [[Kalman Filter]]를 이용한 객체 상태 예측과 헝가리안 알고리즘(Hungarian algorithm)을 통한 탐지(detections)와 트랙(tracks) 간의 데이터 연관(data association)을 기본으로 한다. [4] OC-SORT는 이 과정에 [[Observation-centric Re-Update (ORU)]], [[Observation-Centric Momentum (OCM)]], [[Observation-Centric Recovery (OCR)]] 메커니즘을 통합하여 추론 과정을 강화한다. [3, 6, 8]
- **특징**:
    - **ORU**: 트랙이 재활성화될 때 과거의 추정 오차를 수정하여 트랙의 정확도를 높인다. [3, 6]
    - **OCM**: 연관성 비용 계산 시 객체의 움직임 방향 일관성을 고려하여 비선형 움직임에 대한 강건성을 확보한다. [2, 6]
    - **OCR**: 일시적으로 손실된 트랙을 효과적으로 복구하여 ID 스위치(ID switches)를 줄인다. [3, 8]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - MOT17, MOT20 (Multi-Object Tracking) [1, 4, 7]
    - KITTI (Autonomous Driving) [1, 4]
    - DanceTrack (비선형 움직임이 강한 데이터셋) [1, 4]
    - Head tracking 데이터셋 [1, 4]
- **하드웨어**: 단일 CPU에서 700+ FPS (793 FPS)로 실행 가능. [1, 4, 6, 8]
- **학습 시간**: OC-SORT는 딥러닝 모델처럼 별도의 학습 과정을 거치지 않는 필터링 기반 방법론이며, 기성 탐지(off-the-shelf detections)를 입력으로 사용한다. [1]
- **옵티마이저**: 해당 없음.
- **규제(Regularization)**: 해당 없음.

---

## **⚠️ 한계**
- 기존 [[SORT]]의 세 가지 주요 한계점을 지적하고 개선한다: 상태 추정 노이즈에 대한 민감성, 시간 경과에 따른 오차 누적, 그리고 추정 중심적(estimation-centric)이라는 점.
- [[Kalman Filter]] 기반의 MOT 방법론들이 일반적으로 객체가 선형으로 움직인다는 가정을 한다는 점이 장기 폐색 시 부정확한 추정으로 이어질 수 있다.

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

| **모델** | **MOT17 HOTA** | **MOT20 HOTA** | **MOT20 IDF1** |
|---|---|---|---|
| 기존 SOTA (Published) | (OC-SORT 이전) | (OC-SORT 이전) | (OC-SORT 이전) |
| **OC-SORT** | **63.2** [7] | **62.1** (private detections) [7] | **67.0** (public detections) [8] |
| **OC-SORT (linear interpolation)** | - | **55.2** (public detections) [8] | **67.9** (public detections) [8] |

- OC-SORT는 MOT17 및 MOT20 벤치마크에서 기존 방법론들을 능가하는 최첨단 성능을 달성했다. [7, 8] 특히, 객체의 움직임이 매우 비선형적인 DanceTrack 데이터셋에서도 뛰어난 성능을 보여, 폐색 및 비선형 움직임에 대한 강건성을 입증했다. [1, 4]

---

## **🔮 향후 연구 방향**
- 본 요약에 사용된 자료에서는 논문의 "향후 연구 방향(Future Work)" 섹션에 대한 구체적인 내용이 명시적으로 제공되지 않았습니다. 그러나 OC-SORT가 기존 [[SORT]]의 한계를 재고하고 개선한 점을 고려할 때, 전통적인 필터링 기반 추적 방법론의 지속적인 개선 및 딥러닝 기반 방법론과의 통합 가능성 등이 있을 수 있습니다.

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Kalman Filter]]
- [[SORT]]
- [[Occlusion]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/pdf/2203.14360.pdf
- **코드**: https://github.com/noahcao/OC_SORT

---

## **📚 Related Papers (Dataview)**

### Object Tracking + Context

```dataview
TABLE status, rating, year, Keyword
FROM #OTnContext
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
---

### Long Gap

```dataview
TABLE status, rating, year
FROM #Long-gap
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
---

### Partial Observability

```dataview
TABLE status, rating, year
FROM #PartialObservability
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
---