---
title: Spatiotemporal Grounding
aliases:
tags:
  - task
  - video
  - grounding
  - spatiotemporal
topics:
  - Video Understanding
---
시공간 접지(Spatiotemporal Grounding)는 자연어 쿼리(예: "공을 던진 후 환호하는 파란 유니폼의 선수")가 주어졌을 때, 비디오 내에서 해당 설명에 부합하는 대상이 존재하는 **시간적 구간(Start & End time)** 과 **공간적 위치(Bounding Box 또는 Mask)** 를 동시에 찾아내는 고도의 인공지능 기술입니다.

이는 "언제(When)" 일어난 일인지 찾는 '시간적 접지(Temporal Grounding)'와 "어디(Where)"에 있는지 찾는 '공간적 접지(Spatial Grounding)'를 결합한 형태로, 비디오의 흐름과 언어의 맥락을 완벽히 통합하여 이해해야 하는 난이도 높은 작업입니다.

이 분야의 핵심은 비디오의 연속적인 프레임들 사이의 관계를 파악하는 시공간적 추론(Spatiotemporal Reasoning)입니다.
초기 연구들은 객체 검출기(Object Detector)로 후보군을 먼저 뽑고 텍스트와 매칭하는 다단계 방식을 취했으나, 최근에는 트랜스포머(Transformer)를 기반으로 비디오와 텍스트 특징을 하나의 공간에서 직접 연산하는 엔드투엔드(End-to-End) 방식이 주류를 이루고 있습니다.
특히 TubeDETR과 같은 모델은 시간에 따른 객체의 궤적(Tube)을 쿼리로 정의하여 매우 정교한 접지 성능을 보여주었습니다.

최근의 연구 동향은 크게 세 가지로 요약됩니다.
첫째는 **거대 멀티모달 모델(MLLM)의 활용**입니다. LLM의 강력한 추론 능력을 빌려 "누가 왜 그런 행동을 했는지"와 같은 복잡하고 추상적인 쿼리도 시공간적으로 풀어내고 있습니다.
둘째는 **세그멘테이션과의 결합**입니다. 박스 형태의 위치를 넘어 픽셀 단위로 대상을 분리하는 참조 비디오 객체 세그멘테이션(RVOS)으로 확장되고 있습니다.
셋째는 **장기 비디오 이해와 효율성**입니다. 수 분 이상의 긴 영상에서 찰나의 순간을 정확히 짚어내기 위해 효율적인 메모리 관리 기법과 시공간 어텐션 최적화 연구가 활발합니다.

| Paper | Description | Publication Time |
| :--- | :--- | :--- |
| [Towards Visual Grounding: A Survey](https://arxiv.org/abs/2412.20206) | 정지 영상부터 비디오까지 시각적 접지 기술의 기초와 최신 기법들을 총망라한 종합 서베이입니다. | a year ago |
| [A Survey on Video Temporal Grounding with MLLM](https://arxiv.org/abs/2508.10922) | 거대 멀티모달 모델(MLLM)을 이용해 비디오의 시간적 구간을 정확히 찾아내는 최신 연구들을 정리했습니다. | 5 months ago |
| [ReferDINO: Referring Video Object Segmentation with Visual Grounding Foundations](https://arxiv.org/abs/2501.14607) | 시각적 접지 파운데이션 모델을 기반으로 비디오 내 객체를 정교하게 분할하고 추적하는 혁신적인 연구입니다. | a year ago |
| [MomentSeg: Moment-Centric Sampling for Enhanced Video Pixel Understanding](https://arxiv.org/abs/2510.09274) | 특정 순간(Moment)에 집중하는 샘플링 기법을 통해 비디오 내 객체의 시공간적 위치를 픽셀 수준에서 파악합니다. | 3 months ago |
| [AerialMind: Towards Referring Multi-Object Tracking in UAV Scenarios](https://arxiv.org/abs/2511.21053) | 드론 영상이라는 특수한 환경에서 자연어 지시문을 통해 다수의 객체를 시공간적으로 추적하는 기술을 제안했습니다. | 2 months ago |
| [VISTA: Mitigating Semantic Inertia in Video-LLMs via Training-Free Routing](https://arxiv.org/abs/2505.11830) | Video-LLM이 시공간 정보를 더 정확히 처리할 수 있도록 동적 체인-오브-소트(CoT) 경로 설정을 도입한 연구입니다. | 8 months ago |
| [MotionBench: Benchmarking Fine-grained Video Motion Understanding for VLM](https://arxiv.org/abs/2501.02955) | 시각-언어 모델이 비디오의 세밀한 움직임을 얼마나 잘 파악하고 접지하는지 평가하기 위한 새로운 기준점입니다. | a year ago |
| [Temporal Prompting Matters: Rethinking Referring Video Object Segmentation](https://arxiv.org/abs/2510.07319) | 시간적 프롬프트가 시공간 접지 성능에 미치는 영향을 분석하고 이를 최적화하는 방안을 제시했습니다. | 3 months ago |
| [Action100M: A Large-scale Video Action Dataset](https://arxiv.org/abs/2601.10592) | 1억 개 규모의 방대한 데이터를 통해 시공간적인 행동 이해와 접지 능력을 비약적으로 높일 수 있는 기반을 마련했습니다. | 4 days ago |