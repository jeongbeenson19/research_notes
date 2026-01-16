---
tags:
  - MILAB
  - ComputerVision
  - PoseEstimation
  - TrainingTechnique
---

# Online Hard Keypoint Mining (OHKM)

## 1. 개요 (Overview)

> **Online Hard Keypoint Mining (OHKM)** 은 인체 자세 추정(Human Pose Estimation) 모델을 학습시킬 때, **학습하기 어려운 '까다로운' 키포인트(Hard Keypoint)에 집중**하여 모델의 성능과 강건함(robustness)을 향상시키는 훈련 기법입니다.

- **핵심**: 전체 키포인트의 손실(loss)을 평균 내어 사용하는 대신, 각 미니배치(mini-batch)마다 **손실 값이 가장 큰 K개의 키포인트만 선별**하여 역전파(backpropagation)를 수행합니다.
- **용어**: "Online"은 이러한 선별 과정이 오프라인에서 미리 정해지는 것이 아니라, 학습 중인 모델의 예측 결과에 따라 **실시간으로(online) 동적으로** 이루어진다는 의미입니다.

---

## 2. 배경: Keypoint 학습의 불균형 문제

인체 자세 추정 모델은 보통 이미지 내 모든 키포인트(e.g., 17개)의 위치를 예측하도록 학습됩니다. 하지만 모든 키포인트가 동일한 난이도를 갖지는 않습니다.

- **쉬운 키포인트 (Easy Keypoints)**: 가려지지 않고 명확하게 보이는 얼굴의 눈, 코, 귀 등. 대부분의 경우 모델이 쉽게 예측하며 손실 값이 매우 낮습니다.
- **어려운 키포인트 (Hard Keypoints)**: 다른 사물이나 신체 부위에 의해 **가려지거나(occluded)**, 이미지 경계에 걸쳐 있거나, 복잡한 자세 때문에 형태가 불분명한 관절 등. 모델이 예측하기 어려워하며 손실 값이 높게 나타납니다.

**문제점**: 만약 모든 키포인트의 손실을 단순히 평균 내어 학습하면, **수가 많은 '쉬운' 키포인트들의 낮은 손실 값이 전체 손실을 지배**하게 됩니다. 결과적으로 모델은 '어려운' 키포인트에 대한 학습을 소홀히 하게 되어, 가려짐 등 어려운 상황에 매우 취약해집니다.

---

## 3. 핵심 아이디어: 어려운 샘플에 집중하기

OHKM은 이러한 불균형 문제를 해결하기 위해 **Online Hard Example Mining (OHEM)** 이라는 더 넓은 개념을 키포인트 예측에 적용한 것입니다.

> 모델이 이미 잘 맞추고 있는 수많은 '쉬운' 샘플에 대한 학습은 줄이고, 모델이 어려워하는 소수의 '어려운' 샘플(hard examples)에 집중하여 학습 효율과 성능을 극대화하자.

OHKM은 이 아이디어를 따라, 각 이미지마다 모델이 가장 예측하기 어려워하는, 즉 **손실 값이 가장 큰 키포인트들만 'Hard Keypoint'로 간주**하고 이들의 손실만으로 그래디언트(gradient)를 계산하여 모델을 업데이트합니다.

---

## 4. OHKM 동작 방식

1.  **Forward Pass**: 입력 이미지에 대해 모델을 통과시켜 모든 키포인트(e.g., 17개)에 대한 예측 히트맵(heatmap)을 생성합니다.
2.  **개별 손실 계산**: 각 키포인트의 예측 히트맵과 정답(Ground Truth) 히트맵 사이의 손실(e.g., MSE Loss)을 **개별적으로 모두 계산**합니다.
3.  **Hard Keypoint 선별**: 계산된 17개의 손실 값들을 내림차순으로 정렬하고, **손실 값이 가장 큰 상위 K개의 키포인트**를 선택합니다. (예: K=8)
4.  **최종 손실 계산 및 Backward Pass**: 선택된 K개의 'Hard Keypoint'들의 손실 값만 평균 내어 최종 손실을 계산하고, 이 손실에 대해서만 역전파를 수행하여 모델의 가중치를 업데이트합니다.

---

## 5. OHKM의 장점

- **정확도 향상**: 모델이 어려운 케이스에 집중하게 되므로, 전반적인 키포인트 예측 정확도가 향상됩니다.
- **강건성(Robustness) 증대**: 가려짐(occlusion), 복잡한 자세 등 어려운 상황에 대한 대응 능력이 크게 개선됩니다.
- **효율적인 학습**: 학습에 유의미한 정보(informative gradient)를 제공하는 샘플에 집중함으로써 더 안정적이고 효율적인 수렴을 유도합니다.

---

## 6. 주요 적용 사례: Cascaded Pyramid Network (CPN)

OHKM이 성공적으로 적용된 대표적인 사례는 [[30_Architectures/PoseEstimation/Cascaded Pyramid Network|Cascaded Pyramid Network (CPN)]] 입니다. CPN은 두 단계로 구성됩니다.

1.  **GlobalNet**: 전체적인 피쳐 피라미드 네트워크로, 모든 키포인트의 위치를 대략적으로 예측합니다. 이 단계에서는 상대적으로 '쉬운' 키포인트들을 잘 찾아냅니다.
2.  **RefineNet**: GlobalNet의 모든 레벨 피쳐를 통합하여, **OHKM을 통해 '어려운' 키포인트들을 명시적으로 정제**합니다. 즉, GlobalNet이 예측하기 어려워했던 키포인트들을 집중적으로 학습하여 최종 예측의 완성도를 높입니다.

이 구조 덕분에 CPN은 OHKM을 효과적으로 활용하여 당시 SOTA(State-of-the-Art) 성능을 달성했습니다.

---

## 7. 관련 노트

- **상위 개념**: [[30_Architectures/PoseEstimation/Pose Estimation|Pose Estimation]]
- **적용된 모델**: [[30_Architectures/PoseEstimation/Cascaded Pyramid Network|Cascaded Pyramid Network (CPN)]], [[30_Architectures/PoseEstimation/RefineNet|RefineNet]]
