---
tags:
  - math
  - information_theory
  - statistics
aliases:
  - KL Divergence
  - 쿨백-라이블러 발산
  - 상대 엔트로피
---

# Kullback-Leibler Divergence (KL Divergence)

Kullback-Leibler Divergence(KL 발산)는 두 확률 분포의 차이를 측정하는 지표입니다. 정보 이론에 기반하며, 특정 확률 분포 `P`가 다른 확률 분포 `Q`를 근사할 때 발생하는 정보 손실량(information loss)을 정량화합니다.

KL 발산은 비대칭적(asymmetric)이므로 `KL(P || Q) ≠ KL(Q || P)`이며, 거리(distance) 개념이 아닙니다.

## 수식

-   **이산 확률 분포**: `KL(P || Q) = Σ_x P(x) * log(P(x) / Q(x))`
-   **연속 확률 분포**: `KL(P || Q) = ∫ p(x) * log(p(x) / q(x)) dx`

## 머신러닝에서의 활용

-   **Variational Autoencoders (VAEs)**: 잠재 변수의 사후 분포(posterior)가 사전 분포(prior)와 얼마나 다른지 측정하는 데 사용됩니다.
-   **[[Knowledge Distillation]]**: Student 모델의 출력 분포(`Q`)가 Teacher 모델의 출력 분포(`P`)를 얼마나 잘 모방하는지 측정하는 Distillation Loss로 사용됩니다.
