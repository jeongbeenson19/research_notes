---
alias:
  - TrackTrack
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
status: 🟩 Done
rating: 5
date: 2026-02-03
title: Focusing on Tracks for Online Multi-Object Tracking
authors:
  - Kyujin Shim
  - Kangwook Ko
  - Yujin Yang
  - Changick Kim
year: 2025
venue: CVPR
paper_url: https://ieeexplore.ieee.org/document/11093278
topics:
  - Multi-Object Tracking
  - Data Association
  - Track Initialization
  - Computer Vision
---

## **📄 Focusing on Tracks for Online Multi-Object Tracking 개요**

- **발표 논문**: Focusing on Tracks for Online Multi-Object Tracking, Kyujin Shim, Kangwook Ko, Yujin Yang, Changick Kim (KAIST), CVPR 2025.[1][2]
- **핵심 아이디어**: 기존 [[Multi-Object Tracking (MOT)]] 방법론들이 전역 최적화 기법과 다단계 캐스케이드 연관 전략에 주로 의존하여 MOT의 특정 할당 작업 특성과 가려진 객체를 나타낼 수 있는 유용한 탐지 결과를 간과하는 문제를 해결하기 위해, [[TrackTrack]]이라는 새로운 [[Track-Focused Online Multi-Object Tracker]]를 제안한다. TrackTrack은 두 가지 핵심 전략인 [[Track-Perspective-Based Association (TPA)]]와 [[Track-Aware Initialization (TAI)]]를 통해 이러한 문제를 해결한다. TPA는 트랙 관점에서 사용 가능한 모든 탐지 결과 중 최소 거리를 가진 것을 선택하여 각 트랙을 가장 적합한 탐지 결과와 연결한다. TAI는 현재 활성 트랙 및 더 신뢰할 수 있는 탐지 결과와 크게 겹치는 탐지 결과의 트랙 초기화를 억제하여 잘못된 트랙 생성을 방지한다.[1][2][3]
- **주요 성과**:
    - MOT17, MOT20, DanceTrack 데이터셋에 대한 광범위한 실험을 통해 기존 [[State-of-the-Art (SOTA)]] 트래커들을 능가하는 성능을 보여주며, 다양하고 도전적인 추적 시나리오에서 향상된 견고성과 정확도를 제공한다.[1][2][3]
    - 특히 MOT20 테스트 세트에서 HOTA 및 IDF1 모두에서 온라인 트래커 중 가장 높은 점수를 달성하며, 혼잡한 환경에서 강력한 추적 능력을 입증했다.[1]
    - HOTA (Higher Order Tracking Accuracy) 지표에서 뛰어난 성능을 보인다.[1][2]

---

## **🏗 아키텍처 개요**

[[TrackTrack]]의 전체 알고리즘은 이전 프레임의 트랙을 기반으로 현재 프레임의 바운딩 박스 위치를 [[NSA Kalman filter]]를 사용하여 예측하는 것으로 시작한다. 트랙은 3프레임 이상 추적된 '확인된 트랙(confirmed tracks)'과 3프레임 미만 추적된 '미확인 트랙(unconfirmed tracks)'으로 나뉜다. [[Track-Perspective-Based Association (TPA)]]를 기반으로 탐지 결과와 확인된 트랙이 매칭된다. 그 다음, 매칭되지 않은 높은 신뢰도의 탐지 결과는 미확인 트랙과 TPA를 기반으로 매칭된다. 매칭된 트랙은 업데이트되며, 이들의 현재 위치는 [[Track-Aware Initialization (TAI)]]와 함께 매칭되지 않은 탐지 결과를 사용하여 새로운 트랙을 초기화하는 데 활용된다.[4]

### **0. 기호/차원**
- $T_i$: $i$번째 트랙
- $d_j$: $j$번째 탐지 결과
- $c(T_i, d_j)$: 트랙 $T_i$와 탐지 결과 $d_j$ 사이의 거리 함수[4]
- $	au_p, 	au_q$: TPA 전략의 페널티 항 (각각 0.20, 0.40으로 설정)[4]
- $	au_m$: 매칭 임계값 (MOT17: 0.70, MOT20: 0.55, DanceTrack: 0.60으로 설정)[4]
- $r$: 감소 항 (0.05로 설정)[4]

### **1. [[Track-Perspective-Based Association (TPA)]]**
- **구성**: 각 트랙을 트랙 관점에서 사용 가능한 모든 탐지 결과 중 최소 거리를 가진 가장 적합한 탐지 결과와 연결한다.[1][2][3]
- **특이 사항**: 기존의 독립적인 집합 간 매칭(예: 헝가리안 매칭)과 달리, TPA는 각 트랙의 관점에서 매칭을 수행하여 트랙 연관의 정확도와 견고성을 향상시킨다.[1][3]

### **2. [[Track-Aware Initialization (TAI)]]**
- **구성**: 현재 활성 트랙 및 더 신뢰할 수 있는 탐지 결과와 크게 겹치는 탐지 결과의 트랙 초기화를 억제하여 잘못된 트랙 생성을 방지한다.[1][2][3]
- **특이 사항**: 높은 탐지 노이즈나 가려짐이 있는 시나리오에서 트랙 초기화의 품질을 향상시켜 전반적인 추적 안정성과 신뢰성을 높인다.[3]

---

## **🎯 주요 구성 요소**

### **1. [[Track-Perspective-Based Association (TPA)]]**
- 입력/출력 및 작동 원리 설명: TPA는 트랙 $T_i$와 탐지 $d_j$ 사이의 거리 함수 $c(T_i, d_j)$를 사용하여 매칭을 수행한다. 이 과정은 각 트랙에 대해 가장 적합한 탐지를 찾아 연결하며, 이는 기존의 헝가리안 매칭과 같은 독립적인 매칭 방식과 차별화된다.[1][3][4]
- $$c(T_i, d_j) = \text{distance function considering track perspective}$$ 

### **2. [[Track-Aware Initialization (TAI)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: TAI는 매칭된 트랙의 마지막 알려진 위치를 '삭제 불가능한 앵커'로 설정하거나 신뢰도 1의 탐지 결과로 간주한다. 이후, 연관 후 남은 높은 신뢰도의 탐지 결과에 대해 미리 정의된 앵커와 함께 [[Non-Maximum Suppression (NMS)]]를 수행하여, 기존 활성 트랙이나 더 신뢰할 수 있는 탐지 결과와 크게 겹치는 탐지 결과는 초기화 후보에서 제외한다. 이 과정을 통해 잘못된 트랙 생성을 줄이고 트랙 초기화의 정확도를 높인다.[3]
- 설정 값 (논문 기준): TAI의 NMS IoU 임계값은 0.55로 설정되었다.[4]

### **3. 기타 구성 요소**
- [[NSA Kalman filter]]: 이전 트랙을 기반으로 현재 프레임의 바운딩 박스 위치를 예측하는 데 사용된다.[4]
- 트랙 분류: 트랙은 3프레임 이상 추적된 '확인된 트랙'과 3프레임 미만 추적된 '미확인 트랙'으로 나뉜다.[4]

---

## **⚖️ TrackTrack vs 기존 모델**

| **비교 항목** | **TrackTrack** | **기존 SOTA 온라인 트래커** | **기존 SOTA 오프라인 트래커** |
| :--- | :--- | :--- | :--- |
| **핵심 전략** | TPA, TAI | 전역 최적화, 다단계 캐스케이드 | (다양) |
| **MOT20 HOTA** | 최고 성능[1] | (TrackTrack보다 낮음)[1] | (TrackTrack과 유사하거나 낮음)[1] |
| **MOT20 IDF1** | 최고 성능[1] | (TrackTrack보다 낮음)[1] | (TrackTrack과 유사하거나 낮음)[1] |
| **견고성/정확도** | 향상됨[1][2][3] | (TrackTrack보다 낮음) | (TrackTrack보다 낮음) |
| **복잡도** | 온라인 추적에 적합 | (다양) | (다양) |

- TrackTrack은 MOT17, MOT20, DanceTrack과 같은 다양한 벤치마크에서 기존 [[State-of-the-Art (SOTA)]] 트래커들을 능가하는 성능을 보여주며, 특히 혼잡한 시나리오에서 높은 HOTA 및 IDF1 점수를 달성하여 강력한 추적 능력을 입증한다.[1][2][3]

---

## **🧠 추론/디코딩/생성 과정**
- **방식**: 온라인 [[Multi-Object Tracking (MOT)]] 방식. 각 프레임에서 순차적으로 객체를 추적하고 연관시킨다.[1][2]
- **특징**:
    - [[NSA Kalman filter]]를 사용하여 이전 트랙을 기반으로 현재 프레임의 바운딩 박스 위치를 예측한다.[4]
    - 트랙을 '확인된 트랙'과 '미확인 트랙'으로 구분하여 관리한다.[4]
    - [[Track-Perspective-Based Association (TPA)]]를 통해 탐지 결과와 트랙을 매칭하고, [[Track-Aware Initialization (TAI)]]를 통해 새로운 트랙의 초기화를 관리하여 잘못된 트랙 생성을 억제한다.[1][2][3][4]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - MOT17: 정적 및 이동 카메라가 있는 다양한 혼잡 시나리오.[2]
    - MOT20: 고밀도 군중이 있는 더 복잡한 환경.[2]
    - DanceTrack: 유사한 외형과 비선형 움직임을 보이는 객체 추적에 중점을 둔 데이터셋.[2]
- **하드웨어**: (정보 없음)
- **학습 시간**: (정보 없음)
- **옵티마이저**: (정보 없음)
- **규제(Regularization)**: (정보 없음)

---

## **⚠️ 한계**
- 기존 [[Multi-Object Tracking (MOT)]] 방법론들은 전역 최적화 기법과 다단계 캐스케이드 연관 전략에 주로 의존하여, MOT의 특정 할당 작업 특성과 가려진 객체를 나타낼 수 있는 유용한 탐지 결과를 간과하는 경향이 있다.[1][2][3] (TrackTrack이 해결하고자 하는 기존 방법론의 한계점)

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**HOTA (MOT20)**|**IDF1 (MOT20)**|**MOTA (MOT20)**|
|---|---|---|---|
| 기존 SOTA 온라인 트래커 | (TrackTrack보다 낮음) | (TrackTrack보다 낮음) | (TrackTrack보다 낮음) |
| **TrackTrack** | **최고 성능**[1] | **최고 성능**[1] | **최고 성능**[1] |

- TrackTrack은 MOT17, MOT20, DanceTrack 데이터셋에서 기존 [[State-of-the-Art (SOTA)]] 트래커들을 능가하는 성능을 보여주며, 특히 MOT20 테스트 세트에서 HOTA 및 IDF1 모두에서 온라인 트래커 중 가장 높은 점수를 달성했다.[1][2][3]

---

## **🔮 향후 연구 방향**
- (정보 없음)

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Data Association]]
- [[Kalman Filter]]
- [[Computer Vision]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2510.13235[5]
- **코드**: (정보 없음)

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics[0]) AND file.name != this.file.name
SORT year desc
```
