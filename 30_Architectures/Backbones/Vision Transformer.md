---
tags: #AI #ComputerVision #Transformer #Architecture
aliases: [ViT, 비전 트랜스포머]
---

# Vision Transformer (ViT)

> **한 줄 요약**: 자연어 처리(NLP)에서 성공을 거둔 [[Transformer]] 아키텍처를 이미지 인식(Image Recognition) 문제에 적용하여, 이미지를 패치(patch)의 시퀀스로 처리하는 모델.

**Vision Transformer (ViT)** 는 2020년 Google 연구팀이 발표한 논문 "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"에서 제안되었습니다. 기존의 [[CNN]] 기반 모델이 지배적이던 컴퓨터 비전 분야에 Transformer를 성공적으로 도입하여 새로운 패러다임을 제시한 기념비적인 모델입니다.

---

## 1. 핵심 아이디어: 이미지를 문장처럼 처리하기

ViT의 핵심 아이디어는 이미지를 NLP에서 문장을 처리하는 방식과 유사하게, '단어들의 시퀀스'처럼 다루는 것입니다.

1.  **이미지를 패치로 분할 (Image to Patches)**: 입력 이미지를 `16x16` 또는 `32x32` 픽셀 크기의 작은 정사각형 패치(patch)들로 나눕니다. 예를 들어 `224x224` 이미지를 `16x16` 패치로 나누면 `(224/16) * (224/16) = 14 * 14 = 196`개의 패치가 생성됩니다.

2.  **패치 임베딩 (Patch Embedding)**: 각 패치를 평탄화(flatten)하여 `16x16x3 = 768`차원의 벡터로 만들고, 이를 학습 가능한 선형 투영(linear projection)을 통해 Transformer의 입력 차원(`D` 차원)에 맞는 벡터(토큰)로 변환합니다. 이 과정을 '패치 임베딩'이라 부릅니다.

3.  **`[class]` 토큰 추가**: [[BERT]]에서 영감을 받아, 패치 시퀀스의 맨 앞에 분류(classification)를 위한 특별 토큰인 `[class]` 토큰을 추가합니다. 이 토큰에 해당하는 Transformer 최종 출력이 이미지 전체를 대표하는 특징 벡터로 사용됩니다.

4.  **위치 정보 추가 (Positional Embeddings)**: 패치의 순서, 즉 공간적 위치 정보를 알려주기 위해 각 패치 벡터에 학습 가능한 위치 임베딩(Positional Embedding)을 더해줍니다. 위치 정보가 없으면 Transformer는 패치들의 순서를 구분할 수 없습니다.

5.  **Transformer 인코더 (Transformer Encoder)**: 이렇게 만들어진 전체 토큰 시퀀스( `[class]` 토큰 + 패치 토큰)를 표준 [[Transformer]] 인코더에 입력합니다. 인코더 내부의 [[Multi-Head Attention|Multi-Head Self-Attention]]은 모든 패치 쌍 간의 관계를 계산하여 이미지의 전역적인(global) 특징을 학습합니다.

6.  **분류 (Classification)**: Transformer 인코더를 거친 출력 시퀀스에서 `[class]` 토큰에 해당하는 벡터만을 MLP(Multi-Layer Perceptron) 헤드에 통과시켜 최종 클래스를 예측합니다.

## 2. ViT 아키텍처 상세

ViT는 표준 [[Transformer]]의 인코더 구조를 거의 그대로 사용합니다.

-   **Input**: `(N+1) x D` 차원의 토큰 시퀀스 (N: 패치 개수, D: 임베딩 차원)
-   **Transformer Encoder**:
    -   L개의 동일한 블록이 반복되는 구조.
    -   각 블록은 다음 두 개의 서브레이어(sub-layer)로 구성됩니다.
        1.  **Multi-Head Self-Attention (MSA)**
        2.  **MLP (Multi-Layer Perceptron)**
    -   각 서브레이어의 입력과 출력에는 잔차 연결(Residual Connection)이 적용되며, 서브레이어를 통과한 후에는 Layer Normalization이 수행됩니다.
    -   `MLP`는 2개의 선형 레이어와 GELU 활성화 함수로 구성됩니다.
-   **Output**: MLP Head를 통해 최종 클래스 확률 분포 출력.

## 3. 장점 및 한계

### 가. 장점
-   **뛰어난 확장성 (Excellent Scalability)**: 모델과 데이터셋의 크기가 커질수록 성능이 [[CNN]]보다 빠르게 향상되는 경향을 보입니다. 이는 대규모 데이터(예: JFT-300M, ImageNet-21k)로 사전 학습했을 때 SOTA(State-of-the-art) 성능을 달성한 원동력입니다.
-   **전역적 컨텍스트 학습 (Global Context Modeling)**: Self-Attention 메커니즘은 이미지 전체 패치들 간의 상호작용을 직접 계산하므로, CNN의 지역적인 수용 영역(receptive field) 한계를 벗어나 이미지의 전역적인 컨텍스트를 효과적으로 포착할 수 있습니다.
-   **적은 이미지 관련 편향 (Less Image-specific Inductive Bias)**: ViT는 CNN처럼 지역성(locality)이나 평행이동 등변성(translation equivariance)과 같은 이미지에 특화된 편향(inductive bias)이 적습니다. 이로 인해 더 유연하게 데이터로부터 직접 패턴을 학습할 수 있습니다.

### 나. 한계
-   **대규모 데이터셋 의존성**: 이미지에 대한 사전 지식(편향)이 적기 때문에, 중간 규모의 데이터셋(예: ImageNet-1k)에서는 ResNet과 같은 CNN 모델보다 성능이 낮습니다. 충분한 양의 데이터로 사전 학습하는 과정이 필수적입니다.
-   **높은 연산량**: Self-Attention은 토큰 개수(패치 개수)의 제곱에 비례하는 연산량을 요구합니다. 따라서 고해상도 이미지의 경우 패치 수가 급격히 늘어나 메모리 및 계산 비용이 매우 커집니다.

## 4. 주요 후속 연구

ViT의 한계를 극복하고 성능을 개선하기 위한 다양한 후속 연구가 진행되었습니다.

-   **DeiT (Data-efficient Image Transformer)**: 지식 증류(Knowledge Distillation)를 통해 대규모 데이터셋 없이 ImageNet-1k만으로도 효율적으로 학습하는 방법을 제시했습니다.
-   **Swin Transformer**: 계층적 구조(Hierarchical Structure)와 이동된 윈도우(Shifted Window) 기반의 Self-Attention을 도입하여, ViT의 높은 연산량 문제를 해결하고 일반적인 컴퓨터 비전 작업(탐지, 분할 등)에 더 쉽게 적용할 수 있도록 개선했습니다.
-   **[[Masked Autoencoders]]**: [[BERT]]의 Masked Language Model처럼 이미지 패치의 대부분을 마스킹하고 복원하는 자기지도학습(Self-Supervised Learning) 방식을 제안하여, 사전 학습의 효율성과 성능을 크게 향상시켰습니다.

---

## 5. 관련 개념

-   [[Transformer]]
-   [[Attention]]
-   [[Self-Attention]]
-   [[Multi-Head Attention]]
-   [[CNN]]
-   [[Self-Supervised Learning]]
-   [[Attention Is All You Need]]
-   [[BERT]]

## 6. 참고 자료

-   Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., ... & Houlsby, N. (2020). *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale*. https://arxiv.org/abs/2010.11929
