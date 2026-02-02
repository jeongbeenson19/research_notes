---
title: Re-Identification
aliases:
  - ReID
tags:
  - task
  - video
  - tracking
topics:
  - Video Understanding
  - Computer Vision
---
재식별(Re-identification, Re-ID)은 **서로 다른 시간이나 장소,** 혹은 **겹치지 않는 시야를 가진 여러 카메라**에서 **포착된 객체가 동일한 대상인지를 판별**하는 기술입니다.

주로 사람(Person Re-ID)이나 차량(Vehicle Re-ID)을 대상으로 하며, 특정 카메라에서 사라진 객체가 다른 카메라에 다시 나타났을 때 동일한 식별자(ID)를 부여함으로써 광역적인 추적을 가능하게 합니다. 이는 단순한 객체 감지를 넘어 보안 관제, 스마트 시티, 미아 찾기 등 실생활의 복잡한 시각적 문제를 해결하는 핵심적인 역할을 합니다.

재식별 기술의 핵심은 **카메라의 각도, 조명 조건, 객체의 포즈 변화**, 그리고 **부분적인 가려짐(Occlusion)에도 불구하고 변하지 않는 고유한 특징(Feature Representation)을 추출**하는 것입니다.

과거에는 색상 히스토그램이나 텍스처와 같은 수동 설계 특징을 사용했으나, 현재는 딥러닝 기반의 합성곱 신경망(CNN)이나 트랜스포머(Transformer)를 활용해 매우 정교한 특징 벡터를 추출합니다.

학습 과정에서는 **동일 인물의 이미지는 가깝게, 서로 다른 인물의 이미지는 멀게 배치하도록 유도**하는 **Triplet Loss**나 **Center Loss 같은 거리 학습(Metric Learning) 기법이 필수적으로 사용**됩니다.

또한 최**근에는 라벨링 비용을 줄이기 위한 비지도 학습(Unsupervised Learning)** 이나, 텍스트 설명을 통해 객체를 찾는 **시각-언어 모델 기반의 Re-ID 연구도 활발히 진행**되고 있습니다.

객체 추적(MOT) 시스템에서 Re-ID는 **데이터 연관(Data Association)의 신뢰도를 높이는 결정적인 단서**가 됩니다. 특히 객체가 다른 물체에 가려졌다가 다시 나타나는 '재등장' 상황에서, 이전의 운동 정보가 소실되더라도 **Re-ID를 통해 추출된 외형 특징을 비교함으로써 끊기지 않는 궤적을 유지**할 수 있습니다. 예를 들어 DeepSORT는 고전적인 SORT 알고리즘에 Re-ID 네트워크를 결합하여 추적의 안정성을 획기적으로 개선한 대표적인 사례입니다.

---

## 핵심 연구
---
재식별(Re-ID) 분야에서 핵심적인 역할을 한 논문들은 주로 모델 학습을 위한 표준적인 베이스라인을 정립하거나, 객체의 세밀한 부분(Part)을 활용하는 구조를 제안하여 성능의 비약적인 향상을 이끌어낸 것들입니다.

특히 'Bag of Tricks' 논문은 수많은 연구자가 모델 성능을 높이기 위해 사용하는 표준적인 학습 기법들을 집대성하여 현재까지도 가장 중요한 지침서 역할을 하고 있으며, PCB 논문은 객체를 수평적으로 분할하여 세부 특징을 추출하는 방식의 효용성을 입증했습니다.

또한 TransReID는 합성곱 신경망(CNN) 중심이었던 Re-ID 연구를 트랜스포머(Transformer) 구조로 전환시킨 기념비적인 연구입니다.

| Paper | Description | Publication Time |
| :--- | :--- | :--- |
| [Bag of Tricks and A Strong Baseline for Deep Person Re-identification](https://arxiv.org/abs/1903.07071) | BNNeck 등 Re-ID 모델 성능을 극대화하는 6가지 학습 트릭을 제안하여 현대 Re-ID의 표준 베이스라인을 정립한 매우 중요한 논문입니다. | 7 years ago |
| [Beyond Part Models: Person Retrieval with Refined Part Pooling](https://arxiv.org/abs/1711.09349) | PCB(Part-based Convolutional Baseline)를 통해 사람 이미지를 수평 분할하여 세밀한 특징을 추출하는 방식이 효과적임을 증명했습니다. | 8 years ago |
| [TransReID: Transformer-based Object Re-Identification](https://arxiv.org/abs/2102.04378) | 트랜스포머 아키텍처를 Re-ID에 성공적으로 도입하여 기존 CNN 기반 모델들의 한계를 극복하고 전역적 특징 추출의 우수성을 보여주었습니다. | 5 years ago |
| [Transformer for Object Re-Identification: A Survey](https://arxiv.org/abs/2401.06960) | 최근 트랜스포머 기반의 Re-ID 연구 흐름과 기술적 기여를 한눈에 파악할 수 있는 최신 서베이 논문입니다. | a year ago |
| [Deep Ranking for Person Re-identification via Joint Representation Learning](https://arxiv.org/abs/1505.06821) | 거리 학습(Metric Learning)과 특징 표현 학습을 결합하여 초기 딥러닝 기반 Re-ID의 기틀을 마련한 핵심 연구 중 하나입니다. | 11 years ago |
| [PersonViT: Large-scale Self-supervised Vision Transformer for Person Re-Identification](https://arxiv.org/abs/2408.05398) | 자가 지도 학습(Self-supervised)과 대규모 데이터셋을 활용해 고도화된 특징 표현력을 확보한 최신 트랜스포머 기반 Re-ID 모델입니다. | a year ago |
| [History-Aware Transformation of ReID Features for Multiple Object Tracking](https://arxiv.org/abs/2503.12562) | 추적 과정에서의 신뢰도를 높이기 위해 과거의 이력을 활용한 Re-ID 특징 변환 기법을 제안한 최신 핵심 연구입니다. | 10 months ago |

---

## 연구 동향
---

최근 재식별(Re-ID) 연구는 단순히 이미지 간의 유사도를 측정하는 단계를 넘어, 옷차림이 바뀌거나 조명이 극단적인 환경에서도 견고하게 작동하는 일반화 성능 확보와 거대 언어 모델(LLM)을 활용한 의미론적 이해 결합에 집중하고 있습니다.

특히 2025년과 2026년 초에 발표된 연구들은 멀티모달 데이터(텍스트, 오디오 등)를 활용하여 '어떤 사람인지'에 대한 설명을 추적의 단서로 삼거나, 비지도 환경에서 도메인 간의 격차를 줄이는 혁신적인 기법들을 선보이고 있습니다.

| Paper | Description | Publication Time |
| :--- | :--- | :--- |
| [LLMTrack: Semantic Multi-Object Tracking with Multi-modal Large Language Models](https://arxiv.org/abs/2601.06550) | 대규모 언어 모델을 재식별 과정에 통합하여, 객체의 시각적 특징뿐만 아니라 시맨틱한 속성까지 이해하고 추적에 활용하는 최신 연구입니다. | 9 days ago |
| [History-Aware Transformation of ReID Features for Multiple Object Tracking](https://arxiv.org/abs/2503.12562) | 과거의 특징 정보를 현재의 Re-ID 추출 과정에 반영하여 시간적 일관성을 높이고, 가려짐 상황 이후의 재식별 정확도를 개선했습니다. | 10 months ago |
| [PS-ReID: Advancing Person Re-Identification and Precise Segmentation](https://arxiv.org/abs/2503.21595) | 재식별과 정밀 세그멘테이션을 결합하고 멀티모달 검색 기능을 도입하여 복잡한 도심 환경에서의 객체 식별 능력을 강화했습니다. | 10 months ago |
| [Low-Rank Expert Merging for Multi-Source Domain Adaptation in ReID](https://arxiv.org/abs/2508.06831) | 여러 소스 도메인에서 학습된 모델들을 효율적으로 통합하여, 새로운 환경에서도 별도의 라벨링 없이 높은 재식별 성능을 유지하게 합니다. | 5 months ago |
| [Coarse Attribute Prediction with Task Agnostic Distillation for Clothes Changing ReID](https://arxiv.org/abs/2505.12580) | 옷차림이 변하는 환경(CC-ReID)에서 저화질 이미지의 한계를 극복하기 위해 속성 예측과 지식 증류 기법을 결합한 최신 기법입니다. | 8 months ago |
| [Unsupervised Visible-Infrared ReID via Pseudo-label Correction](https://arxiv.org/abs/2404.06683) | 가시광선과 적외선 영상 간의 재식별을 라벨 없이 수행하기 위해 유사 라벨 수정과 모달리티 정렬 기법을 제안했습니다. | 2 years ago |
| [Transformer for Object Re-Identification: A Survey](https://arxiv.org/abs/2401.06960) | 2024년 말까지의 트랜스포머 기반 Re-ID 연구들을 총망라하여 최신 기술 트렌드와 향후 발전 방향을 제시하는 서베이입니다. | a year ago |
| [AerialMind: Towards Referring Multi-Object Tracking in UAV Scenarios](https://arxiv.org/abs/2511.21053) | 드론 시점에서 자연어 지시문을 통해 특정 대상을 식별하고 추적하는 기술로, Re-ID와 언어 이해의 결합을 보여줍니다. | 2 months ago |