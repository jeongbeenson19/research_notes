---
title: Dense Video Captioning
aliases:
tags:
  - task
  - video
  - captioning
  - dense
topics:
  - Video Understanding
---
**Dense Video Captioning (DVC)** 은 긴 비디오 내에서 발생하는 여러 개의 이벤트를 시간적으로 탐지(**Event Localization**)함과 동시에, 각 이벤트에 대한 자연어 설명(**Captioning**)을 생성하는 기술입니다.
단순히 전체 비디오에 대해 하나의 문장을 생성하는 일반적인 비디오 캡셔닝과 달리, 비디오의 세부적인 시간적 구조를 이해해야 하는 훨씬 복잡한 작업입니다.

### Dense Video Captioning의 핵심 구성 요소

DVC는 전통적으로 다음과 같은 단계로 구성됩니다:
1.  **비디오 특징 추출 (Video Feature Extraction)**: 비디오 프레임들로부터 시공간적 정보를 담은 벡터(주로 C3D, I3D, VideoCLIP 등 사용)를 추출합니다.
2.  **이벤트 제안 (Event Proposal Generation)**: 비디오 내에서 의미 있는 시작점과 끝점을 찾아 후보 구간들을 생성합니다.
3.  **캡션 생성 (Caption Generation)**: 탐지된 각 구간에 대해 상황을 묘사하는 문장을 생성합니다.
4.  **글로벌 컨텍스트 활용**: 개별 이벤트뿐만 아니라 비디오 전체의 맥락을 고려하여 일관성 있는 서사를 만듭니다.

---

### 주요 연구 및 최신 기술 동향

DVC 연구는 초기의 분리된 2단계 방식에서 최근의 통합적이고 거대 모델을 활용하는 방식으로 진화하고 있습니다.

*   **2단계(Two-stage)에서 1단계(End-to-End)로의 전환**: 초기에는 이벤트 탐지와 캡셔닝을 별개 모델로 처리했으나(예: Krishna et al., 2017), 최근에는 두 작업을 동시에 최적화하는 End-to-End 방식이 주류를 이루고 있습니다.
*   **Transformer 기반 시공간 모델링**: Transformer 아키텍처를 도입하여 비디오의 긴 시간적 의존성을 효과적으로 학습하며, 이를 통해 이벤트 간의 관계와 문맥적 흐름을 더 잘 파악하게 되었습니다.
*   **MLLM(멀티모달 대규모 언어 모델)의 도입**: GPT-4V나 LLaVA와 같은 거대 모델을 비디오 이해에 접목하고 있습니다. 이는 풍부한 언어적 사전 지식을 활용해 훨씬 정교하고 상세한 캡션을 생성할 수 있게 합니다.
*   **실시간 및 스트리밍 처리**: 아주 긴 비디오(Long-form video)를 효율적으로 처리하기 위해 비디오를 한꺼번에 읽지 않고 실시간으로 처리하는 스트리밍 방식의 DVC 연구가 활발합니다.
*   **훈련이 필요 없는(Training-free) 접근법**: 대규모 사전 학습 모델의 추론 능력을 극대화하여 별도의 미세 조정 없이도 우수한 성능을 내는 파이프라인들이 등장하고 있습니다.

---

### 핵심 및 최신 관련 연구 리스트

DVC 분야의 시초가 된 연구부터 가장 최근의 SOTA(State-of-the-Art) 모델들을 정리한 리스트입니다.

| Paper | Description | Published |
| :--- | :--- | :--- |
| [Dense-Captioning Events in Videos](https://arxiv.org/abs/1705.00754) | DVC라는 개념을 처음으로 정립하고 ActivityNet Captions 데이터셋을 제안한 선구적 연구입니다. | 9 years ago |
| [Streaming Dense Video Captioning](https://arxiv.org/abs/2404.01297) | 매우 긴 비디오를 실시간으로 처리하며 상세한 캡션을 생성하는 구글의 연구입니다. | 2 years ago |
| [Wolf: Dense Video Captioning with a World Summarization Framework](https://arxiv.org/abs/2407.18908) | Mixture-of-Experts 방식을 도입하여 정확하고 풍부한 비디오 요약을 생성하는 프레임워크입니다. | a year ago |
| [AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark](https://arxiv.org/abs/2410.03051) | 효율적인 연산으로 고성능의 상세 캡셔닝을 수행하며 새로운 벤치마크를 제시했습니다. | a year ago |
| [VideoNarrator: A Training-free Approach Using Multimodal Large Language Models](https://arxiv.org/abs/2507.17050) | MLLM을 활용해 추가 학습 없이도 구조화된 비디오 서사를 생성하는 혁신적인 방식입니다. | 6 months ago |
| [Explicit Temporal-Semantic Modeling for Dense Video Captioning](https://arxiv.org/abs/2511.10134) | 시간적 정보와 시맨틱 정보의 명시적인 결합을 통해 교차 모달 상호작용을 강화한 최신 연구입니다. | 2 months ago |
| [Time-Scaling State-Space Models for Dense Video Captioning](https://arxiv.org/abs/2509.03426) | Transformer의 한계를 넘어 State-Space Model(SSM)을 활용해 긴 비디오를 효율적으로 분할하고 설명합니다. | 5 months ago |
| [Grounded-VideoLLM: Sharpening Fine-grained Temporal Grounding in Video LLMs](https://arxiv.org/abs/2410.03290) | 비디오 LLM 내에서 세밀한 시간적 접지(Grounding) 능력을 강화하여 DVC 성능을 높였습니다. | a year ago |

최근의 DVC는 단순한 사건 기록을 넘어 비디오 내 인과관계를 추론하고, 사용자의 질문에 답하며 이벤트를 탐지하는 **Question-Answering Dense Video Events**와 같은 융합적인 방향으로 확장되고 있습니다. 이러한 흐름은 자율주행, 보안 감시, 그리고 자동 영상 편집 등 다양한 산업 분야에 혁신을 가져오고 있습니다.