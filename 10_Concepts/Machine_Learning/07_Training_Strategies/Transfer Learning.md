---
tags:
  - ML
  - knowledge_transfer
aliases:
  - 전이 학습
---

# Transfer Learning (전이 학습)

Transfer Learning은 특정 문제(Task)를 해결하기 위해 학습된 모델을 다른 관련 있는 문제에 재사용하는 머신러닝 기법입니다. 대규모 데이터셋으로 사전 학습된(pre-trained) 모델의 가중치(weights)를 가져와, 새로운 Task에 맞게 미세 조정(fine-tuning)하는 방식이 일반적입니다.

## 주요 특징

-   적은 데이터로도 높은 성능을 얻을 수 있습니다.
-   학습 시간을 단축시킬 수 있습니다.
-   주로 이미지 분류, 자연어 처리 등에서 사전 학습된 백본 네트워크를 활용하는 형태로 많이 사용됩니다.
-   [[Large Language Models|거대 언어 모델]]의 기반이 되는 핵심 패러다임입니다.

## [[Knowledge Distillation]]과의 차이점

-   **Transfer Learning**: 모델의 **가중치**를 직접 재사용하여 새로운 Task에 맞게 학습을 이어갑니다. 모델 구조는 그대로 유지되거나 일부만 수정됩니다.
-   **Knowledge Distillation**: 모델의 **지식(출력 분포)** 을 전달하는 데 초점을 맞춥니다. 보통 더 작고 다른 구조의 Student 모델을 학습시키는 데 사용됩니다.
