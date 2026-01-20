---
tags:
  - ML
  - CV
  - data_processing
aliases:
  - 데이터 증강
  - 데이터 증대
---

# Data Augmentation (데이터 증강)

**Data Augmentation**은 머신러닝 모델의 성능과 일반화(generalization) 능력을 향상시키기 위해, 기존에 보유한 학습 데이터셋을 인위적으로 변형하고 확장하는 기술입니다. 원본 데이터에 다양한 변환(transformation)을 적용하여 양적으로나 질적으로 더 풍부한 데이터셋을 만들어냅니다.

## 주요 목적

-   **Overfitting 방지**: 모델이 학습 데이터에만 과도하게 최적화되는 것을 막아줍니다.
-   **모델 강건성(Robustness) 향상**: 조명, 각도, 크기, [[Occlusion|가림]] 등 실제 환경에서 발생할 수 있는 다양한 변화에 모델이 강건하게 반응하도록 돕습니다.
-   **데이터 불균형 해소**: 소수 클래스(minority class)의 데이터를 증강하여 데이터 불균형 문제를 완화할 수 있습니다.

## Computer Vision에서의 주요 기법

이미지 데이터에 주로 사용되는 증강 기법은 다음과 같습니다.

-   **기하학적 변환 (Geometric Transformations)**
    -   Flipping (상하/좌우 반전)
    -   Rotation (회전)
    -   Scaling (크기 조절)
    -   Cropping (잘라내기)
    -   Shearing (전단 변환)
-   **색상 공간 변환 (Color Space Transformations)**
    -   Brightness (밝기 조절)
    -   Contrast (대비 조절)
    -   Saturation (채도 조절)
    -   Hue (색상 조절)
-   **기타 기법**
    -   **Cutout / Random Erasing**: 이미지의 일부를 무작위로 지워 [[Occlusion|가림]] 현상을 시뮬레이션합니다.
    -   **Mixup**: 두 이미지를 일정 비율로 섞어 새로운 데이터를 만듭니다.
    -   **CutMix**: 한 이미지의 일부를 잘라 다른 이미지에 붙여넣습니다.

## 관련 개념
- [[Overfitting]]
- [[Generalization]]
- [[Occlusion]]
