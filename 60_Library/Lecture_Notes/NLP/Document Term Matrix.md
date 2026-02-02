
# Document Term Matrix (DTM)

#NLP #TextRepresentation #Concept 

---

## 1. Document Term Matrix (DTM)란?

**Document Term Matrix (문서 단어 행렬, DTM)** 는 텍스트 데이터를 통계적으로 표현하는 행렬입니다. 여러 문서(Document)에 등장하는 각 단어(Term)의 출현 빈도를 행렬로 정리한 것으로, 텍스트 마이닝과 자연어 처리에서 텍스트를 수치화하는 기본적인 방법 중 하나입니다.

- **행 (Rows):** 각 문서를 나타냅니다.
- **열 (Columns):** 전체 문서 집합(corpus)에 등장하는 모든 고유한 단어(어휘)를 나타냅니다.
- **값 (Value):** 특정 문서(행)에 특정 단어(열)가 몇 번 등장했는지를 나타내는 빈도수(frequency)입니다.

DTM은 본질적으로 [[../../../10_Concepts/Machine_Learning/Bag-of-Words|Bag-of-Words (BoW)]] 모델을 여러 문서에 대해 행렬 형태로 구현한 것입니다.

---

## 2. DTM의 구성 과정

1.  **[[../../../10_Concepts/Machine_Learning/Tokenization|토큰화 (Tokenization)]]:** 각 문서를 단어(토큰) 단위로 분할합니다.
2.  **어휘(Vocabulary) 구축:** 전체 문서 집합에서 고유한 단어들의 집합을 만듭니다. 이 집합이 DTM의 열(column)이 됩니다.
3.  **벡터화 (Vectorization):** 각 문서를 어휘(vocabulary)를 기반으로 한 벡터로 표현합니다. 각 벡터의 차원은 어휘의 크기와 같으며, 각 원소는 해당 단어의 등장 빈도를 나타냅니다.
4.  **행렬 생성:** 각 문서에 대한 벡터를 행으로 쌓아 DTM을 완성합니다.

### 예시

**문서 집합 (Corpus):**
- **문서 1:** "apple banana apple"
- **문서 2:** "banana orange"
- **문서 3:** "apple orange grape"

**1. 어휘 구축:**
- `apple`, `banana`, `orange`, `grape`

**2. DTM 생성:**

| 문서   | apple | banana | orange | grape |
| :----- | :---: | :----: | :----: | :---: |
| 문서 1 |   2   |   1    |   0    |   0   |
| 문서 2 |   0   |   1    |   1    |   0   |
| 문서 3 |   1   |   0    |   1    |   1   |


## 3. DTM의 한계

DTM은 간단하고 직관적이지만 몇 가지 중요한 한계를 가집니다.

1.  **희소성 문제 (Sparsity Problem):**
    - 문서의 수가 많고 어휘의 크기가 클수록 DTM은 대부분의 값이 0인 **희소 행렬(Sparse Matrix)** 이 됩니다.
    - 이는 저장 공간의 낭비와 계산 비효율성을 초래할 수 있습니다.

2.  **높은 차원 (High Dimensionality):**
    - 어휘의 크기가 곧 행렬의 차원이 되므로, 단어가 많아질수록 벡터의 차원이 급격하게 커집니다. 이를 '차원의 저주'라고도 합니다.

3.  **단어의 의미 미반영:**
    - 단어의 순서나 문맥 정보를 무시하고 단순히 빈도수만 고려하므로, "I love you"와 "You love I"를 동일하게 처리할 수 있습니다.
    - 단어 간의 의미적 유사성을 파악하지 못합니다. (예: 'fruit'와 'apple'의 관계)

4.  **불용어(Stopwords)의 중요성 왜곡:**
    - 'the', 'a', 'is'와 같은 불용어는 자주 등장하기 때문에 높은 빈도수를 갖게 됩니다.
    - 이로 인해 문서의 실제 주제나 특성을 파악하는 데 방해가 될 수 있습니다. 이 문제를 완화하기 위해 [[../../../10_Concepts/Machine_Learning/TF-IDF|TF-IDF]] 가중치를 사용하기도 합니다.

---

## 4. DTM의 활용

이러한 한계에도 불구하고 DTM은 여러 NLP 작업의 기초가 됩니다.

- **문서 분류 (Document Classification):** DTM을 기반으로 각 문서를 벡터로 표현하여 분류 모델의 입력으로 사용합니다.
- **정보 검색 (Information Retrieval):** 사용자 쿼리와 문서 간의 유사도를 계산하는 데 사용됩니다.
- **문서 군집화 (Document Clustering):** 유사한 주제의 문서를 그룹화하는 데 활용됩니다.
- **토픽 모델링 (Topic Modeling):** DTM으로부터 잠재된 주제를 추출하는 LDA(Latent Dirichlet Allocation)와 같은 알고리즘의 입력으로 사용됩니다.

DTM의 한계를 보완하기 위해 [[../../../10_Concepts/Machine_Learning/TF-IDF|TF-IDF]], [[../../../10_Concepts/Machine_Learning/Word2Vec|Word2Vec]], [[../../../30_Architectures/LanguageModels/BERT|BERT]]와 같은 더 발전된 텍스트 표현 기법들이 사용됩니다.
