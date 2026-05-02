# 1차년도 MoE 구조 — 시공간적 증거 기반 접촉 후보의 신뢰도 추정 아키텍처

  

## 모델 모식도

  

본 1차년도 MoE 아키텍처는 evidence별로 독립된 expert가 분기되어 동작하며, gating network가 expert 활성화를 동적으로 제어하는 구조입니다. 분리 헤드 구조와의 본질적 차이는 evidence 분리가 backbone 단계부터 시작된다는 점이며, 이로 인해 각 expert가 자기 evidence에 특화된 representation을 학습합니다.


위 모식도에서 1차년도 MoE 구조의 새로운 구성요소는 (1) Shared Stem이 얕은 공통 feature를 추출하여 expert 간 기본적 representation 공유를 보장, (2) Gating Network가 입력에 따라 expert 활성화를 동적으로 제어, (3) 네 evidence expert가 각자의 backbone과 head를 가지고 자기 evidence에 특화 학습, (4) S-expert 내부에 부위별 sub-MoE가 중첩되어 AvatarMoE 자산을 직접 활용, (5) Evidence별 pseudo GT supervision으로 expert 특화를 명시적으로 강화, (6) Cross-evidence invariance loss로 expert 간 정보 누설을 방지하는 여섯 부분입니다.

  

각 expert의 출력은 evidence 자체와 그 신뢰도 α를 동반하며, gating network의 가중치 g와 함께 fusion 단계에 전달됩니다. 분리 헤드 구조의 fusion이 단순 confidence 가중인 반면, MoE 구조의 fusion은 gating weight와 confidence가 이중으로 작용하는 두 층 구조입니다.

  

## 시공간적 증거 기반 접촉 신뢰도 추정

  

### Evidence별 Expert 구조

  

**E-Expert (시각 증거)** 는 D2FP pretrained weight로 초기화된 visual backbone을 자체적으로 가지며, image의 visual texture와 appearance에 특화된 representation을 학습합니다. 학습 단계에서 motion-shuffled 입력에 대해 동일한 출력을 내도록 정규화되어 (motion invariance), E-expert가 motion 정보를 implicit하게 학습하는 leakage를 방지합니다. 출력은 두 인체 사이의 visual contact evidence map과 그 신뢰도 α_E이며, 격투 환경의 motion blur 상황에서 α_E가 자연스럽게 낮아지도록 학습됩니다.

  

**M-Expert (운동 불연속성)** 는 short-window (3-5 프레임) temporal backbone을 자체적으로 가지며, (2+1)D conv 또는 temporal attention 구조로 motion discontinuity 신호를 추출합니다. M-expert의 window size가 onset 검출 시간 분해능의 상한을 결정하며, 240 fps benchmark에서 4.17 ms 분해능을 보존하기 위해 출력은 frame-level로 유지됩니다. 학습 단계에서 visual texture가 변경된 입력에 대해 동일한 motion 신호를 내도록 정규화되어 (appearance invariance), appearance leakage를 방지합니다. Pseudo GT는 SMPL vertex의 시간 차분으로 생성되며, fitting 정확도가 높은 프레임만 선택적으로 사용하는 신뢰도 가중 학습이 적용됩니다.

  

**S-Expert (부위 사전 정보)** 는 D2FP pretrained backbone 위에 부위별 sub-MoE 구조를 중첩한 형태입니다. 외부 MoE는 evidence 모달리티를 분기하고, S-expert 내부 sub-MoE는 부위 (손-팔, 다리-발, 몸통, 머리) 를 분기합니다. 이 계층적 MoE는 PI의 AvatarMoE에서 검증된 자세 의존적 부위 인식 동적 게이팅을 직접 재사용하며, 격투 동작 카탈로그에서 부위별 접촉 빈도 분포를 prior로 활용합니다. SMPL parameter로부터 부위 위치 GT가 직접 제공되므로 supervision 강도가 다른 expert보다 강하며, 학습 안정성이 가장 높습니다.

  

**G-Expert (기하 증거)** 는 t-1 시점의 fitted mesh로부터 SDF와 normal alignment를 계산하는 비교적 얕은 expert입니다. 시간 차원의 의존성 순환을 회피하기 위해 t 시점이 아닌 t-1 시점의 메쉬를 입력으로 사용하며, 이는 본 연구의 핵심 명제 (피드백 루프 차단) 가 evidence 추출 단계에서 보존되도록 보장합니다. Pseudo GT는 multi-view SMPL fitting (Harmony4D의 multi-view setup 활용) 으로 정확도를 높인 mesh로부터 생성되며, fitting confidence가 낮은 프레임은 학습에서 제외됩니다.

  

### Expert별 Confidence 추정

  

각 expert는 자체 confidence head를 가지며, α_E, α_M, α_S, α_G는 해당 expert의 evidence 신뢰도를 [0, 1] 범위로 추정합니다. Confidence 추정의 학습 신호는 expert 내부에서 evidence와 신뢰도의 일관성으로 학습되며, expert가 분리되어 있으므로 confidence도 expert 내부 representation에 특화되어 학습됩니다.

  

이는 분리 헤드 구조의 confidence와 본질적으로 다른 점입니다. 분리 헤드 구조의 confidence는 공유 backbone feature 위에서 추정되므로 evidence 간 신뢰도 추정이 entangled될 수 있지만, MoE 구조의 confidence는 expert별 독립 representation 위에서 추정되므로 evidence별 confidence가 독립적으로 학습됩니다. 격투 환경의 evidence 비대칭 상황 (motion blur에서 α_E↓ + α_M↑) 이 더 명확히 학습됩니다.

  

PI의 Confidence-Guided Depth 자산은 LiDAR 깊이맵 보완 도메인에서 신뢰도 기반 selective filtering을 검증한 경험으로, 본 MoE 구조의 expert별 confidence head 설계에 알고리즘 패러다임 차원에서 활용됩니다. 다만 expert 분리로 인해 자산 활용이 단일 confidence head가 아닌 expert별 confidence head 네 개로 분산됩니다.

  

### Pseudo GT 기반 Expert 특화 학습

  

MoE 구조의 학습 안정성은 evidence별 pseudo GT supervision의 품질에 결정적으로 의존합니다. 분리 헤드 구조에서는 implicit supervision만으로 학습이 가능하지만, MoE 구조에서는 expert가 자기 evidence에 특화되도록 explicit supervision이 필요합니다.

  

Pseudo GT 생성은 SMPL parameter가 있는 표준 데이터셋 (Hi4D, Harmony4D) 에서 자동화되지만, **격투형 고속 동작에서 SMPL fitting 자체가 부정확할 수 있다는 본질적 위험**이 존재합니다. 이 위험을 완화하기 위해 (1) Multi-view SMPL fitting (Harmony4D의 multi-view setup 활용) 으로 fitting 정확도를 높이고, (2) Fitting confidence가 임계값 이상인 프레임만 pseudo GT로 사용하며, (3) Pseudo GT의 노이즈를 인지하는 noise-robust loss (예: Huber loss, learned loss attenuation) 를 적용합니다.

  

이 세 layer의 노이즈 제어는 분리 헤드 구조에서는 불필요한 추가 작업이며, MoE 구조의 학습 데이터 요구량이 증가하는 본질적 원인입니다. 1차년도 30-50 clips pilot 단계에서는 이 supervision 만으로 안정적 학습이 어려울 수 있으며, expert별 pretraining 전략으로 보완됩니다.

  

### Expert별 Pretraining 전략

  

1차년도 학습 데이터 부족을 보완하기 위해 expert별로 분리된 pretraining을 수행합니다. **E-expert**는 단일 인체 메쉬 복원 데이터셋 (3DPW 등) 으로 visual feature 추출을 사전 학습, **M-expert**는 motion 데이터셋 (AMASS 등) 으로 motion discontinuity 검출을 사전 학습, **S-expert**는 PI의 D2FP pretrained weight를 backbone으로 직접 활용하고 부위별 sub-MoE는 AvatarMoE pretrained weight를 활용, **G-expert**는 SMPL fitting 결과 기반 self-supervision으로 사전 학습합니다.

  

본 과제 데이터에서는 expert weight를 freeze하거나 작은 learning rate로 fine-tuning하면서 gating network와 fusion module을 주로 학습합니다. 이 단계적 학습은 expert 특화를 사전 단계에서 확보하여 본 과제 데이터에서의 학습 부담을 줄이는 전략입니다.

  

### Cross-Evidence Invariance Loss

  

Expert 분리의 학술적 가치는 각 expert가 자기 evidence에만 특화된다는 가정에 의존하지만, end-to-end 학습에서는 이 가정이 자연스럽게 깨질 수 있습니다. Cross-evidence invariance loss는 이 leakage를 명시적으로 방지하는 정규화입니다.

  

E-expert에 대해서는 motion-shuffled 입력 (시간 순서를 무작위로 섞은 입력) 에서도 동일한 출력을 내도록 강제하며, 이는 E-expert가 motion 정보를 사용하지 않음을 보장합니다. M-expert에 대해서는 visual texture가 변경된 입력 (color jitter, style transfer) 에서도 동일한 motion 신호를 내도록 강제합니다. S-expert와 G-expert에 대해서는 각각 부위 정보와 기하 정보 외의 단서에 invariant하도록 정규화합니다.

  

이 정규화는 evidence별 corruption injection 실험 (2차년도) 의 의미를 보장하는 핵심 메커니즘입니다. 정규화 없이 학습된 expert는 자기 evidence가 오염되어도 다른 evidence의 implicit 학습으로 성능을 유지할 수 있으며, 이는 evidence별 mechanistic 분석을 무의미하게 만듭니다. 정규화를 통해 각 expert의 출력이 자기 evidence에만 의존함을 보장해야 evidence별 corruption injection이 의미 있는 분석이 됩니다.

  

## Mixture of Experts Gate

  

### Gating Network의 역할 정의

  

MoE 구조의 gating network는 분리 헤드 구조의 confidence head와 본질적으로 다른 역할을 수행합니다. **Confidence head는 "evidence가 얼마나 정확한가"를 추정**하며, **Gating network는 "현재 입력 상황에서 어느 expert에 계산 자원을 분배할 것인가"를 결정**합니다. 두 메커니즘은 같은 입력 (격투 환경의 evidence 비대칭 상황) 에서 서로 다른 출력을 만들 수 있으며, 이중 작용이 MoE 구조의 핵심 차별성입니다.

  

예를 들어 motion blur 상황에서 confidence head는 α_E를 낮게 추정하고 (E-expert의 출력은 신뢰할 수 없음), gating network는 g_M을 높게 (M-expert에 계산 자원을 더 분배) 결정합니다. 두 신호는 fusion 단계에서 곱해지거나 합쳐져 최종 contact proposal에 영향을 미치며, 이중 비대칭 활용이 evidence 비대칭성의 정밀한 처리를 가능하게 합니다.

  

### Gating Network 구조

  

Gating network는 shared stem의 출력을 입력으로 받아 네 expert에 대한 가중치 (g_E, g_M, g_S, g_G) 를 계산합니다. 가중치는 softmax로 정규화되어 합이 1이 되며, top-k expert 선택 (예: top-2 또는 top-3) 을 통해 sparse activation을 적용합니다.

  

Sparse activation의 의미는 모든 입력에 대해 모든 expert를 활성화하지 않고, 입력 상황에 따라 선택적으로 일부 expert만 깊이 활성화한다는 것입니다. 이는 계산 효율성 차원의 이득뿐만 아니라, **3차년도 deployment constraint analysis와 직접 연결**되는 자연스러운 설계 변수입니다. 제한된 자원 환경에서 active expert 수를 줄이거나, 특정 상황에서 우선 활성화할 expert를 선택하는 식의 graceful degradation이 구조적으로 가능해집니다.

  

### Gating Network 학습

  

Gating network의 학습은 두 신호로 구성됩니다. 첫째 신호는 최종 contact proposal의 정확도로 역전파되는 gradient이며, 이는 gating이 정확한 예측에 기여하는 expert에 더 큰 가중치를 부여하도록 학습합니다. 둘째 신호는 load balancing loss로, 학습 데이터 전체에서 네 expert가 균등하게 활용되도록 강제하여 gating collapse (특정 expert만 항상 활성화되어 다른 expert가 학습되지 않는 현상) 를 방지합니다.

  

Load balancing의 강도는 하이퍼파라미터로, 너무 강하면 gating이 입력 비의존적으로 균등 가중치에 수렴하여 MoE의 의미가 사라지고, 너무 약하면 collapse가 발생합니다. 본 과제에서는 학습 초기에 강한 load balancing으로 모든 expert가 학습되도록 보장한 후, 학습이 진행됨에 따라 점진적으로 약화시키는 curriculum이 적용됩니다.

  

### S-Expert 내부의 계층적 Sub-MoE

  

S-expert 내부의 부위별 sub-MoE는 외부 MoE와 다른 역할을 수행합니다. 외부 MoE는 evidence 모달리티 (E/M/S/G) 를 분기하고, S-expert 내부 sub-MoE는 신체 부위 (손-팔, 다리-발, 몸통, 머리) 를 분기합니다. 이 계층적 구조는 PI의 AvatarMoE에서 검증된 부위별 동적 게이팅을 직접 재사용합니다.

  

격투 동작에서 부위별 접촉 빈도는 매우 비대칭적입니다. 태권도 동작에서는 다리-발 expert의 활용도가 높고, 레슬링 동작에서는 손-팔과 몸통 expert의 활용도가 높습니다. AvatarMoE의 자세 의존적 부위 인식 게이팅이 이 비대칭성을 자연스럽게 처리하며, 본 과제에서는 격투 동작 카탈로그의 부위별 접촉 빈도 분포를 gating prior로 활용하여 학습을 가속합니다.

  

이 계층적 sub-MoE는 분리 헤드 구조에서는 구현 불가능한 차원이며, MoE 구조의 PI 자산 활용도가 분리 헤드 구조보다 본질적으로 높은 핵심 이유입니다.

  

### Gating의 시간적 안정성

  

Gating network는 frame-level로 동작하지만, 격투 환경의 동작은 0.1초 미만의 짧은 시간 동안 여러 phase를 거치므로 gating weight가 frame 간에 급변할 수 있습니다. 이 급변은 expert 활성화 패턴이 불안정해지고 학습이 어려워지는 원인이 됩니다.

  

이를 완화하기 위해 gating weight에 약한 시간 정규화 (인접 프레임 간 변화 magnitude penalty) 를 적용합니다. 다만 이 정규화는 매우 약하게 적용되어, onset/offset 같은 명확한 이벤트 시점에서는 gating이 빠르게 전환될 수 있도록 허용합니다. 이는 본 연구의 시간 분해능 요구 (240 fps에서 4.17 ms 분해능 보존) 와 정합되는 설계입니다.

  

## 일반 시간 모델과의 차이점 논의

  

### 일반 시간 모델과의 본질적 차이

  

일반 시간 모델 (EMA, GRU, LSTM, Kalman filter) 은 evidence를 단일 입력 벡터로 처리하며 시간축에서 부드러운 평균을 내는 구조입니다. 이 구조는 두 본질적 한계를 가집니다. 첫째 한계는 **evidence 비대칭성을 활용하지 못한다는 점**으로, 한 evidence가 강하고 다른 evidence가 약한 상황에서 강한 evidence에 selective하게 의존할 메커니즘이 부재합니다. 둘째 한계는 **시각 evidence 감소의 두 원인 (접촉 해제 vs 가림) 을 구분하지 못한다는 점**으로, 단일한 평활화 동작이 두 상황에 모두 동일하게 적용됩니다.

  

### MoE 구조의 차별성: Evidence 추출 단계

  

MoE 구조는 evidence 추출 단계부터 일반 시간 모델과 본질적으로 차별화됩니다. 일반 시간 모델이 evidence를 entangled 형태로 처리하는 반면, MoE 구조는 **각 evidence가 독립된 expert에서 추출되며 expert별 backbone이 자기 evidence에 특화된 representation을 학습**합니다.

  

이 차이는 격투 환경의 evidence 비대칭 상황에서 직접 드러납니다. Motion blur 상황에서 일반 시간 모델은 visual feature 전체가 약화된 채로 시간 평활화에 진입하지만, MoE 구조에서는 E-expert만 영향을 받고 M-expert는 자체 backbone에서 motion 신호를 정상적으로 추출합니다. Confidence head와 gating network가 이중으로 E-expert의 영향을 약화시키고 M-expert를 강화하여, motion blur 환경에서도 정확한 contact proposal이 가능합니다.

  

분리 헤드 구조와 비교하면, **MoE 구조는 backbone 단계부터 evidence 분리가 시작되므로 evidence 특화도가 더 강합니다**. 분리 헤드 구조의 backbone은 네 evidence의 평균 신호에 최적화되지만, MoE의 expert backbone은 자기 evidence에만 최적화됩니다. 이는 evidence 비대칭성이 backbone representation에 직접 인코딩됨을 의미하며, 격투 환경의 극단적 evidence 비대칭 상황 (예: 회전 발차기 직후의 motion blur + occlusion 동시 발생) 에서 MoE 구조의 우위가 명확해집니다.

  

### MoE 구조의 차별성: 이중 비대칭 처리

  

분리 헤드 구조의 차별성은 evidence별 confidence 가중 fusion이라는 단일 비대칭 처리에 있는 반면, MoE 구조는 **gating weight와 confidence가 이중으로 작용하는 두 층 비대칭**을 가집니다. Gating은 expert 활성화의 비대칭성을, confidence는 evidence 신뢰도의 비대칭성을 처리하며, 두 메커니즘이 독립적으로 학습되어 서로 다른 신호를 제공합니다.

  

이 이중 비대칭은 fusion 단계에서 단순 곱셈이나 합산으로 결합되지 않고, 학습된 fusion module이 두 신호의 상호작용을 처리합니다. 예를 들어 gating이 M-expert를 강하게 활성화했지만 confidence α_M이 낮은 상황에서는 fusion이 M-expert의 출력을 부분적으로만 신뢰하고 다른 expert와 적극적으로 결합하며, gating이 약하게 활성화하고 confidence가 높은 expert의 출력은 보조적으로 활용됩니다. 이 미묘한 처리는 일반 시간 모델은 물론 분리 헤드 구조에서도 표현하기 어려운 차원입니다.

  

### MoE 구조의 차별성: 시간 처리 단계

  

1차년도 MoE 구조 자체는 본격적 시간 제어를 수행하지 않으며, 시간 차원의 비대칭 처리는 2차년도 4-gate 메모리 제어에서 완성됩니다. 그러나 1차년도 단계에서도 일반 시간 모델과의 구조적 차별성은 다음 측면에서 나타납니다.

  

**Evidence별 시간 처리의 분리**가 가장 중요한 차이입니다. 일반 시간 모델은 모든 evidence가 동일한 시간 처리 (동일한 RNN cell, 동일한 EMA 가중치) 를 거치지만, MoE 구조에서는 M-expert가 자체 short-window temporal backbone을 가지고 다른 expert는 frame-level로 동작합니다. 이 분리는 onset 검출 시간 분해능을 M-expert의 window size로 한정하면서 다른 expert의 frame-level 처리를 보존합니다.

  

분리 헤드 구조에서도 M-head가 short-window temporal processing을 수행할 수 있지만, backbone이 공유되므로 backbone 자체가 frame-level이어야 한다는 제약이 있습니다. MoE 구조에서는 M-expert가 자체 backbone을 가지므로 더 깊은 temporal feature를 추출할 수 있으며, 격투 환경의 복잡한 motion 패턴을 더 정밀하게 표현할 수 있습니다.

  

### 1차년도 MoE 검증의 정당화

  

1차년도 MoE 구조의 학술적 기여는 분리 헤드 구조보다 강한 차별성을 가지며, 이는 단독으로도 출판 가능한 산출물입니다. 정당화의 핵심은 **격투 환경에서 evidence별 expert 특화가 단순 confidence 가중보다 더 강한 비대칭 처리를 가능하게 하며, 이중 비대칭 (gating + confidence) 이 단일 비대칭 (confidence only) 보다 우수하다**는 가설의 정량 입증입니다.

  

검증 protocol은 세 층으로 구성됩니다. 첫째 층은 표준 데이터셋에서의 정확도 비교로, 일반 시간 모델 baseline과 분리 헤드 구조 baseline 모두에 대해 MoE 구조의 우위를 측정합니다. 둘째 층은 evidence별 ablation으로, expert를 하나씩 제거했을 때의 성능 저하를 측정하여 evidence 분리의 효과를 정량화합니다. 셋째 층은 evidence별 corruption injection으로, 특정 expert의 출력을 의도적으로 오염시켰을 때 다른 expert가 얼마나 보완하는지를 측정합니다.

  

세 번째 층의 corruption injection은 MoE 구조에서만 정밀하게 수행 가능한 ablation이며, 이는 MoE 구조의 학술적 차별성을 직접 입증하는 핵심 평가입니다. 분리 헤드 구조에서는 head-level injection만 가능하지만, MoE 구조에서는 expert-level injection이 가능하여 mechanistic 분석의 깊이가 본질적으로 다릅니다.

  

### 2차년도 4-gate와의 연결성

  

1차년도 MoE 구조의 expert별 confidence와 gating weight는 2차년도 4-gate 메커니즘의 풍부한 입력을 제공합니다. 4-gate의 각 게이트는 자기에게 필요한 evidence 조합에 selective하게 의존하는데, MoE 구조의 expert별 분리 출력이 이 selective 의존성을 자연스럽게 표현합니다.

  

Onset-write gate는 M-expert와 E-expert의 출력에 강하게 의존하고 G-expert에 약하게 의존, occlusion-decay gate는 E-expert의 출력 약화와 M-expert의 출력 안정성을 동시에 검출, offset-reset gate는 M-expert와 E-expert의 분리 단서에 의존하는 식의 evidence별 비대칭 활용이 MoE 구조에서 명확히 구현됩니다. 분리 헤드 구조에서도 이 비대칭 활용이 가능하지만, evidence가 공유 backbone에서 추출되므로 expert 간 entanglement로 인해 비대칭 활용의 명확성이 떨어집니다.

  

따라서 1차년도 MoE 구조는 단순 baseline 확보가 아니라 **2차년도 4-gate가 가장 정밀하게 작동 가능한 evidence 처리 구조**를 제공하며, 본 연구 전체의 학술적 명제를 evidence-level에서 가장 강하게 입증하는 구조적 기반입니다. 분리 헤드 구조와 비교하면 1차년도 단계에서 더 큰 학습 부담과 데이터 요구량을 감수하지만, 2차년도 이후의 mechanistic 분석 깊이와 학술적 차별성에서 본질적 우위를 가집니다.