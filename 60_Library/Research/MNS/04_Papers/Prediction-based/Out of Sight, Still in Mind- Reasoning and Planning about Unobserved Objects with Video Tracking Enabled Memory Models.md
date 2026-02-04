---
alias: ["DOOM & LOOM", "Unobserved Object Reasoning"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟧 Reading
rating: 0
date: 2026-02-04
title: "Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models"
authors: ["Yixuan Huang", "Jialin Yuan", "Chanho Kim", "Pupul Pradhan", "Bryan Chen", "Li Fuxin", "Tucker Hermans"]
year: 2024
venue: "IEEE Conference on Robotics and Automation (ICRA) 2024"
paper_url: https://arxiv.org/abs/2309.15278
topics: ["Robotics", "Object-Oriented Memory", "Relational Reasoning", "Planning", "Occlusion", "Video Tracking"]
---

## **📄 Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models 개요**

- **발표 논문**: Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models, Yixuan Huang et al., ICRA 2024[1][2]
- **핵심 아이디어**:
    로봇이 현실 환경에서 안정적으로 작동하기 위해서는 이전에 관찰했지만 현재 가려진(occluded) 객체에 대한 기억(memory)을 가지고 있어야 한다고 주장한다. 이 논문은 [[객체 지향 메모리]](object-oriented memory)를 다중 객체 조작 [[추론]](reasoning) 및 [[계획]](planning) 프레임워크에 인코딩하는 문제를 다룬다. 특히, [[DOOM]]과 [[LOOM]]이라는 두 가지 접근 방식을 제안하며, 이는 [[트랜스포머]](transformer) 기반의 [[관계형 역학]](relational dynamics)을 활용하여 부분 시점 [[포인트 클라우드]](partial-view point clouds)와 [[객체 발견 및 추적 엔진]](object discovery and tracking engine)으로부터 궤적(trajectory)의 이력을 인코딩한다[2]. 기존의 암묵적인(implicit) [[자기회귀 모델]](autoregressive models)보다 명시적인(explicit) 객체 인코딩이 장기 이력 관리 및 다운스트림 계획에 더 견고하다고 가정한다[1].
- **주요 성과**:
    - 가려진 객체(occluded objects)에 대한 추론, 새로운 객체 출현(novel objects appearance), 객체 재출현(object reappearance)을 포함한 여러 도전적인 작업을 수행할 수 있다[2].
    - 광범위한 시뮬레이션 및 실제 환경 실험에서 다양한 수의 객체와 방해 동작(distractor actions)에 대해 우수한 성능을 보인다[2].
    - 암묵적 메모리(implicit memory) 기준선(baseline)보다 뛰어난 성능을 입증했다[2].

---

## **🏗 아키텍처 개요**

[DOOM 및 LOOM 모델의 전체적인 구조 설명]

### **0. 기호/차원**
- $O_t$: 시간 $t$에서의 관찰된 객체 집합
- $M_t$: 시간 $t$에서의 메모리 내 객체 집합 (관찰 및 비관찰 객체 포함)
- $P_t$: 시간 $t$에서의 부분 시점 포인트 클라우드 입력
- $R_{ij}$: 객체 $i$와 $j$ 사이의 관계
- $A$: 로봇의 행동(action)

### **1. 객체 발견 및 추적 엔진 (Object Discovery and Tracking Engine)**
- **구성**: 비디오 추적(video tracking)을 통해 객체를 식별하고 궤적을 유지한다.
- **특이 사항**: [[UVOS]](Unsupervised Video Object Segmentation) 알고리즘을 활용하여 객체 지향 메모리를 명시적으로 관리한다[1].

### **2. 관계형 역학 인코더 (Relational Dynamics Encoder)**
- **구성**: [[트랜스포머]](Transformer) 또는 [[그래프 신경망]](Graph Neural Network, GNN) 기반의 인코더를 사용하여 가변적인 수의 객체를 인코딩한다[1].
- 각 층:
    1. **[[객체 임베딩]](Object Embedding)**: 각 객체의 특징을 추출한다.
    2. **[[관계 인코딩]](Relational Encoding)**: 객체 간의 상호작용 및 환경과의 관계를 학습한다.
- **특이 사항**: Huang et al.의 기존 프레임워크에 UVOS 기반 메모리 모델을 통합하여 관계형 역학을 학습한다[1].

### **3. 메모리 관리 모듈 (Memory Management Module)**
- **구성**: 관찰된 객체와 추적된 비관찰 객체를 통합하여 장기적인 객체 이력을 유지한다.
- **특이 사항**: [[DOOM]]과 [[LOOM]]은 이 모듈을 통해 가려진 객체에 대한 추론을 가능하게 한다[2].

### **4. 주요 수식 요약**
- **객체 관계 예측**:
  - $P(R_{ij, t+1} | M_t, A_t)$
- **객체 상태 업데이트**:
  - $M_{t+1} = f(M_t, P_t, A_t)$ (여기서 $f$는 트랜스포머 관계형 역학을 포함하는 함수)

---

## **🎯 주요 구성 요소**

### **1. [[DOOM (Dynamic Object-Oriented Memory)]]**
- **입력/출력 및 작동 원리 설명**: 부분 시점 포인트 클라우드와 객체 추적 정보를 입력받아, 트랜스포머 관계형 역학을 통해 객체 궤적의 이력을 인코딩하고 동적으로 객체 메모리를 관리한다[2].
- $$M_{t+1} = \text{Transformer}(M_t, \text{ObjectFeatures}(P_t), A_t)$$

### **2. [[LOOM (Long-term Object-Oriented Memory)]]**
- **병렬 처리, 분할, 혹은 특수 기능 설명**: DOOM과 유사하게 트랜스포머 관계형 역학을 활용하지만, 장기적인 관점에서 객체 메모리를 유지하고 관리하는 데 중점을 둔다[2].
- **설정 값 (논문 기준)**: (구체적인 설정 값은 논문 본문 참조 필요)

### **3. [[UVOS (Unsupervised Video Object Segmentation)]]**
- **설명**: 객체 지향 메모리를 명시적으로 관리하기 위해 사용되는 알고리즘으로, 로봇 조작 작업에서 객체에 대한 분할 레이블이 없는 경우에도 활용될 수 있다[1].

---

## **⚖️ [제안 모델] vs [기존 모델]**

| **비교 항목** | **DOOM/LOOM (제안 모델)** | **암묵적 메모리 기준선 (Implicit Memory Baseline)** |
| :--- | :--- | :--- |
| **메모리 관리** | 명시적(Explicit) 객체 지향 메모리[1] | 암묵적(Implicit) 자기회귀 모델[1] |
| **가려진 객체 추론** | 가능[2] | 어려움/불가능 |
| **장기 이력 관리** | 견고함[1] | 제한적 |
| **관계 예측** | 객체-객체 및 객체-환경 관계 예측 가능[1] | 제한적 |
| **복잡도** | $O(N^2)$ 또는 $O(N \log N)$ (트랜스포머/GNN 기반) | $O(N)$ (RNN/CNN 기반) |

- 제안 모델인 DOOM과 LOOM은 명시적인 객체 지향 메모리 관리를 통해 가려진 객체에 대한 추론 및 장기적인 이력 관리에서 기존의 암묵적 메모리 모델보다 우수한 성능과 견고함을 보인다[1][2].

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 객체 발견 및 추적 엔진을 통해 현재 관찰된 객체와 과거 메모리 내 객체 정보를 통합한다. 관계형 역학 인코더를 통해 객체 간의 관계 및 상태 변화를 추론하고, 이를 바탕으로 로봇의 행동 계획을 수립한다.
- **특징**: 가려진 객체에 대한 정보를 메모리에서 유지하고 활용하여, 시야에 없는 객체에 대해서도 추론하고 계획을 세울 수 있다.

---

## **⚙️ 학습 설정**

- **데이터셋**: (구체적인 데이터셋 이름은 논문 본문 참조 필요) 시뮬레이션 및 실제 환경 데이터셋을 활용[2].
- **하드웨어**: (구체적인 GPU/TPU 사양 및 개수는 논문 본문 참조 필요)
- **학습 시간**: (구체적인 학습 시간은 논문 본문 참조 필요)
- **옵티마이저**: (구체적인 옵티마이저 및 파라미터는 논문 본문 참조 필요)
- **규제(Regularization)**: (구체적인 규제 기법은 논문 본문 참조 필요)

---

## **⚠️ 한계**
- (논문 본문에서 명시된 한계점은 검색 결과에서 직접적으로 확인되지 않음. 일반적인 추론)
- UVOS 알고리즘의 성능에 따라 전체 시스템의 객체 추적 및 메모리 관리 성능이 영향을 받을 수 있다.
- 복잡한 환경에서 다수의 객체가 장시간 가려지는 경우, 메모리 내 객체 상태의 정확도가 저하될 수 있다.

---

## **📊 주요 실험 결과**

### **[메인 태스크 성능]**

|**모델**|**가려진 객체 추론 성공률**|**계획 성공률**|
|---|---|---|
| 암묵적 메모리 기준선 | 낮음 | 낮음 |
| **DOOM/LOOM (제안 모델)** | **높음** | **높음** |

---

## **🔮 향후 연구 방향**
- (논문 본문에서 명시된 향후 연구 방향은 검색 결과에서 직접적으로 확인되지 않음. 일반적인 추론)
- UVOS 알고리즘의 견고성 및 정확도 향상.
- 더 복잡하고 동적인 환경에서의 객체 지향 메모리 관리 및 계획 능력 확장.
- 다양한 로봇 조작 작업에 대한 적용 및 일반화.

---

## **🔗 관련 링크**
- [[객체 지향 메모리]]
- [[관계형 추론]]
- [[로봇 계획]]
- [[트랜스포머]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2309.15278[2]
- **코드**: (논문 웹사이트 또는 arXiv 페이지에서 확인 필요)

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
