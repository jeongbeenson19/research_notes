---
tags: #AI #ComputerVision #SelfSupervisedLearning #Transformer #ViT
aliases: [MAE, 마스크드 오토인코더]
---

# Masked Autoencoders (MAE)

> **한 줄 요약**: 이미지의 대부분을 무작위로 가리고(masking), 보이는 일부만을 이용해 가려진 부분을 복원하도록 학습하는 방식의 자기지도학습(Self-Supervised Learning) 모델.

**Masked Autoencoders (MAE)** 는 He Kaiming 연구팀이 2021년에 발표한 논문 "Masked Autoencoders Are Scalable Vision Learners"에서 제안된 컴퓨터 비전 모델입니다. 자연어 처리(NLP) 분야에서 큰 성공을 거둔 [[BERT]]의 "Masked Language Model" 아이디어를 비전 분야에 성공적으로 적용한 사례로 평가받습니다.

---

## 1. 핵심 아이디어 (Core Idea)

MAE의 핵심 아이디어는 매우 간단하지만 강력합니다.

1.  **높은 비율의 마스킹 (High Masking Ratio)**: 입력 이미지를 여러 개의 패치(patch)로 나눈 뒤, **75%** 와 같이 매우 높은 비율의 패치를 무작위로 제거(마스킹)합니다.
2.  **보이는 부분만 인코딩 (Encoding Visible Patches)**: 마스킹되지 않고 **보이는 패치들만** 인코더(Encoder)에 입력합니다.
3.  **전체 복원 (Full Reconstruction)**: 경량화된 디코더(Decoder)가 인코딩된 정보와 마스킹된 위치 정보를 이용해 원본 이미지의 **마스킹된 패치들**을 픽셀 단위로 복원합니다.

이 과정은 마치 "이미지를 위한 BERT"처럼 동작합니다. 모델은 주변의 보이는 패치들로부터 컨텍스트를 파악하여 보이지 않는 부분을 추론하는 능력을 학습하게 되며, 이를 통해 이미지에 대한 풍부한 표현(representation)을 스스로 습득합니다.

## 2. 주요 특징 및 구조

### 가. 비대칭적(Asymmetric) Encoder-Decoder 구조

-   **인코더 (Encoder)**: [[Vision Transformer]] 구조를 사용하지만, 전체 패치의 25% 정도만 처리하므로 연산량이 매우 적습니다. 이 덕분에 매우 큰 모델도 효율적으로 사전 학습(pre-training)시킬 수 있습니다.
-   **디코더 (Decoder)**: 인코더보다 훨씬 작고 가벼운 Transformer 블록으로 구성됩니다. 디코더는 인코더가 출력한 잠재 표현(latent representation)과 마스크 토큰(mask token)을 입력받아 픽셀을 복원하는, 비교적 간단한 작업을 수행합니다.

이러한 비대칭 구조는 MAE의 **학습 효율성**을 극대화하는 핵심 요소입니다.

### 나. 높은 마스킹 비율의 중요성

75%라는 높은 마스킹 비율은 모델이 단순히 주변 픽셀을 복사하는 '쉬운 길'을 택하지 못하게 만듭니다. 대신 이미지의 전체적인 구조, 객체의 형태, 질감 등 더 높은 수준의 의미론적 정보를 학습하도록 강제하는 효과가 있습니다.

### 다. 간단한 복원 목표 (Simple Reconstruction Target)

MAE는 복잡한 데이터 증강(data augmentation)이나 대조 학습(contrastive learning) 없이, 단순히 마스킹된 패치의 원본 픽셀(RGB 값)을 예측하는 **평균 제곱 오차(MSE)** 를 손실 함수로 사용합니다. 이 단순함이 오히려 모델의 일반화 성능을 높이는 데 기여했습니다.

## 3. 의의 및 영향

-   **컴퓨터 비전 자기지도학습의 패러다임 전환**: SimCLR, MoCo와 같은 대조 학습(Contrastive Learning) 계열이 주도하던 비전 자기지도학습 분야에서, 단순한 생성(generative) 방식인 MAE가 더 뛰어난 성능과 확장성을 보여주며 새로운 방향을 제시했습니다.
-   **뛰어난 확장성(Scalability)**: 인코더의 연산량 감소 덕분에 기존 방법들보다 훨씬 더 큰 모델을 더 빠르게 학습시킬 수 있게 되었고, 이는 모델의 성능 향상으로 직결되었습니다.
-   **탁월한 전이 학습(Transfer Learning) 성능**: MAE로 사전 학습된 모델은 이미지 분류(Image Classification), 객체 탐지(Object Detection), 분할(Segmentation) 등 다양한 다운스트림 작업(downstream task)에서 아주 적은 데이터만으로도 미세 조정(fine-tuning)하여 최고 수준의 성능을 달성했습니다.

---

## 4. 관련 개념

-   [[Self-Supervised Learning]]
-   [[Vision Transformer]]
-   [[Autoencoder]]
-   [[BERT]]

## 5. 참고 자료

-   He, K., Chen, X., Xie, S., Li, Y., Dollár, P., & Girshick, R. (2021). *Masked Autoencoders Are Scalable Vision Learners*. arXiv preprint arXiv:2111.06377.
