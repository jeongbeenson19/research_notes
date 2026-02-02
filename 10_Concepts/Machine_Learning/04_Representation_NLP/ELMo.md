---
tags:
  - NLP
  - embedding
  - contextual_embedding
aliases:
  - ELMo
---

# ELMo (Embeddings from Language Models)

**ELMo(Embeddings from Language Models)** 는 2018년 Allen Institute for AI(AI2)에서 발표한 단어 임베딩 모델로, 단어의 의미가 문맥에 따라 달라진다는 점을 효과적으로 포착하여 기존의 정적인(static) 단어 임베딩(예: Word2Vec, GloVe)의 한계를 극복했습니다. ELMo는 **사전 학습된(pre-trained) 심층 양방향 언어 모델(Deep Bidirectional Language Model)** 을 사용하여 각 단어에 대한 **문맥 의존적인(contextualized) 임베딩**을 생성합니다.

## 📖 핵심 아이디어

ELMo의 핵심 아이디어는 다음과 같습니다.

1.  **문맥 의존적 임베딩**: 단어의 의미는 주변 단어(문맥)에 따라 달라집니다. ELMo는 동일한 단어라도 문맥에 따라 다른 임베딩 벡터를 생성하여 다의어(polysemy) 문제를 해결합니다.
2.  **심층 양방향 언어 모델**: 단어 임베딩을 생성하기 위해 심층 양방향 LSTM(Long Short-Term Memory) 네트워크를 사용합니다. 이는 단어의 왼쪽 문맥과 오른쪽 문맥 정보를 모두 활용하여 더 풍부한 의미를 포착합니다.
3.  **계층적 표현**: ELMo는 심층 LSTM의 각 계층(layer)에서 얻은 표현(representation)들을 결합하여 최종 임베딩을 생성합니다. 각 계층은 다른 종류의 문맥 정보를 포착하며, 하위 계층은 구문적(syntactic) 정보를, 상위 계층은 의미적(semantic) 정보를 더 잘 포착하는 경향이 있습니다.

## ⚙️ 아키텍처 및 작동 방식

ELMo는 크게 두 단계로 작동합니다.

### 1. 사전 학습 (Pre-training)

ELMo는 대규모 텍스트 말뭉치(예: 1B Word Benchmark)를 사용하여 심층 양방향 언어 모델을 사전 학습합니다.

*   **양방향 LSTM**: 순방향(forward) LSTM과 역방향(backward) LSTM 두 개를 독립적으로 학습시킵니다.
    *   **순방향 LM**: 이전 단어들을 기반으로 다음 단어를 예측합니다. $P(t_1, t_2, ..., t_N) = \prod_{k=1}^{N} P(t_k | t_1, ..., t_{k-1})$
    *   **역방향 LM**: 다음 단어들을 기반으로 이전 단어를 예측합니다. $P(t_1, t_2, ..., t_N) = \prod_{k=1}^{N} P(t_k | t_{k+1}, ..., t_N)$
*   **손실 함수**: 두 언어 모델의 로그 우도(log-likelihood)를 최대화하는 방향으로 학습됩니다.

### 2. 태스크별 미세 조정 (Fine-tuning)

사전 학습된 ELMo 모델은 특정 NLP 태스크(예: 개체명 인식, 감성 분석, 질의응답)에 적용될 때, 해당 태스크의 모델에 통합되어 사용됩니다.

*   **계층 결합**: 사전 학습된 양방향 LSTM의 각 계층에서 출력되는 은닉 상태(hidden states)들을 가중치 합(weighted sum)하여 최종 ELMo 임베딩을 생성합니다.
    $$ELMo_k = \gamma \sum_{j=0}^{L} s_j h_{k,j}^{LM}$$
    *   $h_{k,j}^{LM}$: $k$번째 단어의 $j$번째 LSTM 계층의 출력입니다.
    *   $s_j$: 각 계층의 가중치로, 태스크별로 학습됩니다.
    *   $\gamma$: 스케일링 파라미터로, 태스크별로 학습됩니다.
*   **태스크 모델 입력**: 이렇게 생성된 ELMo 임베딩은 태스크별 모델(예: 분류기, 시퀀스 레이블링 모델)의 입력으로 사용되거나, 기존 임베딩(예: Word2Vec)과 연결(concatenation)하여 사용될 수 있습니다.

## ✨ 기존 임베딩과의 차이점 및 장점

*   **문맥 의존성**: Word2Vec이나 GloVe는 단어 하나당 하나의 고정된 임베딩을 갖지만, ELMo는 문맥에 따라 단어의 임베딩이 동적으로 변합니다. 이는 다의어 처리 및 미묘한 의미 차이 포착에 매우 효과적입니다.
*   **전이 학습(Transfer Learning)**: 대규모 말뭉치에서 사전 학습된 언어 모델의 지식을 다양한 하류(downstream) NLP 태스크로 전이하여, 적은 양의 태스크별 데이터로도 높은 성능을 달성할 수 있게 합니다.
*   **심층 표현**: 여러 계층의 정보를 결합하여 단어의 다양한 의미적, 구문적 측면을 포착합니다.

## 🔗 관련 개념

-   [[Word Embedding]]
-   [[Contextual Embedding]]
-   [[Word2Vec]]
-   [[GloVe]]
-   [[LSTM]]
-   [[Transformer]]
-   [[BERT]]
-   [[GPT]]
