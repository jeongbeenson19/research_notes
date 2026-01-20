---
tags:
  - ML
  - neural_network
  - architecture
aliases:
  - 홉필드 네트워크
---

# Hopfield Network

**Hopfield Network(홉필드 네트워크)** 는 1982년 존 홉필드(John Hopfield)에 의해 대중화된 순환 신경망(Recurrent Neural Network)의 한 종류입니다. 이 네트워크의 가장 큰 특징은 **연상 메모리(Associative Memory)** 또는 내용 주소화 가능 메모리(Content-Addressable Memory)로 작동한다는 점입니다.

즉, 불완전하거나 노이즈가 낀 입력 패턴이 주어졌을 때, 네트워크가 학습 시에 저장했던 가장 유사한 '완전한' 패턴을 복원하여 출력합니다.

## 작동 원리

-   **에너지 함수**: 네트워크는 각 상태에 대한 '에너지'를 정의하며, 안정된 상태(저장된 패턴)는 에너지의 지역 최솟값(local minimum)에 해당합니다.
-   **패턴 복원**: 입력이 주어지면, 네트워크는 에너지 함수를 최소화하는 방향으로 뉴런의 상태를 반복적으로 업데이트하여 가장 가까운 안정된 상태(저장된 패턴)로 수렴합니다.
-   **학습**: 패턴을 저장하는 과정은 주로 [[Hebbian Rule|헤비안 규칙]]을 사용하여 가중치를 설정함으로써 이루어집니다.
