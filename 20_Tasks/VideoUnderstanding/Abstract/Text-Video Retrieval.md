---
title: Text-Video Retrieval
aliases: Video Text Retrieval, Cross-Modal Video Retrieval, Text-to-Video Retrieval
tags:
  - task
topics: Video Understanding, Information Retrieval, Multimodal Learning
---
**텍스트-비디오 검색(Text-Video Retrieval)** 은 사**용자가 자연어로 입력한 질의**에 **가장 적합한 비디오 클립을 대규모 데이터베이스에서 찾아내는 기술**로 현대의 검색 엔진과 디지털 자산 관리 분야에서 핵심적인 역할을 수행하고 있습니다.

이 기술은 전통적으로 **비디오의 시각적 특징과 텍스트의 언어적 특징을 공통된 벡터 공간으로 투영하여 유사도를 측정하는 방식**을 취해왔으나 최근에는 **비디오의 동적인 시간 정보와 텍스트의 복잡한 문맥을 정교하게 일치**시키려는 시도가 주를 이루고 있습니다.

특히 비디오는 프레임의 연속체로서 공간적 정보뿐만 아니라 시간적 흐름에 따른 사건의 변화를 포함하기 때문에 이를 **효과적으로 요약하고 텍스트와 정렬하는 것이 이 분야의 가장 큰 기술적 도전 과제**입니다.

---

## 핵심 연구
---

가장 먼저 언급해야 할 논문은 5년 전 발표된 [CLIP4Clip: An Empirical Study of CLIP for End to End Video Clip Retrieval](https://arxiv.org/abs/2104.08860)입니다.

이 논문은 이미지-텍스트 사전 학습 모델인 CLIP을 비디오 영역으로 성공적으로 전이시킨 최초의 대중적인 연구로 **비디오의 프레임별 특징을 어떻게 집합(Similarity Calculator)하여 텍스트와 비교할지에 대한 표준적인 프레임워크를 제시**했습니다. 이후 등장한 대다수의 검색 모델이 이 논문에서 제안한 구조를 기본 베이스라인으로 삼고 있습니다.

또한 약 4년 전의 [VideoCLIP: Contrastive Pre-training for Zero-shot Video-Text Understanding](https://arxiv.org/abs/2109.14084)은 **비디오와 텍스트의 정렬을 제로샷(Zero-shot) 관점에서 재해석**하며 **레이블이 없는 대규모 비디오 데이터에서 일반화된 이해력**을 확보하는 방법론을 정립했습니다.

이어서 약 4년 전 발표된 [UMT: Unified Multi-modal Transformers for Joint Video Moment Retrieval and Highlight Detection](https://arxiv.org/abs/2203.12745)은 단순한 검색을 넘어 **비디오 내의 특정 순간을 포착하고 하이라이트를 감지**하는 통합된 **트랜스포머 구조를 제안**하여 미세 단위 검색의 기틀을 마련했습니다.

최근의 거대 모델 트렌드를 주도하는 핵심 연구로는 약 1년 전의 [InternVideo2: Scaling Foundation Models for Multimodal Video Understanding](https://arxiv.org/abs/2403.15377)을 꼽을 수 있습니다. 이 논문은 비디오 기초 모델(Video Foundation Model)의 규모를 확장하여 **검색뿐만 아니라 대화, 인식 등 다양한 태스크에서 압도적인 성능을 증명하며 현재의 '비디오-언어 통합 모델' 시대**를 열었습니다.

마지막으로 9개월 전의 [VideoChat-R1: Enhancing Spatio-Temporal Perception via Reinforcement Fine-Tuning](https://arxiv.org/abs/2504.06958)은 **검색 시스템에 사고(Reasoning)와 강화 학습을 결합하여 모델이 비디오의 복잡한 인과 관계를 이해**하도록 만든 최첨단 연구로 평가받습니다.

| Paper | Key Contribution | Publication Date |
| :--- | :--- | :--- |
| [CLIP4Clip: An Empirical Study of CLIP for End to End Video Clip Retrieval](https://arxiv.org/abs/2104.08860) | CLIP을 비디오 검색의 표준 프레임워크로 정착시킨 이정표적인 연구입니다. | 5 years ago |
| [InternVideo2: Scaling Foundation Models for Multimodal Video Understanding](https://arxiv.org/abs/2403.15377) | 비디오 전용 거대 기초 모델의 가능성을 제시하고 SOTA 성능을 달성했습니다. | a year ago |
| [VideoChat-R1: Enhancing Spatio-Temporal Perception via Reinforcement Fine-Tuning](https://arxiv.org/abs/2504.06958) | 강화 학습을 통해 비디오 내 복잡한 시공간적 추론 능력을 극대화했습니다. | 9 months ago |
| [VideoCLIP: Contrastive Pre-training for Zero-shot Video-Text Understanding](https://arxiv.org/abs/2109.14084) | 대규모 데이터셋 기반의 제로샷 비디오 이해를 위한 사전 학습 기법을 확립했습니다. | 4 years ago |
| [UMT: Unified Multi-modal Transformers for Joint Video Moment Retrieval and Highlight Detection](https://arxiv.org/abs/2203.12745) | 모먼트 검색과 하이라이트 감지를 동시에 수행하는 통합 트랜스포머 모델입니다. | 4 years ago |

---

## 연구 동향
---


지난 3년간의 연구 동향을 살펴보면 가장 두드러진 변화는 **거대 멀티모달 모델(MLLM)을 검색 파이프라인에 적극적으로 통합**하려는 시도입니다.

약 1년 전에 발표된 [InternVideo2.5: Empowering Video MLLMs with Long and Rich Context Modeling](https://arxiv.org/abs/2501.12386)은 긴 비디오와 풍부한 문맥을 처리하기 위해 모델의 수용력을 확장하는 방향을 제시했으며 이를 통해 단순한 키워드 매칭을 넘어선 고차원의 비디오 이해를 가능케 했습니다. 또한 약 9개월 전 등장한 [VideoChat-R1: Enhancing Spatio-Temporal Perception via Reinforcement Fine-Tuning](https://arxiv.org/abs/2504.06958)은 강화 학습 기법을 도입하여 모델이 비디오의 시공간적 관계를 더 정확하게 인식하도록 훈련시킴으로써 검색 성능을 한 단계 끌어올렸습니다.

두 번째 주요 흐름은 **긴 비디오에서의 효율적인 정보 추출과 장기 기억 메커니즘**의 도입입니다.

약 2년 전 제안된 [MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding](https://arxiv.org/abs/2404.05726)은 메모리 증강 구조를 통해 긴 비디오의 맥락을 유지하면서도 필요한 정보를 선별적으로 활용하는 방안을 탐구했습니다. 이와 더불어 약 2년 전의 [VideoAgent: A Memory-augmented Multimodal Agent for Video Understanding](https://arxiv.org/abs/2403.11481) 연구는 여러 기초 모델을 통합된 메모리 메커니즘으로 연결하여 복잡한 비디오 시퀀스 내에서 추론 기반의 검색을 수행하는 에이전트 방식을 선보였습니다.

세 번째로는 검색 속도와 정확도 사이의 효율적 균형을 찾기 위한 지연 상호작용(Late Interaction) 및 어댑터 기반 기술의 발전입니다. 약 10개월 전 발표된 [Video-ColBERT: Contextualized Late Interaction for Text-to-Video Retrieval](https://arxiv.org/abs/2503.19009)은 텍스트 검색의 성공적인 사례인 ColBERT를 비디오 영역으로 확장하여 세밀한 토큰 수준의 정렬을 가능케 함과 동시에 대규모 데이터셋에서의 검색 효율성을 확보하고자 했습니다. 또한 약 9개월 전의 [REEF: Relevance-Aware and Efficient LLM Adapter for Video Understanding](https://arxiv.org/abs/2504.05491)은 기존의 거대 언어 모델을 비디오 검색 태스크에 효율적으로 적응시키기 위한 어댑터 구조를 제안하여 연산 비용을 줄이면서도 관련성 높은 결과를 도출하는 데 집중했습니다.

마지막으로 비디오 내의 구**체적인 시점을 식별하는 시간적 그라운딩(Temporal Grounding) 기능의 강화**가 눈에 띕니다.

약 10개월 전의 [Time-R1: Post-Training Large Vision Language Model for Temporal Video Grounding](https://arxiv.org/abs/2503.13377)은 사후 학습을 통해 모델이 비디오의 시간적 범위를 더 정밀하게 특정하도록 개선했습니다. 약 1년 전의 [Grounded-VideoLLM: Sharpening Fine-grained Temporal Grounding in Video Large Language Models](https://arxiv.org/abs/2410.03290) 역시 비디오 거대 모델이 겪는 세밀한 시간 식별 오류를 줄이기 위한 고도화된 정렬 기법을 적용하여 사용자가 원하는 정확한 장면을 찾아주는 능력을 비약적으로 향상시켰습니다.

| Paper | Description | Publication Date |
| :--- | :--- | :--- |
| [InternVideo2.5: Empowering Video MLLMs with Long and Rich Context Modeling](https://arxiv.org/abs/2501.12386) | 긴 비디오 문맥 모델링을 통해 비디오 MLLM 성능을 개선한 연구입니다. | a year ago |
| [VideoChat-R1: Enhancing Spatio-Temporal Perception via Reinforcement Fine-Tuning](https://arxiv.org/abs/2504.06958) | 강화 학습을 활용하여 비디오 모델의 시공간적 지각 능력을 강화했습니다. | 9 months ago |
| [Video-ColBERT: Contextualized Late Interaction for Text-to-Video Retrieval](https://arxiv.org/abs/2503.19009) | 토큰 수준의 지연 상호작용을 통해 정밀하고 빠른 비디오 검색을 구현했습니다. | 10 months ago |
| [Time-R1: Post-Training Large Vision Language Model for Temporal Video Grounding](https://arxiv.org/abs/2503.13377) | 사후 학습을 통해 특정 비디오 구간을 찾는 시간적 그라운딩 성능을 높였습니다. | 10 months ago |
| [MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding](https://arxiv.org/abs/2404.05726) | 메모리 메커니즘을 도입하여 긴 비디오의 정보를 효과적으로 유지하고 처리합니다. | 2 years ago |
| [Grounded-VideoLLM: Sharpening Fine-grained Temporal Grounding in Video Large Language Models](https://arxiv.org/abs/2410.03290) | 비디오 LLM의 세밀한 시간적 정렬 및 그라운딩 능력을 개선했습니다. | a year ago |
| [Text Is MASS: Modeling as Stochastic Embedding for Text-Video Retrieval](https://arxiv.org/abs/2403.17998) | 텍스트를 확률적 임베딩으로 모델링하여 검색의 불확실성을 해결하려 했습니다. | 2 years ago |
| [REEF: Relevance-Aware and Efficient LLM Adapter for Video Understanding](https://arxiv.org/abs/2504.05491) | 관련성을 고려한 효율적인 어댑터를 통해 비디오 이해 모델을 최적화했습니다. | 9 months ago |

---
