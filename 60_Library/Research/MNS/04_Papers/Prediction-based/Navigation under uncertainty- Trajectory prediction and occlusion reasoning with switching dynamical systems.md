---
aliases: ["Navigation under uncertainty"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟧 Reading
rating: 0
date: 2026-02-04
title: "Navigation under uncertainty: Trajectory prediction and occlusion reasoning with switching dynamical systems"
authors: ["Ran Wei", "Joseph Lee", "Shohei Wakayama", "Petter Hoerling", "Peter Winzell", "Renjith Rajagopal", "Alexander Tschantz", "Conor Heins", "Christopher Buckley", "John Carenbauer", "Hari Thiruvengada", "Mahault Albarracin", "Miguel de Prado"]
year: 2024
venue: "arXiv"
paper_url: https://arxiv.org/abs/2410.10653
topics: ["Trajectory Prediction", "Occlusion Reasoning", "Switching Dynamical Systems", "Autonomous Driving"]
---

## **📄 Navigation under uncertainty: Trajectory prediction and occlusion reasoning with switching dynamical systems 개요**

- **발표 논문**: Navigation under uncertainty: Trajectory prediction and occlusion reasoning with switching dynamical systems (Ran Wei et al., 2024)[1][2]
- **핵심 아이디어**:
    자율주행 및 로봇 내비게이션에서 중요한 주변 객체의 미래 궤적 예측 및 [[오클루전 추론 (Occlusion Reasoning)]] 문제를 해결하기 위해, [[스위칭 동적 시스템 (Switching Dynamical Systems)]]이라는 구조화된 확률적 생성 모델(probabilistic generative model)을 제안한다. 기존의 고용량 모델(예: Transformer)이 대규모 데이터셋에서 효과적이지만, 불확실성 및 오클루전 상황에 대한 일반화에 어려움을 겪는 한계를 극복하고자 한다. 이 프레임워크는 궤적 예측과 오클루전 추론을 통합하여, 높은 예측 정확도와 불확실성 보정(uncertainty calibration)을 동시에 달성한다.[3][1][4]
- **주요 성과**:
    - 기존의 조건부 가우시안 혼합 모델(conditional Gaussian mixture models) 대비 높은 예측 정확도와 불확실성 보정 능력을 보여준다.[5]
    - Waymo open motion dataset을 활용한 초기 실험에서 모델의 유효성을 입증했다.[5][3]

---

## **🏗 아키텍처 개요**

[모델의 전체적인 구조 설명]

### **0. 기호/차원**
- $x_t$: 시간 $t$에서의 객체 상태 (위치, 속도 등)
- $s_t$: 시간 $t$에서의 이산 스위칭 변수 (discrete switching variable)
- $P(x_{t+1} | x_t, s_t)$: 스위칭 변수에 따른 동적 시스템
- $P(s_t | x_t)$: 스위칭 변수의 전이 확률

### **1. 스위칭 동적 시스템 (Switching Dynamical Systems)**
- **구성**: 여러 개의 단순한 동적 시스템(simple dynamical systems)과 이들을 중재하는 이산 스위칭 변수로 구성된다.[5]
- 각 층:
    1. **[[동적 시스템 (Dynamical System)]]**: 객체의 움직임을 모델링
    2. **[[스위칭 변수 (Switching Variable)]]**: 에이전트의 의도(intent) 및 행동 원시(behavior primitives)를 나타내거나, 객체 중심 모델(object-centric models)에서 객체 슬롯(object slots)을 나타낸다.[5]
- **특이 사항**: 일부 동적 시스템은 인간 전문가에 의해 수동으로 지정될 수 있어, 데이터 기반(data-driven)과 기계적(mechanistic) 시스템의 하이브리드 형태를 가질 수 있다.[5]

### **2. 오클루전 추론 (Occlusion Reasoning)**
- **구성**: 스위칭 동적 시스템 내에서 오클루전된 객체의 존재 및 움직임에 대한 불확실성을 유지하도록 설계되었다.[3][4]
- 각 층:
    [세부 구성 요소 나열]

### **3. 주요 수식 요약**
- **스위칭 동적 시스템**:
  - $P(X | S) = \prod_t P(x_t | x_{t-1}, s_t)$
- **스위칭 변수**:
  - $P(S) = \prod_t P(s_t | s_{t-1})$

---

## **🎯 주요 구성 요소**

### **1. [[스위칭 동적 시스템 (Switching Dynamical Systems)]]**
- 입력/출력 및 작동 원리 설명: 이 모델은 여러 개의 간단한 동적 시스템과 이들을 제어하는 이산 스위칭 변수로 구성된다. 궤적 예측을 위해 스위칭 변수는 에이전트의 의도와 행동 원시를 학습하며, 오클루전 추론을 위해 객체 중심 모델에서 객체 슬롯을 나타낸다.[5]
- $$P(x_{1:T}, s_{1:T}) = P(s_1) P(x_1|s_1) \prod_{t=2}^T P(s_t|s_{t-1}) P(x_t|x_{t-1}, s_t)$$

### **2. [[불확실성 보정 (Uncertainty Calibration)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 모델은 예측의 정확도뿐만 아니라 예측과 관련된 불확실성을 정량화하고 보정하는 데 중점을 둔다. 이는 자율주행 시스템의 안전한 의사결정에 필수적이다.[5][3]
- 설정 값 (논문 기준)

### **3. [[오클루전 추론 (Occlusion Reasoning)]]**
- 오클루전된 객체의 존재와 움직임에 대한 불확실성을 명시적으로 다루어, 기존 모델들이 간과했던 부분을 보완한다.[3][4]

---

## **⚖️ [제안 모델] vs [기존 모델]**

| **비교 항목** | **[제안 모델 (Switching Dynamical Systems)]** | **[비교 모델 1 (Conditional Gaussian Mixture Models)]** | **[비교 모델 2 (High-capacity models like Transformers)]** |
| :--- | :--- | :--- | :--- |
| **핵심 접근 방식** | 구조화된 확률적 생성 모델, 스위칭 동적 시스템 | 조건부 가우시안 혼합 모델 | 고용량 함수 근사기 |
| **오클루전 추론** | 명시적으로 불확실성 유지 및 추론 | 일반적으로 오클루션 객체 불확실성 무시 | 일반적으로 오클루션 객체 불확실성 무시 |
| **불확실성 보정** | 높은 불확실성 보정 능력 | 제한적 | 제한적 |
| **일반화 능력** | 장기적인 안전-중요 시나리오에 대한 일반화 개선 | 특정 시나리오에 효과적 | 표준 시나리오에 효과적, 장기 시나리오에 어려움 |
| **복잡도** | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ |

- 제안 모델은 궤적 예측과 오클루전 추론을 통합하여, 기존 모델들이 간과했던 오클루전된 객체에 대한 불확실성을 효과적으로 다루며, 높은 예측 정확도와 불확실성 보정 능력을 제공한다.[5][3][1][4]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 스위칭 동적 시스템의 확률적 추론을 통해 미래 궤적과 스위칭 변수의 시퀀스를 예측한다.
- **특징**: 이산 스위칭 변수를 통해 다양한 행동 양식과 오클루전 상태를 모델링하여, 보다 풍부하고 해석 가능한 예측을 가능하게 한다.

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - Waymo open motion dataset (자율주행 시나리오 데이터)[5][3]
- **하드웨어**: [GPU/TPU 사양 및 개수] (논문에 명시되지 않음)
- **학습 시간**: [Step 수 또는 시간] (논문에 명시되지 않음)
- **옵티마이저**: [이름 및 파라미터 ($\beta_1, \epsilon$ 등)] (논문에 명시되지 않음)
- **규제(Regularization)**:
    - [Dropout, Label Smoothing 등] (논문에 명시되지 않음)

---

## **⚠️ 한계**
- 논문은 초기 실험 결과를 제시하며, 더 광범위한 평가와 심층적인 분석이 필요하다.
- 모델의 예측이 회전 궤적(turning trajectories)에 대해서는 실제와 크게 벗어날 수 있다는 점이 언급되었다.[4]
- 고용량 모델에 비해 복잡한 시나리오에서의 성능 비교가 더 필요할 수 있다.

---

## **📊 주요 실험 결과**

### **[메인 태스크 성능]**

|**모델**|**[예측 정확도]**|**[불확실성 보정]**|
|---|---|---|
| Conditional Gaussian Mixture Models | 수치 (제안 모델보다 낮음) | 수치 (제안 모델보다 낮음) |
| **Switching Dynamical Systems (제안 모델)** | **높음** | **높음** |

---

## **🔮 향후 연구 방향**
- 스위칭 동적 시스템의 확장 및 다양한 자율주행 시나리오에 대한 적용 연구.
- 오클루전 추론의 정확도 및 강건성(robustness) 향상.
- 모델의 해석 가능성(interpretability)을 더욱 높이는 방안 모색.

---

## **🔗 관련 링크**
- [[Trajectory Prediction]]
- [[Occlusion Reasoning]]
- [[Switching Dynamical Systems]]
- [[Autonomous Driving]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2410.10653
- **코드**: (논문에 명시되지 않음)

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
