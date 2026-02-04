---
aliases:
  - Hybrid-SORT
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
  - MOT
  - Long-gap
  - OTnContext
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "Hybrid-SORT: Weak Cues Matter for Online Multi-Object Tracking"
authors:
  - Mingzhan Yang
  - Guangxin Han
  - Bin Yan
  - Wenhua Zhang
  - Jinqing Qi
  - Huchuan Lu
  - Dong Wang
year: 2024
venue: AAAI Conference on Artificial Intelligence
paper_url: https://arxiv.org/abs/2308.00783
topics:
  - Multi-Object Tracking
  - Weak Cues
  - Online Tracking
---

## **📄 Hybrid-SORT: Weak Cues Matter for Online Multi-Object Tracking 개요**

- **발표 논문**: Hybrid-SORT: Weak Cues Matter for Online Multi-Object Tracking, Mingzhan Yang et al., AAAI 2024.
- **핵심 아이디어**:
    [[Multi-Object Tracking (MOT)]]에서 객체 가림(occlusion) 및 군집(clustering) 상황에서 기존의 강한 단서(strong cues, 공간 및 외형 정보)가 모호해지는 문제를 해결하기 위해 약한 단서(weak cues)를 활용하는 새로운 접근 방식인 [[Hybrid-SORT]]를 제안한다.[1][2] 약한 단서로는 신뢰도 상태(confidence state), 높이 상태(height state), 속도 방향(velocity direction)을 도입하여 강한 단서를 보완한다.[1][2] 이 방법은 [[Simple, Online, Real-Time (SORT)]]의 특성을 유지하면서도 성능을 향상시키며, 플러그 앤 플레이(plug-and-play) 및 학습 불필요(training-free) 방식으로 다양한 트래커와 시나리오에 대한 강력한 일반화 능력을 보여준다.[2][3]
- **주요 성과**:
    - MOT17, MOT20, 특히 상호작용과 심한 가림이 빈번한 DanceTrack과 같은 다양한 벤치마크에서 우수한 성능을 달성했다.[1][2]
    - 기존 [[OC-SORT]] 대비 MOT17에서 HOTA 0.4, IDF1 0.9, MOTA 1.3의 성능 향상을 보였다.[4]
    - 더 간단한 파이프라인과 더 빠른 연관(association)을 통해 최첨단 방법보다 우수한 성능을 제공한다.[4]

---

## **🏗 아키텍처 개요**

Hybrid-SORT는 기존의 강한 단서(spatial and appearance information)와 함께 약한 단서(confidence state, height state, velocity direction)를 통합하여 객체 연관(object association)의 견고성을 높인다.[4][1]

### **0. 기호/차원**
- $B$: 바운딩 박스 (Bounding Box)
- $D$: 탐지(Detection)
- $T$: 트랙(Track)
- $C$: 신뢰도(Confidence)
- $H$: 높이(Height)
- $V$: 속도(Velocity)
- $IoU$: Intersection over Union

### **1. 주요 파트**
- **[[Tracklet Confidence Modeling (TCM)]]**
    - **구성**: [[Kalman Filter]]와 선형 예측(Linear Prediction)을 활용하여 트랙릿의 신뢰도를 추정하고 이를 연관 과정에 사용한다.[4]
    - **특이 사항**: 탐지된 객체의 신뢰도 상태를 약한 단서로 활용하여 가려진 객체(occluded objects)와 가리는 객체(occluding objects) 간의 관계를 명확히 한다.[1]
- **[[Height Modulated IoU (HMIoU)]]**
    - **구성**: 기존의 [[IoU]]와 Height IoU를 결합하여 사용한다.[4]
    - **특이 사항**: 객체의 안정적인 높이 정보를 활용하여 군집된 객체(clustered objects)에 대한 식별 능력을 향상시킨다.[4][1]
- **[[Robust Observation-Centric Momentum (ROCM)]]**
    - **구성**: 여러 시간 간격으로 확장된 속도 방향 모델링을 사용하며, 객체 바운딩 박스의 네 모서리 정보를 활용한다.[4]
    - **특이 사항**: 기존의 중심점 기반 속도 예측보다 더 견고한 속도 방향 예측을 제공한다.[4]

### **2. 주요 수식 요약**
- **IoU**:
  - $IoU(B_1, B_2) = \frac{Area(B_1 \cap B_2)}{Area(B_1 \cup B_2)}$
- **HMIoU**:
  - $HMIoU(B_1, B_2) = \alpha \cdot IoU(B_1, B_2) + (1-\alpha) \cdot IoU_{height}(B_1, B_2)$ (가정, 논문에서 구체적인 수식은 검색 결과에 없음)

---

## **🎯 주요 구성 요소**

### **1. [[Tracklet Confidence Modeling (TCM)]]**
- 입력/출력 및 작동 원리 설명: [[Kalman Filter]]를 통해 트랙릿의 상태를 예측하고, 탐지된 객체의 신뢰도(confidence)를 약한 단서로 활용하여 트랙릿의 신뢰도를 모델링한다. 이를 통해 객체 간의 연관(association) 시 가려짐(occlusion) 상황에서 어떤 객체가 전경(foreground)이고 어떤 객체가 배경(background)인지 판단하는 데 도움을 준다.[4][1]

### **2. [[Height Modulated IoU (HMIoU)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 기존의 IoU 매트릭스에 객체의 높이(height) 정보를 변조(modulate)하여 사용한다. 객체의 높이는 다양한 자세 변화에도 비교적 안정적인 특성을 가지며, 깊이 정보(depth information)를 반영할 수 있어 군집된 객체들 사이의 구별 능력을 향상시킨다.[4][1]

### **3. [[Robust Observation-Centric Momentum (ROCM)]]**
- 설명: 객체의 속도 방향(velocity direction)을 모델링하는 데 있어, 기존의 중심점(center)만을 사용하는 대신 바운딩 박스의 네 모서리(four box corners)를 활용하고 여러 시간 간격(multiple temporal intervals)으로 확장하여 예측의 견고성을 높인다.[4]

---

## **⚖️ Hybrid-SORT vs 기존 모델**

| **비교 항목** | **Hybrid-SORT** | **OC-SORT** | **Learnable Trackers (e.g., MOTRv2, SUSHI)** |
| :--- | :--- | :--- | :--- |
| **핵심 아이디어** | 강한 단서 + 약한 단서 활용 | 강한 단서 + 속도 방향 | 학습 기반 특징 추출 및 연관 |
| **약한 단서** | 신뢰도, 높이, 속도 방향 | 속도 방향 | 제한적 또는 없음 |
| **파이프라인** | 간단, 플러그 앤 플레이, 학습 불필요 | 간단, 온라인, 실시간 | 복잡, 학습 필요, 오프라인 처리 가능 |
| **MOT17 HOTA** | OC-SORT 대비 0.4 향상[4] | - | - |
| **MOT17 IDF1** | OC-SORT 대비 0.9 향상[4] | - | - |
| **MOT17 MOTA** | OC-SORT 대비 1.3 향상[4] | - | - |
| **DanceTrack HOTA** | 65.7 (ReID 포함, 휴리스틱 트래커 중 SOTA)[4] | 54.6[3] | 일부 더 높은 성능 |
| **복잡도** | $O(N)$ (SORT 계열) | $O(N)$ (SORT 계열) | $O(N^2)$ 또는 그 이상 (학습 기반) |

- **표에 대한 해석 및 제안 모델의 장점 요약**: [[Hybrid-SORT]]는 [[OC-SORT]]와 같은 기존 휴리스틱(heuristic) 트래커에 비해 약한 단서 모델링을 통해 일관되고 상당한 성능 향상을 보여준다.[4] 특히, 강한 단서가 자주 실패하는 DanceTrack과 같이 도전적이고 밀집된 환경에서 약한 단서의 효과가 두드러진다.[4] 비록 일부 학습 기반 트래커(learnable trackers)에 비해 미세한 성능 차이가 있을 수 있지만, [[Hybrid-SORT]]는 실시간 처리(real-time processing) 능력과 간단한 파이프라인을 유지하면서도 성능을 크게 개선하여 실제 적용에 매우 매력적이다.[4]

---

## **🧠 추론/디코딩/생성 과정**
- **방식**: 온라인 [[Multi-Object Tracking]] (Online Multi-Object Tracking)[1]
- **특징**: [[Simple, Online, Real-Time (SORT)]] 특성을 유지하며, 탐지된 객체와 기존 트랙 간의 연관(association)을 약한 단서를 활용하여 강화한다.[1][2]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - [[MOT17]] (다양한 객체 추적 난이도)[1]
    - [[MOT20]] (밀집된 환경)[1]
    - [[DanceTrack]] (높은 상호작용 및 심한 가림, 복잡한 움직임)[1]
- **하드웨어**: NVIDIA GeForce RTX 3090 GPU 및 Intel(R) Core(TM) i7-11700K @ 3.60GHz CPU (실험 환경)[5]
- **학습 시간**: 해당 논문은 "training-free" 방식으로, 별도의 모델 학습 과정이 필요하지 않다.[2][3]
- **옵티마이저**: 해당 없음 (training-free)
- **규제(Regularization)**: 해당 없음 (training-free)

---

## **⚠️ 한계**
- [[Hybrid-SORT]]는 휴리스틱(heuristic) 트래커 중 최첨단 성능을 달성하지만, [[MOTRv2]] 또는 [[SUSHI]]와 같은 일부 학습 기반(learnable) 트래커에 비해 특정 데이터셋에서 성능이 약간 뒤처질 수 있다.[4] 이는 학습 기반 접근 방식의 내재된 복잡성과 오프라인 처리 능력에서 오는 이점 때문일 수 있다.[4]
- [[MOT17]] 및 [[MOT20]] 벤치마크에서의 제한적인 성능 향상은 이들 벤치마크가 상대적으로 작고 선형적인 움직임이 많아 성능이 이미 포화 상태에 이르렀기 때문이다.[4]

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**HOTA**|**IDF1**|**MOTA**|
|---|---|---|---|
| OC-SORT (MOT17) | - | - | - |
| **Hybrid-SORT (MOT17)** | **+0.4** | **+0.9** | **+1.3** |
| OC-SORT (DanceTrack) | 54.6[3] | 54.6[3] | 89.6[3] |
| **Hybrid-SORT (DanceTrack)** | **62.2**[3] | **63.0**[3] | **91.6**[3] |

---

## **🔮 향후 연구 방향**
- 검색 결과에서 명시적인 향후 연구 방향은 언급되지 않았지만, 약한 단서의 추가적인 활용 가능성 및 다양한 시나리오에서의 일반화 능력 강화가 예상된다.

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Weak Cues]]
- [[SORT]]
- [[Kalman Filter]]
- [[IoU]]
- [[OC-SORT]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2406.13271
- **코드**: https://github.com/ymzis69/HybridSORT

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
