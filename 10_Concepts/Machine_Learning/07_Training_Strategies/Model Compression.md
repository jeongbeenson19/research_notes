---
tags:
  - ML
  - model_optimization
aliases:
  - 모델 압축
---

# Model Compression (모델 압축)

Model Compression은 딥러닝 모델의 크기를 줄이고, 연산량을 최적화하여 더 빠르고 효율적으로 만드는 기술들의 집합입니다. 이를 통해 리소스가 제한된 환경(예: 모바일, 엣지 디바이스)에서도 모델을 효과적으로 배포할 수 있으며, [[Large Language Models|거대 언어 모델]]처럼 규모가 매우 큰 모델을 실제 서비스에 적용 가능하게 만드는 핵심적인 역할을 합니다.

## 주요 기법

- [[Knowledge Distillation]]: 크고 복잡한 Teacher 모델의 지식을 작고 간단한 Student 모델로 전달하는 기법.
- **Pruning (가지치기)**: 모델의 파라미터나 뉴런 중 중요도가 낮은 부분을 제거하여 모델을 경량화하는 기법.
- **Quantization (양자화)**: 모델의 가중치(weights)를 32비트 부동소수점(floating-point)에서 8비트 정수(integer)와 같이 더 낮은 정밀도(precision)로 표현하여 모델 크기를 줄이고 연산 속도를 높이는 기법.
- **Matrix Factorization**: 거대한 가중치 행렬을 더 작은 행렬들의 곱으로 분해하여 파라미터 수를 줄이는 기법.
