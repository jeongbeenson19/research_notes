---
tags:
  - ML
  - model_compression
  - knowledge_transfer
aliases:
  - Distillation Learning
  - 지식 증류
  - 모델 증류
  - 증류 학습
---

# Knowledge Distillation (지식 증류)

**Knowledge Distillation(지식 증류)** 은 크고 복잡하며 성능이 좋은 모델(Teacher Model)의 지식을 작고 효율적인 모델(Student Model)에게 전달하는 [[Model Compression|모델 압축]] 기술 중 하나입니다. 이 기법의 핵심 목표는 Teacher 모델의 성능을 최대한 유지하면서, 추론 속도가 빠르고 적은 리소스를 사용하는 Student 모델을 만드는 것입니다.

이 개념은 Geoffrey Hinton, Oriol Vinyals, Jeff Dean의 2015년 논문 "[Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)"를 통해 널리 알려졌습니다.

## 핵심 아이디어: Dark Knowledge

일반적인 모델 학습은 정답 레이블(Hard Target)만을 사용하여 예측이 정답과 같아지도록 학습합니다. 예를 들어, 고양이 사진을 분류할 때 모델이 "고양이"라고 정확히 예측하는 것에만 집중합니다.

하지만 Teacher 모델의 출력(Logits 또는 Softmax 확률 분포)에는 정답 레이블 이상의 정보가 담겨 있습니다. 예를 들어, Teacher 모델이 고양이 사진에 대해 다음과 같은 예측을 내놓았다고 가정해 봅시다.

- `고양이: 0.90`
- `개: 0.08`
- `자동차: 0.01`
- `비행기: 0.01`

이 확률 분포는 "이 이미지가 고양이일 확률이 매우 높지만, 개와도 약간의 유사성이 있다"는 **'Dark Knowledge'** 를 포함합니다. 즉, 정답 클래스 외의 다른 클래스들과의 관계, 유사도 등 풍부한 정보를 담고 있습니다. Knowledge Distillation은 이 Dark Knowledge를 Student 모델에게 학습시켜, Teacher 모델의 "사고 과정"을 모방하도록 유도합니다.

## 작동 원리

Knowledge Distillation은 일반적으로 다음 세 가지 주요 구성요소로 이루어집니다.

1.  **Teacher Model**: 미리 학습된 크고 성능이 좋은 모델.
2.  **Student Model**: Teacher로부터 지식을 전수받을 작고 가벼운 모델.
3.  **Knowledge Transfer**: Teacher의 지식을 Student에게 전달하는 과정.

학습 과정은 두 가지 손실 함수(Loss Function)의 조합으로 이루어집니다.

### 1. Temperature Scaling을 이용한 Soft Target 생성

Teacher 모델의 Logits(Softmax에 들어가기 전의 값)를 **Temperature(T)** 라는 하이퍼파라미터로 나누어 확률 분포를 부드럽게 만듭니다.


$$Softmax(z_i, T) = exp(z_i / T) / Σ_j exp(z_j / T)$$

-   **T = 1**: 일반적인 Softmax 함수입니다.
-   **T > 1**: 확률 분포가 부드러워져(soften), 작은 확률 값들이 더 커집니다. 이를 통해 Dark Knowledge가 더 강조되어 Student 모델에 더 풍부한 정보를 제공할 수 있습니다.

Teacher와 Student 모델 모두 동일한 T 값을 사용하여 Soft Target과 Soft Prediction을 생성합니다.

### 2. Distillation Loss (증류 손실)

Student 모델의 Soft Prediction이 Teacher 모델의 Soft Target과 유사해지도록 학습하는 손실 함수입니다. 주로 [[Kullback-Leibler Divergence|KL Divergence]]나 Cross-Entropy를 사용합니다.

`L_distill = KL(Soft_Target_Teacher || Soft_Prediction_Student)`

이 손실 함수는 Student가 Teacher의 출력 분포를 모방하도록 만듭니다.

### 3. Student Loss (학생 손실)

Student 모델의 일반적인 예측(T=1일 때)이 실제 정답(Hard Target)과 일치하도록 학습하는 표준적인 Cross-Entropy 손실 함수입니다.

`L_student = CrossEntropy(Hard_Target, Prediction_Student)`

### 4. 최종 손실 함수

최종적으로 두 손실 함수를 가중치 합(weighted sum)하여 전체 손실 함수를 구성하고, 이를 최소화하는 방향으로 Student 모델을 학습시킵니다.

`L_total = α * L_student + (1 - α) * L_distill`

-   `α`는 두 손실의 중요도를 조절하는 하이퍼파라미터입니다.

## 장점

-   **모델 압축 및 추론 속도 향상**: 작은 모델로도 높은 성능을 유지할 수 있어, 모바일이나 엣지 디바이스 배포에 유리합니다.
-   **성능 향상**: 같은 크기의 모델을 처음부터 학습시키는 것보다 Distillation을 통해 학습된 Student 모델이 더 높은 성능을 보이는 경우가 많습니다.
-   **지식 이전**: 대규모 데이터셋으로 학습된 Teacher 모델의 지식을 더 작은 특수 목적의 데이터셋으로 학습하는 Student 모델에게 효과적으로 전달할 수 있습니다.

## 주요 응용 분야

-   **거대 언어 모델([[Large Language Models|LLM]]) 경량화**: [[BERT]], [[GPT]]와 같은 거대 모델을 경량화하여 실제 서비스에 적용하는 데 널리 사용됩니다.
-   **컴퓨터 비전**: [[Detection Essential|Object Detection]], [[Semantic Segmentation]] 등 다양한 비전 태스크에서 모델을 경량화하고 성능을 높이는 데 사용됩니다.
-   **엣지 컴퓨팅**: 리소스가 제한된 엣지 디바이스에서 딥러닝 모델을 구동하기 위한 핵심 기술입니다.

## 관련 개념

-   [[Model Compression]]
-   [[Transfer Learning]]
-   [[Teacher-Student Architecture]]
-   [[Softmax]]
-   [[Kullback-Leibler Divergence]]
