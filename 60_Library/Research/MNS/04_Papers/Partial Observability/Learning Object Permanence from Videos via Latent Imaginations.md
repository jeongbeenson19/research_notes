---
alias:
  - Looping LOCI
type: paper
tags:
  - DeepLearning
  - Paper
  - ObjectPermanence
  - ComputerVision
  - PartialObservability
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "Looping LOCI: Developing Object Permanence from Videos"
authors:
  - Manuel Traub
  - Frederic Becker
  - Sebastian Otte
  - Martin V. Butz
year: 2023
venue: ICLR 2024
paper_url: https://arxiv.org/abs/2310.10372
topics:
  - Object Permanence
  - Compositional Scene Representation
  - Unsupervised Learning
  - Video Understanding
  - Intuitive Physics
---

## **📄 Looping LOCI: Developing Object Permanence from Videos 개요**

- **발표 논문**: Looping LOCI: Developing Object Permanence from Videos by Manuel Traub et al., submitted to ICLR 2024.[1]
- **핵심 아이디어**: 기존 [[Compositional Scene Representation Learning]] 모델들이 객체가 지속적으로 보여야 하거나 [[직관적 물리 (Intuitive Physics)]] 테스트에 실패하는 경향이 있는 문제를 해결하기 위해, [[Loci]] 아키텍처를 확장한 [[Loci-Looped]]를 제안한다.[1] 이 모델은 내부 처리 루프를 통해 [[객체 영속성 (Object Permanence)]] 개념을 학습하며, 감각 입력과 예측을 적응적으로 혼합하여 [[정보 융합 활동 (information-fused activities)]]을 생성한다.[1][2] 이를 통해 객체 [[가려짐 (Occlusion)]] 상황에서도 객체 상태를 추론할 수 있다.[1]
- **주요 성과**:
    - ADEPT 데이터셋에서 기존 [[Loci]] 및 [[SAVi]]와 같은 최신 모델 대비 더 나은 객체 추적 성능을 달성했다.[1][2]
    - CLEVRER 데이터셋에서 감각 입력 중단(마스킹) 상황에서 더 나은 성능을 보였다.[1][2]
    - 명시적인 이력 버퍼나 객체에 대한 지도 정보 없이도 장기간의 객체 가려짐을 통해 객체를 추적하는 방법을 학습한다.[2]

---

## **🏗 아키텍처 개요**

[[Loci-Looped]]는 기존 [[Loci]] (Traub et al., ICLR 2023) 아키텍처에 내부 처리 루프(internal processing loop)를 추가하여 확장한 모델이다.[1][2] 이 루프는 객체 상태를 결정하기 위해 감각 입력(sensory input)을 활용할지, 아니면 이전 객체 상태에만 의존할지를 결정한다.[1]

### **0. 기호/차원**
- (정보 없음)

### **1. 주요 파트 1 (내부 처리 루프)**
- **구성**: 감각 공간 정보(pixel-space information)와 예측(anticipations)을 적응적으로 혼합하여 [[정보 융합 활동 (information-fused activities)]]을 생성하도록 설계되었다.[1][2]
- **특이 사항**: 이 루프는 [[객체 영속성 (Object Permanence)]]과 방향성 관성(directional inertia)을 학습하게 한다.[2]

### **2. 주요 파트 2 (정보 없음)**
- (정보 없음)

### **3. 주요 수식 요약**
- **내부 처리 루프**:
  - $ \text{Adaptive blending of pixel-space information with anticipations} $

---

## **🎯 주요 구성 요소**

### **1. [[내부 처리 루프 (Internal Processing Loop)]]**
- 입력/출력 및 작동 원리 설명: 이 루프는 모델이 객체 상태를 결정할 때, 현재의 시각적 입력과 과거의 객체 상태에 대한 예측을 유연하게 결합한다.[1][2] 이를 통해 객체가 일시적으로 시야에서 사라지더라도 객체의 존재를 유지하고 추적할 수 있게 한다.[1][2]
- $$ \text{Adaptive blending of pixel-space information with anticipations} $$

### **2. [[객체 영속성 학습 메커니즘]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: [[Loci-Looped]]는 명시적인 이력 버퍼(explicit history buffer)나 객체에 대한 지도 정보 없이도 장기간의 객체 가려짐을 통해 객체를 추적하는 방법을 학습한다.[2]

### **3. [기타 구성 요소]**
- (정보 없음)

---

## **⚖️ Looping LOCI vs 기존 모델**

| **비교 항목** | **Looping LOCI** | **Loci** | **SAVi** |
| :--- | :--- | :--- | :--- |
| **객체 영속성 처리** | 내부 루프를 통한 적응적 혼합 및 학습[1][2] | 명시적인 객체 영속성 손실 사용[2] | (정보 없음) |
| **가려짐 상황 성능** | ADEPT 및 CLEVRER에서 SOTA 능가[1][2] | (정보 없음) | (정보 없음) |
| **학습 방식** | 비지도 학습[2] | (정보 없음) | (정보 없음) |
| **복잡도** | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ |

- [[Loci-Looped]]는 명시적인 지도 학습이나 이력 버퍼 없이도 객체 가려짐에 강건한 객체 추적 능력을 보여, 기존 모델들의 한계를 극복한다.[1][2]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 비지도 객체 식별 및 추적 (unsupervised object identification and tracking)[1]
- **특징**: 명시적인 이력 버퍼(explicit history buffer)나 객체에 대한 지도 정보 없이도 장기간의 객체 가려짐을 통해 객체를 추적하는 방법을 학습한다.[2]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - ADEPT[1][2]
    - CLEVRER[1][2]
- **하드웨어**: (정보 없음)
- **학습 시간**: (정보 없음)
- **옵티마이저**: [[Rectified Adam]] (Liu et al., 2021)[2]
- **규제(Regularization)**:
    - Truncated backpropagation through time[2]

---

## **⚠️ 한계**
- (스니펫에서 명확히 언급된 한계점은 없으나, 기존 모델들이 [[직관적 물리 (Intuitive Physics)]] 테스트에 실패하는 경향이 있다는 점을 통해 이 분야의 난이도를 짐작할 수 있다.)

---

## **📊 주요 실험 결과**

### **[메인 태스크 성능]**

|**모델**|**ADEPT (객체 추적)**|**CLEVRER (감각 중단)**|
|---|---|---|
| [비교 모델 A] | (정보 없음) | (정보 없음) |
| [비교 모델 B] | (정보 없음) | (정보 없음) |
| **Looping LOCI** | **SOTA 능가**[1][2] | **SOTA 능가**[1][2] |

---

## **🔮 향후 연구 방향**
- (명시적으로 언급된 부분은 없으나, [[직관적 물리 (Intuitive Physics)]] 학습의 진전을 목표로 한다.[1])

---

## **🔗 관련 링크**
- [[Object Permanence]]
- [[Compositional Scene Representation Learning]]
- [[Loci]]
- [[Unsupervised Learning]]
- [[Intuitive Physics]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2310.10372[3]
- **코드**: (정보 없음, CatalyzeX 링크에 "Paper and Code" 언급[4])

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
