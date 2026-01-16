---
title: Self-Attention
aliases:
  - Self Attention
  - 자기 어텐션
tags:
  - machine-learning
  - attention
  - transformer
topics:
  - scaled-dot-product
  - masking
---
# Self-Attention
## 1. 정의
- 동일한 시퀀스(또는 이미지 패치) 내부에서 각 위치가 다른 위치 정보를 참조해 표현을 갱신하는 어텐션.
- Q, K, V가 모두 같은 입력 $X$에서 생성됨.

## 2. 수식(Scaled Dot-Product)
- 입력 $X \in \mathbb{R}^{n \times d_{model}}$.
- $Q=XW_Q,\; K=XW_K,\; V=XW_V$.
- 어텐션 가중치:
  - $A = \mathrm{softmax}(QK^T / \sqrt{d_k})$.
- 출력:
  - $Z = AV$.

## 3. 마스킹
- **Causal mask**: 미래 토큰을 보지 않도록 $QK^T$의 상삼각을 $-\infty$로 차단.
- **Padding mask**: 실제 토큰만 가중치 계산에 포함.

## 4. 복잡도와 특징
- 시간/메모리 복잡도: $O(n^2 d)$.
- 장점: 장거리 의존성 표현이 쉬움.
- 단점: 긴 시퀀스에서 비용 증가.

## 5. 위치 정보
- Self-attention은 위치 불변이므로 **positional encoding/embedding**이 필요.

## 참고 문헌
- Vaswani, A. et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762

## 링크
- [[Attention]]
- [[Transformer]]
- [[Multi-Head Attention]]
- [[Vision Transformer]]
