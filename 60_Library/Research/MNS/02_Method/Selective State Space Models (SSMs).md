
# Selective State Space Models (SSMs)

**선택적 상태 공간 모델(Selective State Space Models, SSMs)**은 긴 시퀀스 데이터 모델링에서 효율성과 효과를 동시에 추구하는 새로운 유형의 [[State Space Models (SSMs)]]입니다. 특히 [[Transformer]] 아키텍처가 가진 계산 비효율성(시퀀스 길이에 대한 $O(L^2)$ 스케일링)을 해결하면서도, [[Attention]] 메커니즘의 핵심 장점인 내용 기반 추론(content-based reasoning) 능력을 유지하도록 설계되었습니다.

## 핵심 아이디어: 선택성(Selectivity)

기존의 전통적인 [[State Space Models (SSMs)]]은 시간 불변(time-invariant) 파라미터($A, B, C$)를 사용하여 입력과 무관하게 상태를 업데이트했습니다. 이는 모델이 입력의 내용에 따라 정보를 선택적으로 유지하거나 버리는 능력이 부족하여, 정보 밀도가 높은 이산적인 데이터(예: 텍스트)를 처리하는 데 한계가 있었습니다.

**선택적 SSMs**는 이러한 한계를 극복하기 위해 SSM 파라미터들을 **입력 $x_t$의 함수**로 만듭니다. 즉, 파라미터 $A, B, C$가 각 토큰의 내용에 따라 동적으로 변화합니다. 이 '선택성(selectivity)' 덕분에 모델은:

1.  **정보 선택적 전파/망각**: 현재 입력 토큰의 중요도에 따라 과거 정보를 상태에 '기억'하거나 '잊을지'를 결정할 수 있습니다.
2.  **내용 기반 추론**: [[Attention]] 메커니즘처럼 명시적인 유사도 계산 없이도, 입력 내용에 기반하여 정보를 처리하고 추론하는 능력을 가집니다.

## Mamba에서의 활용

Mamba는 이 선택적 SSMs를 핵심 구성 요소로 활용하여 [[Transformer]]의 효율성 문제를 해결했습니다. Mamba 아키텍처는 [[Attention]]이나 [[MLP]] 블록 없이 [[Selective SSM]]을 통합한 단순화된 엔드-투-엔드 신경망입니다.

### **작동 방식**

Mamba에서 선택적 SSMs는 다음과 같이 작동합니다.

1.  **입력 의존적 파라미터**: 각 시간 스텝 $t$에서, SSM의 파라미터 행렬 $A, B, C$ 및 이산화 파라미터 $\Delta$는 현재 입력 토큰 $x_t$에 의해 동적으로 생성됩니다.
    $$A_t = f_A(x_t), B_t = f_B(x_t), C_t = f_C(x_t), \Delta_t = f_\Delta(x_t)$$
    여기서 $f_A, f_B, f_C, f_\Delta$는 신경망 레이어(예: 선형 프로젝션)로 구현됩니다.
2.  **이산화 (Discretization)**: 연속 시간 SSM은 이산화 파라미터 $\Delta_t$를 사용하여 이산 시간 SSM으로 변환됩니다.
    $$h_t = \bar{A}_t h_{t-1} + \bar{B}_t x_t$$
    $$y_t = \bar{C}_t h_t + \bar{D}_t x_t$$
    여기서 $\bar{A}_t, \bar{B}_t$는 $A_t, B_t, \Delta_t$에서 유도된 이산화 파라미터이며, $\bar{C}_t, \bar{D}_t$는 $C_t, D_t$와 같거나 유사하게 사용됩니다.
3.  **병렬 처리 최적화**: 선택성이 도입되면 컨볼루션 연산의 효율성이 떨어질 수 있지만, Mamba는 하드웨어 인지 병렬 알고리즘을 통해 이산화 및 재귀 계산을 효율적으로 가속화합니다. 이는 GPU 메모리 레이아웃에 최적화되어 특히 SRAM을 효율적으로 활용합니다.

## 주요 장점

-   **선형 시간 복잡도**: 시퀀스 길이에 대해 선형적으로 스케일링($O(L)$)하므로, 매우 긴 시퀀스(수십만, 심지어 백만 토큰)에서도 효율적인 처리가 가능합니다. 이는 [[Transformer]]의 이차 복잡도($O(L^2)$) 문제를 해결합니다.
-   **향상된 내용 기반 추론**: 파라미터의 선택성을 통해 입력의 내용에 따라 정보를 필터링하고 요약하는 능력을 확보하여, [[Transformer]]에 필적하는 추론 성능을 보입니다.
-   **하드웨어 효율성**: 특수 설계된 병렬 알고리즘과 GPU 메모리 최적화를 통해 빠른 추론 처리량(throughput)을 달성합니다.
-   **다양한 양식에서의 성능**: 언어 모델링, 오디오 처리, 유전체학 등 여러 도메인에서 [[State-of-the-Art (SOTA)]] 성능을 달성합니다.

## 관련 개념
-   [[State Space Models (SSMs)]]
-   [[Mamba: Linear-Time Sequence Modeling with Selective State Spaces]]
-   [[Transformer]]
-   [[Attention]]
-   [[Sequence Modeling]]
