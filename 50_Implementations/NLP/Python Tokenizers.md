
# Python에서의 토크나이저 (Tokenizers in Python)

#NLP #Implementation #Python #Tokenization

---

## 1. 개요

자연어 처리(NLP) 파이프라인에서 텍스트를 모델이 이해할 수 있는 형태로 변환하는 첫 단계는 **토큰화(Tokenization)** 입니다. 파이썬은 이러한 토큰화 작업을 수행할 수 있는 다양한 라이브러리와 도구를 제공합니다. 이 문서에서는 파이썬에서 널리 사용되는 토크나이저 라이브러리들을 소개하고 기본적인 사용법을 다룹니다.

[[../../../10_Concepts/Machine_Learning/Tokenization|토큰화]]는 텍스트를 단어, 구, 또는 하위 단어(subword)와 같은 의미 있는 단위인 **토큰**으로 분리하는 과정입니다.

---

## 2. 주요 파이썬 토크나이저 라이브러리

### 2.1. NLTK (Natural Language Toolkit)

NLTK는 파이썬에서 가장 오래되고 광범위하게 사용되는 NLP 라이브러리 중 하나입니다. 다양한 토크나이저를 제공하며, 연구 및 교육 목적으로 많이 활용됩니다.

-   **설치:** `pip install nltk`
-   **데이터 다운로드:** `nltk.download('punkt_tab')` (Punkt Tokenizer 사용을 위해)

#### 예시: 단어 토큰화 (Word Tokenization)

```python
import nltk
from nltk.tokenize import word_tokenize

text = "Hello, world! This is an example sentence."
tokens = word_tokenize(text)
print(tokens)
# 출력: ['Hello', ',', 'world', '!', 'This', 'is', 'an', 'example', 'sentence', '.']
```

#### 예시: 문장 토큰화 (Sentence Tokenization)

```python
from nltk.tokenize import sent_tokenize

text = "Hello, world! This is an example sentence. How are you?"
sentences = sent_tokenize(text)
print(sentences)
# 출력: ['Hello, world!', 'This is an example sentence.', 'How are you?']
```

#### 주요 NLP 작업 메서드

NLTK는 토큰화 외에도 품사 태깅(POS Tagging), 어간 추출(Stemming), 표제어 추출(Lemmatization) 등 다양한 기본 NLP 작업을 위한 메서드를 제공합니다.

-   **데이터 다운로드:** 아래 예시를 실행하기 위해 추가 데이터가 필요할 수 있습니다.
    `nltk.download('averaged_perceptron_tagger')`
    `nltk.download('wordnet')`
    `nltk.download('omw-1.4')`

##### 품사 태깅 (Part-of-Speech Tagging)

```python
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

text = "NLTK provides many useful functions."
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
print(pos_tags)
# 출력: [('NLTK', 'NNP'), ('provides', 'VBZ'), ('many', 'JJ'), ('useful', 'JJ'), ('functions', 'NNS'), ('.', '.')]
```

##### 어간 추출 (Stemming)

단어의 어미를 제거하여 어간을 추출합니다.

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "runs", "runner", "easily", "fairly"]
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)
# 출력: ['run', 'run', 'runner', 'easili', 'fairli']
```

##### 표제어 추출 (Lemmatization)

단어의 원형(표제어)을 찾습니다. 어간 추출보다 더 정교하며, 단어의 품사 정보를 활용할 수 있습니다.

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("running", pos='v')) # 동사 (verb)
print(lemmatizer.lemmatize("runs", pos='v'))
print(lemmatizer.lemmatize("runner", pos='n')) # 명사 (noun)
print(lemmatizer.lemmatize("better", pos='a')) # 형용사 (adjective)
```

### 2.2. SpaCy

SpaCy는 산업용 NLP 애플리케이션 개발에 최적화된 고성능 라이브러리입니다. NLTK보다 빠르고 효율적이며, 토큰화 외에도 품사 태깅, 개체명 인식 등 다양한 기능을 통합적으로 제공합니다.

-   **설치:** `pip install spacy`
-   **모델 다운로드:** `python -m spacy download en_core_web_sm` (영어 모델)

#### 예시: 토큰화

```python
import spacy

# 모델 로드 (한 번만 실행)
nlp = spacy.load("en_core_web_sm")

text = "SpaCy is a powerful NLP library. It's fast!"
doc = nlp(text)

tokens = [token.text for token in doc]
print(tokens)
# 출력: ['SpaCy', 'is', 'a', 'powerful', 'NLP', 'library', '.', 'It', "'s", 'fast', '!']

# 각 토큰의 속성 접근
for token in doc:
    print(f"{token.text:<10} {token.pos_:<10} {token.is_punct:<10} {token.is_space:<10}")
```

### 2.3. Hugging Face Transformers (tokenizers 라이브러리)

Hugging Face의 `transformers` 라이브러리는 [[BERT]], [[GPT]] 등 최신 트랜스포머 기반 모델을 위한 토크나이저를 제공합니다. 이들은 주로 **단어 하위 단위(subword) 토큰화**에 중점을 둡니다.

-   **설치:** `pip install transformers`

#### 예시: BERT 토크나이저

```python
from transformers import AutoTokenizer

# 사전 학습된 모델의 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Using subword tokenization is efficient."
tokens = tokenizer.tokenize(text)
print(tokens)
# 출력: ['using', 'sub', '##word', 'token', '##ization', 'is', 'efficient', '.']

# 인코딩 (토큰 ID로 변환)
encoded_input = tokenizer(text, return_tensors="pt")
print(encoded_input)
# 출력: {'input_ids': tensor([[ 101, 2478, 1700, 2773, 19204, 2003, 6360, 102]]), 'token_type_ids': tensor([[0, 0, 0, 0, 0, 0, 0, 0]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1]])}
```

### 2.4. KoNLPy (Korean NLP Library)

KoNLPy는 한국어 자연어 처리를 위한 파이썬 라이브러리입니다. 한국어는 교착어(agglutinative language)의 특성상 띄어쓰기만으로는 단어를 분리하기 어렵고, 형태소 분석(morphological analysis)이 필수적입니다. KoNLPy는 여러 형태소 분석기(Okt, Kkma, Komoran, Hannanum, Mecab 등)를 파이썬에서 쉽게 사용할 수 있도록 통합된 인터페이스를 제공합니다.

-   **설치:** `pip install konlpy` (Java Development Kit (JDK)가 필요합니다. 설치 전에 JDK를 먼저 설치해야 합니다.)

#### 예시: 형태소 분석 (Morphological Analysis) - Okt 사용

```python
from konlpy.tag import Okt

okt = Okt()

text = "아버지가 방에 들어가신다."

# 형태소 분석 (pos tagging)
morphs = okt.pos(text)
print("형태소 분석:", morphs)
# 출력: 형태소 분석: [('아버지', 'Noun'), ('가', 'Josa'), ('방', 'Noun'), ('에', 'Josa'), ('들어가신다', 'Verb'), ('.', 'Punctuation')]

# 명사 추출
nouns = okt.nouns(text)
print("명사 추출:", nouns)
# 출력: 명사 추출: ['아버지', '방']

# 구문 분석 (phrases)
phrases = okt.phrases(text)
print("구문 분석:", phrases)
# 출력: 구문 분석: ['아버지', '아버지방', '방']
```

#### 예시: Kkma 사용

```python
from konlpy.tag import Kkma

kkma = Kkma()

text = "안녕하세요, 한국어 분석을 시작합니다."

# 형태소 분석
morphs = kkma.pos(text)
print("형태소 분석:", morphs)
# 출력: 형태소 분석: [('안녕', 'NNG'), ('하', 'XSV'), ('세요', 'EFN'), (',', 'SP'), ('한국어', 'NNG'), ('분석', 'NNG'), ('을', 'JKO'), ('시작', 'NNG'), ('하', 'XSV'), ('ㅂ니다', 'EFN'), ('.', 'SF')]

# 문장 분리
sentences = kkma.sentences(text)
print("문장 분리:", sentences)
# 출력: 문장 분리: ['안녕하세요,', '한국어 분석을 시작합니다.']
```

---

## 3. 토크나이저 선택 가이드

-   **연구 및 교육, 기본 NLP 작업:** NLTK는 다양한 알고리즘과 데이터셋을 제공하여 시작하기에 좋습니다.
-   **성능과 통합된 파이프라인:** SpaCy는 빠른 속도와 통합된 NLP 기능을 제공하여 실제 애플리케이션에 적합합니다.
-   **최신 딥러닝 모델:** [[BERT]], [[GPT]] 등 트랜스포머 기반 모델을 사용한다면 Hugging Face `transformers` 라이브러리의 토크나이저가 필수적입니다. 이들은 모델과 함께 사전 학습된 토크나이저를 제공하여 호환성을 보장합니다.

파이썬의 풍부한 생태계 덕분에, 어떤 NLP 작업이든 적절한 토크나이저를 찾아 효율적으로 텍스트를 처리할 수 있습니다.
