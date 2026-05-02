## 시공간적 증거 기반 접촉 신뢰도 추정
---
### Evidence별 추출 메커니즘

**시각 증거 $E_t$** 는 image backbone의 frame-level feature에서 두 인체 표면의 접촉 단서를 직접 추출합니다. 영상에 직접 관찰되는 접촉의 visual cue (피부 변형, 의복 주름, 조명 변화 등) 가 주된 학습 대상이며, E-head는 backbone feature를 입력으로 받아 두 인체 사이의 접촉 가능성 map을 출력합니다. PI의 D2FP 경험에서 입력 의존적 implicit body prior를 query 형태로 추출한 설계 원리가 E-head의 구조적 기반이 됩니다.

**운동 불연속성 $M_t$** 는 인접 프레임의 backbone feature 또는 fitted SMPL vertex의 시간 변화로부터 두 인체 표면 간 상대 속도의 급변을 검출합니다. M-head는 short-window temporal processing (3-5 프레임) 을 자체적으로 수행하며, 이 window size가 onset 검출 시간 분해능의 상한을 결정합니다. 본 연구의 자체 240 fps benchmark에서 4.17 ms 분해능을 보존하기 위해, M-head의 temporal window는 출력 시간 분해능을 frame-level로 유지하는 (2+1)D 구조로 설계됩니다.

**부위 사전 정보 $S_t$** 는 어느 신체 부위가 접촉할 가능성이 높은지에 대한 사전 지식을 제공하며, SMPL parameter로부터 부위별 위치를 직접 supervision받아 학습됩니다. S-head는 PI의 D2FP에서 검증된 부위별 query 추출 방식을 본 과제의 부위 접촉 사전 정보 형태로 재설계하며, 격투 동작의 표준 카탈로그 (앞차기, 돌려차기, 옆차기 등) 에서 부위별 접촉 빈도 분포를 prior로 활용합니다.

**기하 증거 $G_t$** 는 mesh surface 간 거리와 법선 일관성으로 산출되며, 단독으로 사용되지 않고 보조 신호로만 활용됩니다. G-head는 $t-1$ 시점의 fitted mesh로부터 $G_t$를 계산하여 시간 차원의 의존성 순환을 회피하며, 이 처리는 본 연구의 핵심 명제 (피드백 루프 차단) 가 evidence 추출 단계에서도 보존되도록 보장합니다.
### 신뢰도 추정 메커니즘

각 evidence head는 자체 confidence head $α$를 동반합니다. $α_E, α_M, α_S, α_G$는 각각 해당 evidence의 신뢰도를 $[0, 1]$ 범위로 추정하며, 이 신뢰도는 격투 환경의 evidence 비대칭 상황 (motion blur, occlusion, 정적 접촉 유지 등) 에서 어느 evidence를 더 신뢰할지를 결정합니다.

신뢰도 추정의 학습 신호는 두 층으로 구성됩니다. 첫째 층은 evidence 자체의 정확도와 신뢰도의 일관성으로, 정확한 evidence에 대해 높은 confidence를, 부정확한 evidence에 대해 낮은 confidence를 부여하도록 학습됩니다. 둘째 층은 최종 contact proposal의 정확도로 역전파되는 신호로, confidence가 가중 결합에서 적절한 가중치를 부여하여 최종 예측 정확도를 향상시키도록 학습됩니다.

PI의 Confidence-Guided Depth 경험에서 LiDAR 깊이맵 보완 도메인의 신뢰도 기반 selective filtering 메커니즘이 본 confidence head 설계의 알고리즘 패러다임 차원 자산입니다. LiDAR vs 시각 접촉이라는 modality 차이가 있으나, 신뢰도를 별도 head로 추정하고 가중 결합에 활용하는 설계 원리는 직접 재사용됩니다.

### Confidence-Weighted Fusion

네 evidence와 그 신뢰도는 confidence-weighted fusion으로 결합되어 최종 contact proposal Ĉ_t를 산출합니다. Fusion은 단순 가중 평균이 아니라 **신뢰도가 매우 낮은 evidence를 자동으로 배제하는 selective filtering** 형태로 설계됩니다. 이는 격투 환경의 evidence 비대칭성에서 한 evidence가 거의 신뢰할 수 없을 때 그 evidence가 노이즈로 작용하지 않도록 보장하는 메커니즘입니다.

Fusion 출력은 contact proposal과 그 자체의 uncertainty로 구성되며, 이 uncertainty가 후속 4-gate 메모리 제어 (2차년도) 의 입력으로 전달됩니다. 즉 1차년도 산출물의 학술적 가치는 단순 정확도가 아니라 **uncertainty-aware contact proposal**을 제공한다는 점에 있으며, 이는 4-gate가 잘못된 접촉을 메모리에 잘못 기록하는 것을 사전에 방지하는 구조적 기반입니다.