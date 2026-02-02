---
title: Video Saliency Detection
aliases:
tags:
  - task
  - video
  - saliency
  - detection
topics:
  - Video Understanding
---
비디오 돌출 영역 검출(Video Saliency Detection, VSD)은 비디오 시퀀스에서 인간의 시선을 가장 강하게 끄는 영역이나 객체를 자동으로 식별하는 기술입니다.
이는 단순히 정지 이미지에서의 돌출 영역을 찾는 것을 넘어, 비디오 특유의 **움직임(Motion)** 정보와 **시간적 일관성(Temporal Consistency)** 을 효과적으로 활용해야 한다는 점에서 더 복잡한 문제입니다.
VSD는 크게 인간이 어디를 보는지 예측하는 **시선 예측(Fixation Prediction)** 과 가장 눈에 띄는 객체를 픽셀 단위로 분할하는 **비디오 돌출 객체 검출(Video Salient Object Detection, VSOD)** 로 나뉩니다.

VSD의 핵심 기법은 시간 흐름에 따른 객체의 움직임을 어떻게 모델링하느냐에 달려 있습니다.
초기에는 옵티컬 플로우(Optical Flow)를 사용하여 움직임 정보를 수동으로 추출했으나, 딥러닝 시대에 접어들면서 3D CNN(C3D, I3D 등)이나 ConvLSTM과 같은 순환 신경망 구조를 통해 시공간 특징을 직접 학습하는 방식이 주류가 되었습니다.
특히 프레임 간의 급격한 변화를 억제하고 매끄러운 추적 결과를 얻기 위해 시간적 제약 조건을 손실 함수에 반영하는 기법들이 중요하게 다뤄집니다.
최근에는 트랜스포머(Transformer)의 어텐션 메커니즘을 이용해 비디오 전체의 맥락을 파악하거나, 소리(Audio)와 영상(Visual) 정보를 융합하여 '소리가 나는 위치'를 돌출 영역으로 판단하는 오디오-비주얼(Audio-Visual) 융합 연구가 활발히 진행되고 있습니다.

현재 연구 동향은 크게 세 가지로 요약됩니다.
첫째, **트랜스포머 기반 고도화**입니다. 긴 비디오 시퀀스에서도 멀리 떨어진 프레임 간의 관계를 파악하여 전역적인 돌출도를 계산하는 모델들이 등장하고 있습니다.
둘째, **비지도/자기지도 학습(Unsupervised/Self-supervised Learning)** 의 확산입니다. 픽셀 단위의 정교한 라벨링 비용을 줄이기 위해, 움직임 정보 자체를 감독 신호로 삼아 스스로 학습하는 모델들이 주목받고 있습니다.
셋째, **멀티모달 융합 및 특수 환경 적용** 입니다. 단순히 시각 정보에 의존하지 않고 오디오 정보를 결합하거나, 360도 전방위 영상(Omnidirectional Video), 수중 영상 등 특수한 도메인에서의 돌출 영역을 찾는 연구가 증가하고 있습니다.

| Paper | Description | Publication Time |
| :--- | :--- | :--- |
| [Spherical Vision Transformers for Audio-Visual Saliency in 360-Degree Videos](https://arxiv.org/abs/2508.20221) | 360도 전방위 영상에서 시각 정보와 오디오 정보를 융합하여 돌출 영역을 예측하는 최신 트랜스포머 연구입니다. | 5 months ago |
| [VoCap: Video Object Captioning and Segmentation from Any Prompt](https://arxiv.org/abs/2508.21809) | 돌출된 객체를 분할할 뿐만 아니라 해당 객체의 의미와 동작을 텍스트로 설명하는 통합 멀티모달 프레임워크입니다. | 5 months ago |
| [Deep video representation learning: a survey](https://arxiv.org/abs/2405.06574) | 비디오의 시공간 특징 학습 기법 전반을 다루며, VSOD 모델의 기반이 되는 최신 표현 학습 기술을 정리했습니다. | a year ago |
| [Transformer-based Video Saliency Prediction with High Temporal Dimension](https://arxiv.org/abs/2401.07942) | 트랜스포머 구조를 사용하여 비디오의 시간 차원 정보를 효율적으로 디코딩하고 정밀한 돌출 지도를 생성하는 모델입니다. | 2 years ago |
| [Motion-aware Memory Network for Fast Video Salient Object Detection](https://arxiv.org/abs/2208.00946) | 움직임을 인식하는 메모리 네트워크를 통해 실시간에 가까운 속도로 돌출 객체를 검출하는 효율적인 구조를 제안했습니다. | 2 years ago |
| [Confidence-guided Adaptive Gate and Dual Differential Enhancement for VSOD](https://arxiv.org/abs/2105.06714) | 시공간 큐의 신뢰도를 판단하는 적응형 게이트를 도입하여 복잡한 배경에서의 검출 성능을 높였습니다. | 5 years ago |
| [DAVE: A Deep Audio-Visual Embedding for Dynamic Saliency Prediction](https://arxiv.org/abs/1905.10693) | 오디오-비주얼 임베딩을 통해 소리와 시각 정보의 연관성을 이용한 동적 돌출 영역 예측의 초기 핵심 연구입니다. | 7 years ago |
| [Deep Inside CNNs: Visualising Image Classification Models and Saliency Maps](https://arxiv.org/abs/1312.6034) | CNN의 그래디언트를 활용하여 돌출 지도를 생성하는 기초 원리를 제시한 기념비적인 논문입니다. | 12 years ago |
| [Spatio-Temporal Saliency Networks for Dynamic Saliency Prediction](https://arxiv.org/abs/1607.04730) | 비디오 시퀀스에서 시공간 정보를 통합하여 돌출도를 예측하는 초기 딥러닝 기반 네트워크를 제안했습니다. | 10 years ago |