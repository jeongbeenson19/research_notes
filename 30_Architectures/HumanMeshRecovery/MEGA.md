---
tags:
  - MILAB
  - ComputerVision
  - HumanMeshRecovery
  - GenerativeModel
  - Transformer
---

# MEGA: Masked Generative Autoencoder for Human Mesh Recovery

## 1. 요약 (Abstract)
> **MEGA (Masked Generative Autoencoder)** 는 단일 2D 이미지로부터 3D 인체 메시(mesh)를 복원하는 Human Mesh Recovery(HMR) 작업을 위한 새로운 프레임워크입니다. [[../../Backbones/Transformer|Transformer]] 기반의 마스크된 생성 오토인코더(Masked Generative Autoencoder)를 사용하여, 가려지거나 보이지 않는 신체 부위를 포함한 전체 3D 메시를 생성적으로 복원합니다. 이 방식은 2D 키포인트 같은 값비싼 레이블 의존도를 줄이고, 3D 모션 캡처 데이터셋만으로도 사전 학습(pre-training)이 가능하게 하여, 보다 강건하고 사실적인 3D 인체 모델 생성을 목표로 합니다.

---

## 2. 배경: 기존 Human Mesh Recovery의 한계

Human Mesh Recovery는 2D 이미지라는 불완전한 정보로부터 3D 형상을 추정하는 본질적으로 모호한(ill-posed) 문제입니다. 기존 연구들은 주로 다음과 같은 한계를 가집니다.

- **강한 지도 학습 의존성**: 정확한 3D 메시를 복원하기 위해, 이미지와 완벽하게 정렬된 3D 데이터 또는 2D 키포인트 주석이 필수적이었습니다. 이러한 데이터를 구축하는 것은 매우 비용이 많이 듭니다.
- **가려짐(Occlusion)에 대한 취약성**: 이미지에서 신체 일부가 가려지거나 잘렸을 경우, 해당 부위의 메시를 정확하게 복원하는 데 어려움을 겪습니다.
- **단일 결과물(Deterministic Output)**: 대부분의 모델은 하나의 이미지를 입력받아 단 하나의 3D 메시를 결과로 내놓습니다. 하지만 2D 이미지의 모호성으로 인해 여러 가지 타당한 3D 자세가 존재할 수 있음에도 이를 표현하지 못합니다.

---

## 3. 핵심 아이디어: Masked Generative Autoencoder

MEGA는 자연어 처리의 Masked Language Model(MLM)이나 비전 분야의 Masked Autoencoder(MAE)에서 영감을 얻어 HMR 문제를 **"조건부 생성(Conditional Generation)"** 문제로 재정의합니다.

- **마스크된 입력, 전체 복원**: 모델은 의도적으로 **마스킹된(가려진) 부분적인 인체 정보**를 입력받아, 보이지 않는 부분을 포함한 **완전한 전체 인체 메시**를 복원하도록 학습됩니다. 
- **전체적인(Holistic) 표현 학습**: 이 과정은 모델이 단순히 보이는 부분만 따라 그리는 것이 아니라, 인체의 구조적 제약, 각 부위 간의 관계 등 **전체적인 사전 지식(prior)** 을 학습하도록 강제합니다. 이를 통해 가려진 부분도 그럴듯하게 생성할 수 있는 능력을 갖추게 됩니다.
- **생성적 복원(Generative Recovery)**: 결정론적으로 하나의 결과만 내놓는 것이 아니라, 확률적인(stochastic) 샘플링을 통해 **하나의 이미지에 대해 다양하고 타당한 여러 개의 3D 메시**를 생성할 수 있습니다.

---

## 4. MEGA 아키텍처

MEGA는 [[../../Backbones/Transformer|Transformer]] 인코더-디코더 구조를 기반으로 합니다.

1.  **VQ-VAE Tokenizer**: 연속적인 3D 인체 메시를 이산적인(discrete) 코드북의 인덱스, 즉 **메시 토큰(mesh token)** 시퀀스로 변환하는 VQ-VAE를 사전 학습합니다. 이를 통해 HMR 문제를 텍스트 생성과 유사한 시퀀스 생성 문제로 치환합니다.

2.  **이미지 인코더**: 입력 이미지로부터 특징(feature)을 추출하여 임베딩을 생성합니다. 이는 생성 과정의 **조건(condition)** 으로 사용됩니다.

3.  **Masked Generative Autoencoder**: 
    - **인코더**: 이미지 임베딩과 **마스킹된 메시 토큰**을 입력받아, 이를 압축된 잠재 표현(latent representation)으로 인코딩합니다.
    - **디코더**: 인코더의 잠재 표현과 이미지 조건을 바탕으로, **전체 메시 토큰 시퀀스(마스킹되지 않은)**를 예측(복원)합니다.

---

## 5. 학습 방식

MEGA는 두 단계의 학습 과정을 거칩니다.

1.  **사전 학습 (Self-Supervised Pre-training)**: 대규모 3D 모션 캡처 데이터셋(예: AMASS)만을 사용하여 VQ-VAE와 Masked Autoencoder를 **자기지도학습(self-supervised)** 방식으로 학습시킵니다. 이 단계에서는 이미지 데이터나 2D 주석이 전혀 필요 없으며, 모델은 오직 3D 인체 데이터로부터 인체의 구조적 특성을 학습합니다.

2.  **지도 학습 (Supervised Fine-tuning)**: 사전 학습된 모델을 이미지-3D 쌍 데이터셋을 이용해 미세 조정합니다. 이 단계에서 모델은 이미지 특징을 조건으로 하여 마스킹된 메시 토큰을 예측하는 방법을 학습합니다.

---

## 6. 실험 및 결과

- **정량적 성능**: MEGA는 결정론적(deterministic) 모드와 확률론적(stochastic) 모드 모두에서 기존 SOTA(State-of-the-Art) 모델들의 성능을 능가했습니다. 특히 여러 개의 결과물을 생성하여 평가하는 확률론적 평가 지표에서 큰 성능 향상을 보였습니다.
- **정성적 결과**: 가려진 신체 부위에 대해서도 매우 사실적이고 자연스러운 메시를 생성했으며, 단일 이미지에 대해 해부학적으로 타당한 다양한 포즈를 성공적으로 생성해냈습니다.

---

## 7. 공헌 및 의의

- **새로운 패러다임 제시**: HMR 문제를 생성 모델링 관점에서 접근하여, 마스크된 입력을 통해 전체를 복원하는 새로운 패러다임을 제시했습니다.
- **데이터 의존성 완화**: 대규모 3D 데이터만으로 사전 학습이 가능해져, 값비싼 2D-3D 페어 데이터에 대한 의존성을 줄였습니다.
- **다중 가설 생성**: 2D 이미지의 모호성을 인정하고, 이에 대응하여 다양하고 타당한 3D 메시를 여러 개 생성할 수 있는 길을 열었습니다.

---

## 8. 관련 노트

- **기반 기술**: [[../../40_Papers/Attention Is All You Need|Attention Is All You Need]], [[../../Backbones/Transformer|Transformer]]
- **상위 분야**: [[../PoseEstimation/Pose Estimation|Pose Estimation]], [[../../../60_Library/Book_Notes/Computer Vision & Deep Learning|Computer Vision & Deep Learning]]
- **기초 네트워크**: [[ANN|ANN]], [[CNN|CNN]]
- **평가 지표**: [[../../../10_Concepts/Computer_Vision/Metrics/Evaluation Metrics|Evaluation Metrics]]

