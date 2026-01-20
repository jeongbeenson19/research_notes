---
title: Video Object Referring Segmentation
aliases:
tags:
  - task
  - video
  - segmentation
  - referring
topics:
  - Video Understanding
---
참조 비디오 객체 세그멘테이션(Referring Video Object Segmentation, RVOS)은 자연어 형태의 지시문(예: "빨간 셔츠를 입고 달리는 사람")을 입력받아 비디오 내의 특정 객체를 식별하고, 전 프레임에 걸쳐 해당 객체의 마스크를 정밀하게 추출하며 추적하는 기술입니다.

일반적인 비디오 인스턴스 세그멘테이션(VIS)이 사전에 정의된 카테고리(사람, 자동차 등)를 찾는 것과 달리, RVOS는 텍스트와 시각 정보 사이의 복잡한 관계를 이해해야 하는 교차 모달(Cross-modal) 추론 능력이 필수적입니다.
이 기술은 객체의 외형뿐만 아니라 "공을 던지는"과 같은 동작 특성이나 "나무 뒤에 있는"과 같은 공간적 관계까지 해석해야 하므로 컴퓨터 비전 분야에서도 매우 도전적인 과제로 꼽힙니다.

최근의 연구 동향은 크게 세 가지 방향으로 급변하고 있습니다.

첫째는 메타의 SAM 2와 같은 파운데이션 모델의 도입입니다. SAM 2의 강력한 제로샷 분할 능력을 언어 모델과 결합하여 별도의 정교한 학습 없이도 텍스트만으로 고품질의 비디오 마스크를 얻는 연구가 주류를 이루고 있습니다.

둘째는 시각-언어 모델(VLM)의 고도화로, LLaVA와 같은 거대 모델을 '두뇌'로 삼아 복잡한 지시문을 해석하고 객체를 논리적으로 찾아내는 방식입니다.

셋째는 데이터셋의 진화입니다. 단순히 외형만 묘사하던 초기 단계에서 벗어나, MeViS 데이터셋처럼 객체의 미세한 움직임 변화(Motion Expression)를 추적하거나, OVIS/MOSE 데이터셋처럼 극심한 가려짐과 긴 영상에서의 안정성을 평가하는 쪽으로 연구의 초점이 이동하고 있습니다.

| Paper | Description | Publication Time |
| :--- | :--- | :--- |
| [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714) | 프롬프트 기반 비디오 세그멘테이션의 새 지평을 연 모델로, RVOS의 가장 강력한 백본 기술로 활용됩니다. | a year ago |
| [ReferDINO: Referring Video Object Segmentation with Visual Grounding Foundations](https://arxiv.org/abs/2501.14607) | 시각적 접지(Visual Grounding) 파운데이션 모델을 활용해 텍스트와 픽셀 사이의 정렬 성능을 극대화한 연구입니다. | a year ago |
| [Sa2VA: Marrying SAM2 with LLaVA for Dense Grounded Understanding](https://arxiv.org/abs/2501.04001) | SAM2의 정밀한 분할 능력과 LLaVA의 강력한 언어 추론 능력을 결합한 통합 멀티모달 모델입니다. | a year ago |
| [MeViS: A Multi-Modal Dataset for Referring Motion Expression Video Segmentation](https://arxiv.org/abs/2512.10945) | 객체의 외형이 아닌 '움직임'에 대한 묘사를 중심으로 세그멘테이션을 수행하도록 설계된 대규모 데이터셋과 벤치마크입니다. | a month ago |
| [Long-RVOS: A Comprehensive Benchmark for Long-term Referring Video Object Segmentation](https://arxiv.org/abs/2505.12702) | 수분 이상의 긴 비디오 시나리오에서 일관되게 지시된 객체를 추적하는 성능을 평가하기 위한 새로운 기준점입니다. | 8 months ago |
| [SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking](https://arxiv.org/abs/2411.11922) | SAM 2에 모션 인식 메모리를 탑재하여, 혼잡한 장면에서도 지시된 객체를 놓치지 않고 추적하도록 개선했습니다. | a year ago |
| [VoCap: Video Object Captioning and Segmentation from Any Prompt](https://arxiv.org/abs/2508.21809) | 텍스트 입력으로 객체를 분할할 뿐만 아니라, 반대로 분할된 궤적을 텍스트로 설명하는 양방향 멀티모달 기능을 제공합니다. | 5 months ago |
| [ReferDINO-Plus: 2nd Solution for 4th PVUW MeViS Challenge at CVPR 2025](https://arxiv.org/abs/2503.23509) | 2025년 최신 RVOS 챌린지에서 상위권을 차지한 기술로, 최신 트랜스포머 기술의 집약체입니다. | 10 months ago |
| [Multimodal Referring Segmentation: A Survey](https://arxiv.org/abs/2508.00265) | 텍스트와 오디오 등 다양한 모달리티를 활용한 참조형 세그멘테이션 기술의 전반을 다룬 최신 서베이 논문입니다. | 6 months ago |