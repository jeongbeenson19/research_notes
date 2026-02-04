# Temporal Modeling

**시간적 모델링(Temporal Modeling)** 은 컴퓨터 비전, 특히 비디오 분석에서 시간의 흐름에 따른 데이터의 변화와 패턴을 학습하고 이해하는 과정을 의미합니다.

정지된 이미지를 분석하는 것과 달리, 비디오는 '시간'이라는 차원을 추가로 가지고 있습니다. Temporal Modeling은 바로 이 시간 축에 걸쳐 있는 프레임 간의 관계, 즉 **시간적 의존성(temporal dependency)** 을 포착하는 데 중점을 둡니다.

## 중요성

- **행동 및 이벤트 이해**: 사람의 행동(걷기, 달리기)이나 특정 이벤트(공을 차는 순간)는 여러 프레임에 걸쳐 일어나는 동적인 과정입니다. 시간적 모델링 없이는 이러한 동적인 개념을 이해할 수 없습니다.
- **모션 정보 활용**: 객체의 움직임, 속도, 가속도 등은 비디오를 이해하는 데 핵심적인 단서입니다.
- **인과 관계 추론**: 어떤 사건이 다른 사건의 원인이 되는 등의 인과 관계를 파악하는 데 필수적입니다.

## 주요 접근 방식

1.  **3D CNN (3D Convolutional Neural Networks)**:
    - 2D CNN이 이미지의 가로, 세로(space) 차원에서 특징을 추출하는 반면, 3D CNN은 여기에 시간(time) 차원을 더해 3D 컨볼루션 필터를 적용합니다.
    - 짧은 시간 내의 공간-시간 특징(spatio-temporal features)을 동시에 학습하는 데 효과적입니다. (예: C3D, I3D)

2.  **Two-Stream Networks**:
    - 비디오를 두 개의 스트림으로 나누어 처리하는 방식입니다.
    - **Spatial Stream**: 단일 프레임의 RGB 이미지를 입력받아 '무엇'이 보이는지(외형 정보)에 집중합니다.
    - **Temporal Stream**: 여러 프레임에 걸친 옵티컬 플로우(Optical Flow)를 입력받아 '어떻게' 움직이는지(모션 정보)에 집중합니다.
    - 두 스트림의 결과를 나중에 융합(fuse)하여 최종 예측을 수행합니다.

3.  **RNN (Recurrent Neural Networks)**:
    - LSTM, GRU와 같은 순환 신경망은 시퀀스 데이터 처리에 특화된 모델입니다.
    - 각 프레임에서 추출된 특징을 순차적으로 입력받아, 내부 상태(hidden state)에 시간적 정보를 압축하고 누적하여 다음 프레임 예측에 활용합니다.

4.  **Transformer-based Models**:
    - 최근 가장 활발히 연구되는 접근 방식으로, 어텐션(Attention) 메커니즘을 사용합니다.
    - 시퀀스 내의 모든 프레임 쌍 간의 관계를 직접 계산하므로, RNN의 장기 의존성 문제(long-term dependency problem)를 해결하고 더 길고 복잡한 시간적 패턴을 학습하는 데 유리합니다. (예: TimeSformer, [[40_Papers/Long Short-Term Transformer for Online Action Detection|LSTR]])

## 응용 분야

- [[20_Tasks/VideoUnderstanding/Abstract/Video Action Recognition|Action Recognition]]
- [[Online Action Detection]]
- [[Video Understanding]]
- 객체 추적 (Object Tracking)
- 비디오 요약 (Video Summarization)

## 관련 링크
- [[Transformer]]
- [[RNN]]
- [[3D-CNN]]
- [[Optical Flow]]
