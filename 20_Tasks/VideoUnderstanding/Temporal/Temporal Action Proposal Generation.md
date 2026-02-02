---
title: Temporal Action Proposal Generation
aliases:
tags:
  - task
  - video
  - proposal
  - localization
topics:
  - Video Understanding
---
**Temporal Action Proposal Generation (TAPG)** 은 잘라지지 않은(Untrimmed) 긴 비디오에서 행동(Action)이 발생할 가능성이 높은 시간 구간들을 후보(Proposal)로 생성하는 작업입니다. 이는 Temporal Action Detection(TAD)의 전처리 단계로, 높은 재현율(Recall)과 정확한 경계(Boundary)를 가진 제안을 생성하는 것이 핵심입니다.

### TAPG의 핵심 개념 및 특징

1.  **Class-agnostic (클래스 무관)**: TAPG는 어떤 행동인지 분류하지 않고, 단지 "여기서 무언가 의미 있는 행동이 일어날 것 같다"는 구간만 제안합니다. 분류는 이후 단계에서 수행됩니다.
2.  **High Recall (높은 재현율)**: 가능한 한 모든 실제 행동을 포함하는 제안을 생성해야 하므로, 높은 재현율이 중요합니다. 일부 false positive는 허용되지만, false negative는 치명적입니다.
3.  **Precise Boundaries (정밀한 경계)**: 제안된 구간의 시작과 끝이 실제 행동의 경계와 최대한 일치해야 합니다. 경계가 부정확하면 후속 인식 성능이 크게 저하됩니다.
4.  **Temporal Scale Variation (시간적 스케일 변화)**: 행동은 몇 프레임에서 몇 분까지 매우 다양한 길이를 가지므로, 다중 스케일 처리가 필수적입니다.

---

### 주요 연구 및 최신 기술 동향

TAPG 기술은 초기의 슬라이딩 윈도우 방식에서 최근의 Boundary-Matching 및 Anchor-free 방식으로 진화하고 있습니다.

*   **Boundary-Matching Networks**: 행동의 시작(Start)과 끝(End)을 별도로 예측한 후 매칭하여 제안을 생성하는 방식이 주류를 이루고 있습니다. BMN(Boundary-Matching Network)이 대표적입니다.
*   **Anchor-free 접근법**: 이미지 객체 탐지에서 영감을 받아, 미리 정의된 앵커 없이도 경계를 직접 회귀(Regression)하는 방식이 도입되었습니다.
*   **Dense Boundary Generator**: 모든 프레임에서 경계일 가능성(Boundary Score)을 밀집하게 예측하고, 이를 조합하여 제안을 생성하는 방법이 연구되고 있습니다.
*   **Transformer 기반 모델링**: Self-attention을 통해 비디오의 전역적 맥락(Global Context)을 파악하고, 장거리 의존성(Long-range Dependency)을 모델링하여 정확한 제안을 생성합니다.
*   **Background Constraint**: 행동 영역과 배경 영역을 명시적으로 구분하여, 배경에서 생성되는 잘못된 제안을 억제합니다.
*   **Graph Neural Networks (GNN)**: 비디오 세그먼트 간의 관계를 그래프로 모델링하여, 시간적 문맥과 구조를 더욱 정교하게 파악합니다.
*   **Zero-shot Proposal Generation**: 보지 못한 카테고리의 행동에 대해서도 일반화된 제안을 생성할 수 있는 능력이 최근 연구 주제입니다.

---

### 핵심 연구 및 최신 논문 리스트

TAPG 분야의 토대를 마련한 초기 연구부터 최신 SOTA 모델까지를 포함한 리스트입니다.

| Paper | Description | Published |
| :--- | :--- | :--- |
| [BMN: Boundary-Matching Network for Temporal Action Proposal Generation](https://arxiv.org/abs/1907.09702) | 시작 경계와 끝 경계를 매칭하는 방식으로 정확한 제안을 생성하는 대표적인 연구입니다. | 6 years ago |
| [BSN++: Complementary Boundary Regressor with Scale-Balanced Relation Modeling](https://arxiv.org/abs/2009.07641) | BSN을 개선하여 다중 스케일 관계 모델링과 경계 회귀를 결합한 연구입니다. | 5 years ago |
| [Fast Learning of Temporal Action Proposal via Dense Boundary Generator](https://arxiv.org/abs/1911.04127) | 밀집 경계 생성기를 통해 빠르고 정확한 제안 생성을 달성한 연구입니다. | 6 years ago |
| [Temporal Action Proposal Generation with Transformers](https://arxiv.org/abs/2105.12043) | Transformer를 TAPG에 적용하여 장거리 문맥 정보를 효과적으로 활용한 연구입니다. | 5 years ago |
| [Temporal Action Proposal Generation with Background Constraint](https://arxiv.org/abs/2112.07984) | 배경 제약 조건을 도입하여 잘못된 제안을 줄이고 정확도를 향상시킨 연구입니다. | 4 years ago |
| [Boundary Content Graph Neural Network for TAPG](https://arxiv.org/abs/2008.01432) | GNN을 활용하여 경계와 콘텐츠 간의 관계를 그래프로 모델링한 연구입니다. | 5 years ago |
| [ActionFormer: Localizing Moments of Actions with Transformers](https://arxiv.org/abs/2202.07925) | Transformer 기반으로 행동 순간을 직접 탐지하는 통합 프레임워크입니다. | 3 years ago |
| [Towards Completeness: Generalizable Action Proposal Generator for Zero-Shot TAL](https://arxiv.org/abs/2408.13777) | Zero-shot 환경에서도 완전성 있는 제안을 생성할 수 있는 일반화된 모델입니다. | a year ago |
| [Learning Salient Boundary Feature for Anchor-free Temporal Action Localization](https://arxiv.org/abs/2103.13137) | Anchor-free 방식으로 경계 특징을 학습하여 정확한 제안을 생성합니다. | 5 years ago |

TAPG는 Temporal Action Detection의 성능을 결정짓는 핵심 기술입니다. 최근에는 **end-to-end 학습**을 통해 제안 생성과 분류를 동시에 최적화하는 방향으로 발전하고 있으며, **대규모 사전 학습 모델**을 활용하여 일반화 능력을 크게 향상시키고 있습니다. 특히 실시간 비디오 분석이 필요한 **보안 감시, 스포츠 분석, 자율주행** 등의 분야에서 핵심적인 역할을 하고 있습니다.