---
aliases: ["IMM-JHSE"]
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
  - Homography
  - IMM
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "One Homography is All You Need: IMM-based Joint Homography and Multiple Object State Estimation"
authors: ["Paul Johannes Claasen", "Johan Pieter de Villiers"]
year: 2024
venue: "Expert Systems with Applications"
paper_url: https://arxiv.org/abs/2409.02562
topics: ["Multi-Object Tracking", "Homography Estimation", "Interacting Multiple Model (IMM)", "State Estimation", "Computer Vision"]
---

## **📄 One Homography is All You Need: IMM-based Joint Homography and Multiple Object State Estimation 개요**

- **발표 논문**: "One Homography is All You Need: IMM-based Joint Homography and Multiple Object State Estimation" by Paul Johannes Claasen and Johan Pieter de Villiers, presented in Expert Systems with Applications.[1][2]
- **핵심 아이디어**:
    기존 다중 객체 추적(MOT) 방법론들이 종종 포괄적인 3D 센서 정보를 통합하는 것과 달리, 이 논문은 단일 초기 [[Homography]] 추정치만을 사용하여 온라인 [[Multi-Object Tracking (MOT)]]을 위한 혁신적인 접근 방식을 제시한다.[3][4][1] [[IMM Joint Homography State Estimation (IMM-JHSE)]]이라는 방법을 제안하며, [[Homography matrix]]와 그 동역학을 트랙 상태 벡터의 구성 요소로 모델링하여 타겟 움직임을 카메라 움직임과 분리한다.[3][4][1] 이 접근 방식은 이전 방법론에서 흔히 발생했던 예측된 트랙 위치를 왜곡하는 복잡한 카메라 움직임 보상 기법의 필요성을 제거한다.[3][4][1] 정적 및 동적 카메라 움직임 모델을 [[IMM filter]]를 사용하여 결합한다.[4][1]
- **주요 성과**:
    - 최소한의 3D 정보(단일 초기 Homography 추정치)만을 사용하여 MOT의 효율성과 적응성을 향상시킨다.[3][1]
    - 카메라 움직임 보상 기법의 명시적인 영향을 제거하여 예측된 트랙 위치 상태의 왜곡을 방지한다.[4][1]
    - 바운딩 박스 기반 BIoU 점수와 지면 평면 기반 Mahalanobis 거리를 IMM과 유사한 방식으로 혼합하여 연관(association)을 수행함으로써, 지면 평면에서 벗어나는 움직임에도 강건하다.[4][1]

---

## **🏗 아키텍처 개요**

IMM-JHSE는 [[Interacting Multiple Model (IMM)]] 필터를 사용하여 정적 및 동적 카메라 움직임 모델을 결합한다.[4][1] [[Homography matrix]]와 그 동역학을 트랙 상태 벡터의 일부로 모델링한다.[3][4][1] 간단한 바운딩 박스 움직임 모델을 사용하여 이미지 평면 정보를 통합하기 위해 바운딩 박스 위치를 예측한다.[4][1]

### **0. 기호/차원**
- **주요 기호 및 차원 정의**:
    - $H$: Homography matrix[3]
    - $x_t$: 트랙 상태 벡터 (지면 평면 상태 $x_t^W$와 Homography 열 벡터 $h_1^W, h_2^W, h_3^W$ 포함)[5]
    - $x_t^W = [x_t^W, \dot{x}_t^W, y_t^W, \dot{y}_t^W]^T$: 지면 평면 상태 (위치 및 속도)[5]
    - $h_1^W, h_2^W, h_3^W$: Homography matrix $H_W$의 첫 번째, 두 번째, 세 번째 열 벡터[5]
- **입력 데이터 차원**:
    - 초기 Homography 추정치 (단일)[4][1]
    - 바운딩 박스 측정값 (2D)[4][1]

### **1. Interacting Multiple Model (IMM) 필터**
- **구성**: [[Interacting Multiple Model (IMM)]] 필터[3][4][1]
- 각 층:
    1. **[[정적 카메라 움직임 모델]]**: 상수 Homography를 가정한다.[3]
    2. **[[동적 카메라 움직임 모델]]**: 카메라 움직임 관측에 따라 조정된다.[3]
- **특이 사항**: 두 모델을 결합하여 동적 환경에서의 추적 적응성을 높인다.[3]

### **2. 트랙 상태 벡터 모델링**
- **구성**: 트랙 상태 벡터 (Homography matrix 및 타겟 특성(위치, 속도) 포함)[3][4][1]
- 각 층:
    - [[Homography matrix]] 및 그 동역학 모델링[3][4][1]
    - 타겟의 지면 평면 상태 (위치, 속도) 모델링[3][5]

### **3. 주요 수식 요약**
- **트랙 상태 벡터**:
  - $x_t = [x_t^W, \dot{x}_t^W, y_t^W, \dot{y}_t^W, h_1^W, h_2^W, h_3^W]^T$[5]
- **지면 평면 상태**:
  - $x_t^W = [x_t^W, \dot{x}_t^W, y_t^W, \dot{y}_t^W]^T$[5]
- **Homography 열 벡터**:
  - $h_1^W, h_2^W, h_3^W$는 Homography matrix $H_W$의 열 벡터이다.[5]

---

## **🎯 주요 구성 요소**

### **1. [[IMM (Interacting Multiple Model) 필터]]**
- 입력/출력 및 작동 원리 설명: 여러 모델(정적/동적 카메라 움직임 모델)을 병렬로 실행하고, 각 모델의 가중치를 업데이트하며, 최종적으로 가중치 평균을 통해 상태 추정치를 산출한다.[3][4][1]
- $$P(M_j|Z_k) = \frac{1}{c} P(Z_k|M_j) \sum_{i=1}^r P(M_j|M_i) P(M_i|Z_{k-1})$$

### **2. [[Homography Matrix]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 이미지 평면과 지면 평면 간의 2D-2D 매핑을 제공한다.[1][6][5] 트랙 상태 벡터의 일부로 모델링되어 카메라 움직임과 타겟 움직임을 분리하는 데 사용된다.[3][4][1]
- 설정 값 (논문 기준): 단일 초기 Homography 추정치만 필요하다.[4][1]

### **3. [바운딩 박스 움직임 모델]**
- 간단한 바운딩 박스 움직임 모델을 사용하여 이미지 평면 정보를 통합하고 바운딩 박스 위치를 예측한다.[4][1]
- $x_t^M = x_{t-1}^M + \frac{1}{n-1} \sum_{i=t-n+1}^{t-1} (x_i^M - x_{i-1}^M)$

---

## **⚖️ [IMM-JHSE] vs [기존 모델]**

| **비교 항목** | **[IMM-JHSE]** | **[기존 3D MOT]** | **[기존 카메라 보상 MOT]** |
| :--- | :--- | :--- | :--- |
| **필요 3D 정보** | 단일 초기 Homography 추정치[4][1] | 정규 3D 측정값[4][1] | 정보 부족 |
| **카메라 움직임 처리** | Homography를 상태 벡터에 포함하여 카메라 움직임과 타겟 움직임 분리[3][4][1] | 복잡한 카메라 움직임 보상 기법 필요[3][4][1] | 명시적인 카메라 움직임 보상 기법 사용[3][4][1] |
| **강건성** | 지면 평면에서 벗어나는 움직임에도 강건함[4][1] | 정보 부족 | 정보 부족 |
| **복잡도** | $O(\dots)$ (정보 부족) | $O(\dots)$ (정보 부족) | $O(\dots)$ (정보 부족) |

- **표에 대한 해석 및 제안 모델의 장점 요약**: IMM-JHSE는 최소한의 3D 정보(단일 초기 Homography)만을 사용하여 기존 3D MOT 방법론의 복잡성을 줄이고, 카메라 움직임의 영향을 효과적으로 제거하여 예측 정확도를 높인다.[3][4][1] 또한, 바운딩 박스 기반 BIoU와 지면 평면 기반 Mahalanobis 거리를 혼합하여 다양한 움직임에 대한 강건성을 확보한다.[4][1]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: [[IMM filter]]를 기반으로 한 상태 추정 및 예측[3][4][1]
- **특징**:
    - 바운딩 박스 기반 BIoU 점수와 지면 평면 기반 Mahalanobis 거리를 IMM과 유사한 방식으로 혼합하여 연관(association)을 수행한다.[4][1]
    - 동적 프로세스 및 측정 노이즈 추정 기법을 활용한다.[4][1]

---

## **⚙️ 학습 설정**

- **데이터셋**: 정보 부족
- **하드웨어**: 정보 부족
- **학습 시간**: 정보 부족
- **옵티마이저**: 정보 부족
- **규제(Regularization)**: 정보 부족

---

## **⚠️ 한계**
- 높은 타겟 밀도(high target density) 상황에서는 추적 성능이 저하될 수 있다.[3]

---

## **📊 주요 실험 결과**

정보 부족

---

## **🔮 향후 연구 방향**
- 높은 타겟 밀도 상황에서의 추적 성능 개선을 위한 정교화(refinements)를 탐색할 수 있다.[3]

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Homography]]
- [[IMM Filter]]
- [[State Estimation]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2409.02562[7]
- **코드**: 정보 부족

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics[0]) AND file.name != this.file.name
SORT year desc
```
