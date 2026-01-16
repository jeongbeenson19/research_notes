---
tags:
  - ML
  - architecture
aliases:
  - 교사-학생 모델
  - Teacher-Student Model
---

# Teacher-Student Architecture

Teacher-Student Architecture는 크고 복잡한 **Teacher 모델**이 작고 간단한 **Student 모델**의 학습 과정을 지도(guide)하는 프레임워크를 의미합니다.

Teacher 모델은 이미 특정 Task에 대해 높은 성능으로 학습된 상태이며, Student 모델은 Teacher 모델의 예측 결과나 내부 표현을 모방하도록 학습됩니다.

이 구조의 가장 대표적인 예시가 바로 [[Knowledge Distillation]]입니다. Knowledge Distillation에서는 Teacher 모델의 부드러운 출력(soft target)을 학습 신호로 사용하여 Student 모델을 훈련시킵니다.
