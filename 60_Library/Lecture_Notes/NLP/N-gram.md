---
tags: #NLP #LanguageModel #TextProcessing
aliases: [N-그램, 엔그램]
---

# N-gram

> **한 줄 요약**: 텍스트나 음성 데이터에서 연속적으로 나타나는 `n`개의 아이템(단어, 문자 등) 시퀀스.

**N-gram**은 자연어 처리(NLP)와 텍스트 마이닝에서 텍스트를 작은 단위로 분해하여 분석하는 가장 기본적인 방법 중 하나입니다. 여기서 `n`은 시퀀스의 길이를 나타내는 정수입니다.

-   **Unigram (1-gram)**: 1개의 아이템 (주로 단어) 묶음
-   **Bigram (2-gram)**: 연속된 2개의 아이템 묶음
-   **Trigram (3-gram)**: 연속된 3개의 아이템 묶음

---

## 1. N-gram 생성 방법 (Sliding Window)

N-gram은 "슬라이딩 윈도우(Sliding Window)" 방식을 통해 텍스트의 처음부터 끝까지 창문(window)을 `n`의 크기로 설정하고 한 칸씩 이동하며 시퀀스를 추출합니다.

**예시 문장**: `The quick brown fox jumps over the lazy dog`

-   **Unigrams**: `The`, `quick`, `brown`, `fox`, `jumps`, `over`, `the`, `lazy`, `dog`
-   **Bigrams**: `The quick`, `quick brown`, `brown fox`, `fox jumps`, `jumps over`, `over the`, `the lazy`, `lazy dog`
-   **Trigrams**: `The quick brown`, `quick brown fox`, `brown fox jumps`, ...

## 2. N-gram 언어 모델의 확률 계산

N-gram의 핵심은 이전 단어들을 기반으로 다음 단어가 나타날 확률을 계산하는 것입니다. 이는 **최대우도추정(Maximum Likelihood Estimation, MLE)** 을 통해 계산됩니다.

### 가. 다음 단어의 조건부 확률

N-gram 모델은 **마르코프 가정(Markov Assumption)** 에 기반합니다. 즉, 특정 단어의 등장 확률은 오직 그 이전의 `n-1`개 단어에만 의존한다는 가정입니다.

이를 수식으로 표현하면 다음과 같습니다.

$$P(w_i | w_1, ..., w_{i-1}) ≈ P(w_i | w_{i-n+1}, ..., w_{i-1})$$`

이 확률은 훈련 코퍼스에서의 빈도를 세어 계산합니다.

$$P(w_i | w_{i-n+1}, ..., w_{i-1}) = count(w_{i-n+1}, ..., w_{i-1}, w_i) / count(w_{i-n+1}, ..., w_{i-1})$$

**예시 (Bigram, n=2):**
$$P(dog | lazy) = count("lazy dog") / count("lazy")$$

만약 훈련 코퍼스에서 "lazy"가 10번 등장했고, 그중 "lazy dog"이 5번 등장했다면, `P(dog | lazy)`는 `5 / 10 = 0.5`가 됩니다.

### 나. 문장 전체의 확률

문장 전체의 확률은 각 단어의 조건부 확률을 **연쇄 법칙(Chain Rule)** 에 따라 곱하여 계산합니다.

$$P(w_1, w_2, ..., w_k) = P(w_1) * P(w_2 | w_1) * P(w_3 | w_1, w_2) * ...$$

N-gram의 마르코프 가정을 적용하면 이 수식은 크게 단순화됩니다.

**예시 (Bigram, n=2):**
$$P(The, lazy, dog) ≈ P(The) * P(lazy | The) * P(dog | lazy)$$

이러한 방식으로 N-gram 모델은 특정 문장이 얼마나 자연스러운지(등장할 확률이 높은지)를 수치적으로 평가할 수 있습니다.

## 3. N-gram의 활용

N-gram 모델은 특정 단어 시퀀스 다음에 어떤 단어가 나타날 확률을 계산하는 **통계적 언어 모델(Statistical Language Model)** 의 근간을 이룹니다. 즉, `n-1`개의 단어 시퀀스가 주어졌을 때, `n`번째 단어를 예측하는 데 사용됩니다.

-   **언어 모델링**: 문장의 자연스러움을 평가하거나 다음 단어를 예측합니다.
-   **기계 번역 및 음성 인식**: 후보 번역/인식 결과들의 확률을 평가합니다.
-   **철자 교정 및 자동 완성**: 오타를 교정하거나 다음 입력 단어를 추천합니다.
-   **텍스트 분류**: 문서에 특정 N-gram이 얼마나 자주 나타나는지를 특징(feature)으로 사용합니다.

## 4. 한계점

N-gram 모델은 간단하고 효과적이지만 명확한 한계를 가집니다.

1.  **희소성 문제 (Sparsity Problem)**: `n`이 커질수록 훈련 데이터에 등장하지 않는 N-gram의 수가 기하급수적으로 증가합니다. 훈련 코퍼스에 한 번도 나타나지 않은 N-gram은 확률이 0으로 계산되어, 실제로는 유효한 문장임에도 불구하고 확률을 0으로 예측할 수 있습니다.
    -   **해결책**: 스무딩(Smoothing), 백오프(Back-off) 등의 기법을 사용하여 0의 확률을 보정합니다.

2.  **장기 의존성 포착의 어려움 (Long-term Dependency)**: N-gram은 `n`이라는 작은 창문 내의 지역적인 문맥(local context)만을 고려합니다. 따라서 문장 내에서 멀리 떨어진 단어 간의 의미적 관계나 문법 구조를 파악하기 어렵습니다.
    -   *예시*: "The man who lives in a big house on the hill **is** happy." 에서 주어 "man"과 동사 "is" 사이의 관계를 파악하기 위해선 매우 큰 `n`이 필요합니다.

이러한 한계로 인해 현대 NLP에서는 [[RNN]], [[LSTM]], [[Transformer]]와 같은 딥러닝 기반의 모델들이 장기 의존성을 더 잘 학습하여 N-gram 모델을 대체하고 있습니다.

---

## 5. 관련 개념

-   [[Large Language Models|LLM]]
-   [[Tokenization]]
-   [[Bag-of-Words]]
-   [[Corpus]]
