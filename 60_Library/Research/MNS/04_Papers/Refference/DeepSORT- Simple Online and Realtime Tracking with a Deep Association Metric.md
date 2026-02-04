---
alias: ["Deep SORT"]
type: paper
tags:
  - DeepLearning
  - Paper
  - ObjectTracking
status: 🟩 Done
rating: 4 # 1~5점
date: 2017-03-21
title: "Simple Online and Realtime Tracking with a Deep Association Metric"
authors: ["Nicolai Wojke", "Alex Bewley", "Dietrich Paulus"]
year: 2017
venue: "International Conference"
paper_url: "https://arxiv.org/abs/1703.07402"
topics: ["Multiple Object Tracking", "Deep Learning", "Computer Vision", "Data Association"]
---

## **📄 Simple Online and Realtime Tracking with a Deep Association Metric 개요**

- **발표 논문**: Simple Online and Realtime Tracking with a Deep Association Metric (Deep SORT), Nicolai Wojke, Alex Bewley, Dietrich Paulus, 2017.[1]
- **핵심 아이디어**:
기존의 [[SORT (Simple Online and Realtime Tracking)]] 프레임워크에 외형 정보(appearance information)를 통합하여 다중 객체 추적(Multiple Object Tracking, MOT) 성능을 개선한 방법론을 제안한다. 특히, 객체 재식별(re-identification)을 위한 [[딥 러닝 (Deep Learning)]] 기반의 [[연관성 측정 (Association Metric)]]을 도입하여, 장기간의 [[가려짐 (Occlusion)]] 상황에서도 객체 ID 전환(identity switches)을 효과적으로 줄이는 데 중점을 둔다.[2][1][3]
- **주요 성과**:
    - 기존 SORT 대비 ID 전환(identity switches)을 45% 감소시켰다.[1][3]
    - 높은 프레임 속도(high frame rates)에서도 경쟁력 있는 전반적인 성능을 달성했다.[1][3]
    - 실시간(realtime) 온라인 추적 환경에 적합한 속도와 정확도를 제공한다.[4]

---

## **🏗 아키텍처 개요**

Deep SORT는 기본적으로 SORT 프레임워크를 따르며, 여기에 외형 정보를 활용하는 딥 러닝 기반의 연관성 측정(deep association metric)을 추가한다.

### **0. 기호/차원**
- 객체 상태(State of each target): $x = [u, v, s, r, \dot{u}, \dot{v}, \dot{s}]$[4]
    - $(u, v)$: 타겟의 중심 픽셀 위치 (수평, 수직)
    - $s$: 타겟 바운딩 박스의 스케일 (면적)
    - $r$: 타겟 바운딩 박스의 종횡비 (aspect ratio), 상수로 간주
    - $\dot{u}, \dot{v}, \dot{s}$: 각각 $u, v, s$의 속도 성분

### **1. SORT (Simple Online and Realtime Tracking) 기반**
- **구성**:
    1. **[[객체 감지 (Object Detection)]]**: Faster R-CNN (FrRCNN)과 같은 CNN 기반 감지기를 활용하여 각 프레임에서 객체 바운딩 박스를 얻는다.[4]
    2. **[[상태 추정 (State Estimation)]]**: 각 트랙의 상태는 [[칼만 필터 (Kalman Filter)]]를 사용하여 선형 등속도 모델(linear constant velocity model)으로 예측 및 업데이트된다.[4]
    3. **[[데이터 연관 (Data Association)]]**: 헝가리안 알고리즘(Hungarian algorithm)을 사용하여 현재 감지된 객체와 기존 트랙을 연결한다.[2][4]
- **특이 사항**:
    - 기존 SORT는 주로 바운딩 박스 간의 [[IoU (Intersection-over-Union)]] 거리를 연관성 측정에 사용한다.[2]
    - 짧은 시간의 가려짐(occlusion)은 IoU 거리로 암묵적으로 처리될 수 있다.[4]

### **2. Deep Association Metric 통합**
- **구성**:
    1. **[[외형 특징 추출 (Appearance Feature Extraction)]]**: 대규모 사람 재식별(person re-identification) 데이터셋으로 사전 학습된 [[합성곱 신경망 (Convolutional Neural Network, CNN)]]을 사용하여 각 감지된 객체로부터 외형 특징(appearance feature)을 추출한다.[2][1]
    2. **[[연관성 비용 (Association Cost)]]**: 마할라노비스 거리(Mahalanobis distance)와 외형 특징 간의 코사인 거리(cosine distance)를 결합한 새로운 연관성 비용을 계산한다.[5]
    3. **[[게이팅 (Gating)]]**: 마할라노비스 거리와 외형 거리 모두에 대한 임계값을 사용하여 불가능한 연관성을 필터링한다.[5]

### **3. 주요 수식 요약**
- **마할라노비스 거리 (Mahalanobis Distance)**:
  - $d^{(1)} = (d_j - y_i)^T S_i^{-1} (d_j - y_i)$[5]
    - $d_j$: $j$-번째 감지(detection)
    - $y_i, S_i$: $i$-번째 트랙의 측정 공간에서의 평균 및 공분산
- **외형 거리 (Appearance Distance)**:
  - $d^{(2)} = \min \{1 - r_j^T r_k \mid r_k \in R_i \}$[5]
    - $r_j$: $j$-번째 감지의 외형 특징
    - $R_i$: $i$-번째 트랙과 연관된 최근 외형 특징들의 집합
- **연관성 비용 행렬 (Cost Matrix)**:
  - $c_{i,j} = \lambda d^{(1)} + (1-\lambda) d^{(2)}$ (실제 구현에서는 카메라 움직임이 클 경우 $\lambda=0$으로 설정)[5]
- **게이트 행렬 (Gate Matrix)**:
  - $b_{i,j} = \mathbb{1}[d^{(1)} \le t^{(1)}] \times \mathbb{1}[d^{(2)} \le t^{(2)}]$ (마할라노비스 거리는 불가능한 측정을 걸러내는 데 사용)[5]

---

## **🎯 주요 구성 요소**

### **1. [[딥 연관성 측정 (Deep Association Metric)]]**
- 입력/출력 및 작동 원리 설명:
    - 입력: 감지된 객체의 이미지 패치.
    - 출력: L2 정규화된 외형 특징 벡터.
    - 작동 원리: 대규모 재식별 데이터셋에서 [[트리플렛 손실 (Triplet Loss)]]을 사용하여 학습된 CNN을 통해 객체의 고유한 외형 특징을 추출한다. 이 특징은 트랙과 감지 간의 유사도를 측정하는 데 사용되어, 기존 SORT의 IoU 기반 연관성 측정의 한계를 보완한다.[5]
- $$c_{i,j} = \lambda d^{(1)} + (1-\lambda) d^{(2)}$$[5]

### **2. [[칼만 필터 (Kalman Filter)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명:
    - 각 객체 트랙에 대해 독립적으로 동작하며, 객체의 위치, 크기, 종횡비 및 이들의 속도를 추정한다.
    - 감지된 바운딩 박스를 사용하여 트랙 상태를 업데이트하며, 감지가 없는 경우 선형 등속도 모델로 상태를 예측한다.[4]
- 설정 값 (논문 기준):
    - 초기 칼만 필터 공분산은 튜닝을 통해 설정된다.[4]
    - 새로운 트래커 생성 시 속도 공분산은 불확실성을 반영하여 큰 값으로 초기화된다.[4]

### **3. [[헝가리안 알고리즘 (Hungarian Algorithm)]]**
- 연관성 비용 행렬을 기반으로 감지된 객체와 기존 트랙 간의 최적의 일대일 매칭(one-to-one correspondence)을 수행한다.[4]

---

## **⚖️ [Deep SORT] vs [SORT]**

| **비교 항목** | **Deep SORT** | **SORT** |
| :--- | :--- | :--- |
| **연관성 측정** | 외형 특징 기반 딥 연관성 측정 + 마할라노비스 거리 | IoU (Intersection-over-Union) |
| **가려짐 처리** | 외형 특징을 통해 장기간 가려짐에도 ID 유지 가능 | 단순 모션 모델로 가려짐에 취약, ID 전환 빈번 |
| **ID 전환** | 45% 감소[1][3] | 빈번함[5] |
| **복잡도** | SORT보다 약간 높지만, 딥 연관성 학습은 오프라인에서 수행 | 단순하고 효율적 |
| **성능** | 높은 정확도와 실시간 처리 속도[1][3][4] | 빠른 속도, ID 전환 문제로 정확도 한계[5] |

- Deep SORT는 SORT의 단순성과 효율성을 유지하면서, 딥 러닝 기반의 외형 특징을 활용하여 ID 전환 문제를 크게 개선함으로써 다중 객체 추적의 견고성을 향상시켰다.[2][1][3]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 온라인(online) 프레임-바이-프레임(frame-by-frame) 추적 방식.[1][4]
- **특징**:
    - **트랙 생성 및 삭제**: IoU가 낮은 감지는 새로운 트랙으로 간주되며, 일정 기간(T 프레임) 동안 감지되지 않으면 트랙이 종료된다.[4]
    - **확률 기간 (Probationary Period)**: 새로운 트랙은 오탐(false positives)을 방지하기 위해 충분한 증거가 축적될 때까지 시험 기간을 거친다.[4]
    - **재식별**: 객체가 다시 나타나면 새로운 ID로 추적이 재개될 수 있다 (본 논문의 범위는 아님).[4]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - 딥 연관성 측정 학습: 대규모 사람 재식별(person re-identification) 데이터셋.[1]
    - 객체 감지: PASCAL VOC 챌린지 데이터셋으로 학습된 FrRCNN(VGG16) 사용.[4]
- **하드웨어**: Intel i7 2.5GHz 머신 (싱글 코어), 16GB 메모리에서 추적 구성 요소가 260Hz로 실행.[4]
- **학습 시간**: 딥 연관성 측정은 오프라인에서 사전 학습된다.[1]
- **옵티마이저**: (논문에 명시되지 않음, 재식별 네트워크 학습 시 사용되었을 것으로 추정)
- **규제(Regularization)**: (논문에 명시되지 않음)

---

## **⚠️ 한계**
- **재식별의 한계**: 본 논문에서는 장기간 가려짐 이후 객체가 다시 나타났을 때 새로운 ID로 추적을 재개하는 방식이므로, 장기적인 ID 유지는 추가 연구가 필요하다.[4]
- **단순 모션 모델**: 선형 등속도 모델은 복잡하거나 비선형적인 객체 움직임을 정확하게 예측하는 데 한계가 있을 수 있다.[4]

---

## **📊 주요 실험 결과**

### **[MOT 벤치마크 성능]**

|**모델**|**MOTA (↑)**|**MOTP (↑)**|**ID sw (↓)**|**FP (↓)**|**FN (↓)**|
|---|---|---|---|---|---|
| MDP [12] | 30.3 | 71.3 | 680 | 9717 | 32422 |
| SORT (Proposed) | 33.4 | 72.1 | 1001 | 7318 | 32615 |
| Deep SORT (확장) | (SORT 대비 ID sw 45% 감소) | (경쟁력 있는 성능) | (SORT 대비 45% 감소) | | |

- Deep SORT는 MOT 벤치마크에서 기존 SORT 대비 ID 전환을 45% 감소시키며, 높은 프레임 속도에서도 경쟁력 있는 성능을 보여주었다.[1][3]
- 특히, ID 전환(ID sw) 지표에서 큰 개선을 이루어, 가려짐 상황에서의 트랙 견고성을 입증했다.[1][3]

---

## **🔮 향후 연구 방향**
- **탐지 및 추적 프레임워크의 긴밀한 결합**: 탐지 품질이 추적 성능에 미치는 중요성을 강조하며, 탐지(detection)와 추적(tracking)을 더욱 긴밀하게 결합하는 프레임워크에 대한 연구를 제안한다.[4]
- **장기 가려짐 처리**: 객체 재식별(re-identification)을 통해 장기간의 가려짐을 처리하는 방법에 대한 추가 연구가 필요하다.[4]

---

## **🔗 관련 링크**
- [[Multiple Object Tracking]]
- [[Kalman Filter]]
- [[Hungarian Algorithm]]
- [[Deep Learning]]
- [[Person Re-identification]]

## **📌 참고 링크**
- **논문 원문**: [https://arxiv.org/abs/1703.07402](https://arxiv.org/abs/1703.07402)[1]
- **코드**: (논문에서 직접적인 코드 링크는 제공되지 않으나, GitHub 등에서 Deep SORT 구현을 찾을 수 있음)

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics[0]) AND file.name != this.file.name
SORT year desc
```
