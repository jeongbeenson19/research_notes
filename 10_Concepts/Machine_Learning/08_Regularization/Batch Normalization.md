

## ✅ 1. 배치 정규화(Batch Normalization, BN)란?

### 📌 정의

**Batch Normalization**은 딥러닝 모델 학습 시 각 층의 입력 분포를 정규화하여 **학습 안정성**과 **속도**를 높이는 기법입니다.  
2015년 Ioffe & Szegedy가 발표한 논문 "_Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift_"에서 소개되었습니다.

---

## ✅ 2. 왜 필요한가? (Internal Covariate Shift)

### 🔍 Internal Covariate Shift란?

- 신경망 학습 중, **이전 층의 파라미터 변화로 인해 다음 층의 입력 분포가 계속 바뀌는 현상**을 말합니다.
    
- 이로 인해 학습이 느려지고, 모델이 수렴하기 어렵습니다.
    
- 해결책: 각 층의 입력 분포를 **정규화(standardization)** 하여 분포 변화를 억제.
    

> 📌 **Covariate Shift vs. Internal Covariate Shift**
> 
> - **Covariate Shift**: 학습 데이터와 테스트 데이터의 입력 분포가 다른 현상 (데이터셋 차원의 문제).
>     
> - **Internal Covariate Shift**: 신경망 내부에서 층 간 입력 분포가 계속 바뀌는 현상 (모델 학습 과정의 문제).
>     

---

## ✅ 3. 배치 정규화의 수식 및 작동 방식

### 🔧 동작 과정 (Forward Pass 기준)

BN은 어떤 layer (Conv든 FC든)의 출력을 정규화합니다. 주어진 미니배치 $\{x^{(1)}, x^{(2)}, ..., x^{(m)}\}$ 에 대해 다음 순서를 따릅니다:

#### (1) 배치 평균과 분산 계산

$$\mu_B = \frac{1}{m} \sum_{i=1}^m x^{(i)}, \quad \sigma_B^2 = \frac{1}{m} \sum_{i=1}^m \left(x^{(i)} - \mu_B\right)^2
$$

#### (2) 정규화

$$
\hat{x}^{(i)} = \frac{x^{(i)} - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}
$$

- $\epsilon$: 수치적 안정성을 위한 작은 상수
    

#### (3) 스케일과 시프트 (학습 가능 파라미터 도입)

$$
y^{(i)} = \gamma \hat{x}^{(i)} + \beta
$$

- $\gamma, \beta$: 각각 scale과 shift를 조정하는 학습 가능한 파라미터
    

→ 이는 단순히 정규화에서 그치는 것이 아니라, **원래의 표현력을 유지**할 수 있도록 보완한 구조입니다.

---

## ✅ 4. CNN에서의 BN 적용 방식

- Fully Connected layer: 각 뉴런의 activation에 대해 BN 수행
    
- Convolution layer: 채널 단위로 정규화 (같은 채널 내 모든 공간 위치 공유)
    

즉, Conv layer의 경우 $N \times C \times H \times W$ 형상에서 **C 채널별로 평균과 분산을 계산**합니다.

---

## ✅ 5. 장점

|장점|설명|
|---|---|
|✅ 학습 속도 증가|정규화로 인해 더 큰 학습률 사용 가능|
|✅ Gradient vanishing/exploding 완화|안정적인 분포 유지로 인해 역전파 시 문제가 덜함|
|✅ Regularization 효과|Dropout 없이도 overfitting 감소|
|✅ 초기화에 덜 민감|초기 가중치 설정이 완벽하지 않아도 안정적으로 학습|

---

## ✅ 6. 학습과 테스트 시 동작 차이

- **학습 시**: 각 배치에 대해 평균과 분산을 실시간 계산
    
- **추론 시**: 학습 중 모은 **Running Mean/Variance**를 사용해 정규화
    

이렇게 해야, **deterministic output**을 보장할 수 있음.

---

## ✅ 7. Internal Covariate Shift vs. 일반 Covariate Shift

|개념|Internal Covariate Shift|일반 Covariate Shift|
|---|---|---|
|위치|딥러닝 모델 **내부 층**|학습 데이터 vs. 테스트 데이터|
|원인|학습 중 파라미터 변화|분포가 다른 데이터 샘플링|
|해결법|BatchNorm 등 정규화|Domain Adaptation 등|

---

## ✅ 8. BN의 한계와 대안

|문제점|설명|대안|
|---|---|---|
|❌ 작은 배치 크기에서 부정확한 통계|배치마다 평균/분산의 분산이 큼|Layer Norm, Group Norm, Instance Norm|
|❌ 순서 민감성|RNN, 시계열 등에 적합하지 않음|Layer Norm 사용|
|❌ 추론 시 복잡도 증가|Running stat 관리 필요|정적인 정규화 기법 고려|

---

## ✅ 9. 직관 요약

- 딥러닝 학습은 층이 많아질수록 내부 분포가 계속 바뀌어 **불안정**해짐
    
- BN은 이를 "학습 중 매 순간, 입력을 평균 0, 분산 1에 가깝게 재조정"하여 학습을 더 빠르고 안정적으로 만듦
    
- 동시에 $\gamma, \beta$를 통해 **표현력도 유지**
    

---

## ✅ 10. 참고 자료

- 논문: [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift (Ioffe & Szegedy, 2015)](https://arxiv.org/abs/1502.03167)
    
- 관련 대안들: LayerNorm (Transformer에서 주로 사용), GroupNorm (CV에서 Batch 크기 작을 때 사용)
    

---

필요하다면 실제 PyTorch 코드 예시나 LayerNorm/GroupNorm과의 비교도 이어서 설명드릴 수 있어요.