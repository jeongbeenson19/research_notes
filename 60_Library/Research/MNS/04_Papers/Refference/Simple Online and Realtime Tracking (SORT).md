---
aliases: ["SORT"]
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
status: 🟩 Done
rating: 4
date: 2026-02-04
title: "Simple Online and Realtime Tracking"
authors: ["Alex Bewley", "Zongyuan Ge", "Lionel Ott", "Fabio Ramos", "Ben Upcroft"]
year: 2016
venue: "ICIP 2016"
paper_url: "https://arxiv.org/abs/1602.00763"
topics: ["Multi-Object Tracking", "Kalman Filter", "Hungarian Algorithm", "Online Tracking", "Real-time Tracking"]
---

## **📄 Simple Online and Realtime Tracking (SORT) 개요**

- **발표 논문**: Simple Online and Realtime Tracking (Alex Bewley et al., ICIP 2016)
- **핵심 아이디어**:
    [[다중 객체 추적 (Multi-Object Tracking, MOT)]]을 위한 실용적이고 효율적인 접근 방식으로, [[Tracking-by-Detection]] 패러다임을 따른다. 복잡한 외형 특징(appearance features) 없이, 객체 탐지(object detection) 품질에 크게 의존하며, 탐지된 바운딩 박스의 움직임과 [[IoU (Intersection over Union)]]를 기반으로 데이터 연관(data association)을 수행한다. 프레임 간 객체 변위를 예측하기 위해 [[Kalman Filter]]를 사용하고, 탐지와 트랙 간의 할당 문제 해결을 위해 [[Hungarian Algorithm]]을 활용한다.
- **주요 성과**:
    - 최신 온라인 트래커와 유사하거나 더 나은 정확도를 달성했다.
    - 260Hz의 매우 빠른 처리 속도를 보여, 당시 최첨단(state-of-the-art) 트래커들보다 20배 이상 빠르다.
    - 복잡한 계산 없이도 효과적인 추적이 가능함을 입증하며, MOT 연구에 중요한 기준선(baseline)을 제시했다.

---

## **🏗 아키텍처 개요**

SORT는 4가지 주요 구성 요소로 이루어진 간단한 온라인 추적 프레임워크이다.

### **0. 기호/차원**
- **상태 벡터 (State Vector)**: $x = [u, v, s, r, \dot{u}, \dot{v}, \dot{s}]^T$
    - $u, v$: 바운딩 박스 중심의 2D 좌표
    - $s$: 스케일 (면적)
    - $r$: 종횡비 (aspect ratio)
    - $\dot{u}, \dot{v}, \dot{s}$: 각 변수의 속도

### **1. 탐지 (Detection)**
- **구성**: 외부의 객체 탐지기(예: Faster R-CNN)를 사용하여 각 프레임에서 객체의 바운딩 박스를 얻는다. SORT의 성능은 이 탐지 품질에 크게 좌우된다.

### **2. 예측 (Prediction)**
- **구성**: [[Kalman Filter]]를 사용하여 각 트랙의 현재 상태를 다음 프레임으로 전파(propagate)하고, 새로운 위치를 예측한다. 선형 등속 모델(linear constant velocity model)을 가정한다.

### **3. 연관 (Association)**
- **구성**: 예측된 트랙과 현재 프레임에서 탐지된 바운딩 박스 간의 연관을 수행한다.
- **측정 기준**: 두 박스 간의 [[IoU (Intersection over Union)]] 거리를 비용(cost)으로 사용한다.
- **알고리즘**: [[Hungarian Algorithm]]을 사용하여 할당 문제를 해결하고, 비용이 특정 임계값보다 낮은 경우에만 매칭을 수락한다.

### **4. 트랙 생명 주기 관리 (Track Lifecycle Management)**
- **구성**:
    - **초기화**: 매칭되지 않은 탐지는 새로운 트랙으로 초기화된다.
    - **종료**: 특정 시간($T_{Lost}$) 동안 매칭되지 않은 트랙은 종료된다.

---

## **🎯 주요 구성 요소**

### **1. [[Kalman Filter]]**
- **입력/출력 및 작동 원리**: 객체의 상태를 8차원 벡터 $[x, y, a, h, \dot{x}, \dot{y}, \dot{a}, \dot{h}]$로 모델링하고(논문에서는 7차원으로 기술하나, 일반적으로 8차원으로 구현됨), 등속 모델을 가정하여 다음 프레임의 상태를 예측한다. 새로운 탐지가 매칭되면, 예측된 상태와 측정된 바운딩 박스를 사용하여 상태를 업데이트한다.
- $$x_k = F x_{k-1}$$
- $$P_k = F P_{k-1} F^T + Q$$

### **2. [[Hungarian Algorithm]]**
- **작동 원리**: 예측된 트랙과 현재 탐지 간의 IoU 거리를 비용 행렬로 사용하여, 총 비용을 최소화하는 최적의 할당을 찾는다. 이를 통해 각 트랙에 가장 적합한 탐지를 효율적으로 매칭할 수 있다.

---

## **⚖️ SORT vs 기존 모델**

| **비교 항목** | **SORT** | **기존 온라인 MOT 방법** |
| :--- | :--- | :--- |
| **핵심 아이디어** | 간단한 모션 예측 및 IoU 기반 연관 | 복잡한 외형 특징, 다중 단서 융합 |
| **외형 특징 사용** | 아니오 | 예 |
| **처리 속도** | 매우 빠름 (260Hz) | 상대적으로 느림 |
| **정확도** | SOTA와 유사하거나 더 나음 | 높지만, 복잡도와 속도에서 손해 |
| **복잡도** | 매우 낮음 | 높음 |

- SORT는 복잡성을 줄이고 오직 모션 정보에만 집중함으로써, 놀라울 정도로 높은 정확도와 전례 없는 실시간 처리 속도를 달성했다. 이는 객체 탐지 기술의 발전이 MOT 성능 향상의 핵심 동인임을 보여주었다.

---

## **🧠 추론 과정**
- **방식**: 프레임별로 진행되는 온라인 추적.
- **특징**:
    1. 각 트랙의 다음 위치를 [[Kalman Filter]]로 예측한다.
    2. 현재 프레임에서 객체를 탐지한다.
    3. 예측된 트랙과 탐지 간의 IoU 거리를 계산하여 비용 행렬을 만든다.
    4. [[Hungarian Algorithm]]으로 최적의 매칭을 찾는다.
    5. 매칭된 트랙은 탐지된 바운딩 박스로 상태를 업데이트한다.
    6. 매칭되지 않은 트랙은 $T_{Lost}$ 카운터를 증가시키고, 매칭되지 않은 탐지는 새로운 트랙을 생성한다.

---

## **⚙️ 학습 설정**

- **학습**: SORT 자체는 학습 과정이 없다. 성능은 전적으로 외부 객체 탐지기의 학습 결과에 의존한다.

---

## **⚠️ 한계**
- **ID 스위치**: 외형 특징을 사용하지 않기 때문에, 객체가 장기간 가려지거나(occlusion) 서로 교차할 때 동일한 ID를 유지하는 데 어려움이 있다. 이로 인해 ID 스위치 발생률이 상대적으로 높다.
- **탐지 의존성**: 탐지기의 성능에 매우 민감하다. 탐지기가 객체를 놓치면 해당 객체의 트랙이 쉽게 종료될 수 있다.

---

## **📊 주요 실험 결과**

- **MOT Challenge 2015** 벤치마크에서 기존의 여러 온라인 및 오프라인 방법론들을 능가하는 성능을 보였다.
- 특히 MOTA(Multiple Object Tracking Accuracy) 지표에서 높은 점수를 기록하며, 추적의 전반적인 정확도를 입증했다.

---

## **🔮 향후 연구 방향**
- SORT의 높은 ID 스위치 문제를 해결하기 위해, 외형 특징(appearance features)을 통합하는 연구가 필요하다. 이는 DeepSORT의 등장을 이끌었다.
- 보다 정교한 모션 모델을 도입하여 비선형적인 움직임을 더 잘 예측하는 방향으로 발전할 수 있다.

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Kalman Filter]]
- [[Hungarian Algorithm]]
- [[DeepSORT]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/1602.00763
- **코드**: https://github.com/abewley/sort

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics[0]) AND file.name != this.file.name
SORT year desc
```
