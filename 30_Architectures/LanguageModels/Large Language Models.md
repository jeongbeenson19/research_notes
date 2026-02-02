---
tags:
  - NLP
  - LLM
  - architecture
aliases:
  - 거대 언어 모델
  - LLM
---

# Large Language Models (LLM)

Large Language Models(거대 언어 모델)은 수십억 개 이상의 파라미터를 가진 매우 큰 규모의 딥러닝 모델을 의미하며, 주로 자연어 처리(NLP) 분야에서 사용됩니다. 방대한 양의 텍스트 데이터로 사전 학습(pre-trained)되어, 문맥을 이해하고 생성하는 능력이 뛰어납니다.

## 주요 특징

-   **거대한 규모**: 수십억에서 수천억 개의 파라미터를 가집니다.
-   **사전 학습 및 미세 조정**: [[Transfer Learning|전이 학습]]의 패러다임을 기반으로, 대규모 코퍼스로 사전 학습된 후 특정 Task에 맞게 미세 조정(fine-tuning)하여 사용됩니다.
-   **In-context Learning / Few-shot Learning**: 별도의 학습 없이, 프롬프트에 몇 가지 예시(shot)를 제공하는 것만으로 새로운 Task를 수행하는 능력을 보입니다.

## 대표적인 모델

-   [[GPT]] (Generative Pre-trained Transformer) 계열
-   [[BERT]] (Bidirectional Encoder Representations from Transformers)
-   T5, LaMDA, LLaMA 등

## 경량화

LLM은 크기가 매우 크기 때문에 실제 서비스에 배포하기 어렵습니다. 따라서 [[Knowledge Distillation]]과 같은 [[Model Compression]] 기법을 통해 모델을 경량화하는 연구가 활발히 진행되고 있습니다.
