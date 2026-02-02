# Word2Vec

#NLP #Embedding

---

## 1. 개요

**Word2Vec(Word to Vector)** 은 2013년 구글의 Tomas Mikolov 연구팀이 제안한 단어 임베딩(Word Embedding) 모델입니다. 단어를 저차원의 연속적인 벡터(dense vector)로 표현하는 방법론으로, 자연어 처리 분야에 큰 발전을 가져왔습니다.

Word2Vec의 핵심 아이디어는 **"비슷한 문맥에서 등장하는 단어는 비슷한 의미를 가질 것이다"** 라는 분포 가설(Distributional Hypothesis)에 기반합니다. 이 아이디어를 바탕으로, 특정 단어의 의미를 주변 단어들과의 관계를 통해 학습하고, 이를 벡터 공간에 표현합니다.

---

## 2. 핵심 모델

Word2Vec은 두 가지 주요 학습 모델을 제안합니다.

### 2.1. CBOW (Continuous Bag-of-Words)

- **방식:** 주변 단어들(context words)을 입력으로 하여, 중심 단어(center word)를 예측하는 모델입니다.
- **예시:** 문장 `["The", "cat", "sits", "on", "the", "mat"]` 에서
    - Context: `["The", "cat", "on", "the"]`
    - Center: `sits`
    - CBOW는 `["The", "cat", "on", "the"]`를 보고 `sits`를 맞추도록 학습됩니다.
- **특징:** 여러 주변 단어의 정보를 종합하므로, 작은 데이터셋에서도 준수한 성능을 보이며 학습 속도가 빠릅니다.

### 2.2. Skip-gram

- **방식:** 중심 단어(center word)를 입력으로 하여, 주변 단어들(context words)을 예측하는 모델입니다.
- **예시:** 문장 `["The", "cat", "sits", "on", "the", "mat"]` 에서
    - Center: `sits`
    - Context: `["The", "cat", "on", "the"]`
    - Skip-gram은 `sits`를 보고 `["The", "cat", "on", "the"]`를 각각 맞추도록 학습됩니다.
- **특징:** 하나의 중심 단어로 여러 주변 단어를 예측해야 하므로 CBOW보다 학습이 어렵고 시간이 더 걸립니다. 하지만, 희귀한 단어(rare word)에 대해 더 좋은 임베딩 성능을 보이며, 일반적으로 더 품질 좋은 단어 벡터를 생성하는 것으로 알려져 있습니다.

---

## 3. 학습 최적화 기법

Word2Vec은 대규모 어휘 집합을 효율적으로 학습하기 위해 다음과 같은 최적화 기법을 사용합니다.

- **Negative Sampling:** 전체 어휘 집합을 대상으로 소프트맥스(softmax) 계산을 하는 대신, 실제 정답(positive sample)인 주변 단어 하나와, 정답이 아닌(negative samples) 몇 개의 단어만을 샘플링하여 이진 분류 문제로 변환합니다. 이를 통해 계산량을 대폭 줄입니다.
- **Hierarchical Softmax:** 어휘 집합의 모든 단어를 이진 트리(binary tree) 구조로 표현하고, 루트에서 해당 단어까지의 경로를 예측하는 방식으로 계산량을 줄입니다.

---

## 4. 결과 및 의의

- **의미적 관계 포착:** Word2Vec으로 생성된 단어 벡터들은 단어 간의 의미적, 문법적 관계를 벡터 공간에 잘 표현합니다. 예를 들어, `vec("king") - vec("man") + vec("woman")` 와 `vec("queen")`의 벡터가 매우 유사하게 나타나는 것이 대표적입니다.
- **전이 학습의 기반:** 사전 학습된(pre-trained) Word2Vec 임베딩은 다양한 다운스트림 NLP 작업(감성 분석, 개체명 인식 등)의 성능을 크게 향상시키는 기반이 되었습니다.
- **단어의 분산 표현:** [[Bag-of-Words]]나 [[TF-IDF]]와 같은 희소 표현(sparse representation) 방식의 한계를 극복하고, 단어를 의미를 함축한 밀집 표현(dense representation)으로 바꾸는 패러다임을 열었습니다.

Word2Vec은 이후 등장하는 [[GloVe]], FastText, 그리고 [[BERT]]와 같은 문맥적 임베딩(Contextual Embedding) 모델의 발전에 큰 영향을 미쳤습니다.
