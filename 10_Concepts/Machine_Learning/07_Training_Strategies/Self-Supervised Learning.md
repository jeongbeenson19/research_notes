---
tags: #AI #MachineLearning
aliases: [자기지도학습, SSL]
---

# Self-Supervised Learning (SSL)

> **한 줄 요약**: 데이터 자체에서 라벨(label)을 자동으로 생성하여, 라벨이 없는 대규모 데이터셋을 활용해 모델을 사전 학습(pre-training)하는 기계 학습 패러다임.

**자기지도학습(Self-Supervised Learning, SSL)**은 명시적인 라벨링 작업 없이 데이터 내부에 존재하는 구조적 정보나 관계를 활용하여 스스로 학습 문제를 만들고 해결하는 방식입니다. 이는 대규모의 라벨링되지 않은(unlabeled) 데이터를 효과적으로 활용하여 표현(representation)을 학습하는 것을 목표로 합니다.

---

## 1. 핵심 아이디어

SSL의 핵심은 **Pretext Task(구실 과제)** 라는 가상의 문제를 설계하는 것입니다. 모델은 이 Pretext Task를 풀도록 학습되며, 이 과정에서 데이터의 의미론적 특징을 담은 풍부한 표현을 스스로 학습하게 됩니다. 이렇게 사전 학습된 모델은 이후에 소량의 라벨링된 데이터만으로도 특정 **Downstream Task(전이 과제)** (예: 분류, 탐지)에 미세 조정(fine-tuning)되어 높은 성능을 보일 수 있습니다.

### 주요 Pretext Task 예시

-   **이미지 분야**: 
    -   **Context Prediction**: 이미지의 일부 패치를 보고 주변 패치를 예측 (예: [[Masked Autoencoders (MAE)]])
    -   **Colorization**: 흑백 이미지를 입력받아 원본 컬러 이미지를 복원
    -   **Rotation Prediction**: 이미지를 0, 90, 180, 270도 회전시킨 뒤, 얼마나 회전되었는지 맞추기
    -   **Contrastive Learning**: 같은 이미지에 다른 데이터 증강(augmentation)을 적용한 두 버전을 가깝게, 다른 이미지의 버전은 멀게 만드는 방식 (예: SimCLR, MoCo)

-   **자연어 처리 분야**:
    -   **Masked Language Model (MLM)**: 문장의 일부 단어를 마스킹하고 주변 단어를 이용해 예측 (예: [[BERT]])
    -   **Next Sentence Prediction (NSP)**: 두 문장이 이어지는 문장인지 예측

## 2. 의의 및 중요성

-   **라벨링 비용 절감**: 수동으로 데이터를 라벨링하는 데 드는 막대한 시간과 비용을 절감할 수 있습니다.
-   **데이터 효율성 증대**: 인터넷에 존재하는 방대한 양의 라벨 없는 데이터를 활용하여 모델의 성능을 극대화할 수 있습니다.
-   **일반화 성능 향상**: Pretext Task를 통해 데이터의 본질적인 구조를 학습하므로, 특정 작업에 과적합(overfitting)될 위험이 적고 더 일반화된 표현을 얻을 수 있습니다.

SSL은 현대 [[Large Language Models|거대 언어 모델(LLM)]]과 비전 모델들의 성공을 이끈 핵심 기술 중 하나로 평가받고 있습니다.

---

## 3. 관련 개념

-   [[Transfer Learning]]
-   [[Unsupervised Learning]]
-   [[Masked Autoencoders (MAE)]]
-   [[BERT]]
