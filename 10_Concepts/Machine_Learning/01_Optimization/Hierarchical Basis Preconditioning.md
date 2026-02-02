---
tags:
  - ML
  - optimization
  - theory
  - ResNet
aliases:
  - 계층적 기저 사전조건화
  - HBP
---

# Hierarchical Basis Preconditioning (계층적 기저 사전조건화)

**Hierarchical Basis Preconditioning (HBP)** 는 본래 수치해석 분야, 특히 [[Multi-Grid Method|다중격자법]]에서 유래한 개념입니다. 조건수가 커서 풀기 어려운(ill-conditioned) 선형 시스템이나 편미분방정식(PDE) 문제를 더 쉽게 풀기 위해 사용됩니다.

핵심 아이디어는 문제를 **계층적 기저(Hierarchical Basis)** 로 재구성하여, 고주파(fine-scale) 성분과 저주파(coarse-scale) 성분을 다층적으로 분리하고, 이를 통해 최적화 문제의 조건수를 개선(**Preconditioning**)하는 것입니다.

## 📖 ResNet과의 연결

ResNet을 수학적으로 해석한 여러 연구에서는 ResNet의 **Residual Connection(잔차 연결)** 이 바로 이 **계층적 기저 사전조건화**와 유사한 역할을 수행한다고 설명합니다.

### Plain Network vs. ResNet

-   **Plain Network (일반 신경망)**: 네트워크가 깊어질수록, 전체 함수를 한 번에 학습해야 하는 최적화 문제는 조건수가 매우 커져(ill-conditioned) 학습이 어려워집니다. (Degradation 문제 발생)
-   **ResNet (잔차 신경망)**: Residual Connection `H(x) = F(x) + x` 구조를 통해, 네트워크가 전체 함수 `H(x)`를 직접 학습하는 대신 **잔차 함수 `F(x)`** 만을 학습하도록 유도합니다.

### ResNet이 HBP처럼 작동하는 방식

1.  **저주파 성분 보존**: 입력 `x`가 항등 매핑(Identity Mapping)인 Shortcut Connection을 통해 그대로 전달됩니다. 이는 정보의 큰 틀, 즉 저주파(coarse-scale) 성분이 손실 없이 보존됨을 의미합니다.
2.  **고주파 성분 학습**: 각 Residual Block은 이 저주파 성분에 약간의 수정(perturbation)을 가하는 **잔차 `F(x)`** 만을 학습합니다. 이는 고주파(fine-scale) 성분을 점진적으로 보정하는 과정과 유사합니다.

이러한 구조는 마치 다중격자법이 저주파와 고주파를 분리하여 문제를 푸는 방식처럼, 전체 최적화 문제를 조건수가 더 좋은(well-conditioned) 형태로 변환합니다. 결과적으로 ResNet은 매우 깊은 네트워크에서도 안정적인 학습이 가능해집니다.

## ✨ 요약 비교

| 항목        | Plain Network                                | ResNet (Residual Connection)                                                                 |
| ----------- | -------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **조건수**    | 크고 ill-conditioned                         | Preconditioning을 통해 개선됨                                                                |
| **학습 방식** | 전체 함수를 직접 학습                        | **계층적 기저 사전조건화**처럼 큰 스케일(저주파)은 유지하고, 작은 스케일(고주파)의 잔차만 학습 |
| **효과**      | 학습 불안정, 성능 저하(degradation) 문제 발생 | 안정적인 학습, 경사 소실(vanishing gradient) 문제 완화                                       |

## 🔗 관련 개념

-   [[ResNet]]
-   [[Multi-Grid Method]]
-   [[Optimization]]
-   [[Condition Number]]