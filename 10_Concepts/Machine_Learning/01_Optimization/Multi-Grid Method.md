---
tags:
  - numerical_methods
  - optimization
  - CV
  - theory
aliases:
  - 다중격자법
  - Multigrid
---

# Multi-Grid Method (다중격자법)

**Multi-Grid Method(다중격자법)**는 본래 수치해석 분야에서 편미분방정식(PDE)과 같은 대규모 선형 시스템을 효율적으로 풀기 위해 개발된 알고리즘입니다.

핵심 아이디어는 단일 해상도의 격자(grid)에서 문제를 푸는 대신, **다양한 해상도의 격자들을 계층적으로 오가며** 해를 점진적으로 개선하는 것입니다.

## 📖 기본 원리

-   **고주파 오차와 저주파 오차**: 오차(error)는 다양한 주파수 성분으로 구성됩니다. 일반적인 반복법(예: 야코비법)은 고주파(local, high-frequency) 오차는 빠르게 줄이지만, 저주파(global, low-frequency) 오차는 매우 느리게 줄입니다.
-   **격자 해상도와 오차**: 저해상도(coarse) 격자에서는 저주파 오차가 고주파 오차처럼 보이게 됩니다. 따라서 저해상도 격자에서는 저주파 오차를 효율적으로 제거할 수 있습니다.

### 작동 방식 (V-Cycle)
1.  **Smoothing**: 현재의 고해상도(fine) 격자에서 몇 번의 반복법을 수행하여 고주파 오차를 줄입니다.
2.  **Restriction**: 남은 잔차(residual error)를 저해상도(coarse) 격자로 전달합니다.
3.  **Recursion**: 저해상도 격자에서 문제를 풉니다. 이 과정은 가장 거친 격자에 도달할 때까지 재귀적으로 반복될 수 있습니다.
4.  **Prolongation/Interpolation**: 저해상도 격자에서 계산된 보정값(correction)을 다시 고해상도 격자로 전달(보간)하여 해를 보정합니다.
5.  **Post-Smoothing**: 보정된 해에 대해 다시 몇 번의 반복법을 수행하여 남은 고주파 오차를 제거합니다.

## ✨ 딥러닝에서의 활용

Multi-Grid의 아이디어는 딥러닝, 특히 컴퓨터 비전 분야에서 연산 효율성과 성능을 높이기 위해 차용되었습니다.

-   **다양한 스케일의 특징 학습**: 저해상도 특징 맵에서는 전체적인 문맥(저주파)을, 고해상도 특징 맵에서는 세부적인 디테일(고주파)을 학습하는 구조에 영감을 주었습니다. [[Feature Pyramid Network]] 등이 이러한 아이디어와 관련이 있습니다.
-   **효율적인 Backbone 설계**: ResNet을 기반으로 하는 Detection이나 Segmentation 모델에서, 각 스테이지의 블록마다 다른 dilation rate을 적용하는 **Multi-Grid** 전략을 사용하기도 합니다. 이는 연산량을 크게 늘리지 않으면서 다양한 크기의 receptive field를 확보하여 성능을 높이는 데 도움을 줍니다. (예: DeepLabv3+)
-   **ResNet과 HBP**: [[Hierarchical Basis Preconditioning|계층적 기저 사전조건화]]의 관점에서 ResNet을 해석할 때, Multi-Grid 방법론은 그 이론적 배경을 제공합니다.

## 🔗 관련 개념
-   [[Hierarchical Basis Preconditioning]]
-   [[ResNet]]
-   [[Feature Pyramid Network]]
-   [[Dilated Convolution]]