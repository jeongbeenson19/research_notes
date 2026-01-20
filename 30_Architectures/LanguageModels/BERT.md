# BERT (Bidirectional Encoder Representations from Transformers)
#NLP #LLM #Transformer

---

## 1. 개요

**BERT(Bidirectional Encoder Representations from Transformers)**는 2018년 구글에서 발표한 혁신적인 언어 표현 모델입니다. 이름 그대로, [[../Backbones/Transformer|Transformer]]의 **인코더(Encoder)** 구조를 사용하여 문장의 **양방향(Bidirectional)** 문맥을 동시에 학습하는 것이 핵심입니다.

BERT의 등장은 기존의 단방향(unidirectional) 언어 모델(e.g., [[GPT|GPT]])이 가진 한계를 극복하고, 자연어 이해(NLU) 분야의 성능을 전반적으로 크게 향상시키는 계기가 되었습니다.

---

## 2. 핵심 아이디어: 양방향 문맥 학습

기존의 언어 모델들은 문장을 왼쪽에서 오른쪽으로 순차적으로 읽거나(GPT), 왼쪽-오른쪽과 오른쪽-왼쪽 모델을 각각 훈련하여 얕게 결합하는 방식을 사용했습니다.

반면, BERT는 **"마스크 언어 모델(Masked Language Model, MLM)"** 이라는 새로운 사전 학습 목표를 통해 문장 전체를 한 번에 보고 깊은 양방향 문맥을 학습합니다.

### 2.1. 사전 학습(Pre-training) 목표

BERT는 두 가지 비지도 학습 작업을 동시에 수행합니다.

1.  **마스크 언어 모델 (Masked Language Model, MLM):**
    - 입력 문장에서 일부 단어를 무작위로 `[MASK]` 토큰으로 바꿉니다.
    - 모델은 `[MASK]` 토큰에 들어갈 원래 단어가 무엇인지 주변 문맥 전체를 이용하여 예측하도록 학습됩니다.
    - 이를 통해 모델은 단어의 의미를 파악하기 위해 좌우 양쪽의 문맥을 모두 고려하는 능력을 기르게 됩니다.

2.  **다음 문장 예측 (Next Sentence Prediction, NSP):**
    - 두 개의 문장 A, B를 주고, 문장 B가 문장 A의 바로 다음 문장인지(IsNext) 아닌지(NotNext)를 예측하도록 학습합니다.
    - 이를 통해 모델은 문장 간의 관계를 이해하는 능력을 학습하며, 질의응답(QA)이나 자연어 추론(NLI)과 같은 작업에 도움을 줍니다.

---

## 3. 아키텍처: Transformer 인코더

BERT는 [[../Backbones/Transformer|Transformer]] 아키텍처에서 **인코더 스택**만을 사용합니다. 이는 문장의 모든 단어 위치에서 전체 시퀀스를 참조하여 각 단어에 대한 깊은 문맥적 표현(representation)을 생성하는 데 이상적입니다.

- **BERT-Base:** 12개의 인코더 레이어, 1억 1천만 개의 파라미터
- **BERT-Large:** 24개의 인코더 레이어, 3억 4천만 개의 파라미터

---

## 4. 미세 조정 (Fine-tuning)

사전 학습된 BERT 모델은 다양한 다운스트림 NLP 작업에 맞게 **미세 조정(Fine-tuning)**될 수 있습니다. 사전 학습을 통해 얻은 풍부한 언어 표현 위에 작업별로 특화된 간단한 분류 레이어를 추가하여 훈련하는 방식입니다.

- **분류 작업:** 문장 감성 분석, 스팸 메일 분류 등
- **질의응답:** 질문과 문단을 입력받아 정답의 위치를 예측
- **개체명 인식 (NER):** 각 단어가 인명, 지명 등 어떤 개체에 속하는지 분류

---

## 5. 의의 및 영향

- **NLU 성능의 새로운 기준 제시:** BERT는 GLUE, SQuAD 등 11개의 NLP 벤치마크에서 최고 성능(SOTA)을 달성하며 자연어 이해 능력의 새로운 기준을 세웠습니다.
- **전이 학습의 보편화:** 대규모 데이터로 사전 학습한 모델을 특정 작업에 미세 조정하는 '사전 학습-미세 조정' 패러다임을 NLP 분야의 표준으로 만들었습니다.
- **다양한 후속 모델:** RoBERTa, ALBERT, ELECTRA 등 BERT의 아이디어를 개선하고 발전시킨 수많은 후속 모델의 등장을 이끌었습니다.

---

## 6. 관련 노트

- **기반 아키텍처**: [[../Backbones/Transformer|Transformer]], [[../../40_Papers/Attention Is All You Need|Attention Is All You Need]]
- **비교 모델**: [[GPT|GPT]]
