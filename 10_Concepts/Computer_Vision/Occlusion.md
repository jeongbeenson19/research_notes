---
tags:
  - CV
  - computer_vision
  - object_detection
  - object_tracking
aliases:
  - 가림
  - 폐색
  - 오클루전
---

# Occlusion (가림)

**Occlusion(가림)** 은 Computer Vision 분야에서 3차원 공간의 한 객체가 다른 객체에 의해 부분적으로 또는 완전히 가려져 카메라에 보이지 않는 현상을 의미합니다. 이는 객체의 형태, 위치, 정체성을 파악하는 데 필요한 시각적 정보의 손실을 유발하기 때문에 Computer Vision의 여러 Task에서 가장 근본적이고 어려운 문제 중 하나로 꼽힙니다.

## Occlusion이 어려운 이유

Occlusion은 다음과 같은 주요 Task에서 심각한 성능 저하를 유발합니다.

-   **[[Detection Essential|객체 탐지]]**: 객체의 일부만 보일 경우, 탐지 모델이 객체를 인식하지 못하거나 다른 클래스로 잘못 분류할 수 있습니다. (예: 사람의 다리만 보고 기둥으로 오인)
-   **[[Object Tracking|객체 추적]]**: 추적하던 객체가 다른 객체 뒤에 숨었다가 다시 나타날 때, 추적기가 동일한 객체임을 인지하지 못하고 새로운 ID를 부여하는 문제(ID-switch)가 발생할 수 있습니다.
-   **[[Pose Estimation|자세 추정]]**: 신체의 일부(예: 등 뒤로 감춘 팔)가 가려지면 해당 관절을 예측할 수 없어 불완전하거나 잘못된 포즈를 추정하게 됩니다.
-   **[[Semantic Segmentation|의미 분할]]**: 가려진 객체의 경계가 불분명하여 픽셀 단위로 정확하게 분할하기 어렵습니다.
-   **3D 재구성**: 가려진 부분은 깊이 정보를 얻을 수 없어 3D 모델에 구멍(hole)이 생깁니다.

## Occlusion의 종류

-   **부분 가림 (Partial Occlusion)**: 객체의 일부가 다른 객체에 의해 가려진 경우.
-   **완전 가림 (Full Occlusion)**: 객체 전체가 일시적으로 완전히 가려진 경우. (주로 [[Object Tracking]]에서 문제됨)
-   **자기 가림 (Self-Occlusion)**: 객체 스스로 자신의 일부를 가리는 경우. (예: 사람이 팔짱을 껴서 팔 일부가 몸통에 가려지는 경우)
-   **객체 간 가림 (Inter-Object Occlusion)**: 한 객체가 다른 독립된 객체에 의해 가려지는 경우.

## Occlusion 처리 기법

Occlusion 문제를 해결하거나 완화하기 위해 다양한 접근법이 연구되고 있습니다.

### 1. 모델 기반 및 문맥 활용 기법 (Model-based & Contextual Methods)

-   **부분 기반 모델 (Part-based Models)**: 객체를 머리, 몸통, 다리와 같은 여러 부분의 조합으로 보고, 보이는 부분들을 조합하여 전체 객체를 추론합니다. [[Pose Estimation]]의 `Part Affinity Fields`가 대표적인 예입니다.
-   **형태 사전 정보 활용 (Shape Priors)**: 객체의 평균적인 형태나 템플릿 정보를 모델에 사전 지식으로 주어, 가려진 부분을 복원하거나 추론하도록 합니다.
-   **문맥 정보 활용 (Contextual Information)**: 주변 객체나 장면의 전체적인 문맥을 활용합니다. (예: '식탁' 위에는 '컵'이나 '접시'가 있을 확률이 높다는 정보 활용)

### 2. 움직임 예측 기반 기법 (Motion Prediction Methods)

주로 [[Object Tracking|객체 추적]]에서 사용되며, 객체의 움직임을 모델링하여 가려진 동안의 위치를 예측합니다.

-   **칼만 필터 ([[Kalman Filter]])** / **파티클 필터 (Particle Filter)**: 객체의 이전 속도와 방향을 기반으로 현재 위치를 예측하고, 객체가 다시 나타났을 때 예측된 위치 근처에서 탐색하여 ID를 다시 연결합니다.

### 3. 데이터 주도 기법 (Data-driven Methods)

딥러닝 모델이 Occlusion에 강건해지도록 학습 데이터나 모델 구조 자체를 개선하는 방식입니다.

-   **데이터 증강 (Data Augmentation)**: 학습 이미지에 의도적으로 가림 현상을 만듭니다. 이미지의 일부를 검은 사각형으로 가리는 'Cutout'이나 무작위로 지우는 'Random Erasing' 기법을 통해 모델이 일부 정보가 없어도 객체를 잘 인식하도록 훈련시킵니다.
-   **어텐션 메커니즘 (Attention Mechanisms)**: 모델이 이미지의 모든 부분을 동일하게 보지 않고, 가려지지 않은 유용한 부분에 더 집중(attention)하도록 학습시킵니다.
-   **생성 모델을 이용한 복원 (Generative Inpainting)**: GAN과 같은 생성 모델을 사용하여 가려진 부분을 그럴듯하게 복원한 후, 복원된 이미지를 후속 Task에 입력으로 사용합니다.
-   **강건한 특징 표현 학습 (Robust Feature Representation)**: Occlusion에 덜 민감한 특징(feature)을 학습하도록 손실 함수를 설계하거나 모델 구조를 개선합니다.

## 관련 개념

-   [[Detection Essential|Object Detection]]
-   [[Object Tracking]]
-   [[Pose Estimation]]
-   [[Semantic Segmentation]]
-   [[Data Augmentation]]
