---
title: Video Captioning
aliases:
tags:
  - task
  - video
  - captioning
  - nlp
topics:
  - Video Understanding
  - Natural Language Processing
---
비디오 캡셔닝(Video Captioning)은 **비디오의 내용을 이해하고 이를 자연어 문장으로 설명**하는 기술입니다. 단순히 정지된 이미지를 설명하는 이미지 캡셔닝(Image Captioning)에서 나아가, 시**간적 변화(Temporal dynamics)와 객체 간의 상호작용을 포착**해야 하는 복합적인 컴퓨터 비전 및 자연어 처리 작업입니다.

최근의 비디오 캡셔닝 연구는 크게 두 가지 방향으로 진화하고 있습니다.

첫째는 대규모 멀티모달 모델(MLLM)을 활용하여 비디오에 대한 깊은 추론 능력을 결합하는 것이며, 둘째는 긴 비디오에서 여러 사건을 시간대별로 묘사하는 댄스 비디오 캡셔닝(Dense Video Captioning)의 효율성을 높이는 것입니다. 특히 최근 며칠 사이에도 비디오 이해와 그라운딩 능력을 갖춘 오픈 소스 모델들이 발표되는 등 기술 발전이 매우 빠르게 이루어지고 있습니다.

주요 기술적 흐름은 다음과 같습니다.

- **비디오 추론 및 구조화된 사고**: 단순히 본 것을 묘사하는 단계를 넘어, 강화학습(RL)이나 Chain-of-Thought(CoT) 기법을 도입해 비디오 속 사건의 인과관계나 의도를 논리적으로 추론하여 캡션을 생성하려는 시도가 늘고 있습니다.
- **긴 비디오 이해(Long-form Video Understanding)**: 수 초 분량의 짧은 클립을 넘어 분 단위 이상의 긴 영상에서 일관된 맥락을 유지하며 설명을 생성하는 것이 주요 도전 과제입니다. 이를 위해 메모리 증강(Memory-augmented) 구조나 효율적인 프레임 선택 기법이 연구되고 있습니다.
- **멀티모달 통합**: 시각 정보뿐만 아니라 오디오 정보를 함께 활용하여 더욱 풍부한 설명을 생성하거나, 특정 객체를 텍스트와 연결하는 비디오 그라운딩(Video Grounding) 기술과의 결합이 활발합니다.

---

## 핵심 연구
---
비디오 캡셔닝 분야에서 기술적 패러다임을 전환하거나 현재의 표준을 정립한 핵심 논문들을 선정해 드립니다. 이 논문들은 초기 딥러닝 기반 모델부터 최신 대규모 멀티모달 모델(MLLM)에 이르기까지 비디오 이해 기술의 진화 과정을 보여줍니다.

비디오 캡셔닝의 역사는 2015년 제안된 **Sequence to Sequence -- Video to Text**를 통해 **비디오를 프레임의 시퀀스로, 캡션을 단어의 시퀀스로 처리**하는 **인코더-디코더** 구조가 정착되면서 본격적으로 시작되었습니다.

이후 **Transformer의 등장과 함께 비디오의 공간적, 시간적 특징을 동시에 학습하는 효율적인 구조들이 연구**되었으며 특히 **SwinBERT**는 오프라인에서 추출된 특징 대신 비디오 프레임을 직접 입력으로 사용하는 엔드투엔드 Transformer 모델로서 큰 성과를 거두었습니다.

최근에는 **CLIP4Clip**과 같이 강력한 사전 학습 모델인 CLIP을 비디오 영역으로 확장하여 언어와 시각 정보를 정렬하는 방식이 표준으로 자리 잡았으며 **VideoChat**과 같은 모델들은 비디오 이해를 단순한 묘사를 넘어 대화형 시스템으로 진화시켰습니다.

가장 최신 트렌드는 **InternVideo2.5**나 **Molmo2**처럼 아주 긴 비디오 맥락을 이해하거나 비디오 내의 객체를 정확히 찾아내어 설명하는 그라운딩 능력을 갖춘 거대 멀티모달 모델들이 주도하고 있습니다.

| Paper | Description | Published |
| :--- | :--- | :--- |
| [Sequence to Sequence -- Video to Text](https://arxiv.org/abs/1505.00487) | 비디오 캡셔닝에 LSTM 기반의 인코더-디코더 구조를 최초로 도입한 기초적인 논문입니다. | 11 years ago |
| [CLIP4Clip: An Empirical Study of CLIP for End to End Video Clip Retrieval](https://arxiv.org/abs/2104.08860) | 이미지-텍스트 사전 학습 모델인 CLIP을 비디오 분야에 성공적으로 전이시킨 핵심 연구입니다. | 5 years ago |
| [SwinBERT: End-to-End Transformers with Sparse Attention for Video Captioning](https://arxiv.org/abs/2111.13196) | 비디오 Transformer를 사용하여 특징 추출과 캡션 생성을 통합한 엔드투엔드 모델입니다. | 4 years ago |
| [VideoChat: Chat-Centric Video Understanding](https://arxiv.org/abs/2305.06355) | 대규모 언어 모델(LLM)을 비디오 모델과 결합하여 대화형 비디오 이해를 가능하게 한 선구적 모델입니다. | 2 years ago |
| [Streaming Dense Video Captioning](https://arxiv.org/abs/2404.01297) | 긴 비디오를 스트리밍 방식으로 처리하며 세부 사건들을 실시간으로 묘사하는 기술을 제안합니다. | 2 years ago |
| [InternVideo2.5: Empowering Video MLLMs with Long and Rich Context Modeling](https://arxiv.org/abs/2501.12386) | 방대한 데이터를 바탕으로 매우 긴 비디오의 맥락을 완벽하게 파악하는 최신 거대 비디오 모델입니다. | a year ago |
| [Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding](https://arxiv.org/abs/2601.10611) | 비디오 내 객체 그라운딩과 이해 능력이 탁월한 최신 오픈 소스 SOTA 모델입니다. | 4 days ago |
| [VideoCap-R1: Enhancing MLLMs for Video Captioning via Structured Thinking](https://arxiv.org/abs/2506.01725) | 강화학습과 구조적 사고를 통해 비디오의 복합적인 상황을 논리적으로 설명하는 모델입니다. | 8 months ago |

---

## 연구 동향
---
지난 3년 동안 비디오 캡셔닝 분야는 단순한 '장면 묘사'에서 **'복합적 추론과 맥락 이해'** 로 그 패러다임이 완전히 변화했습니다.

2023년에는 ChatGPT와 같은 거대 언어 모델(LLM)을 비디오 모델과 결합하려는 시도가 주를 이루었으며 이 과정에서 비디오의 시각적 특징을 언어 모델이 이해할 수 있는 토큰으로 변환하는 효율적인 어댑터 구조들이 대거 등장했습니다. 

특히 **VideoChat**과 같은 모델들은 비디오를 보고 대화할 수 있는 인터페이스를 제시하며 캡셔닝 기술을 대화형 시스템의 일부로 편입시켰습니다.

2024년에 접어들면서 연구의 초점은 수 초 분량의 짧은 클립을 넘어 수 분에서 수 시간 단위의 **긴 비디오를 처리**하는 쪽으로 이동했습니다.

긴 영상을 효율적으로 압축하여 기억하는 메모리 증강 메커니즘이나 스트리밍 방식으로 영상을 처리하며 주요 사건들을 실시간으로 포착해 설명하는 댄스 비디오 캡셔닝 기술들이 비약적으로 발전했습니다. 이는 자율주행이나 보안 모니터링처럼 실시간성과 긴 호흡의 이해가 필요한 실제 응용 분야에서의 활용 가능성을 크게 높였습니다.

2025년부터 현재까지는 추론(Reasoning)과 그라운딩(Grounding)이 핵심 키워드가 되었습니다.

최근의 논문들은 비디오에서 단순히 **'무엇이 일어나는지'를 넘어 '왜 그런 일이 일어났는지'를 구조적으로 사고**하여 설명하는 능력을 강조합니다. 또한 생성된 캡션의 단어들이 비디오의 어느 시점, 어느 위치의 객체를 가리키는지 정확하게 연결하는 정교한 공간적-시간적 정렬 기술이 도입되었습니다. 이러한 흐름은 비디오 캡셔닝 기술이 인간의 시각적 사고 방식을 더욱 닮아가고 있음을 보여줍니다.

| Paper | Description | Published |
| :--- | :--- | :--- |
| [Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding](https://arxiv.org/abs/2601.10611) | 비디오 내 객체를 정확히 짚어내며 설명하는 그라운딩 능력과 높은 성능을 갖춘 최신 오픈 소스 모델입니다. | 4 days ago |
| [VideoCap-R1: Enhancing MLLMs for Video Captioning via Structured Thinking](https://arxiv.org/abs/2506.01725) | 강화학습을 통해 비디오 속 복합적인 상황을 논리적으로 추론하고 설명하는 구조적 사고 기능을 도입했습니다. | 8 months ago |
| [InternVideo2.5: Empowering Video MLLMs with Long and Rich Context Modeling](https://arxiv.org/abs/2501.12386) | 100만 토큰 이상의 긴 컨텍스트를 지원하여 매우 긴 영상에서도 풍부하고 정확한 설명을 생성합니다. | a year ago |
| [Streaming Dense Video Captioning](https://arxiv.org/abs/2404.01297) | 비디오를 끝까지 기다리지 않고 실시간으로 처리하며 연속된 사건들을 상세히 설명하는 효율적인 구조를 제시했습니다. | 2 years ago |
| [MA-LMM: Memory-Augmented Large Multimodal Model for Long-Term Video Understanding](https://arxiv.org/abs/2404.05726) | 과거의 시각 정보를 저장하는 메모리 메커니즘을 통해 긴 비디오의 앞뒤 맥락을 놓치지 않고 설명합니다. | 2 years ago |
| [VideoChat: Chat-Centric Video Understanding](https://arxiv.org/abs/2305.06355) | 비디오 모델과 LLM을 결합하여 캡셔닝을 넘어 대화형 비디오 이해의 기초를 닦은 핵심 연구입니다. | 2 years ago |
| [Any2Caption: Interpreting Any Condition to Caption for Controllable Video Generation](https://arxiv.org/abs/2503.24379) | 비디오 생성 시 사용자의 복합적인 의도를 정확한 캡션으로 변환하여 생성 품질을 높이는 데 기여했습니다. | 10 months ago |
| [Video-VoT-R1: An efficient video inference model integrating image packing and AoE architecture](https://arxiv.org/abs/2503.15807) | 이미지 패킹 기술과 효율적인 아키텍처를 통해 비디오 캡셔닝의 추론 속도와 정확도를 동시에 개선했습니다. | 10 months ago |

---