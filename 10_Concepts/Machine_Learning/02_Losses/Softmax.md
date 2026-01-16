---
tags:
  - ML
  - activation_function
aliases:
  - 소프트맥스
---

# Softmax Function

Softmax 함수는 다중 클래스 분류(Multi-class Classification) 문제에서 모델의 출력(Logits)을 각 클래스에 대한 확률 분포로 변환하는 활성화 함수입니다.

출력 벡터의 모든 요소를 0과 1 사이의 값으로 만들고, 모든 요소의 합이 1이 되도록 정규화합니다. 이를 통해 특정 입력이 각 클래스에 속할 상대적인 확률을 나타낼 수 있습니다.

## 수식

입력 벡터 `z`에 대한 Softmax 함수는 다음과 같이 정의됩니다.

`Softmax(z_i) = exp(z_i) / Σ_j exp(z_j)`

## Temperature Scaling

[[Knowledge Distillation]]에서는 **Temperature(T)** 하이퍼파라미터를 사용하여 Softmax의 출력을 부드럽게 조절합니다.

`Softmax(z_i, T) = exp(z_i / T) / Σ_j exp(z_j / T)`

-   T > 1 이면 확률 분포가 부드러워져, 정답 외의 클래스(Dark Knowledge)에 대한 정보가 더 강조됩니다.
