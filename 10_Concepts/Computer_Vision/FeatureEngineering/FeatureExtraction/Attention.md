---
title: 어텐션(Attention)
aliases:
  - Attention
  - 어텐션
tags:
  - machine-learning
  - attention
  - transformer
topics:
  - self-attention
  - cross-attention
  - bahdanau
---

# 어텐션(Attention)

## 1. 정의
- **목적**: 시퀀스/공간 입력에서 현재 위치에 필요한 정보를 **가중치로 선택(소프트 선택)** 하여 문맥을 통합.
- **결과**: 각 위치는 주변(또는 다른 시퀀스) 정보를 섞어 **업데이트된 단일 표현 벡터**를 얻음.

## 2. Bahdanau(2014) vs Transformer(2017)
### 2.1 구조적 차이
- **Bahdanau**: RNN encoder–decoder 유지, 디코더 시점 t마다 소스(인코더 히든 상태)에 **cross-attention** 수행 → $c_t$ 생성.
- **Transformer**: RNN 제거, **self-attention**을 기본 블록으로 스택; 디코더에는 **cross-attention**도 포함.

### 2.2 스코어링(유사도 계산)
- **Bahdanau**: additive attention, 작은 MLP(FFN)로 energy 계산.
- **Transformer**: scaled dot-product attention, $QK^T$ 내적 후 $\sqrt{d_k}$로 나눠 스케일링.

### 2.3 멀티헤드
- **Bahdanau**: 보통 단일 어텐션.
- **Transformer**: **Multi-Head Attention**으로 서브공간 병렬 어텐션 → concat → 선형변환.

## 3. Transformer가 표준이 된 이유
- **병렬화**: RNN의 순차 처리 병목 제거 → 대규모 학습 유리.
- **성능/학습 효율**: 번역 등에서 강한 성능과 학습 효율 제시.
- **범용성**: NLP뿐 아니라 비전(패치 기반), 멀티모달로 확장 용이.
- **현황**: 표준 선택지이지만, 효율/장문 처리 요구로 SSM 등 대안이 경쟁·보완.

## 4. Q/K/V는 무엇을 나누는가
- **입력 자체**를 나누는 것이 아니라, 각 위치 표현 벡터 x_i를 **서로 다른 선형변환으로 투영**.
- 입력 행렬 $X \in \mathbb{R}^{n \times d_{model}}$:
  - $Q = XW_Q$
  - $K = XW_K$
  - $V = XW_V$
- 각 위치 $i$에서 $x_i → (q_i, k_i, v_i)$는 **분해가 아니라 학습된 3개의 프로젝션**.

## 5. 어텐션 계산(한 헤드, self-attention)
### 5.1 가중치
- $s_{ij} = (q_i · k_j) / \sqrt{d_k}$
- $\alpha_{ij} = softmax_j(s_{ij})$

### 5.2 출력 벡터
- $z_i = \sum_{j=1}^{n} \alpha_{ij} v_j$

### 5.3 핵심 결론
- “$Q_i$와 유사한 $K_j$를 찾고 $V$를 가져오는가?” → **맞다**.
- 하지만 기본은 **단일 $V$ 선택이 아니라 가중합**:
  - 여러 $V_j$를 $\alpha_{ij}$로 **혼합**해 **출력 단일 벡터** z_i를 생성.
  - $\alpha_{ij}$가 한 위치에 몰리면 “사실상 하나 선택”처럼 보일 수 있음.

## 6. 직관: 검색 시스템 비유
- **Q(Query)**: “지금 필요한 정보 조건”.
- **K(Key)**: “각 위치의 검색용 태그(매칭 표현)”.
- **V(Value)**: “실제로 가져올 내용(본문 표현)”.

동작:
1) 현재 위치가 Q를 생성
2) 모든 위치의 K와 비교해 관련도 계산
3) 관련도 가중치로 V들을 섞어 현재 위치의 새 표현 생성

**K와 V를 분리하는 이유**
- 매칭에 유리한 표현(K)과 전달할 내용(V)을 동일하게 둘 필요가 없기 때문(학습 자유도 증가).

## 7. 문장 예시: “나는 밥을 먹었다”
토큰: [나는, 밥을, 먹었다]
- “먹었다” 위치 $i$에서:
  - $q_i$: 현재 필요한 것(예: 목적어/상황)을 찾는 질의
  - $k_j$: 각 토큰의 구분 표식(주어/목적어/동사 등)
  - $v_j$: 각 토큰이 제공하는 내용 정보
- 결과: “먹었다”의 출력 $z_i$는 “밥을” 등 정보를 가중합해 **문맥이 반영된 동사 표현**으로 업데이트.

## 8. 이미지 예시: ViT 패치(16×16)
- 이미지를 패치로 나누고 각 패치를 임베딩 $x_p$로 변환.
- 각 패치도 $x_p → (q_p, k_p, v_p)$.
- 예: “공” 패치가 “발/선수/골대” 패치의 $K$와 잘 매칭되면 해당 $V$를 많이 가져와,
  - 공 패치 표현이 **주변 문맥을 포함한 표현**으로 업데이트됨.

## 9. Self-attention vs Cross-attention
- **Self-attention**: Q, K, V가 같은 시퀀스/이미지 표현 X에서 생성.
- **Cross-attention**: Q는 한 쪽(예: 디코더), K/V는 다른 쪽(예: 인코더)에서 생성.
  - “질문은 디코더가 만들고, 자료는 인코더에서 가져온다.”

## 10. 임베딩 벡터가 정보를 갖는 이유
- 초기 임베딩/프로젝션은 의미가 거의 없음.
- 학습은 목적함수(다음 토큰 예측, 분류, 자기지도 등)를 줄이도록 파라미터를 업데이트.
- 그 과정에서 예측에 유리한 규칙(문법 역할, 의미 유사성, 시각 패턴 등)이
  - 선형변환/내적/가중합으로 뽑히기 쉬운 형태로
  - 벡터 공간에 “인코딩”됨.

## 11. 한 문장 요약
- **어텐션은 “Q로 K를 검색해, 관련도 가중치로 여러 V를 섞어 단일 출력 벡터를 만드는 연산”이고, Transformer는 이를 self-attention 중심의 스택 구조로 확장해 병렬 학습과 범용성을 크게 올린 표준 아키텍처다.**
## 참고 문헌
- Vaswani, A. et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762
- Bahdanau, D., Cho, K., Bengio, Y. (2014). *Neural Machine Translation by Jointly Learning to Align and Translate*. https://arxiv.org/abs/1409.0473

## 링크
- [[Transformer]]
- [[Vision Transformer]]
- [[Self-Attention]]
- [[Cross-Attention]]
- [[Bahdanau Attention]]
- [[Multi-Head Attention]]
