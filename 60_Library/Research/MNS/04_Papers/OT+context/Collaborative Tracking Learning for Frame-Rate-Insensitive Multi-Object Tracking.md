---
alias:
  - ColTrack
type: paper
tags:
  - DeepLearning
  - Paper
  - OTnContext
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: Collaborative Tracking Learning for Frame-Rate-Insensitive Multi-Object Tracking
authors:
  - Yiheng Liu
  - Junta Wu
  - Yi Fu
year: 2023
venue: ICCV
paper_url: https://arxiv.org/abs/2308.05911
topics:
  - Multi-Object Tracking
  - MOT
  - Deep Learning
  - Computer Vision
---

## **📄 Collaborative Tracking Learning for Frame-Rate-Insensitive Multi-Object Tracking 개요**

- **발표 논문**: Collaborative Tracking Learning for Frame-Rate-Insensitive Multi-Object Tracking (ColTrack), Yiheng Liu, Junta Wu, Yi Fu, ICCV 2023.[1][2]
- **핵심 아이디어**:
기존 [[Multi-Object Tracking (MOT)]] 방법론들이 낮은 프레임률(low frame rate) 비디오에서 성능 저하를 겪는 문제를 해결하기 위해, [[ColTrack]]이라는 종단 간(end-to-end) MOT 접근 방식을 제안한다.[1][3][4] ColTrack은 동일한 객체에 속하는 여러 과거 쿼리(historical queries)를 [[협력적 추적 쿼리 (collaborative tracking queries)]]로 활용하여, 시간적으로 풍부한 객체 설명을 통해 신뢰할 수 없는 특징(unreliable features)의 영향을 완화한다.[1][3][4] 이는 [[DETR]] 계열의 탐지 아키텍처에서 다중 쿼리 도입 시 발생하는 중복 예측 억제 능력 상실 및 이분 매칭 손실(bipartite matching loss) 훈련 실패 문제를 [[정보 정제 모듈 (Information Refinement Module, IRM)]]과 [[추적 객체 일관성 손실 (Tracking Object Consistency Loss, TOCLoss)]]을 통해 해결한다.[1][3][4]
- **주요 성과**:
    - 높은 프레임률 비디오에서 대규모 데이터셋인 [[Dancetrack]] 및 [[BDD100K]]에서 최신 방법론들보다 우수한 성능을 달성하고, [[MOT17]]에서는 기존 종단 간 방법론들을 능가한다.[1][3][4]
    - 낮은 프레임률 비디오에서 최신 방법론들 대비 현저히 우수한 성능을 보여, 프레임률 요구 사항을 줄여 더 빠른 처리 속도를 얻으면서도 높은 성능을 유지한다.[1][3][4]
    - 예를 들어, Dancetrack에서 MOTRv2의 HOTA 69.9를 넘어 72.6의 HOTA를 달성하여, 프레임 간 시간적 차이가 최소일 때도 효과적임을 입증했다.[4]

---

## **🏗 아키텍처 개요**

ColTrack은 쿼리 기반의 종단 간 MOT 모델로, 여러 과거 쿼리를 활용하여 객체를 추적한다.[3][4]

### **0. 기호/차원**
- $N$: 객체 수
- $T$: 시간 스텝 (프레임)
- $Q_h$: 과거 쿼리 (historical queries)
- $Q_c$: 협력적 추적 쿼리 (collaborative tracking queries)
- $IRM$: 정보 정제 모듈 (Information Refinement Module)
- $TOCLoss$: 추적 객체 일관성 손실 (Tracking Object Consistency Loss)

### **1. 트랜스포머 인코더 (Transformer Encoder)**
- **구성**: 이미지 특징 맵(image feature maps)과 새로 나타나는 객체(emerging objects)의 탐지 쿼리(detection queries)를 제공한다.[4]
- **특이 사항**: 일반적인 [[Transformer]] 기반 모델의 인코더와 유사하게 작동하여 공간적 특징을 추출한다.

### **2. 시간 블로킹 디코더 (Temporal Blocking Decoders)**
- **구성**: 여러 개의 시간 블로킹 디코더가 반복적으로 예측을 정제한다.[4]
- 각 층:
    1. **[[협력적 추적 쿼리]]**: 동일한 객체에 대한 여러 과거 쿼리가 함께 사용되어 풍부한 시간적 정보를 제공한다.[1][3][4]
    2. **[[정보 정제 모듈 (IRM)]]**: 각 시간 블로킹 디코더 사이에 삽입되어, 동일한 타겟에 속하는 협력적 추적 쿼리 간의 정보 융합을 가능하게 하면서 중복 예측을 억제하는 능력을 유지한다.[1][3][4]

### **3. 주요 수식 요약**
- **정보 정제 모듈 (IRM)**:
  - IRM은 협력적 추적 쿼리 간의 정보 융합을 담당하며, DETR-like 아키텍처의 일대일 매칭 전략과 다중 쿼리 도입 간의 불일치 문제를 해결한다.[1][3]
- **추적 객체 일관성 손실 (TOCLoss)**:
  - 과거 쿼리들이 해당 타겟에 대한 판별적인 특징(discriminative features)을 수집하도록 유도하여, 일관된 추적을 보장한다.[3][4]

---

## **🎯 주요 구성 요소**

### **1. [[협력적 추적 쿼리 (Collaborative Tracking Queries)]]**
- 입력/출력 및 작동 원리 설명: 동일한 객체에 대한 여러 과거 시점의 쿼리들을 함께 사용하여, 단일 쿼리로는 얻기 어려운 풍부한 시간적 맥락과 객체 설명을 제공한다.[1][3][4] 이는 신뢰할 수 없는 특징이나 프레임 간 큰 변화가 있는 낮은 프레임률 환경에서 객체 추적의 견고성을 높인다.[1][3][4]
- $$Q_c = \text{Combine}(Q_{h,1}, Q_{h,2}, ..., Q_{h,k})$$
  (여기서 $Q_{h,i}$는 $i$번째 과거 쿼리이며, Combine 함수는 이들을 통합하는 연산을 의미한다.)

### **2. [[정보 정제 모듈 (Information Refinement Module, IRM)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 시간 블로킹 디코더 사이에 삽입되어, 동일한 타겟에 속하는 협력적 추적 쿼리들 간의 정보 융합을 효과적으로 수행한다.[1][3][4] 이 모듈은 DETR-like 아키텍처의 중복 예측 억제 능력을 유지하면서 다중 쿼리 사용의 이점을 극대화한다.[1][3]
- 설정 값 (논문 기준): 각 시간 블로킹 디코더 사이에 하나씩 삽입된다.[1][3][4]

### **3. [[추적 객체 일관성 손실 (Tracking Object Consistency Loss, TOCLoss)]]**
- 과거 쿼리들이 해당 타겟에 대한 일관된 추적을 위해 판별적인 특징을 수집하도록 유도하는 손실 함수이다.[3][4] 이는 협력적 추적 쿼리 간의 상호작용을 효과적으로 안내한다.[1][3]

---

## **⚖️ ColTrack vs 기존 모델**

| **비교 항목** | **ColTrack** | **YOLOX+Bytetrack** | **FairMOT** | **MOTRv2** |
| :--- | :--- | :--- | :--- | :--- |
| **핵심 아이디어** | 협력적 추적 쿼리, IRM, TOCLoss를 통한 프레임률 불감성 MOT[1][3][4] | Kalman 필터 및 IOU 매칭 기반[4] | Kalman 필터 및 IOU 매칭 기반[4] | Transformer 기반 MOT[4] |
| **낮은 프레임률 성능** | 매우 우수, 높은 성능 유지[1][3][4] | 프레임률 감소 시 성능 급격 저하[4] | 프레임률 감소 시 성능 급격 저하[4] | ColTrack보다 낮은 HOTA (Dancetrack 기준)[4] |
| **처리 속도** | 프레임률 요구 사항 감소로 더 빠른 처리 속도 가능[1][3][4] | - | - | - |
| **아키텍처** | 쿼리 기반 종단 간, Deformable Attention[4] | - | - | - |
| **복잡도** | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ |

- ColTrack은 낮은 프레임률 비디오에서 기존 [[YOLOX+Bytetrack]]이나 [[FairMOT]]와 같이 Kalman 필터 및 IOU 매칭에 의존하는 전통적인 방법론들이 겪는 급격한 성능 저하 문제를 해결한다.[4] ColTrack의 [[Deformable Attention]] 기반 종단 간 아키텍처는 내용 특징(content features)을 활용하여 추적하므로, 프레임 간 큰 변화가 있는 어려운 상황에서 더 유리하다.[4]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 쿼리 기반의 종단 간(end-to-end) 방식으로, 트랜스포머 디코더를 통해 객체 예측을 반복적으로 정제한다.[1][3][4]
- **특징**: 협력적 추적 쿼리와 IRM을 통해 시간적 단서(temporal clues)를 효과적으로 융합하고 특징을 정제하여, 프레임률 변화에 둔감하게 견고한 추적 성능을 제공한다.[1][3][4]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - [[Dancetrack]] (대규모 데이터셋)[1][3][4]
    - [[BDD100K]] (대규모 데이터셋)[1][3][4]
    - [[MOT17]][1][3][4]
- **하드웨어**: (정보 없음)
- **학습 시간**: (정보 없음)
- **옵티마이저**: (정보 없음)
- **규제(Regularization)**: (정보 없음)

---

## **⚠️ 한계**
- 논문에서 명시적인 한계점은 언급되지 않았으나, DETR-like 아키텍처에서 다중 쿼리 도입 시 중복 예측 억제 능력 상실 및 이분 매칭 손실 훈련 실패 문제가 발생할 수 있으며, ColTrack은 IRM을 통해 이를 해결한다.[1][3]

---

## **📊 주요 실험 결과**

### **메인 태스크 성능 (HOTA)**

|**모델**|**HOTA (Dancetrack)**|**HOTA (MOT17)**|**HOTA (BDD100K)**|
|---|---|---|---|
| MOTRv2 | 69.9 | - | - |
| **ColTrack** | **72.6** | **61.0** | **(최신 방법론 대비 우수)** |

- ColTrack은 Dancetrack 데이터셋에서 MOTRv2의 HOTA 69.9를 능가하는 72.6을 달성했다.[4]
- MOT17 데이터셋에서 61.0의 HOTA를 기록하며 기존 종단 간 방법론들을 능가한다.[2]
- BDD100K에서도 최신 방법론들보다 높은 성능을 보인다.[1][3][4]

---

## **🔮 향후 연구 방향**
- (논문에서 명시적인 향후 연구 방향은 언급되지 않음)
- ColTrack의 프레임률 불감성(frame-rate insensitivity) 특성을 활용하여, 제한된 컴퓨팅 자원을 가진 엣지 디바이스(edge devices)에서의 [[MOT]] 적용 가능성을 더욱 확장할 수 있다.[1][3][4]

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Transformer]]
- [[DETR]]

## **📌 참고 링크**
- **논문 원문**: [https://arxiv.org/abs/2308.05911](https://arxiv.org/abs/2308.05911)[5]
- **코드**: [https://github.com/yolomax/ColTrack](https://github.com/yolomax/ColTrack)[1][3][6]
