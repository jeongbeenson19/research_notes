---
title: Video Object Segmentation
aliases:
  - VOS
tags:
  - task
  - video
  - segmentation
topics:
  - Video Understanding
---
비디오 객체 세그멘테이션(Video Object Segmentation, VOS)은 **비디오의 첫 프레임에서 관심 객체의 마스크(또는 바운딩 박스)가 주어졌을 때, 나머지 모든 프레임에서 해당 객체를 정밀하게 추적하고 픽셀 수준으로 분할하는 반지도 학습(Semi-supervised) 태스크**입니다.

참조 비디오 객체 세그멘테이션(RVOS)이 **자연어 텍스트를 입력으로 받는 것과 달리**, VOS는 시각적 마스크 자체가 유일한 감독 신호이므로 외형 변화, 가려짐, 빠른 움직임 등의 복잡한 상황에서도 일관된 세그멘테이션을 유지해야 하는 어려움이 있습니다.
이 기술은 영상 편집, 자율 주행, 로봇 비전, 의료 영상 분석 등 광범위한 분야에서 핵심적인 역할을 합니다.

VOS 연구의 발전은 메모리 메커니즘(Memory Mechanism)의 진화 역사로 볼 수 있습니다.

초기에는 온라인 학습을 통해 각 비디오마다 모델을 미세 조정했으나, 2019년 STM(Space-Time Memory) 네트워크가 등장하면서 이전 프레임들의 특징과 마스크를 메모리에 저장하고 현재 프레임과 매칭하는 방식이 주류가 되었습니다.

이후 XMem, AOT, Cutie 등의 모델들이 메모리 효율성을 높이고 장기적인 추적 성능을 개선하는 방향으로 발전해왔습니다.

최근에는 메타의 SAM 2가 VOS 분야에 혁명을 일으켰습니다. SAM 2는 프롬프트 기반의 파운데이션 모델로서 별도의 데이터셋별 학습 없이도 놀라운 제로샷 성능을 보여주며, 복잡한 실세계 시나리오를 다루는 MOSE, LVOS 등의 최신 벤치마크에서 기존 방법들을 압도하고 있습니다.

현재 연구 동향은 크게 세 가지로 요약됩니다.

첫째, **장기 비디오(Long-term Video)에서의 안정성 확보**입니다. LVOS와 MOSEv2 같은 데이터셋은 수분에 걸친 영상에서 객체가 사라졌다가 다시 나타나는 재등장(Re-appearance) 상황을 평가합니다.

둘째는 **복잡한 실세계 환경에 대한 강건성**입니다. M³-VOS처럼 다양한 물체 상태 변화(고체가 액체로 변하는 등)나 극심한 가려짐 상황을 다루는 연구가 증가하고 있습니다.

셋째는 **효율성과 실시간 처리**입니다. 메모리 사용량을 줄이면서도 정확도를 유지하는 경량화 모델들과 온디바이스 배포를 목표로 하는 연구가 활발합니다.

| Paper | Description | Publication Time |
| :--- | :--- | :--- |
| [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714) | 프롬프트 기반 비디오 세그멘테이션의 새로운 패러다임을 제시한 파운데이션 모델로, VOS의 판도를 완전히 바꾼 핵심 논문입니다. | a year ago |
| [MOSEv2: A More Challenging Dataset for Video Object Segmentation](https://arxiv.org/abs/2508.05630) | 극심한 가려짐, 빠른 움직임, 유사 객체가 혼재하는 복잡한 실세계 시나리오를 평가하는 최신 벤치마크입니다. | 5 months ago |
| [LVOS: A Benchmark for Large-scale Long-term Video Object Segmentation](https://arxiv.org/abs/2404.19326) | 장기 비디오에서 객체의 재등장과 일관성 유지 능력을 평가하기 위한 대규모 데이터셋입니다. | 2 years ago |
| [M³-VOS: Multi-Phase, Multi-Transition, Multi-Scenery VOS](https://arxiv.org/abs/2412.13803) | 물체의 물리적 상태 변화(얼음이 녹아 물이 되는 등)를 포함한 극도로 어려운 시나리오를 다루는 연구입니다. | a year ago |
| [SeC: Advancing Complex VOS via Progressive Concept Construction](https://arxiv.org/abs/2507.15852) | 개념 기반 점진적 학습을 통해 복잡한 비디오에서도 안정적인 세그멘테이션을 실현한 최신 방법론입니다. | 6 months ago |
| [Segment Any Motion in Videos](https://arxiv.org/abs/2503.22268) | 사전 마스크 없이도 움직임 정보만으로 비디오 내 모든 객체를 자동으로 분할하는 비지도 학습 접근법입니다. | 10 months ago |
| [LiVOS: Light Video Object Segmentation with Gated Linear Matching](https://arxiv.org/abs/2411.02818) | 메모리 효율성을 극대화하면서도 높은 정확도를 유지하는 경량화된 VOS 모델입니다. | a year ago |
| [VideoSAM: Open-World Video Segmentation](https://arxiv.org/abs/2410.08781) | 개방형 환경에서 사전 정의되지 않은 모든 객체를 추적하고 분할할 수 있는 범용 VOS 프레임워크입니다. | a year ago |
| [The 2017 DAVIS Challenge on Video Object Segmentation](https://arxiv.org/abs/1704.00675) | VOS 분야의 표준 벤치마크를 확립한 역사적으로 중요한 논문으로, 현재까지도 성능 평가 기준으로 사용됩니다. | 9 years ago |