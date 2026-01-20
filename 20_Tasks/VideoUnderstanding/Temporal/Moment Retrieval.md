---
title: Moment Retrieval
aliases:
tags:
  - task
  - video
  - retrieval
  - temporal
topics:
  - Video Understanding
---
**Moment Retrieval (MR)** 또는 **Temporal Sentence Grounding in Videos (TSGV)** 는 자연어 질의(Query)가 주어졌을 때, 긴 비디오 내에서 그 질의에 의미적으로 대응하는 정확한 시간 구간(Temporal Moment)을 찾아내는 작업입니다.
예를 들어, "사람이 문을 여는 순간"이라는 질의에 대해 비디오의 특정 시작 시간과 종료 시간을 타임스탬프로 반환합니다.

### Moment Retrieval의 핵심 개념 및 특징

1.  **Cross-modal Matching (크로스 모달 정합)**: 시각적 정보(비디오)와 언어적 정보(텍스트 질의)를 공통의 임베딩 공간에 매핑하여 유사도를 계산하고, 가장 관련성이 높은 구간을 찾아냅니다.
2.  **Temporal Localization (시간적 위치 추정)**: 단순히 "관련 있다/없다"를 판단하는 것이 아니라, 정확한 시작(start)과 끝(end) 타임스탬프를 예측해야 하므로 시간적 경계를 정밀하게 파악하는 것이 핵심입니다.
3.  **Ambiguity Handling (모호성 처리)**: 하나의 질의에 대해 여러 개의 관련 모멘트가 존재할 수 있으므로, 이를 순위화(Ranking)하거나 다중 모멘트를 반환하는 것이 실용적입니다.

---

### 주요 연구 및 최신 기술 동향

Moment Retrieval 분야는 초기의 단순한 슬라이딩 윈도우 방식에서 최근의 Transformer 기반 및 대규모 멀티모달 모델을 활용한 고도화된 접근법으로 진화하고 있습니다.

*   **DETR 기반 End-to-End 학습**: Detection Transformer(DETR)의 구조를 차용하여 Moment를 '객체'처럼 탐지하는 방식이 주류를 이루고 있습니다. Query 임베딩을 통해 비디오-텍스트를 직접 정렬합니다.
*   **대규모 Vision-Language Model (VLM) 활용**: CLIP과 같은 대규모 사전 학습 모델을 기반으로 비디오와 텍스트 간의 공통 표현 학습을 강화하고, Zero-shot 성능을 향상시킵니다.
*   **Weakly-supervised 및 Point-supervised 학습**: 완전한 시간적 주석(Annotation) 없이도 학습할 수 있도록, 비디오-문장 쌍만 주어진 상태나 일부 포인트만 지정된 상태에서 학습하는 기법이 연구되고 있습니다.
*   **멀티모달 대규모 언어 모델(MLLM) 통합**: GPT나 LLaMA와 같은 LLM의 언어 이해 능력을 활용하여 복잡한 질의를 처리하고, 대화형 Moment Retrieval을 가능하게 합니다.
*   **실시간 및 온라인 검색**: 전체 비디오를 한 번에 보지 않고도 스트리밍 환경에서 실시간으로 모멘트를 찾을 수 있도록 하는 온라인 MR 연구가 활발합니다.
*   **Negative Query 처리**: "사람이 문을 닫지 않는 순간"과 같은 부정적 질의나 모호한 질의를 다루는 능력도 최근 연구 주제로 떠오르고 있습니다.

---

### 핵심 연구 및 최신 논문 리스트

Moment Retrieval 분야의 기초를 마련한 연구부터 최신 SOTA 모델까지를 포함한 리스트입니다.

| Paper | Description | Published |
| :--- | :--- | :--- |
| [Temporal Sentence Grounding in Videos: A Survey and Future Directions](https://arxiv.org/abs/2201.08071) | MR/TSGV 분야의 역사, 벤치마크, 주요 방법론을 포괄적으로 정리한 대표적인 서베이 논문입니다. | 3 years ago |
| [Time-R1: Post-Training Large Vision Language Model for Temporal Video Grounding](https://arxiv.org/abs/2503.13377) | 대규모 VLM을 사후 학습(Post-training)하여 시간적 그라운딩 성능을 크게 향상시킨 최신 연구입니다. | 10 months ago |
| [Number it: Temporal Grounding Videos like Flipping Manga](https://arxiv.org/abs/2411.10332) | 비디오를 만화책처럼 '번호 매기기' 방식으로 처리하여 직관적이고 정확한 시간적 그라운딩을 제안합니다. | a year ago |
| [Universal Video Temporal Grounding with Generative Multi-modal LLMs](https://arxiv.org/abs/2506.18883) | 생성형 MLLM을 활용하여 다양한 형태의 질의(질문, 설명 등)를 통합적으로 처리하는 범용 모델입니다. | 7 months ago |
| [Grounding-MD: Grounded Video-language Pre-training for Open-World Moment Detection](https://arxiv.org/abs/2504.14553) | 오픈 월드 환경에서 범용적으로 모멘트를 탐지할 수 있도록 사전 학습된 강력한 모델입니다. | 9 months ago |
| [LLaVA-MR: Large Language-and-Vision Assistant for Video Moment Retrieval](https://arxiv.org/abs/2411.14505) | LLaVA 아키텍처를 MR에 특화시켜 긴 비디오에서도 정확한 모멘트 검색을 가능하게 합니다. | a year ago |
| [UMT: Unified Multi-modal Transformers for Joint Video Moment Retrieval and Highlight Detection](https://arxiv.org/abs/2203.12745) | Moment Retrieval과 Highlight Detection을 동시에 수행하는 통합 Transformer 프레임워크입니다. | 4 years ago |
| [TAG: Temporal-Aware Approach for Zero-Shot Video Temporal Grounding](https://arxiv.org/abs/2508.07925) | Zero-shot 환경에서 시간적 정보를 효과적으로 활용하여 추가 학습 없이 MR을 수행합니다. | 5 months ago |
| [TimeLoc: Unified End-to-End Framework for Precise Timestamp Localization](https://arxiv.org/abs/2503.06526) | Temporal Action Detection, Moment Retrieval 등 여러 시간적 위치 추정 작업을 통합한 범용 프레임워크입니다. | 10 months ago |

Moment Retrieval 기술은 단순한 검색을 넘어, 사용자가 긴 비디오 콘텐츠를 효율적으로 소비하고 탐색할 수 있도록 돕는 **핵심 인터페이스**로 자리잡고 있습니다. 최근에는 YouTube, Netflix와 같은 플랫폼에서 "특정 장면 찾기" 기능의 기반 기술로 활용되고 있으며, **VideoLLM**의 발전과 함께 대화형 질의 응답 시스템으로 진화하고 있습니다.