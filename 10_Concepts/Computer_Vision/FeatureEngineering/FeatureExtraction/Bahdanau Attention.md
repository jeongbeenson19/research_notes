---
title: Bahdanau Attention
aliases:
  - Additive Attention
  - Bahdanau 어텐션
tags:
  - machine-learning
  - attention
topics:
  - encoder-decoder
  - rnn
---
# Bahdanau Attention (Additive)
## 1. 개요
- 2014 NMT에서 제안된 **additive attention**.
- 디코더 상태와 인코더 히든 상태를 MLP로 결합해 alignment 점수를 계산.

## 2. 수식
- 디코더 상태 $s_{t-1}$, 인코더 히든 $h_i$.
- 에너지:
  - $e_{t,i} = v_a^T \tanh(W_s s_{t-1} + W_h h_i)$.
- 정규화:
  - $\alpha_{t,i} = \mathrm{softmax}_i(e_{t,i})$.
- 컨텍스트:
  - $c_t = \sum_i \alpha_{t,i} h_i$.

## 3. 특징
- 내적 대신 비선형 결합을 사용해 표현력이 높음.
- RNN 기반 encoder–decoder에서 널리 사용됨.

## 4. Dot-Product와 비교
- **Additive**: 작은 MLP로 점수 계산.
- **Dot-Product**: $q_i \cdot k_j$ 내적으로 빠르고 병렬화에 유리.

## 참고 문헌
- Bahdanau, D., Cho, K., Bengio, Y. (2014). *Neural Machine Translation by Jointly Learning to Align and Translate*. https://arxiv.org/abs/1409.0473

## 링크
- [[Attention]]
- [[Cross-Attention]]
