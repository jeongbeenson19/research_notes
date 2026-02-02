---
title: Video Summarization
aliases:
tags:
  - task
  - video
  - summarization
topics:
  - Video Understanding
---
**Video Summarization(비디오 요약)** 은 긴 원본 비디오의 핵심 내용을 유지하면서 시청자가 짧은 시간 안에 전체 내용을 파악할 수 있도록 압축된 버전을 생성하는 기술입니다. 단순히 흥미로운 장면을 찾는 Highlight Detection과 달리, 비디오 전체의 **서사 구조(Narrative Structure)** 와 **포괄성(Representativeness)** 을 유지하는 것이 목표입니다.

---

## 1. 핵심 개념 및 정의

### 1.1 작업 정의
긴 비디오 $V$가 주어졌을 때, 요약본 $S$를 생성합니다. $S$는 원본의 아주 일부분($10\sim15\%$)이지만, 전체의 의미를 충분히 전달해야 합니다.

### 1.2 요약의 형태
- **Static Summarization (Keyframes)**: 비디오를 대표하는 몇 장의 정지 이미지(Keyframes) 세트를 추출합니다. (Storyboard 방식)
- **Dynamic Summarization (Video Skimming)**: 의미 있는 짧은 비디오 클립들을 연결하여 짧은 요약 영상을 만듭니다. (Trailer 방식)

### 1.3 핵심 목표
- **Representativeness (대표성)**: 요약본이 원본 비디오의 모든 주요 사건을 포함해야 함.
- **Diversity (다양성)**: 요약본 내에 중복되거나 유사한 내용이 없어야 함.
- **Coherence (일관성)**: 요약된 클립들 간의 흐름이 자연스럽고 논리적이어야 함.

---

## 2. 아키텍처 및 핵심 모듈

### 2.1 전체 파이프라인
```
비디오 분할(Shot/Scene Segmentation) → 특징 추출 → 중요도/점수 산출 → 세그먼트 선택(Subset Selection) → 요약본 생성
```

### 2.2 비디오 분할 (Segmentation)
비디오를 처리 가능한 최소 단위로 나눕니다.
- **Shot Segmentation**: 카메라 앵글이 바뀌는 지점을 기준으로 분할.
- **Scene Segmentation**: 장소나 시간이 바뀌는 논리적 단위로 분할.
- **Fixed-length Segmentation**: 일정 시간(예: 2초) 단위로 기계적 분할.

### 2.3 특징 추출 (Feature Extraction)
- **Visual**: ResNet, I3D, VideoMAE 등을 통해 공간/시간적 특징 추출.
- **Audio**: 환호성, 음악 변화, 음성 정보(ASR) 활용.
- **Semantic**: CLIP 등을 활용해 텍스트(질의)와의 관계성 추출.

### 2.4 중요도 산출 및 시간적 모델링
- **RNN/LSTM**: 비디오의 순차적 흐름을 모델링하여 각 프레임의 중요도 점수를 매깁니다.
- **Self-Attention (Transformer)**: 프레임 간의 전역적 관계를 파악하여 어떤 장면이 비디오 전체에서 독보적인지 계산합니다.
- **Graph Modeling**: 비디오 세그먼트를 노드로 연결하여 중심도가 높은(중요한) 노드를 식별합니다.

---

## 3. 요약 기술 및 방법론

### 3.1 지도 학습 (Supervised)
사람이 직접 만든 요약본을 정답(Ground Truth)으로 사용합니다.
- **Sequence-to-Sequence**: 원본 시퀀스를 입력받아 중요도 점수 시퀀스를 출력.
- **Regression**: 각 프레임이 요약본에 포함될 확률을 회귀 모델로 학습.

### 3.2 비지도 학습 (Unsupervised) - 주류 연구
정답 데이터 없이 "좋은 요약"의 기준을 모델링합니다.
- **GAN (Generative Adversarial Networks)**: 요약본으로부터 원본을 복원할 수 있는지(대표성), 요약본이 얼마나 다양한지(다양성)를 판별자와 경쟁하며 학습.
- **Reinforcement Learning (RL)**: 대표성, 다양성, 가독성 등을 보상(Reward)으로 설정하여 에이전트가 최적의 프레임을 선택하도록 학습.
- **Reconstruction Error**: 요약본의 특징값들로 원본 비디오 전체를 얼마나 잘 재구성할 수 있는지 측정.

### 3.3 약지도 및 웹 기반 학습 (Weakly-supervised)
- **Web-guided**: 유튜브 등에서 검색된 유사한 주제의 비디오들을 참고하여 공통적으로 나타나는 중요 장면을 학습.
- **Title-guided**: 비디오 제목이나 설명글을 기반으로 관련성 높은 장면 추출.

---

## 4. 최신 연구 동향 (2024-2026)

*   **VLM/LLM 통합**: 단순히 시각적 특징만 보는 게 아니라, "이 장면이 왜 중요한가?"를 언어적으로 이해하여 요약합니다. LLM을 활용해 비디오의 시나리오를 분석하고 요약하는 연구가 활발합니다.
*   **Query-Focused Summarization**: 사용자가 "이 비디오에서 요리 과정만 요약해줘"라고 요청하면 그에 맞춰 요약본을 생성하는 맞춤형 요약입니다.
*   **Long Video Processing**: 수 시간 분량의 비디오를 메모리 효율적으로 요약하기 위해 계층적(Hierarchical) 구조나 State Space Model(Mamba 등)을 도입하고 있습니다.
*   **Narrative & Storytelling**: 조각난 클립들을 단순히 붙이는 게 아니라, 기승전결이 있는 한 편의 이야기처럼 구성하는 기술이 주목받고 있습니다.

---

## 5. 핵심 연구 및 최신 논문 리스트

| Paper | Description | Published |
| :--- | :--- | :--- |
| [Video Summarization Techniques: A Comprehensive Review](https://arxiv.org/abs/2410.04449) | 최신 비디오 요약 기술과 벤치마크, 도전 과제를 총망라한 종합 서베이 논문입니다. | a year ago |
| [Video Summarization with Large Language Models](https://arxiv.org/abs/2504.11199) | LLM을 활용하여 비디오의 의미적 맥락을 파악하고 정교한 요약을 생성하는 최신 연구입니다. | 9 months ago |
| [Your Interest, Your Summaries: Query-Focused Long Video Summarization](https://arxiv.org/abs/2410.14087) | 사용자의 질의에 따라 긴 비디오를 맞춤형으로 요약하는 기술을 제안합니다. | a year ago |
| [From Long Videos to Engaging Clips: Multimodal Narrative Understanding](https://arxiv.org/abs/2507.02790) | 인간의 편집 방식에서 영감을 얻어 서사적 구조를 유지하며 요약 클립을 만드는 프레임워크입니다. | 7 months ago |
| [A Survey on Generative AI and LLM for Video Generation and Understanding](https://arxiv.org/abs/2404.16038) | 생성형 AI와 LLM이 비디오 요약 및 스트리밍 기술을 어떻게 변화시키고 있는지 분석합니다. | 2 years ago |
| [QVHighlights: Detecting Moments and Highlights in Videos](https://arxiv.org/abs/2107.09609) | 질의 기반 모멘트 탐지와 하이라이트 예측을 결합하여 요약의 품질을 높이는 기초 연구입니다. | 4 years ago |
| [UMT: Unified Multi-modal Transformers for Video Understanding](https://arxiv.org/abs/2203.12745) | 멀티모달 트랜스포머를 통해 비디오의 핵심 지점을 찾아내는 통합 모델입니다. | 4 years ago |

---

## 6. 기술적 핵심 모듈 상세

1.  **Saliency Scoring Module**: 각 세그먼트의 중요도를 0~1 사이로 예측.
2.  **Redundancy Elimination**: 유사한 장면이 중복 선택되지 않도록 조절 (Determinantal Point Processes, DPP 활용).
3.  **Knapsack Optimizer**: 정해진 요약본 길이(제약 조건) 내에서 총 중요도 점수를 최대화하는 최적화 알고리즘.
4.  **Temporal Aggregation**: 긴 시간 동안의 흐름을 파악하기 위해 다중 스케일(Multi-scale)로 정보를 취합하는 모듈.

비디오 요약은 대량의 영상 콘텐츠를 소비해야 하는 현대 사회에서 정보 탐색 비용을 줄여주는 핵심 기술입니다. 최근에는 **개인화(Personalization)** 와 **생성형 AI(Generative AI)** 의 결합으로 인해, 사용자가 원하는 스타일로 비디오를 요약하거나 새로운 설명을 덧붙이는 방향으로 빠르게 진화하고 있습니다.