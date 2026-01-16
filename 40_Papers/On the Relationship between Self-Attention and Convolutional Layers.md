---
title: On the Relationship between Self-Attention and Convolutional Layers
aliases:
  - Self-Attention and Convolutional Layers
  - Cordonnier 2019
tags:
  - paper
  - attention
  - convolution
  - vision
year: 2019
venue: ICLR
arxiv: https://arxiv.org/abs/1911.03584
---
# On the Relationship between Self-Attention and Convolutional Layers (Cordonnier et al., 2019)
## 한줄 요약
- **상대적 위치 인코딩을 갖는 멀티헤드 self-attention은 충분한 헤드 수가 있으면 일반적인 합성곱을 정확히 표현할 수 있고, 실제로 초기 레이어에서 합성곱과 유사한 지역 패턴을 학습한다.**

## 문제의식
- 비전에서 attention이 convolution을 대체할 수 있는지, 그리고 실제로 **어떤 방식으로 동작하는지**를 이론/실험으로 규명.

## 핵심 결과(이론)
### 1) MHSA가 Convolution을 표현할 수 있음
- **정리(요지)**: 상대적 위치 인코딩($D_p \ge 3$)을 가진 MHSA는 **$K \times K$ 합성곱**을 표현 가능.
  - 필요한 조건: **헤드 수 $N_h = K^2$**, 출력 채널 수는 **$\min(D_h, D_{out})$**.
- 직관: 각 헤드가 **특정 상대 위치(shift)** 만을 선택하도록 구성하면, 합성곱의 각 커널 위치와 1:1 대응.

### 2) 구성적 증명(핵심 아이디어)
- 상대적 위치 인코딩을 다음과 같이 잡으면, **특정 이동량 $\Delta$만 선택하는 hard attention**을 만들 수 있음:
  - $r_\delta = (\|\delta\|^2, \delta_1, \delta_2)$
  - $v = -\\alpha(1, -2\Delta_1, -2\Delta_2)$
  - $A_{q,k} = v^T r_{k-q} = -\alpha\|\delta-\Delta\|^2 + c$
- $\alpha \to \infty$일 때, softmax가 **한 위치만 1로 수렴**.

### 3) 실용적 제약
- 일반적인 Transformer 설정처럼 $D_h = D_{out}/N_h$로 두면 **모든 채널을 완전히 표현하기 어렵다**는 점을 지적.
- 정확한 재파라미터화를 위해서는 **헤드 차원을 충분히 크게** 두는 것이 유리.

## 핵심 결과(실험)
- **Attention-only 모델(6층)로 CIFAR-10 실험**:
  - quadratic relative positional encoding, learned relative encoding, content-based attention 등을 비교.
- 관찰:
  - **초기 레이어는 로컬 그리드 패턴**을 학습해 합성곱 커널처럼 동작.
  - **깊은 레이어는 더 넓은 범위**를 보거나 content 기반 패턴을 함께 사용.
- 성능(테이블 요약):
  - ResNet18: 0.938
  - SA quadratic: 0.938
  - SA learned: 0.918
  - SA learned + content: 0.871

## 해석
- Self-attention은 **합성곱을 포함하는 더 일반적 연산**으로 볼 수 있음.
- 비전에서 **초기 레이어는 지역성 inductive bias**가 강하게 나타나며, 깊은 레이어로 갈수록 **전역적/내용 기반**으로 확장.

## 실무적 시사점
- 비전용 attention 설계 시 **상대적 위치 인코딩**과 **초기 레이어의 지역성**이 중요.
- CNN + Attention 혼합 구조가 성능적으로 유리할 수 있음.

## 링크
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Transformer]]
- [[CNN]]
