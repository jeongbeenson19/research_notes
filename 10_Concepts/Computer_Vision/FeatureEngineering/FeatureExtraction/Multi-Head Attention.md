---
title: Multi-Head Attention
aliases:
  - Multi Head Attention
  - 멀티헤드 어텐션
tags:
  - machine-learning
  - attention
  - transformer
topics:
  - parallel heads
  - projection
---
# Multi-Head Attention
## 1. 정의
- 여러 개의 어텐션 헤드를 병렬로 계산해 서로 다른 서브공간에서 정보 결합.

## 2. 수식
- 헤드 수 $h$, 각 헤드 차원 $d_k$, 모델 차원 $d_{model}$.
- 각 헤드:
  - $\mathrm{head}_i = \mathrm{Attention}(QW_i^Q, KW_i^K, VW_i^V)$.
- 병합:
  - $\mathrm{MHA}(Q,K,V) = \mathrm{Concat}(\mathrm{head}_1,\ldots,\mathrm{head}_h)W^O$.
- 보통 $d_{model} = h \cdot d_k$로 설정.

## 3. 효과
- 서로 다른 관계(문법, 의미, 위치 등)를 동시에 포착.
- 단일 헤드보다 표현력 증가.

## 4. 비용
- 계산량은 단일 헤드 대비 유사하지만, 병렬화에 유리.

## 참고 문헌
- Vaswani, A. et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762

## 링크
- [[Attention]]
- [[Self-Attention]]
- [[Transformer]]
