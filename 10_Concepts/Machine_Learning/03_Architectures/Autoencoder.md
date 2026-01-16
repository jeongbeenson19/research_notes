---
tags: #AI #MachineLearning #NeuralNetwork
aliases: [오토인코더]
---

# Autoencoder

> **한 줄 요약**: 입력 데이터를 저차원의 잠재 공간(latent space)으로 압축했다가 다시 원본 데이터로 복원하는 과정을 통해 데이터의 특징을 효율적으로 학습하는 비지도 학습(Unsupervised Learning) 신경망 모델.

**오토인코더(Autoencoder)** 는 입력을 출력과 최대한 동일하게 만들도록 학습되는 신경망입니다. 이 과정은 두 부분으로 구성됩니다.

1.  **인코더 (Encoder)**: 입력 데이터를 더 낮은 차원의 잠재 변수(latent variable) 또는 코드(code)로 압축(encoding)합니다.
2.  **디코더 (Decoder)**: 압축된 코드를 다시 원본 데이터의 차원으로 복원(decoding)합니다.

모델은 입력과 복원된 출력 간의 **복원 오류(reconstruction error)**(예: [[Mean Squared Error|MSE]])를 최소화하는 방향으로 학습됩니다.

---

## 1. 구조 및 특징

오토인코더의 가장 큰 특징은 병목(bottleneck) 구조입니다. 인코더를 통해 입력 데이터의 차원을 점차 줄여나가다가 가장 낮은 차원의 '코드'에 도달하고, 디코더는 이 코드를 받아 다시 차원을 늘려나갑니다. 

이 병목 구조 때문에 오토인코더는 데이터의 가장 중요하고 본질적인 특징(representation)만을 잠재 공간에 남기도록 강제됩니다. 이는 [[Principal Component Analysis|주성분 분석(PCA)]]과 유사한 차원 축소(dimensionality reduction) 효과를 낳지만, 비선형적인 관계도 학습할 수 있다는 장점이 있습니다.

## 2. 종류

다양한 목적에 맞게 변형된 오토인코더들이 존재합니다.

-   **Denoising Autoencoder**: 입력에 의도적으로 노이즈를 추가한 뒤, 원본의 노이즈 없는 데이터를 복원하도록 학습하여 더 강건한(robust) 특징을 학습합니다.
-   **Sparse Autoencoder**: 잠재 공간의 뉴런 대부분이 비활성화되도록 정규화(regularization)를 추가하여, 데이터의 특정 패턴에만 반응하는 뉴런을 만들도록 유도합니다.
-   **Variational Autoencoder (VAE)**: 잠재 공간이 특정 확률 분포(주로 정규 분포)를 따르도록 학습하는 생성 모델(Generative Model)의 일종입니다. 이를 통해 기존에 없던 새로운 데이터를 생성할 수 있습니다.
-   **[[Masked Autoencoders|Masked Autoencoder (MAE)]]**: 입력의 일부를 마스킹하고, 마스킹된 부분을 복원하도록 학습하는 방식으로, 특히 비전 분야에서 뛰어난 성능을 보입니다.

## 3. 활용 분야

-   **차원 축소 및 데이터 시각화**
-   **특징 추출 (Feature Extraction)**
-   **이상 탐지 (Anomaly Detection)**: 정상 데이터만으로 학습시킨 뒤, 복원 오류가 큰 데이터를 이상치로 판단
-   **데이터 생성 (Generative Models)**
-   **노이즈 제거 (Denoising)**

---

## 4. 관련 개념

-   [[Unsupervised Learning]]
-   [[Dimensionality Reduction]]
-   [[Generative Model]]
-   [[Masked Autoencoders]]
