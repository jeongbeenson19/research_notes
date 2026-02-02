# Online Action Detection

**온라인 행동 감지(Online Action Detection, OAD)**는 실시간으로 입력되는 비디오 스트림에서 **미래의 정보를 보지 않고**, 각 프레임(또는 현재 시점)에서 어떤 행동이 일어나고 있는지를 감지하고 분류하는 컴퓨터 비전 태스크입니다.

이는 전체 비디오를 다 보고 난 후에 분석하는 **오프라인(Offline) 행동 감지**와 근본적인 차이가 있으며, 실시간 상호작용이 필수적인 응용 분야에서 핵심적인 기술입니다.

## 핵심 제약과 목표

- **인과성(Causality)**: 예측은 오직 과거와 현재의 프레임에만 기반해야 합니다. 미래 프레임을 사용하는 것은 '온라인'이라는 제약 조건에 위배됩니다.
- **낮은 지연 시간(Low Latency)**: 행동이 발생하면 최대한 빠르게 감지해야 합니다.
- **조기 예측(Early Prediction)**: 행동이 완전히 끝나기 전, 진행 중인 상태에서도 감지가 가능해야 합니다.

## 주요 접근 방식

1.  **특징 추출 (Feature Extraction)**:
    - 실시간으로 들어오는 비디오 프레임에서 즉시 시각적 특징을 추출합니다.
    - 주로 I3D, SlowFast, ResNet 등 사전 학습된 2D/3D CNN 모델이 백본(Backbone)으로 사용됩니다.

2.  **시간적 모델링 (Temporal Modeling)**:
    - 추출된 특징들의 시퀀스를 모델링하여 시간적 의존성을 학습합니다.
    - **RNN/LSTM 기반 모델**: 순차적인 데이터 처리에 강점을 가지며, 과거 정보를 내부 상태(hidden state)에 저장하여 현재 예측에 활용합니다.
    - **Transformer 기반 모델**: 어텐션 메커니즘을 통해 더 길고 복잡한 시간적 관계를 학습하는 데 효과적입니다. [[Long Short-Term Transformer for Online Action Detection|LSTR]]은 트랜스포머를 온라인 환경에 맞게 변형한 대표적인 예시입니다.

## 주요 과제 (Challenges)

- **부분적인 정보**: 행동의 전체 모습이 아닌, 시작 부분이나 중간 부분만 보고 예측해야 하므로 정보가 불완전합니다.
- **배경과의 구분**: '행동이 없는 상태(배경)'와 '의미 있는 행동'을 구분하는 것이 어렵습니다. 실제 비디오에서 배경 프레임이 행동 프레임보다 훨씬 많아 데이터 불균형 문제가 발생합니다.
- **시점의 불확실성**: 언제 행동이 시작될지 모르기 때문에, 모델은 지속적으로 스트림을 분석하며 행동의 시작점을 탐지해야 합니다.

## 관련 논문
- [[Long Short-Term Transformer for Online Action Detection]]

## 관련 링크
- [[Temporal Modeling]]
- [[Video Understanding]]
- [[20_Tasks/VideoUnderstanding/Abstract/Video Action Recognition|Action Recognition]]
