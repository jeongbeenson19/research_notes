---
aliases: ["Mamba: Linear-Time Sequence Modeling with Selective State Spaces"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟩 Done
rating: 5
date: 2023-12-01
title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
authors: ["Albert Gu", "Tri Dao"]
year: 2023
venue: "arXiv"
paper_url: "https://arxiv.org/abs/2312.00752"
topics: ["State Space Models", "Sequence Modeling", "Transformers", "Deep Learning", "Language Modeling"]
---

## **📄 Mamba: Linear-Time Sequence Modeling with Selective State Spaces 개요**

- **발표 논문**: Mamba: Linear-Time Sequence Modeling with Selective State Spaces by Albert Gu and Tri Dao, arXiv (2023)[1][2]
- **핵심 아이디어**:
    Mamba는 [[Transformer]] 아키텍처의 핵심인 [[Attention]] 메커니즘을 [[Selective State Space Models (SSMs)]]로 대체하여 긴 시퀀스에서의 계산 비효율성을 해결하는 새로운 모델 아키텍처를 제안합니다. 기존 SSM의 한계점인 내용 기반 추론(content-based reasoning) 능력을 개선하기 위해 SSM 파라미터가 입력에 따라 동적으로 변화하도록 설계하여, 모델이 현재 토큰에 따라 정보를 선택적으로 전파하거나 망각할 수 있게 합니다. 이는 선형적인 시퀀스 길이 스케일링을 가능하게 하며, 하드웨어 인지 병렬 알고리즘을 통해 효율적인 추론을 제공합니다.[3][4][1][5][6][2][7]
- **주요 성과**:
    - [[Transformer]] 대비 5배 빠른 추론 처리량(throughput)을 달성합니다.[4][5][8]
    - 시퀀스 길이에 대해 선형적으로 스케일링하며, 최대 백만 길이의 시퀀스에서도 성능이 향상됩니다.[4][1][5][6][9][2]
    - 언어, 오디오, 유전체학 등 다양한 양식에서 [[State-of-the-Art (SOTA)]] 성능을 달성합니다.[3][4][1][5][6][2]
    - Mamba-3B 모델은 동일 크기의 [[Transformer]] 모델을 능가하고, 두 배 크기의 [[Transformer]] 모델과 유사한 성능을 보입니다.[4][1][2]

---

## **🏗 아키텍처 개요**

Mamba는 [[Attention]]이나 [[MLP]] 블록 없이 [[Selective SSM]]을 통합한 단순화된 엔드-투-엔드 신경망 아키텍처입니다.[4][1][5][6][2] 이는 기존 [[SSM]] 아키텍처와 [[Transformer]]의 [[MLP]] 블록 설계를 단일 블록으로 결합하여 단순하고 균일한 아키텍처를 이룹니다.[1][8]

### **0. 기호/차원**
- $x_t$: 시퀀스의 $t$번째 입력 토큰
- $h_t$: 시퀀스의 $t$번째 시점의 은닉 상태 (latent state)
- $y_t$: 시퀀스의 $t$번째 출력
- $A, B, C, D$: 상태 공간 모델의 파라미터 행렬
- $\Delta$: 이산화(discretization) 파라미터

### **1. Mamba 블록**
- **구성**: Mamba 블록은 선형 투영(linear projections), 게이팅된 [[MLP]] 경로, 그리고 병렬로 연결된 [[Selective State Space]] 경로로 구성됩니다.[8] 이후 정규화(normalization) 및 잔여 연결(residual connections)이 적용됩니다.[8]
- 각 층:
    1. **[[Selective State Space Model (SSM)]]**: 입력에 따라 파라미터가 동적으로 결정되는 상태 공간 모델.
    2. **[[Gated MLP]]**: 게이팅 메커니즘을 포함하는 다층 퍼셉트론.
- **특이 사항**: [[Transformer]]와 달리 별도의 [[Attention]] 메커니즘이나 [[MLP]] 블록 없이 단일 블록으로 구성되어 있습니다.[4][1][5][6][2]

### **2. 전체 구조**
- Mamba는 이러한 Mamba 블록을 반복적으로 쌓아 올리는 방식으로 구성됩니다.[8] 이는 언어, 오디오, 유전체학 등 다양한 양식에서 일반적인 시퀀스 모델 백본으로 활용됩니다.[4][1][5][6][2]

### **3. 주요 수식 요약**
- **연속 시간 SSM**:
  - $\frac{dh(t)}{dt} = Ah(t) + Bx(t)$
  - $y(t) = Ch(t) + Dx(t)$
- **이산화된 SSM**:
  - $h_t = A_t h_{t-1} + B_t x_t$
  - $y_t = C_t h_t + D_t x_t$
  - 여기서 $A_t, B_t, C_t$는 입력 $x_t$에 따라 동적으로 생성되는 파라미터입니다.

---

## **🎯 주요 구성 요소**

### **1. [[Selective State Space Models (SSMs)]]**
- **입력/출력 및 작동 원리 설명**: 기존 [[SSM]]은 시간 불변(time-invariant) 파라미터($A, B, C$)를 사용하여 입력과 무관하게 상태를 업데이트했습니다. Mamba는 이 파라미터들을 입력 $x_t$의 함수로 만들어, 모델이 현재 토큰에 따라 정보를 선택적으로 전파하거나 망각할 수 있도록 합니다.[1][8][7] 이는 모델이 "내용 기반 추론(content-based reasoning)"을 수행할 수 있게 하여, 정보 밀도가 높은 이산적인 데이터(예: 텍스트)에서 성능을 크게 향상시킵니다.[4][1][5][6][8][2]
- $$A_t = f_A(x_t), B_t = f_B(x_t), C_t = f_C(x_t)$$

### **2. [[Hardware-aware Parallel Algorithm]]**
- **병렬 처리, 분할, 혹은 특수 기능 설명**: [[Selective SSM]]의 파라미터가 입력 의존적이 되면서 효율적인 컨볼루션(convolution) 사용이 어려워지지만, Mamba는 재귀 모드(recurrent mode)에서 작동하는 하드웨어 인지 병렬 알고리즘을 설계했습니다.[4][1][5][6][2] 이 알고리즘은 GPU 메모리 레이아웃에 최적화되어 있으며, 특히 SRAM을 효율적으로 활용하여 이산화 및 재귀 계산을 가속화합니다.[4][9]
- **설정 값 (논문 기준)**: NVIDIA A100 GPU에서 표준 PyTorch 스캔보다 최대 20-40배 빠르며, 시퀀스 길이 2K 이상에서는 [[FlashAttention-2]]보다도 빠릅니다.[8]

### **3. [[Simplified Architecture]]**
- Mamba는 [[Transformer]]의 [[MLP]] 블록과 기존 [[SSM]] 아키텍처의 설계를 단일 블록으로 통합하여, [[Attention]]이나 별도의 [[MLP]] 블록 없이도 강력한 성능을 발휘하는 단순하고 균일한 아키텍처를 제공합니다.[4][1][5][6][8][2]

---

## **⚖️ Mamba vs Transformer**

| **비교 항목** | **Mamba** | **Transformer** | **비교 모델 2** |
| :--- | :--- | :--- | :--- |
| **시퀀스 길이 스케일링** | 선형 ($O(L)$)[4][1][5][6][9][2] | 제곱 ($O(L^2)$)[6][8][7] | |
| **추론 처리량** | 5배 높음[4][5][8] | 낮음 | |
| **내용 기반 추론** | 가능 (Selective SSM)[4][1][5][6][8][2] | 가능 (Attention)[6] | |
| **아키텍처 복잡도** | 단순하고 균일함 (단일 Mamba 블록)[1][8] | Attention 및 MLP 블록의 조합 | |
| **장거리 의존성 모델링** | 효과적 (SSM의 고유 메커니즘)[6][9] | 효과적 (Attention)[6] | |
| **복잡도** | $O(L)$ | $O(L^2)$ | |

- Mamba는 [[Transformer]]의 핵심 단점인 긴 시퀀스에 대한 계산 비효율성($O(L^2)$)을 해결하고, 선형적인 스케일링($O(L)$)을 통해 훨씬 빠른 추론 속도를 제공합니다.[4][1][5][6][9][8][2][7] 또한, [[Selective SSM]]을 통해 [[Transformer]]와 유사한 내용 기반 추론 능력을 유지하면서도, 백만 토큰 이상의 매우 긴 컨텍스트에서도 성능이 향상되는 강점을 가집니다.[4][1][5][6][9][8][2]

---

## **🧠 추론/디코딩/생성 과정**
- **방식**: Mamba는 추론 시 재귀적(recurrent)으로 작동합니다.[4][1][6][9]
- **특징**: [[Transformer]]처럼 이전 요소들의 캐시(cache)가 필요 없으므로, 단계별로 일정한 시간(constant time per step)만 소요됩니다.[1][6][9] 이는 배치 크기를 훨씬 크게 가져갈 수 있게 하여 처리량을 크게 향상시킵니다.[8]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - 언어 모델링: The Pile[8]
    - 오디오 파형 및 DNA 시퀀스[3][4][1][5][6][9][2]
- **하드웨어**: NVIDIA A100 GPU[8]
- **학습 시간**: 명시된 학습 시간은 없으나, 최대 100만 길이의 시퀀스까지 성능이 향상됨을 보여줍니다.[4][1][5][6][9][2]
- **옵티마이저**: (정보 없음)
- **규제(Regularization)**: (정보 없음)

---

## **⚠️ 한계**
- 기존 [[State Space Models (SSMs)]]은 내부 역학이 시간에 고정되어 있어 정보 밀도가 높은 이산적인 데이터(예: 텍스트)에서 어려움을 겪었습니다.[8] Mamba는 [[Selective SSM]]을 통해 이 문제를 해결했지만, 초기 [[SSM]]의 이러한 한계가 Mamba 개발의 동기가 되었습니다.[4][1][5][6][8][2]

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**Pile Perplexity (1.4B)**|**LAMBADA Perplexity (1.4B)**|**LAMBADA Accuracy (1.4B)**|
|---|---|---|---|
| Pythia-1.4B | - | - | 55.2% (평균)[8] |
| RWKV-1.5B | - | - | 54.3% (평균)[8] |
| **Mamba-1.4B** | **6.80**[8] | **5.04**[8] | **59.7% (평균)**[8] |

- **언어 모델링**: Mamba-3B 모델은 동일 크기의 [[Transformer]]를 능가하고, 두 배 크기의 [[Transformer]]와 유사한 성능을 보였습니다.[4][1][2] 특히, 1.4B 파라미터 모델에서 Mamba는 [[Pythia-1.4B]] 및 [[RWKV-1.5B]]를 능가하는 성능을 보여주며, [[Transformer]]급 품질을 선형 비용으로 달성했습니다.[8]
- **오디오 및 유전체학**: Mamba는 [[SaShiMi]], [[Hyena]], [[Transformer]]와 같은 이전 [[SOTA]] 모델들을 능가하며, 백만 길이의 시퀀스까지 긴 컨텍스트에서 성능이 향상됩니다.[1][6]

---

## **🔮 향후 연구 방향**
- Mamba는 언어, 오디오, 유전체학 등 여러 양식에서 사전 학습 품질 및 도메인별 작업 성능 모두에서 일반적인 시퀀스 [[Foundation Model]] 백본으로서의 잠재력을 입증했습니다.[5][6] 이는 긴 컨텍스트를 다루는 다양한 응용 분야에서 Mamba의 확장 가능성을 시사합니다.[8]

---

## **🔗 관련 링크**
- [[State Space Models]]
- [[Transformer]]
- [[Attention]]
- [[Recurrent Neural Networks]]
- [[Convolutional Neural Networks]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2312.00752[1][2]
- **코드**: (논문에서 직접적인 코드 링크는 찾지 못했으나, 관련 구현이 존재할 수 있음)

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics[0]) AND file.name != this.file.name
SORT year desc
```
