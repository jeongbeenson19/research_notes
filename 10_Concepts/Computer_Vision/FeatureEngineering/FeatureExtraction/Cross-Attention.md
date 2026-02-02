---
title: Cross-Attention
aliases:
  - Cross Attention
  - 교차 어텐션
tags:
  - machine-learning
  - attention
  - transformer
topics:
  - encoder-decoder
  - conditioning
---
# Cross-Attention
## 1. 정의
- 한 시퀀스의 표현을 다른 시퀀스의 정보로 **조건부 갱신**하는 어텐션.
- Q는 한 쪽(예: 디코더), K/V는 다른 쪽(예: 인코더)에서 생성됨.

## 2. 수식
- 디코더 상태 $S \in \mathbb{R}^{m \times d_{model}}$, 인코더 출력 $H \in \mathbb{R}^{n \times d_{model}}$.
- $Q = SW_Q,\; K = HW_K,\; V = HW_V$.
- $Z = \mathrm{softmax}(QK^T / \sqrt{d_k})V$.
- 두 쪽 차원이 다르면, 별도 프로젝션으로 $d_k$ 차원으로 맞춘다.

## 3. 직관
- “질문(디코더)이 자료(인코더)를 검색한다.”
- 번역에서 디코더 각 스텝이 소스 문장 전체를 참조.

## 4. 사용처
- seq2seq, 멀티모달(텍스트가 이미지/오디오를 참조) 등.

## 참고 문헌
- Vaswani, A. et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762
- Bahdanau, D., Cho, K., Bengio, Y. (2014). *Neural Machine Translation by Jointly Learning to Align and Translate*. https://arxiv.org/abs/1409.0473

## 링크
- [[Attention]]
- [[Transformer]]
- [[Self-Attention]]
