# 자연어 처리 (Natural Language Processing)


#NLP #ComputerScience #MachineLearning

---

## 1. 자연어 처리란?

**자연어 처리(Natural Language Processing, NLP)** 는 인간이 사용하는 언어(자연어)를 컴퓨터가 이해하고, 해석하며, 생성할 수 있도록 하는 인공지능(AI)의 한 분야입니다. NLP 기술을 통해 컴퓨터는 텍스트나 음성 데이터를 처리하여 사람과 유사한 방식으로 소통하고 정보를 추출할 수 있습니다.

**주요 목표:**
- **자연어 이해 (Natural Language Understanding, NLU):** 컴퓨터가 인간의 언어를 이해하는 것.
- **자연어 생성 (Natural Language Generation, NLG):** 컴퓨터가 인간의 언어로 텍스트를 생성하는 것.

---

## 2. 자연어 처리의 역사

- **초기 (1950s-1960s):** 규칙 기반 시스템. 주로 기계 번역에 초점. (예: 조지타운-IBM 실험)
- **통계적 접근 (1990s-2000s):** 대규모 말뭉치(corpus)를 사용하여 통계적 모델을 학습. (예: [[ANN|인공 신경망]], [[Support Vector Machines|Support Vector Machines]])
- **딥러닝 시대 (2010s-현재):** [[RNN|순환 신경망(RNN)]], [[30_Architectures/Backbones/Transformer|트랜스포머(Transformer)]]와 같은 딥러닝 모델의 등장으로 NLP 분야에 혁신적인 발전을 가져옴. (예: [[../../../30_Architectures/LanguageModels/BERT|BERT]], [[../../../30_Architectures/LanguageModels/GPT|GPT]])

---

## 3. 자연어 처리의 주요 기술

### 3.1. 텍스트 전처리 (Text Preprocessing)

컴퓨터가 텍스트를 이해하기 쉽도록 정제하는 과정입니다.

- **[[Tokenization]]:** 문장을 단어, 구, 또는 다른 의미 있는 단위(토큰)로 분할하는 과정. (자세한 내용은 [[../../../50_Implementations/NLP/Python Tokenizers|Python에서의 토크나이저]] 문서 참고)
- **정제 (Cleaning):** 불필요한 문자, 태그, 기호 등을 제거.
- **정규화 (Normalization):**
    - **어간 추출 (Stemming):** 단어의 어미를 제거하여 어간을 추출. (e.g., "running" -> "run")
    - **표제어 추출 (Lemmatization):** 단어의 기본형(사전형)을 추출. (e.g., "is", "are", "am" -> "be")
- **불용어 처리 (Stopword Removal):** 분석에 큰 의미가 없는 단어(조사, 관사 등)를 제거. (e.g., "a", "the", "is", "은", "는")

### 3.2. 구문 분석 (Syntactic Analysis)

문장의 문법적 구조를 분석합니다.

- **품사 태깅 (Part-of-Speech, POS Tagging):** 각 단어에 해당하는 품사(명사, 동사, 형용사 등)를 태깅.
- **구문 분석 (Parsing):** 문장의 구조를 분석하여 파스 트리(Parse Tree)를 생성. 문법적 관계를 파악하는 데 사용.

### 3.3. 의미 분석 (Semantic Analysis)

단어와 문장의 의미를 분석합니다.

- **개체명 인식 (Named Entity Recognition, NER):** 텍스트에서 인명, 지명, 기관명 등 고유한 개체를 식별.
- **단어 의미 명확화 (Word Sense Disambiguation, WSD):** 문맥에 따라 단어의 중의적인 의미를 구분.
- **감성 분석 (Sentiment Analysis):** 텍스트에 나타난 감정(긍정, 부정, 중립)을 분석.

### 3.4. 주요 응용 기술

- **기계 번역 (Machine Translation):** 한 언어를 다른 언어로 자동 번역.
- **텍스트 요약 (Text Summarization):** 긴 문서의 핵심 내용을 간결하게 요약.
- **질의응답 (Question Answering, QA):** 사용자의 질문에 대해 텍스트에서 정답을 찾아 제공.
- **챗봇 및 대화형 AI (Chatbots & Conversational AI):** 사용자와 자연어로 대화하는 시스템.

---

## 4. 주요 모델 및 아키텍처

- **[[Bag-of-Words|Bag-of-Words (BoW)]]:** 단어의 순서를 무시하고 출현 빈도만으로 텍스트를 표현.
- **[[TF-IDF]]:** 단어의 중요도를 평가하는 통계적 가중치.
- **Word Embedding:**
    - **[[Word2Vec|Word2Vec]], [[GloVe|GloVe]]:** 단어를 저차원 벡터 공간에 표현하여 의미적 유사성을 포착.
- **[[RNN|순환 신경망 (RNN)]]:** 순차적인 데이터 처리에 강점을 가짐.
    - **[[LSTM|LSTM (Long Short-Term Memory)]], [[GRU|GRU (Gated Recurrent Unit)]]:** 장기 의존성 문제를 해결한 RNN 변형 모델.
- **[[30_Architectures/Backbones/Transformer|트랜스포머 (Transformer)]]:** 어텐션 메커니즘을 사용하여 병렬 처리를 가능하게 하고, NLP의 성능을 크게 향상시킴.
    - **[[../../../30_Architectures/LanguageModels/BERT|BERT (Bidirectional Encoder Representations from Transformers)]]:** 양방향 문맥을 이해하는 사전 훈련 모델.
    - **[[../../../30_Architectures/LanguageModels/GPT|GPT (Generative Pre-trained Transformer)]]:** 대규모 텍스트 생성에 뛰어난 성능을 보이는 사전 훈련 모델.

---

## 5. 자연어 처리의 응용 분야

- **검색 엔진:** 사용자 쿼리의 의도를 파악하여 더 정확한 검색 결과를 제공.
- **소셜 미디어 분석:** 여론 분석, 트렌드 파악, 마케팅에 활용.
- **의료:** 의료 기록 분석, 진단 보조, 논문 검색.
- **금융:** 뉴스 분석을 통한 시장 예측, 사기 탐지.
- **법률:** 법률 문서 분석, 판례 검색, 계약서 검토.

---

## 6. 자연어 처리의 과제

- **언어의 모호성:** 중의성, 비유, 반어법 등 문맥에 따라 의미가 달라지는 문제.
- **데이터 부족 문제:** 특정 언어나 도메인에 대한 학습 데이터가 부족.
- **편향성:** 학습 데이터에 존재하는 편견이 모델에 그대로 반영될 수 있음.
- **상식 및 추론:** 인간처럼 상식을 기반으로 추론하는 능력의 부재.

---

## 7. 미래 전망

- **대규모 언어 모델 (LLM)의 발전:** 더욱 정교하고 거대한 모델의 등장.
- **멀티모달 NLP:** 텍스트뿐만 아니라 이미지, 음성 등 다양한 양식의 데이터를 함께 처리.
- **설명 가능한 AI (XAI):** 모델의 판단 근거를 인간이 이해할 수 있도록 설명하는 기술의 중요성 증대.
- **개인화 및 윤리:** 개인 맞춤형 서비스와 함께 데이터 프라이버시 및 AI 윤리 문제가 중요한 화두가 될 것.


## 1. n-gram with rnn

## 2. word2Vec
### 2.1 dense vector
### 2.2 distributed representation

## 3. GloVe
## 4. ELMO
## 5. Seq2Seq
## 6. attention & Transformer



