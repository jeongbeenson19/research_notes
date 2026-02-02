---
tags:
  - paper
  - knowledge_distillation
  - hinton_2015
aliases:
  - "Hinton's Distillation Paper"
---

# Distilling the Knowledge in a Neural Network

-   **Authors**: Geoffrey Hinton, Oriol Vinyals, Jeff Dean
-   **Year**: 2015
-   **Link**: [https://arxiv.org/abs/1503.02531](https://arxiv.org/abs/1503.02531)

## 요약

이 논문은 현대적인 [[Knowledge Distillation]] 개념을 정립한 핵심적인 연구입니다. 복잡하고 큰 모델(Teacher)의 지식을 작고 빠른 모델(Student)에게 효율적으로 전달하는 방법을 제안했습니다.

주요 아이디어는 Teacher 모델의 최종 출력 확률(soft targets)을 Student 모델의 학습 목표로 사용하는 것입니다. 특히 **Temperature Scaling**을 Softmax 함수에 적용하여, 정답 레이블 외에 다른 클래스들과의 관계를 나타내는 "Dark Knowledge"를 효과적으로 학습 신호로 활용하는 방법을 제시했습니다.

이 연구는 [[Model Compression]] 분야에 큰 영향을 주었으며, 이후 다양한 Distillation 기법 연구의 기반이 되었습니다.
