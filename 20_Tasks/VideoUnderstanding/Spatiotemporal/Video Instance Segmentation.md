---
title: Video Instance Segmentation
aliases:
  - VIS
tags:
  - task
  - video
  - segmentation
  - instance
topics:
  - Video Understanding
---
비디오 인스턴스 세그멘테이션(Video Instance Segmentation, VIS)은 비디오 프레임 내의 모든 객체를 감지(Detection)하고, 각 객체의 정교한 마스크(Mask)를 추출하며, 프레임 간에 동일한 객체에 일관된 식별자(ID)를 부여하여 추적(Tracking)하는 세 가지 작업을 동시에 수행하는 고난도 태스크입니다.

단순한 박스 형태의 객체 추적(MOT)과 달리 픽셀 수준의 정밀한 분할이 요구되기에 자율 주행, 영상 편집, 로봇 제어 등에서 핵심적인 기술로 평가받습니다.

초기 연구들은 Mask R-CNN을 비디오로 확장한 형태에서 시작했으나, 현재는 어텐션 메커니즘을 통해 비디오 전체의 시공간 정보를 한 번에 처리하는 트랜스포머 기반 모델들이 주류를 형성하고 있습니다.

최근의 연구 동향은 크게 두 가지 흐름으로 나뉩니다.

첫 번째는 메타(Meta)가 발표한 SAM 2(Segment Anything Model 2)와 같은 거대 파운데이션 모델을 활용하여, 별도의 추가 학습 없이도 다양한 도메인에서 높은 수준의 세그멘테이션과 추적을 수행하는 제로샷(Zero-shot) 능력을 확보하는 것입니다.

두 번째는 '검은색 옷을 입은 사람'과 같은 자연어 지시문을 통해 특정 객체만을 추적하고 분할하는 참조 비디오 객체 세그멘테이션(Referring Video Object Segmentation, RVOS)으로의 확장입니다. 또한 유튜브-VIS(YouTube-VIS)나 OVIS와 같은 벤치마크 데이터셋에서 더 긴 영상과 복잡한 가려짐 상황을 해결하기 위한 장기 메모리(Long-term Memory) 관리 기법들이 활발히 연구되고 있습니다.

| Paper | Description | Publication Time |
| :--- | :--- | :--- |
| [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714) | 비디오 인스턴스 세그멘테이션의 패러다임을 바꾼 거대 파운데이션 모델로, 프롬프트를 통해 실시간 추적과 분할이 가능합니다. | a year ago |
| [SAM2MOT: A Novel Paradigm of Multi-Object Tracking by Segmentation](https://arxiv.org/abs/2504.04519) | SAM 2의 세그멘테이션 능력을 다중 객체 추적에 통합하여 픽셀 수준의 정교한 관리를 실현한 최신 연구입니다. | 9 months ago |
| [A Temporal Modeling Framework for Video Pre-Training on VIS](https://arxiv.org/abs/2503.17672) | 비디오 전용 사전 학습 프레임워크를 통해 시간적 일관성을 강화한 VIS 모델입니다. | 10 months ago |
| [VoCap: Video Object Captioning and Segmentation from Any Prompt](https://arxiv.org/abs/2508.21809) | 어떤 프롬프트로도 객체를 추적, 분할하고 동시에 캡셔닝까지 수행하는 멀티모달 통합 모델입니다. | 5 months ago |
| [Latest Object Memory Management for Temporally Consistent VIS](https://arxiv.org/abs/2507.19754) | 장기 비디오 추적에서 인스턴스의 일관성을 유지하기 위한 혁신적인 메모리 관리 기법을 제안했습니다. | 6 months ago |
| [SiamMask: A Framework for Fast Online Object Tracking and Segmentation](https://arxiv.org/abs/2207.02088) | 추적과 세그멘테이션을 실시간으로 동시에 수행하는 초기 프레임워크로, 많은 온라인 모델의 기초가 되었습니다. | 4 years ago |
| [Segment Any Motion in Videos](https://arxiv.org/abs/2503.22268) | 움직임 정보를 활용하여 비디오 내의 모든 움직이는 객체를 자동으로 분할하는 최신 기법입니다. | 10 months ago |
| [PVUW 2025 Challenge Report: Advances in Pixel-level Video Understanding](https://arxiv.org/abs/2504.11326) | 2025년 최신 비디오 이해 챌린지의 결과와 기술적 성취를 종합적으로 정리한 보고서입니다. | 9 months ago |