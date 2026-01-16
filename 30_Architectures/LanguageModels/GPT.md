# GPT (Generative Pre-trained Transformer)
#NLP #LLM #Transformer #GenerativeModel

---

## 1. 개요

**GPT(Generative Pre-trained Transformer)**는 OpenAI에서 개발한 대규모 언어 모델(Large Language Model, LLM) 시리즈입니다. 이름에서 알 수 있듯이, [[../Backbones/Transformer|Transformer]] 아키텍처를 기반으로 하며, '생성(Generative)' 모델링 방식을 사용합니다.

GPT의 핵심 아이디어는 **비지도 사전 학습(Unsupervised Pre-training)**과 **지도 미세 조정(Supervised Fine-tuning)** 두 단계로 구성됩니다.

1.  **사전 학습:** 대규모의 레이블 없는 텍스트 데이터(책, 웹사이트 등)를 사용하여 모델이 언어의 패턴, 문법, 사실적 지식 등 광범위한 언어 능력을 학습합니다. 이 과정에서 GPT는 다음에 올 단어를 예측하는 방식으로 훈련됩니다.
2.  **미세 조정:** 특정 다운스트림 작업(예: 번역, 질의응답, 분류)에 맞게 레이블이 있는 소규모 데이터셋으로 모델을 추가 훈련하여 성능을 최적화합니다.

---

## 2. 아키텍처: Transformer 디코더

GPT는 [[../Backbones/Transformer|Transformer]]의 인코더-디코더 구조 중 **디코더(Decoder) 부분만**을 사용합니다. 이는 텍스트 생성 작업에 특화된 구조입니다.

- **자기 회귀 (Autoregressive):** GPT는 이전 시점의 단어들만을 바탕으로 다음 단어를 순차적으로 예측합니다.
- **마스크된 셀프 어텐션 (Masked Self-Attention):** 예측하려는 현재 위치 이후의 단어들을 마스킹하여, 모델이 미래의 정보를 참고하지 못하도록 합니다. 이는 텍스트를 왼쪽에서 오른쪽으로 생성하는 자연스러운 방식을 모방합니다.

---

## 3. 주요 시리즈

- **GPT-1 (2018):** 최초의 GPT 모델. 대규모 비지도 사전 학습의 가능성을 보여주었습니다.
- **GPT-2 (2019):** 모델의 크기와 학습 데이터셋을 대폭 확장하여, 별도의 미세 조정 없이도 다양한 작업을 수행하는 **제로샷(Zero-shot)** 학습 능력을 보여주어 큰 주목을 받았습니다.
- **GPT-3 (2020):** 파라미터 수를 1,750억 개까지 늘려, 몇 개의 예시만으로도 새로운 작업을 수행하는 **퓨샷(Few-shot)** 학습에서 놀라운 성능을 보였습니다.
- **InstructGPT & ChatGPT (2022):** 인간의 지시를 더 잘 따르고, 대화 형식에 최적화되도록 **인간 피드백 기반 강화학습(RLHF)** 을 도입했습니다.
- **GPT-4 (2023):** 추론 능력과 정확도를 크게 향상시켰으며, 텍스트뿐만 아니라 이미지 입력도 처리할 수 있는 **멀티모달(Multi-modal)** 능력을 갖추었습니다.

---

## 4. 의의 및 영향

GPT 시리즈의 발전은 자연어 처리 분야를 넘어 AI 전반에 큰 영향을 미쳤습니다. 특히 GPT-3 이후 '초거대 AI' 또는 '파운데이션 모델'의 시대를 열었으며, ChatGPT는 AI 기술의 대중화를 이끈 결정적인 계기가 되었습니다.

---

## 5. 관련 노트

- **기반 아키텍처**: [[../Backbones/Transformer|Transformer]]
- **관련 개념**: [[../../10_Concepts/Machine_Learning/ANN|ANN]], [[../../40_Papers/Attention Is All You Need|Attention Is All You Need]]
- **경쟁 모델**: BERT (Bidirectional Encoder Representations from Transformers)
