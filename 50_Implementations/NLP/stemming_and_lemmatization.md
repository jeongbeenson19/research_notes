
# Stemming and Lemmatization (어간 추출과 표제어 추출)

#NLP #Concept #Preprocessing #Tokenization

---

## 1. 개요

텍스트 정규화(Text Normalization)는 [[Corpus|말뭉치]]에 존재하는 다양한 형태의 단어들을 하나의 표준 형태로 통일하는 과정입니다. 예를 들어, 'run', 'runs', 'running'은 모두 '달리다'라는 동일한 의미를 갖지만, 컴퓨터는 이를 다른 단어로 인식합니다. **어간 추출(Stemming)**과 **표제어 추출(Lemmatization)**은 이러한 단어들을 각각의 어근(root)이나 기본형(lemma)으로 변환하여, 모델이 단어의 의미를 더 일관되게 학습할 수 있도록 돕는 핵심적인 정규화 기법입니다.

이 두 기법은 [[Tokenization|토큰화]]와 [[stopword|불용어]] 제거 이후에 적용되는 일반적인 전처리 단계입니다.

---

## 2. 어간 추출 (Stemming)

**어간 추출(Stemming)** 은 단어의 형태학적 규칙에 기반하여 접미사(suffix)나 접두사(prefix)를 잘라내고 어간(stem)을 추출하는 방법입니다. 이 과정은 사전을 참조하지 않고 정해진 규칙에 따라 진행되므로 속도가 매우 빠릅니다.

-   **특징:**
    -   **빠른 속도:** 간단한 규칙 기반으로 동작하여 계산 비용이 적습니다.
    -   **정확성 부족:** 규칙에만 의존하므로, 결과로 나오는 어간이 실제 사전에 존재하지 않는 단어일 수 있습니다. (예: `argue` -> `argu`)
    -   **과도한 단순화 (Over-stemming):** 서로 다른 의미의 단어를 같은 어간으로 변환할 수 있습니다. (예: `universal`, `university` -> `univers`)
    -   **미흡한 단순화 (Under-stemming):** 같은 의미의 단어를 다른 어간으로 변환할 수 있습니다. (예: `data`, `datum` -> `data`, `datu`)

### 2.1. 주요 알고리즘

-   **Porter Stemmer:** 가장 널리 알려진 어간 추출 알고리즘으로, 5단계의 규칙을 통해 접미사를 제거합니다. 비교적 부드러운(gentle) 성능을 보입니다.
-   **Lancaster Stemmer:** Porter Stemmer보다 더 공격적으로 어간을 추출하는 알고리즘입니다. 더 많은 단어를 동일한 어간으로 통합하지만, 그만큼 정확성은 떨어질 수 있습니다.

### 2.2. Python 예제 (NLTK)

[[Python Tokenizers|NLTK 라이브러리]]를 사용하여 Porter Stemmer를 실습할 수 있습니다.

```python
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

words = ["studies", "studying", "study", "argues", "argued", "argument", "arguments", "am", "is", "are", "better"]
tokens = word_tokenize(' '.join(words))

stemmed_words = [stemmer.stem(token) for token in tokens]

print("Original Words:", tokens)
print("Stemmed Words: ", stemmed_words)
# 출력:
# Original Words: ['studies', 'studying', 'study', 'argues', 'argued', 'argument', 'arguments', 'am', 'is', 'are', 'better']
# Stemmed Words:  ['studi', 'studi', 'studi', 'argu', 'argu', 'argument', 'argument', 'am', 'is', 'are', 'better']
```
*결과에서 볼 수 있듯이 `studies`와 `studying`은 `studi`로, `argues`와 `argued`는 `argu`라는 사전에 없는 단어로 변환되었습니다. 또한 `am, is, are`와 `better`는 어간이 추출되지 않았습니다.*

---

## 3. 표제어 추출 (Lemmatization)

**표제어 추출(Lemmatization)** 은 단어의 문법적, 문맥적 의미를 고려하여 사전에 등재된 기본형, 즉 **표제어(Lemma)** 를 찾는 과정입니다. 예를 들어, 'am', 'are', 'is'의 표제어는 모두 'be'입니다.

-   **특징:**
    -   **높은 정확도:** 결과물이 사전에 존재하는 단어이므로 의미론적으로 더 정확합니다.
    -   **품사 정보 활용:** 단어의 품사(Part-of-Speech, POS) 정보를 입력으로 받아 더 정확한 표제어를 찾습니다. (예: `running`이 동사일 경우 `run`, 명사일 경우 `running` 그대로 반환)
    -   **느린 속도:** 사전을 조회하고 형태소를 분석하는 과정이 필요하므로 어간 추출보다 속도가 느립니다.

### 3.1. Python 예제 (NLTK)

NLTK의 `WordNetLemmatizer`는 WordNet이라는 대규모 어휘 데이터베이스를 사용하여 표제어를 추출합니다.

-   **데이터 다운로드:** `nltk.download('wordnet')`, `nltk.download('averaged_perceptron_tagger')`

```python
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

lemmatizer = WordNetLemmatizer()

words = ["studies", "studying", "study", "argues", "argued", "argument", "arguments", "am", "is", "are", "better"]
tokens = word_tokenize(' '.join(words))

# 품사 태깅
pos_tokens = pos_tag(tokens)

# NLTK의 품사 태그를 WordNet이 이해하는 형식으로 변환하는 함수
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return 'a' # adjective
    elif treebank_tag.startswith('V'):
        return 'v' # verb
    elif treebank_tag.startswith('N'):
        return 'n' # noun
    elif treebank_tag.startswith('R'):
        return 'r' # adverb
    else:
        return 'n' # default: noun

lemmatized_words = [lemmatizer.lemmatize(token, pos=get_wordnet_pos(pos)) for token, pos in pos_tokens]

print("Original Words with POS:", pos_tokens)
print("Lemmatized Words:", lemmatized_words)
# 출력:
# Original Words with POS: [('studies', 'NNS'), ('studying', 'VBG'), ('study', 'NN'), ('argues', 'VBZ'), ('argued', 'VBD'), ('argument', 'NN'), ('arguments', 'NNS'), ('am', 'VBP'), ('is', 'VBZ'), ('are', 'VBP'), ('better', 'RBR')]
# Lemmatized Words: ['study', 'study', 'study', 'argue', 'argue', 'argument', 'argument', 'be', 'be', 'be', 'good']
```
*품사 정보를 활용하여 `studies`, `studying`은 `study`로, `argues`, `argued`는 `argue`로 정확히 변환되었습니다. `am, is, are`는 `be`로, 부사(RBR) `better`는 원급인 형용사 `good`으로 변환된 것을 볼 수 있습니다.*

---

## 4. Stemming vs. Lemmatization 비교

| 구분 | 어간 추출 (Stemming) | 표제어 추출 (Lemmatization) |
| :--- | :--- | :--- |
| **목표** | 단어의 접미사를 제거하여 어간을 찾음 | 단어의 문법적, 의미적 기본형(표제어)을 찾음 |
| **정확도** | 낮음 (결과가 사전에 없는 단어일 수 있음) | 높음 (결과가 항상 사전에 있는 단어임) |
| **속도** | 빠름 | 느림 |
| **의존성** | 규칙(Rules) | 사전(Dictionary) 및 품사(POS) 정보 |
| **예시** | `studies` -> `studi` | `studies` -> `study` |
| **예시** | `better` -> `better` | `better` -> `good` |

---

## 5. 언제 무엇을 사용해야 하는가?

-   **어간 추출 (Stemming)이 유용한 경우:**
    -   **정보 검색(IR) 및 검색 엔진:** 속도가 매우 중요하고, 약간의 정확성 손실이 검색 결과에 큰 영향을 미치지 않는 시스템에 적합합니다. 사용자가 'studying computers'라고 검색해도 'study computer' 관련 문서를 찾아줄 수 있습니다.
    -   **텍스트 분류:** 문서의 전반적인 주제를 파악하는 데에는 어간만으로도 충분한 경우가 많습니다.

-   **표제어 추출 (Lemmatization)이 유용한 경우:**
    -   **챗봇, Q&A 시스템:** 사용자의 질문 의도를 정확하게 파악하고 문법적으로 올바른 답변을 생성해야 할 때 필수적입니다.
    -   **기계 번역:** 단어의 정확한 의미와 문법적 역할이 중요하므로 표제어 추출이 선호됩니다.
    -   **의미 분석:** 단어의 미묘한 의미 차이를 분석해야 하는 작업에 적합합니다.

결론적으로, **속도가 중요하면 어간 추출**을, **정확성이 중요하면 표제어 추출**을 선택하는 것이 일반적인 접근 방식입니다. 현대적인 NLP 애플리케이션에서는 정확성을 위해 표제어 추출이 더 널리 사용되는 추세입니다.
