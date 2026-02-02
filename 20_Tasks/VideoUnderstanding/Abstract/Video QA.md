---
title: Video QA
aliases:
  - Video Question Answering
tags:
  - task
  - video
  - qa
  - nlp
topics:
  - Video Understanding
  - Natural Language Processing
---
**Video Question Answering (VideoQA)** 분야는 비디오라는 **풍부한 시각적 정보와 자연어 질문을 결합하여, 기계가 비디오의 내용을 이해하고 관련 질문에 답하는 인공지능 연구의 핵심 영역**입니다. 단순히 정적인 이미지를 분석하는 Image QA를 넘어, 비디오의 핵심 요소인 **시간적 흐름(Temporal Dynamics)과 객체 간의 인과 관계(Causal Relationships)를 파악**해야 한다는 점에서 훨씬 높은 복잡도를 가집니다.

최근의 VideoQA 연구는 대규모 언어 모델(LLM)의 강력한 추론 능력을 비디오 이해에 접목한 Video-LLM(또는 Video-LMM)을 중심으로 급격히 발전하고 있습니다. 

과거에는 고정된 프레임 피처를 추출하여 융합하는 방식이 주를 이루었다면, 현재는 비디오 프레임을 텍스트 토큰과 유사한 방식으로 인코딩하여 LLM이 직접 비디오 컨텍스트를 읽고 추론하게 만드는 방향으로 패러다임이 전환되었습니다.

특히 수 분에서 수 시간에 이르는 긴 비디오(Long-form Video)에서 핵심 사건을 찾아내고(Temporal Grounding), 이를 바탕으로 논리적인 답변을 생성하는 능력이 주요한 벤치마크 척도로 자리 잡았습니다.

비디오 이해 모델들의 성능을 측정하기 위해 EgoSchema(1인칭 시점), ActivityNet-QA(일상 행동), Video-MME(다양한 장르의 종합 평가)와 같은 고난도 데이터셋이 널리 활용되고 있습니다.

최신 연구 트렌드는 단순히 답변을 내놓는 것을 넘어, **'생각의 흐름(Chain-of-Thought)'** 기법을 적용해 비디오의 **특정 구간을 단계별로 짚어가며 추론**하거나, **강화 학습(RL)을 통해 시공간적 인지 능력을 정교화**하는 방식으로 나아가고 있습니다.

---

## 핵심 연구
---
Video Question Answering (VideoQA) 분야에서 현재의 발전을 이끌어낸 핵심 논문들은 크게 **(1) 아키텍처의 혁신**, **(2) 대규모 비디오-언어 사전 학습(VLP)**, 그리고 **(3) Video-LLM으로의 패러다임 전환**이라는 세 가지 흐름으로 나뉩니다.

초기에는 비디오 프레임을 단순히 시계열 데이터로 처리하는 데 집중했다면, 점차 **비디오와 텍스트를 공통 공간에 매핑**하는 모델들이 등장했고, 현재는 **LLM의 추론 능력을 직접 비디오에 투영**하는 방식이 주류가 되었습니다.

VideoQA 분야의 지형을 바꾼 주요 논문들을 아래와 같이 정리하였습니다.

| Paper | Publication Date | Key Contribution |
| :--- | :--- | :--- |
| [Video-ChatGPT: Towards Detailed Video Understanding via Large Vision and Language Models](https://arxiv.org/abs/2306.05424) | 2 years ago | 비디오-언어 정렬을 통해 비디오에 대한 세부적인 대화와 질의응답이 가능한 시스템의 선구적 연구 |
| [Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis](https://arxiv.org/abs/2405.21075) | 2 years ago | Video-LLM의 한계를 명확히 측정할 수 있는 최초의 대규모 다중 장르 통합 평가 벤치마크 구축 |
| [InternVideo2: Scaling Foundation Models for Multimodal Video Understanding](https://arxiv.org/abs/2403.15377) | a year ago | 비디오 인식 및 대화 분야에서 SOTA를 달성하며 대규모 비디오 파운데이션 모델의 효율적 설계 제시 |
| [MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding](https://arxiv.org/abs/2404.05726) | 2 years ago | 외부 메모리 메커니즘을 도입하여 기존 모델들이 어려워하던 장편 비디오 이해 문제 해결의 실마리 제공 |
| [VideoChat-Flash: Hierarchical Compression for Long-Context Video Modeling](https://arxiv.org/abs/2501.00574) | a year ago | 계층적 압축 기법을 통해 매우 긴 비디오 컨텍스트를 효율적으로 처리하는 방법론 제안 |
| [VideoUnderstanding with Large Language Models: A Survey](https://arxiv.org/abs/2312.17432) | 2 years ago | LLM 기반 비디오 이해 연구의 흐름을 정리하고 미래 방향성을 제시한 핵심 서베이 논문 |
| [VideoAgent: Long-form Video Understanding with Large Language Model as Agent](https://arxiv.org/abs/2403.10517) | 2 years ago | LLM을 단순 추론기가 아닌 능동적 '에이전트'로 정의하여 긴 비디오에서 정보를 탐색하고 답하게 함 |
| [PerceptionLM: Open-Access Data and Models for Detailed Visual Understanding](https://arxiv.org/abs/2504.13180) | 9 months ago | 비공개 상용 모델들에 대항하여 오픈 소스 데이터와 모델을 공개하며 연구 생태계 확장에 기여 |
| [VideoLoom: A Video Large Language Model for Joint Spatial-Temporal Understanding](https://arxiv.org/abs/2601.07290) | 7 days ago | 최근 7일 전 발표된 논문으로, 시공간적 인지를 통합하여 세밀한 로컬라이제이션 성능을 극대화함 |

이 외에도 아카이브에는 등록되지 않았으나 학계에서 거대한 영향을 끼친 **VideoBERT**(비디오 토큰화를 통한 자기지도학습 도입), **ActivityNet-QA**(대규모 행동 중심 Q&A 데이터셋), **EgoSchema**(1인칭 시점의 복잡한 추론 벤치마크) 등의 연구들이 VideoQA 분야의 근간을 이루고 있습니다. 특히 최근에는 [VideoLoom](https://arxiv.org/abs/2601.07290)이나 [Watching, Reasoning, and Searching](https://arxiv.org/abs/2601.06943)과 같이 비디오 이해를 에이전틱(Agentic)한 관점으로 접근하거나 외부 지식 검색과 결합하려는 시도들이 가장 뜨거운 연구 주제로 부상하고 있습니다.

---

## 연구 동향
---
최근 Video QA 및 비디오 이해 분야의 연구는 단순한 영상 분석을 넘어, **인공지능이 자율적으로 정보를 탐색하고 시공간적 인과 관계를 추론**하는 '**에이전틱(Agentic) 추론**'과 '**정교한 시공간 정렬**'로 진화하고 있습니다.

2026년 1월 현재 가장 최신 연구들은 비디오가 가진 정보의 한계를 극복하기 위해 **외부 웹 검색을 결합**하거나, 고정된 **프레임 샘플링 방식**에서 벗어나 **동적으로 중요한 시점을 찾아내는 기술**에 집중하고 있습니다.

특히 불과 며칠 전 발표된 연구들은 비디오 내의 객체 움직임과 시간적 변화를 물리적인 수준에서 이해하려는 시도를 보여주며, 오픈 소스 기반의 강력한 모델들을 통해 상용 모델에 의존하지 않는 독자적인 연구 생태계를 구축하고 있습니다.

이러한 흐름은 모델이 비디오의 '무엇(What)'뿐만 아니라 '언제(When)', '어디서(Where)', 그리고 '왜(Why)'라는 질문에 답할 수 있게 만드는 데 핵심적인 기여를 하고 있습니다.

최근 주목받는 주요 논문들과 그 기여점은 다음과 같습니다.

| Paper | Publication Date | Key Contribution |
| :--- | :--- | :--- |
| [Watching, Reasoning, and Searching: A Video Deep Research Benchmark on Open Web for Agentic Video Reasoning](https://arxiv.org/abs/2601.06943) | 8 days ago | 비디오 내용과 오픈 웹 검색을 결합하여 답을 찾는 에이전틱 추론 벤치마크를 제시함 |
| [VideoLoom: A Video Large Language Model for Joint Spatial-Temporal Understanding](https://arxiv.org/abs/2601.07290) | 7 days ago | 시공간적 정보를 단일 LLM 내에서 통합 처리하여 세밀한 로컬라이제이션 성능을 극대화함 |
| [Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding](https://arxiv.org/abs/2601.10611) | 4 days ago | 상용 모델 증류 없이 고품질 데이터만으로 학습된 강력한 오픈 소스 비디오-언어 모델을 공개함 |
| [Action100M: A Large-scale Video Action Dataset](https://arxiv.org/abs/2601.10592) | 4 days ago | 물리적 세계에서의 행동 이해를 돕기 위한 1억 개 규모의 대규모 비디오 액션 데이터셋 구축 |
| [STEP3-VL-10B Technical Report](https://arxiv.org/abs/2601.09668) | 5 days ago | 효율적인 크기(10B)로 최상위권의 다중 모달 지능을 구현한 오픈 소스 파운데이션 모델 보고서 |
| [Video-LMM Post-Training: A Deep Dive into Video Reasoning with Large Multimodal Models](https://arxiv.org/abs/2510.05034) | 3 months ago | 비디오 추론 능력을 극대화하기 위한 포스트 트레이닝 기법을 체계적으로 분석하고 최적화함 |
| [VTimeCoT: Thinking by Drawing for Video Temporal Grounding and Reasoning](https://arxiv.org/abs/2510.14672) | 3 months ago | 시각적인 '그리기' 개념을 도입해 비디오의 시간적 구간을 더 명확하게 짚어내는 추론 방식 제안 |
| [StreamMem: Query-Agnostic KV Cache Memory for Streaming Video Understanding](https://arxiv.org/abs/2508.15717) | 5 months ago | 스트리밍 비디오의 효율적인 이해를 위해 쿼리에 무관하게 정보를 저장하는 메모리 구조 설계 |
| [Thinking With Videos: Multimodal Tool-Augmented Reinforcement Learning for Long Video Reasoning](https://arxiv.org/abs/2508.04416) | 5 months ago | 도구 활용과 강화 학습을 결합하여 장편 비디오에서의 복잡한 논리적 추론 성능을 향상시킴 |
| [Inference-time Physics Alignment of Video Generative Models with Latent World Models](https://arxiv.org/abs/2601.10553) | 4 days ago | 추론 시점에 비디오의 물리적 일관성을 맞추는 기법을 통해 QA의 정확도를 간접적으로 높임 |

이러한 논문들은 모델이 단순히 비디오 프레임을 텍스트로 설명하는 수준을 넘어, 비디오 속의 물리 법칙을 이해하고(Inference-time Physics Alignment), 부족한 정보를 외부에서 찾아내며(Watching, Reasoning, and Searching), 장시간의 컨텍스트를 효율적으로 기억하는(StreamMem) 방향으로 Video QA 기술을 한 단계 격상시키고 있습니다. 특히 [Molmo2](https://arxiv.org/abs/2601.10611)나 [Action100M](https://arxiv.org/abs/2601.10592)과 같은 연구는 연구자들이 상용 API에 의존하지 않고도 고도화된 비디오 AI를 연구할 수 있는 중요한 토대를 마련했습니다.

---
