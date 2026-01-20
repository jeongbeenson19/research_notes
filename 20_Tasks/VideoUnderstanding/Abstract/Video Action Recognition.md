---
title: Video Action Recognition
aliases: Action Recognition
tags:
  - task
  - video
  - classification
topics:
  - Video Understanding
---
비디오 행동 인식(Video Action Recognition)은 비디오 클립 내에서 사람이 수행하는 행동을 자동으로 식별하고 분류하는 컴퓨터 비전의 핵심 분야입니다.

정지 이미지와 달리 비디오는 시간(Temporal) 차원이 추가되어 있으며, 동작의 선후 관계와 흐름을 파악해야 하므로 공간적(Spatial) 특징과 시간적 특징을 동시에 학습하는 시공간(Spatiotemporal) 모델링이 필수적입니다.

이 분야는 지난 10년간 전통적인 2D CNN을 넘어 3D CNN, 그리고 최근의 트랜스포머(Transformer)와 대규모 멀티모달 모델(VLLM)로 급격히 진화해 왔습니다.

## 핵심 연구
---

행동 인식의 초기 발전을 이끈 핵심 논문들은 주로 **특징 추출 방식의 혁신**에 집중했습니다. 
가장 먼저 [Two-Stream Convolutional Networks for Action Recognition in Videos](https://arxiv.org/abs/1406.2199) (11년 전)는 비디오를 정지 영상인 RGB 스트림과 움직임 정보인 광학 흐름(Optical Flow) 스트림으로 나누어 처리하는 구조를 제안하여 시공간 정보를 분리 학습하는 표준을 세웠습니다. 

이후 [SlowFast Networks for Video Recognition](https://arxiv.org/abs/1812.03982) (6년 전)는 **공간적 의미를 파악**하는 'Slow' 경로와 **빠른 움직임을 파악**하는 'Fast' 경로를 **병렬로 구성하여 효율성을 극대화**하며 성능을 한 단계 끌어올렸습니다.

---

## 연구 동향
---

최근 3년(2023~2025년) 사이의 연구는 **비디오 트랜스포머의 고도화**와 **자기주도 학습(Self-Supervised Learning)의 확산**으로 요약됩니다. 특히 [VideoMAE](https://arxiv.org/abs/2203.12602) (현재는 v2 등으로 발전) 시리즈는 **비디오의 높은 중복성을 이용해 90% 이상의 패치를 마스킹하고 복원하는 방식**으로 **강력한 시공간 표현을 학습**하여 사전 학습 효율성을 획기적으로 높였습니다. 

또한 [InternVideo2.5: Empowering Video MLLMs with Long and Rich Context Modeling](https://arxiv.org/abs/2501.12386) (1년 전)와 같은 최신 연구들은 **수천 개의 프레임을 처리할 수 있는 긴 컨텍스트 모델링 기술을 도입**하여 복잡한 서사를 가진 **긴 비디오에서도 정확한 행동 이해가 가능하도록 기여**했습니다. 

더불어 [VideoMamba: State Space Model for Efficient Video Understanding](https://arxiv.org/abs/2403.06977) (2년 전)는 **트랜스포머의 계산 복잡도 문제를 해결**하기 위해 **State Space Model(SSM)을 도입**하여 긴 비디오에서도 효율적인 연산이 가능함을 보여주었습니다.

| Paper | Description | Publication Date |
| :--- | :--- | :--- |
| [Two-Stream Convolutional Networks for Action Recognition in Videos](https://arxiv.org/abs/1406.2199) | RGB와 Optical Flow를 각각 학습하는 이중 스트림 구조를 최초 제안함 | 11년 전 |
| [SlowFast Networks for Video Recognition](https://arxiv.org/abs/1812.03982) | 상이한 프레임 레이트를 가진 두 경로를 통해 시공간 특징을 효율적으로 포착함 | 6년 전 |
| [InternVideo2.5: Empowering Video MLLMs with Long and Rich Context Modeling](https://arxiv.org/abs/2501.12386) | 대규모 데이터와 긴 문맥 이해를 통해 비디오 파운데이션 모델의 성능을 극대화함 | 1년 전 |
| [VideoMamba: State Space Model for Efficient Video Understanding](https://arxiv.org/abs/2403.06977) | Mamba 구조를 비디오에 적용하여 효율적인 긴 비디오 시퀀스 처리를 가능하게 함 | 2년 전 |
| [A Survey on Backbones for Deep Video Action Recognition](https://arxiv.org/abs/2405.05584) | 최신 딥러닝 기반 행동 인식 백본 네트워크들의 발전 과정을 체계적으로 정리함 | 2년 전 |
| [SMART-Vision: Survey of Modern Action Recognition Techniques in Vision](https://arxiv.org/abs/2501.13066) | 현대적인 행동 인식 기술과 시공간 역학 분석 방법론에 대한 종합적인 리뷰를 제공함 | 1년 전 |
| [Video Understanding with Large Language Models: A Survey](https://arxiv.org/abs/2312.17432) | LLM을 활용한 비디오 이해 기술의 최신 동향과 멀티모달 융합 방식을 다룸 | 2년 전 |
| [CAST: Cross-Attention in Space and Time for Video Action Recognition](https://arxiv.org/abs/2311.18825) | 시공간 교차 주의 집중 기법을 통해 균형 잡힌 비디오 특징 이해를 도모함 | 1년 전 |
| [Enhancing Video Transformers for Action Understanding with VLM-aided Training](https://arxiv.org/abs/2403.16128) | 비전-언어 모델(VLM)의 지식을 활용하여 비디오 트랜스포머의 학습 성능을 향상시킴 | 2년 전 |
| [Video Understanding by Design: How Datasets Shape Architectures and Insights](https://arxiv.org/abs/2509.09151) | 데이터셋의 특성이 비디오 모델의 구조 설계와 통찰에 미치는 영향을 분석함 | 4개월 전 |