---
tags:
  - algorithm
  - statistics
  - control_theory
  - CV
aliases:
  - 칼만 필터
---

# Kalman Filter (칼만 필터)

**칼만 필터**는 시간에 따라 변화하는 시스템의 상태를 측정값(measurement)을 기반으로 추정(estimate)하는 재귀적(recursive) 필터 알고리즘입니다. 측정값에 포함된 노이즈(noise)를 고려하여, 시스템의 현재 상태를 더 정확하게 추정하는 데 사용됩니다.

## 핵심 아이디어

칼만 필터는 **예측(Predict)** 과 **갱신(Update)** 의 두 단계를 반복적으로 수행합니다.

1.  **예측 (Predict)**: 이전 상태를 기반으로 현재 상태를 예측합니다. 이 예측은 시스템의 움직임을 모델링한 동역학 모델(dynamic model)을 따르지만, 불확실성을 포함합니다.
2.  **갱신 (Update)**: 센서를 통해 얻은 새로운 측정값을 사용하여 예측된 상태를 보정(correct)합니다. 즉, 불확실한 예측과 노이즈가 낀 측정값 사이에서 최적의 절충안을 찾아 더 정확한 추정치를 계산합니다.

## 수학적 원리: 예측과 갱신

칼만 필터의 핵심은 상태 공간 표현(state-space representation)을 통해 시스템을 모델링하고, 두 가지 주요 단계를 통해 재귀적으로 상태를 추정하는 것입니다.

-   **상태 변수(State Variables)**:
    -   $\mathbf{x}_k$: 시간 $k$에서의 시스템 상태 벡터 (e.g., $[u, v, s, r, \dot{u}, \dot{v}, \dot{s}]^T$)
    -   $\mathbf{P}_k$: 상태 추정의 불확실성을 나타내는 오차 공분산 행렬
    -   $\mathbf{z}_k$: 시간 $k$에서의 측정값 벡터
    -   $\mathbf{u}_k$: 시간 $k$에서의 제어 입력 벡터 (외부 힘 등)

---

### **1. 예측 단계 (Predict Step)**

이전 상태($k-1$)의 추정치를 사용하여 현재 상태($k$)를 예측합니다.

1.  **상태 예측 (State Prediction)**
    $$ \hat{\mathbf{x}}_{k|k-1} = \mathbf{F}_k \hat{\mathbf{x}}_{k-1|k-1} + \mathbf{B}_k \mathbf{u}_k $$
    -   $\hat{\mathbf{x}}_{k|k-1}$: 예측된 상태 (a priori)
    -   $\hat{\mathbf{x}}_{k-1|k-1}$: 이전 단계에서 갱신된 최종 상태 (a posteriori)
    -   $\mathbf{F}_k$: 상태 전이 행렬 (State Transition Matrix). 시스템의 동역학 모델.
    -   $\mathbf{B}_k$: 제어 입력 행렬 (Control Input Matrix).

2.  **오차 공분산 예측 (Error Covariance Prediction)**
    $$ \mathbf{P}_{k|k-1} = \mathbf{F}_k \mathbf{P}_{k-1|k-1} \mathbf{F}_k^T + \mathbf{Q}_k $$
    -   $\mathbf{P}_{k|k-1}$: 예측된 오차 공분산
    -   $\mathbf{P}_{k-1|k-1}$: 이전 단계의 갱신된 오차 공분산
    -   $\mathbf{Q}_k$: 프로세스 노이즈 공분산 (Process Noise Covariance). 동역학 모델 자체의 불확실성을 나타냅니다.

---

### **2. 갱신 단계 (Update Step)**

현재 시간($k$)의 측정값을 사용하여 예측 단계를 통해 얻은 예측치를 보정합니다.

1.  **칼만 이득 계산 (Kalman Gain Calculation)**
    $$ \mathbf{K}_k = \mathbf{P}_{k|k-1} \mathbf{H}_k^T (\mathbf{H}_k \mathbf{P}_{k|k-1} \mathbf{H}_k^T + \mathbf{R}_k)^{-1} $$
    -   $\mathbf{K}_k$: 칼만 이득. 예측과 측정값 중 어느 쪽에 더 비중을 둘지 결정하는 값.
    -   $\mathbf{H}_k$: 관측 행렬 (Observation Matrix). 상태 변수를 측정값 공간으로 변환합니다.
    -   $\mathbf{R}_k$: 측정 노이즈 공분산 (Measurement Noise Covariance). 센서 측정의 불확실성을 나타냅니다.

2.  **상태 갱신 (State Update)**
    $$ \hat{\mathbf{x}}_{k|k} = \hat{\mathbf{x}}_{k|k-1} + \mathbf{K}_k (\mathbf{z}_k - \mathbf{H}_k \hat{\mathbf{x}}_{k|k-1}) $$
    -   $\hat{\mathbf{x}}_{k|k}$: 측정값으로 보정된 최종 상태 (a posteriori)
    -   $\mathbf{z}_k$: 현재 측정값
    -   $(\mathbf{z}_k - \mathbf{H}_k \hat{\mathbf{x}}_{k|k-1})$: 측정 잔차(Residual). 실제 측정값과 예측된 측정값의 차이.

3.  **오차 공분산 갱신 (Error Covariance Update)**
    $$ \mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}_k) \mathbf{P}_{k|k-1} $$
    -   $\mathbf{P}_{k|k}$: 갱신된 오차 공분산
    -   $\mathbf{I}$: 단위 행렬 (Identity Matrix)

이 두 단계를 거쳐 갱신된 $\hat{\mathbf{x}}_{k|k}$와 $\mathbf{P}_{k|k}$는 다음 시간($k+1$)의 예측 단계 입력으로 사용되어, 필터가 시간에 따라 계속해서 상태를 추정하게 됩니다.

## Computer Vision에서의 활용

칼만 필터는 특히 [[Object Tracking]] 분야에서 핵심적인 역할을 합니다.

-   **움직임 예측**: 탐지된 객체의 다음 위치와 속도를 예측합니다.
-   **[[Occlusion|가림]] 상황 대처**: 객체가 다른 물체에 가려져 탐지되지 않을 때, 칼만 필터는 움직임 모델에 따라 객체의 위치를 계속해서 예측합니다. 이후 객체가 다시 나타나면, 예측된 위치를 기반으로 동일한 객체임을 인식하고 추적을 이어갈 수 있도록 돕습니다.
-   **측정 노이즈 완화**: 객체 탐지기(detector)의 출력값(bounding box 위치 등)이 프레임마다 미세하게 흔들리는 경우, 칼만 필터가 이를 부드럽게 보정하여 안정적인 추적 경로를 만듭니다.

## 관련 개념
-   [[Object Tracking]]
-   [[Occlusion]]
