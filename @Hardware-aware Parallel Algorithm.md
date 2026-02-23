---
tags:
  - DeepLearning
  - SequenceModeling
  - HardwareOptimization
  - Mamba
aliases:
  - 하드웨어 인지 병렬 알고리즘
---

# Hardware-aware Parallel Algorithm (하드웨어 인지 병렬 알고리즘)

**하드웨어 인지 병렬 알고리즘(Hardware-aware Parallel Algorithm)**은 특정 하드웨어 아키텍처(주로 GPU)의 특성을 고려하여 계산을 최적화하고 병렬 처리의 효율성을 극대화하는 알고리즘입니다. [[Mamba: Linear-Time Sequence Modeling with Selective State Spaces]] 아키텍처에서 특히 중요한 역할을 합니다.

## 핵심 아이디어: Selective SSMs의 효율적 구현

[[Mamba]]의 핵심인 [[Selective State Space Models (SSMs)]]은 SSM 파라미터가 입력에 따라 동적으로 변화합니다. 이러한 '선택성'은 모델의 내용 기반 추론 능력을 크게 향상시키지만, 전통적인 [[SSM]]s에서 사용되던 효율적인 컨볼루션(convolution) 기반의 병렬화 기법을 적용하기 어렵게 만듭니다. 입력에 따라 파라미터가 달라지므로, 고정된 필터를 사용하는 컨볼루션 연산으로 전체 시퀀스를 한 번에 처리하기 어렵기 때문입니다.

이러한 문제를 해결하기 위해 Mamba는 **하드웨어 인지 병렬 알고리즘**을 개발하여 [[Selective State Space Models (SSMs)]]를 효율적으로 구현합니다. 이 알고리즘은 재귀 모드(recurrent mode)로 작동하면서도 병렬 처리가 가능하도록 설계되었습니다.

## 작동 방식 (Mamba 기준)

Mamba의 하드웨어 인지 병렬 알고리즘은 GPU 아키텍처, 특히 메모리 계층 구조를 깊이 이해하여 최적화되었습니다.

1.  **재귀 모드에서의 병렬화**:
    -   [[Selective State Space Models (SSMs)]]는 본질적으로 시퀀스를 토큰별로 순차적으로 처리하는 재귀적인 특성을 가집니다.
    -   Mamba의 알고리즘은 이러한 재귀 계산을 하드웨어 수준에서 병렬화하여, 각 시간 스텝의 계산을 독립적으로 가속화합니다. 이는 각 토큰에 대한 상태 업데이트를 효율적으로 분배하고 동시에 처리하는 것을 목표로 합니다.

2.  **GPU 메모리 최적화**:
    -   **SRAM (Shared Memory)** 활용: GPU의 고대역폭 온-칩 메모리인 SRAM을 적극적으로 활용합니다. Mamba의 계산 과정에서 중간 결과 및 파라미터를 SRAM에 효율적으로 배치하여, 훨씬 느린 DRAM(Global Memory) 접근을 최소화합니다. 이는 메모리 병목 현상을 줄이고 계산 속도를 극대화합니다.
    -   **메모리 레이아웃 최적화**: GPU의 물리적 메모리 구조에 맞춰 데이터와 파라미터의 접근 패턴을 최적화하여 캐시 효율성을 높이고, 데이터 전송 지연을 줄입니다.

3.  **이산화 및 재귀 계산 가속화**:
    -   연속 시간 SSM을 이산화하고, 이 이산화된 SSM의 재귀 계산 과정을 가속화하는 데 중점을 둡니다.
    -   이는 특히 배치 처리(batch processing) 시 재귀 계산을 효율적으로 구성하여, 여러 시퀀스 또는 여러 토큰에 대한 계산을 동시에 수행할 수 있도록 합니다.

## 주요 장점

-   **선형적인 시퀀스 길이 스케일링**: 복잡한 입력 의존적 파라미터에도 불구하고, 계산 복잡도를 시퀀스 길이에 대해 선형적으로($O(L)$) 유지할 수 있습니다.
-   **높은 추론 처리량**: NVIDIA A100 GPU에서 표준 PyTorch 스캔보다 최대 20-40배 빠른 속도를 보이며, 시퀀스 길이 2K 이상에서는 [[FlashAttention-2]]보다도 빠릅니다. 이는 대규모 언어 모델의 실시간 추론에 매우 유리합니다.
-   **GPU 자원 효율성**: SRAM과 같은 온-칩 메모리를 효율적으로 활용하여 메모리 사용량을 최적화하고, 계산 자원을 최대한 활용합니다.
-   **확장성**: 백만 길이 이상의 매우 긴 시퀀스에서도 효율적이고 강력한 성능을 제공하여, 다양한 양식(언어, 오디오, 유전체학 등)의 대규모 데이터셋 모델링에 적합합니다.

## 관련 개념
-   [[Mamba: Linear-Time Sequence Modeling with Selective State Spaces]]
-   [[Selective State Space Models (SSMs)]]
-   [[Transformer]]
-   [[GPU Optimization]]
-   [[SRAM]]
