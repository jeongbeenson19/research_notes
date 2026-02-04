---
aliases:
  - MOTIP
type: paper
tags:
  - DeepLearning
  - Paper
  - Long-gap
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: Multiple Object Tracking as ID Prediction
authors:
  - Ruopeng Gao
  - Yijun Zhang
  - Limin Wang
year: 2025
venue: CVPR
paper_url: https://arxiv.org/abs/2403.16848
topics:
  - Multiple Object Tracking
  - ID Prediction
  - Computer Vision
  - Deep Learning
---

## **📄 Multiple Object Tracking as ID Prediction 개요**

- **발표 논문**: Multiple Object Tracking as ID Prediction by Ruopeng Gao, Yijun Zhang, Limin Wang (CVPR 2025)[1][2][3]
- **핵심 아이디어**:
    기존의 [[다중 객체 추적 (MOT, Multiple Object Tracking)]] 방법론들이 수작업으로 설계된 휴리스틱(handcrafted heuristics)에 의존하여 궤적 유지 및 비용 행렬 계산을 수행하는 한계를 극복하고자 한다[1][4]. 이 논문은 MOT를 [[In-context ID Prediction]] 문제로 재정의하여, 객체 탐지(object detection)와 연관(association)을 분리하고, 객체 연관을 [[End-to-end]] 학습 가능한 태스크로 전환하는 새로운 관점을 제안한다[1][2][4]. 이는 현재 탐지된 객체에 대해 [[ID Decoder]]와 [[Learnable ID Dictionary]]를 활용하여 직접 ID 레이블을 디코딩함으로써, 보지 못한 궤적(unseen trajectories)에도 일반화될 수 있도록 한다[1][2].
- **주요 성과**:
    - MOT를 [[In-context ID Prediction]]으로 단순화하여 [[End-to-end]] 학습을 가능하게 함[1][2].
    - 기존 휴리스틱 기반 방법론의 유연성 및 최적 추적 능력 학습의 한계를 해결[1].
    - 객체 수준 특징(object-level features)과 학습 가능한 ID 딕셔너리를 사용하여 현재 탐지된 객체의 ID 레이블을 직접 디코딩함으로써, 보지 못한 궤적에 대한 일반화(generalization)를 보장[1].

---

## **🏗 아키텍처 개요**

[[MOTIP]] 모델은 [[DETR]] 기반의 탐지기(detector), 학습 가능한 ID 딕셔너리(learnable ID dictionary), 그리고 ID 디코더(ID Decoder)의 세 가지 주요 구성 요소로 이루어져 있다[1].

### **0. 기호/차원**
- $T$: 시퀀스 길이 또는 시간 스텝
- $t$: 현재 프레임
- $T_{t-T:t-1}$: 과거 궤적 (historical trajectories)
- $D_t$: 현재 프레임 $t$에서의 탐지(detections)
- $ID_{labels}$: ID 레이블
- $ID_{embeddings}$: ID 임베딩

### **1. DETR 탐지기 (DETR Detector)**
- **구성**: [[DETR]] (DEtection TRansformer) 기반의 객체 탐지기로, 비디오 스트림 내에서 객체를 정확하게 찾아내는 역할을 한다[1][5].
- **특이 사항**: COCO 데이터셋으로 사전 학습된 가중치를 사용하여 초기화되며, 해당 데이터셋에서 탐지 사전 학습(detection pre-training)을 수행한다[5].

### **2. 학습 가능한 ID 딕셔너리 (Learnable ID Dictionary)**
- **구성**: 서로 다른 객체 ID를 나타내는 학습 가능한 임베딩(embeddings) 집합[1].
- **역할**: 각 궤적을 클래스로 취급하고, 전체 학습 과정 동안 일관된 고유 ID 레이블을 할당한다[5].

### **3. ID 디코더 (ID Decoder)**
- **구성**: 표준 [[Transformer Decoder]]를 사용한다[1].
- **역할**: 객체 특징(object features)과 해당 ID 임베딩(ID embeddings)을 결합하여 과거 궤적($T_{t-T:t-1}$)을 형성한다[1]. 이후 ID 토큰(ID tokens)을 [[Identity Prompts]]로 간주하고, 이를 기반으로 [[In-context ID Prediction]]을 수행하여 현재 객체의 ID 레이블을 예측한다[1].
- **특이 사항**: 가변 길이의 과거 트랙렛(variable-length historical tracklets)을 처리하며, 선형 분류 헤드(linear classification head)를 통해 ID 레이블을 예측한다[1].

### **4. 주요 수식 요약**
- 논문 스니펫에서는 구체적인 수식이 제공되지 않음.

---

## **🎯 주요 구성 요소**

### **1. In-context ID Prediction**
- 입력/출력 및 작동 원리 설명: [[MOTIP]]의 핵심 메커니즘으로, 과거 궤적 정보($T_{t-T:t-1}$)를 컨텍스트로 활용하여 현재 프레임의 탐지된 객체에 대한 ID 레이블을 예측한다[1]. ID 디코더는 ID 토큰을 프롬프트로 사용하여 이 예측을 수행한다[1].
- $$ID_{predicted} = Decoder(Features_{current}, ID_{prompts})$$ (개념적 수식)

### **2. ID Decoder (Transformer Decoder)**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 표준 [[Transformer Decoder]]를 사용하여 가변 길이의 과거 트랙렛을 처리하고, 선형 분류 헤드를 통해 ID 레이블을 예측한다[1]. 훈련 시에는 [[DETR]] 구성 요소의 순차적 포워드 패스(sequential forward passes)를 병렬화하여 효율성을 높인다[5].

### **3. ID 충돌 해결 (Duplicate ID Handling)**
- 동일한 프레임 내에서 중복 ID가 발생하는 경우, 가장 높은 신뢰도(confidence)를 가진 객체를 선택하고 나머지는 새로운 객체(newborn objects)로 레이블링하는 규칙을 적용하여 ID 충돌을 방지한다[5].

---

## **⚖️ MOTIP vs 기존 모델**

| **비교 항목** | **MOTIP (제안 모델)** | **기존 주류 MOT 방법론** |
| :--- | :--- | :--- |
| **ID 연관 방식** | [[In-context ID Prediction]] (End-to-end 학습)[1][2] | 수작업 휴리스틱(handcrafted heuristics) 기반[1][4] |
| **궤적 유지** | ID 디코더를 통한 직접 ID 디코딩[1] | 복잡한 휴리스틱 기법[4] |
| **비용 행렬 계산** | 필요 없음 (직접 ID 예측)[1] | 수작업으로 설계된 비용 행렬[1] |
| **일반화 능력** | 보지 못한 궤적에 대한 일반화 보장[1] | 도메인별 데이터에 대한 최적 추적 능력 학습에 제한[1] |
| **복잡도** | $O(N \cdot L)$ (N: 객체 수, L: 궤적 길이, Transformer 기반) | $O(N^2)$ 또는 그 이상 (매칭 알고리즘에 따라 다름) |

- [[MOTIP]]는 기존의 수작업 휴리스틱에 의존하는 [[MOT]] 방법론의 한계를 극복하고, [[End-to-end]] 학습을 통해 객체 연관(object association)을 수행함으로써 더 유연하고 일반화된 추적 능력을 제공한다[1].

---

## **🧠 추론/디코딩/생성 과정**
- **방식**: [[In-context ID Prediction]][1].
- **특징**: ID 디코더가 ID 토큰을 [[Identity Prompts]]로 사용하여 현재 탐지된 객체의 ID 레이블을 직접 예측한다[1]. 중복 ID 발생 시, 가장 높은 신뢰도를 가진 객체를 유지하고 나머지는 새로운 객체로 처리하는 규칙을 적용한다[5].

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - DanceTrack[5]
    - SportsMOT[5]
    - BFT[5]
- **하드웨어**: 8개의 NVIDIA RTX 4090 GPU[5]
- **학습 시간**:
    - DanceTrack: 10 에포크 (5, 9 에포크에서 학습률 10배 감소)[5]
    - SportsMOT: 13 에포크 (8, 12 에포크에서 학습률 10배 감소)[5]
    - BFT: 22 에포크 (16, 20 에포크에서 학습률 감소)[5]
- **옵티마이저**: (구체적인 옵티마이저 이름 및 파라미터는 스니펫에 명시되지 않음)
- **규제(Regularization)**: (구체적인 규제 기법은 스니펫에 명시되지 않음)
- **기타**: COCO 데이터셋으로 사전 학습된 가중치를 사용하여 [[DETR]] 부분 초기화 및 해당 데이터셋에서 탐지 사전 학습 수행[5]. 각 GPU의 배치 크기는 1로 설정[5]. 훈련 데이터의 다양성을 높이기 위해 1에서 4 사이의 무작위 샘플링 간격(random sampling intervals)을 사용한다[5].

---

## **⚠️ 한계**
- 논문 스니펫에서는 [[MOTIP]] 자체의 구체적인 한계점이 명시적으로 언급되지 않았다. 다만, 기존 [[MOT]] 방법론의 일반적인 문제점(객체 가려짐, 흐림, 높은 유사성 등)은 언급되어 있다[6].

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**
- 논문 스니펫에서는 DanceTrack, SportsMOT, BFT 데이터셋에서 훈련되었다고 언급되지만[5], 구체적인 성능 지표(예: MOTA, IDF1 등) 및 수치는 제공되지 않는다.

---

## **🔮 향후 연구 방향**
- 논문 스니펫에서는 향후 연구 방향에 대한 구체적인 내용은 언급되지 않음.

---

## **🔗 관련 링크**
- [[Multiple Object Tracking]]
- [[DETR]]
- [[Transformer]]

## **📌 참고 링크**
- **논문 원문**: [https://arxiv.org/abs/2403.16848](https://arxiv.org/abs/2403.16848)[4]
- **코드**: [https://github.com/MCG-NJU/MOTIP](https://github.com/MCG-NJU/MOTIP)[2]

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE year, Keyword
FROM #Long-gap
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
