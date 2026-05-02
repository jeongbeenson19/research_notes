# 2차년도 MoE 구조 — 분리 헤드 구조와 달라지는 지점

  

## 전체 구조 변경 개요

  

2차년도의 핵심 contribution인 4-gate 비대칭 메모리 제어, Online Self-Correction, Auxiliary Supervision, 다섯 평가 지표는 **MoE 구조에서도 동일한 골격**을 유지합니다. 4-gate가 evidence와 confidence를 입력받아 시간 차원의 비대칭 처리를 수행한다는 본질은 변하지 않으며, 분리 헤드 구조와 MoE 구조의 차이는 **4-gate에 입력되는 evidence의 표현 방식과 corruption injection의 정밀도**에서 주로 나타납니다. 따라서 이 답변은 분리 헤드 구조 답변에서 동일한 부분은 생략하고 **달라지는 지점만**을 정리합니다.

  

## 모델 모식도에서 달라지는 부분

  

```

[1차년도 MoE 산출물]

Expert별 evidence (E_t, M_t, S_t, G_t)

+ Expert별 confidence (α_E, α_M, α_S, α_G)

+ Gating weights (g_E, g_M, g_S, g_G) ◄── NEW

+ uncertainty-aware contact proposal Ĉ_t

│

▼

┌────────────────────────────────────┐

│ Event Detection Module │

│ (이벤트 분류기) │

│ │

│ Expert-specific event evidence: │ ◄── NEW

│ - Onset: M-expert ↑ + E-expert ↑ │

│ + S-expert match │

│ - Offset: M-expert separation + │

│ E-expert separation │

│ - Occlusion: E-expert ↓ + │

│ M-expert flat │

│ - Maintain: 기타 │

└────────────────────────────────────┘

│

Event probabilities

│

▼

┌────────────────────────────────────┐

│ 4-Gate Asymmetric Memory Control │

│ │

│ Gate별 expert dependency: │ ◄── NEW

│ - Onset gate: M, E expert에 강의존│

│ - Offset gate: M, E expert에 강의존│

│ - Occlusion gate: E↓ + M-flat 검출│

│ - Maintain gate: 모든 expert 약신호│

│ │

│ 각 gate가 expert 출력에 대한 │

│ selective cross-attention 수행 │ ◄── NEW

└────────────────────────────────────┘

│

Temporal contact state C_{t+1}

│

┌─────────────────┴─────────────────┐

│ │

▼ ▼

Mesh refinement Online Self-Correction

& SMPL fitting Module

│ │

▼ ▼

Mesh sequence Drift detection (분리 헤드와 동일)

│ │

└─────────────────┬─────────────────┘

│

▼

Correction signal

│

└──────► Feedback to 4-gate

+ Expert-specific routing ◄── NEW

(어느 expert의 출력을 우선 신뢰할지

교정 단계에서 재결정)

  

[학습 단계 추가 모듈]

Auxiliary Supervision (분리 헤드와 공통)

+ Expert-specific consistency loss ◄── NEW

+ Gating stability under corruption ◄── NEW

```

  

분리 헤드 구조와의 모식도 차이는 (1) 1차년도 산출물에 gating weight가 추가로 포함, (2) Event Detection이 expert별 evidence에 명시적으로 분리 의존, (3) 4-Gate가 expert 출력에 대한 selective cross-attention을 수행, (4) Online Self-Correction의 교정 신호가 expert별 routing 재결정까지 포함, (5) 학습 단계에 expert-specific consistency loss와 gating stability loss가 추가된 다섯 부분입니다.

  

## 4-Gate Asymmetric Memory Control에서 달라지는 부분

  

### Gate별 Expert Cross-Attention 구조

  

분리 헤드 구조의 4-gate는 evidence와 confidence를 단일 벡터로 입력받아 게이트를 활성화하는데, MoE 구조에서는 **각 gate가 자기에게 필요한 expert 출력에 selective cross-attention**하는 구조로 정밀화됩니다.

  

이는 1차 답변에서 언급한 **gate 반영 단계의 가장 큰 도전**이 MoE 구조에서 명시적 형태로 구현된다는 의미입니다. Onset gate는 M-expert와 E-expert 출력을 query로, S-expert 출력을 key/value로 cross-attention하여 "운동 급변과 시각 급변이 부위 사전 정보와 일치하는가"를 직접 검증합니다. Offset gate는 M-expert와 E-expert의 분리 단서에 cross-attention하며, Occlusion gate는 E-expert의 약화와 M-expert의 안정성을 동시에 query하는 dual-condition cross-attention을 수행합니다.

  

분리 헤드 구조에서는 evidence가 공유 backbone에서 추출되므로 cross-attention이 evidence별로 명확히 분리되지 않지만, MoE 구조에서는 expert별 출력이 독립적이므로 **각 gate의 evidence 의존성이 attention weight로 명시적으로 표현**됩니다. 이는 onset-offset asymmetry score (지표 5) 의 evidence-level asymmetry 측정을 attention weight 분석으로 정밀하게 수행 가능하게 하는 구조적 기반입니다.

  

### Gating Weight와 Gate Activation의 상호작용

  

MoE 구조에서는 1차년도의 gating weight (g_E, g_M, g_S, g_G) 가 4-gate의 게이트 활성화와 상호작용합니다. Onset 시점에 gating이 g_M과 g_E를 높게 활성화한 상황에서 onset gate가 활성화되면, **두 비대칭 메커니즘이 일관된 신호를 제공**하므로 onset 검출 신뢰도가 높습니다. 반대로 gating이 g_S만 높게 활성화한 상황에서 onset gate가 활성화되면, 두 메커니즘이 불일치하므로 onset 검출 신뢰도가 낮습니다.

  

이 일관성 검증은 분리 헤드 구조에서는 불가능한 차원이며, **MoE 구조의 이중 비대칭 (gating + gate) 이 시간 차원에서 자기 검증 메커니즘**으로 작동합니다. 잘못된 onset 검출의 위험을 두 메커니즘의 일관성 요구로 자연스럽게 감소시키며, 이는 contact hysteresis와 mesh drift cascade 차단에 기여합니다.

  

## Online Self-Correction Module에서 달라지는 부분

  

### Expert-Specific Routing 재결정

  

분리 헤드 구조의 self-correction은 메모리 정리, 재기록, 재초기화의 세 교정 신호를 4-gate에 전달하지만, MoE 구조에서는 **어느 expert의 출력을 교정 단계에서 우선 신뢰할지를 재결정**하는 추가 차원이 있습니다.

  

예를 들어 drift detection이 t 시점의 메쉬에서 비물리적 자세를 검출했을 때, drift의 원인이 어느 expert의 잘못된 출력에서 비롯되었는지를 추정합니다. Drift가 두 인체의 비현실적 근접 (interpenetration) 형태이면 G-expert의 잘못된 geometric evidence가 원인일 가능성이 높고, drift가 비물리적 motion (joint velocity 급변) 형태이면 M-expert의 잘못된 motion 신호가 원인일 가능성이 높습니다.

  

Self-correction은 추정된 원인 expert의 영향을 일시적으로 약화시키고 다른 expert의 출력을 보강하는 routing 재결정을 수행합니다. 이는 **drift 원인의 expert-level 분해**가 가능한 MoE 구조에서만 구현 가능한 메커니즘이며, 분리 헤드 구조에서는 evidence가 entangled되어 drift 원인의 분해가 어렵습니다.

  

### Drift Detection의 Expert별 분해

  

Drift detection 자체도 MoE 구조에서 정밀화됩니다. 분리 헤드 구조에서는 drift가 "메쉬 시퀀스의 비물리적 변화"라는 단일 신호로 검출되지만, MoE 구조에서는 expert별 출력의 시간 변화를 독립적으로 모니터링하여 어느 expert에서 비정상 패턴이 발생했는지를 분해 검출합니다.

  

예를 들어 M-expert의 출력이 시간적으로 inconsistent한 패턴을 보이면 M-expert의 motion 신호가 신뢰할 수 없는 상태로 진입했음을 의미하고, E-expert의 출력이 갑자기 약화되면 occlusion 시작을 의미합니다. 두 신호는 동일한 메쉬 drift로 발현될 수 있지만 원인이 다르며, 다른 교정 신호가 필요합니다. 이 expert-level drift detection은 다음 답변에서 상세히 다룰 평가 protocol의 정밀도와도 직접 연결됩니다.

  

## Auxiliary Supervision에서 달라지는 부분

  

### Expert-Specific Consistency Loss

  

분리 헤드 구조의 보조 감독은 drift prediction, inconsistency detection, onset/offset event consistency의 세 항목으로 구성되는데, MoE 구조에서는 **expert-specific consistency loss**가 추가됩니다.

  

이 loss는 학습 단계에서 각 expert의 출력이 시간 차원에서 자기 일관성을 가지도록 강제합니다. M-expert의 출력은 인접 프레임 간 motion 신호의 자연스러운 연속성을 유지해야 하고, S-expert의 출력은 부위 위치의 점진적 변화를 따라야 하며, G-expert의 출력은 메쉬 변화에 일관된 응답을 보여야 합니다. Expert별로 별도 일관성 loss를 부여하면, 한 expert의 일시적 오류가 다른 expert로 전파되는 것을 학습 단계에서 명시적으로 차단할 수 있습니다.

  

분리 헤드 구조에서는 evidence가 공유 backbone에서 추출되므로 expert-specific 일관성 정의 자체가 불가능합니다. 단일 evidence vector의 일관성만 정의 가능하며, 이는 evidence별 비대칭 일관성을 표현하지 못합니다.

  

### Gating Stability under Corruption

  

MoE 구조의 학습 단계에 추가되는 또 하나의 보조 감독은 **corruption injection 환경에서의 gating 안정성**입니다. 학습 단계에서 의도적으로 한 expert의 출력을 오염시킨 후, gating network가 오염된 expert의 가중치를 자동으로 낮추고 다른 expert로 routing을 재분배하도록 학습됩니다.

  

이 학습은 inference 단계에서 evidence가 부분적으로 신뢰할 수 없을 때 gating이 자동으로 안정적인 expert에 의존하도록 보장하며, 본 연구의 핵심 명제 (잘못된 evidence의 시간적 전파 차단) 를 gating 차원에서도 강화합니다. 분리 헤드 구조에서는 gating network 자체가 없으므로 이 차원의 학습이 부재합니다.

  

### Pseudo GT 안정성 추가 고려

  

1차년도에서 pseudo GT의 노이즈 문제를 다뤘는데, 2차년도 학습 단계에서도 이 문제가 지속됩니다. 보조 감독의 학습 신호가 pseudo GT에 의존할 때, pseudo GT의 노이즈가 보조 감독의 신뢰도를 약화시킬 수 있습니다. 이를 완화하기 위해 **각 보조 감독 loss에 pseudo GT confidence를 가중**으로 적용하여, pseudo GT 신뢰도가 낮은 프레임의 학습 영향을 약화시키는 noise-robust 학습을 적용합니다.

  

이는 분리 헤드 구조에서는 implicit supervision이 주된 학습 신호이므로 pseudo GT 의존도가 낮지만, MoE 구조에서는 expert 특화를 위한 pseudo GT 의존도가 높으므로 noise robustness가 결정적입니다.

  

## 평가 기법에서 달라지는 부분

  

### 다섯 지표의 측정 방식 정밀화

  

다섯 평가 지표 (contact hysteresis, post-contact MPJPE drift, contact-conditioned MPJPE, interpenetration volume, onset-offset asymmetry score) 자체는 MoE 구조에서도 동일하게 정의됩니다. 그러나 측정 방식이 정밀화됩니다.

  

**Onset-offset asymmetry score**의 evidence-level asymmetry 측정이 MoE 구조에서 본격적으로 가능해집니다. Onset 시점과 offset 시점에서 어느 expert에 더 의존하는지를 gating weight와 gate cross-attention weight로 직접 측정 가능하며, "onset은 M-expert에 60%, E-expert에 30%, S-expert에 10% 의존하고 offset은 M-expert에 40%, E-expert에 50%, S-expert에 10% 의존한다"는 식의 정량 보고가 가능합니다. 분리 헤드 구조에서는 evidence별 ablation으로만 간접 측정 가능하지만, MoE 구조에서는 직접 측정이 가능합니다.

  

### Contact-Corruption Injection의 차원 확장

  

본 연구의 핵심 평가인 contact-corruption injection이 MoE 구조에서 본격적으로 정밀화됩니다. 분리 헤드 구조에서는 head-level injection (특정 head 출력을 오염) 만 가능하지만, MoE 구조에서는 **expert-level injection**이 가능합니다.

  

차원 확장의 구체적 형태는 (1) **Evidence 종류별 주입**으로 E-expert만 오염, M-expert만 오염, S-expert만 오염, G-expert만 오염을 비교, (2) **Evidence 강도별 주입**으로 각 expert의 confidence를 단계적으로 낮추는 sweep 수행, (3) **Evidence 조합별 주입**으로 두 expert를 동시에 오염시켜 4-gate의 redundancy 측정, (4) **시간적 주입 패턴**으로 단일 프레임 spike, 짧은 burst, 지속적 오염을 비교, (5) **Gating 오염 주입**으로 gating weight 자체를 의도적으로 잘못된 expert에 분배하여 gating의 robustness 측정의 다섯 차원입니다.

  

이 다섯 차원의 protocol은 분리 헤드 구조에서는 일부만 수행 가능하며, MoE 구조에서만 완전한 형태로 가능합니다. 학술적 의미는 단순 ablation 풍부도가 아니라 **본 연구의 차별성을 mechanistic하게 입증할 evidence가 5배 증가**한다는 점입니다. Top-tier 학회 reviewer가 요구하는 "왜 이 메커니즘이 작동하는가"의 깊이 있는 분석에 직접 대응합니다.

  

### Expert-Level Robustness Profile

  

MoE 구조에서 새롭게 정의되는 평가 항목은 **expert-level robustness profile**입니다. 각 expert를 독립적으로 오염시킨 corruption injection 결과를 종합하여, "본 연구의 메커니즘이 어떤 종류의 evidence 오염에 강하고 어떤 종류에 약한가"를 expert별 분해하여 보고합니다.

  

예를 들어 4-gate가 visual evidence 오염은 잘 차단하지만 motion evidence 오염은 상대적으로 취약하다는 식의 결함 분석이 가능하며, 이는 본 연구의 학술적 정직성을 강화합니다. 모든 evidence에 대해 일관되게 강건하다는 비현실적 주장이 아니라, evidence별로 차이가 있고 그 차이의 원인이 메커니즘 설계와 일관된다는 mechanistic 설명을 제공합니다.

  

이 robustness profile은 3차년도 deployment constraint analysis와도 직접 연결됩니다. 제한된 자원 환경에서 어느 expert를 우선 활성화할지의 전략이 robustness profile에 기반하여 결정될 수 있으며, "motion evidence가 약화되는 환경에서는 visual evidence와 part prior에 selective하게 의존하는 graceful degradation 전략" 같은 구체적 권고가 가능합니다.

  

## 종합

  

2차년도 MoE 구조는 분리 헤드 구조와 동일한 4-gate, Self-Correction, Auxiliary Supervision, 다섯 평가 지표의 골격을 유지하되, **다음 다섯 차원에서 정밀화**됩니다.

  

첫째, 4-gate가 expert별 출력에 selective cross-attention하여 evidence별 비대칭 의존성이 명시적으로 표현됩니다. 둘째, gating weight와 gate activation의 이중 비대칭이 시간 차원에서 자기 검증 메커니즘으로 작동합니다. 셋째, Online Self-Correction의 교정 신호가 expert-level routing 재결정까지 확장됩니다. 넷째, Auxiliary Supervision에 expert-specific consistency loss와 gating stability under corruption이 추가됩니다. 다섯째, Contact-corruption injection이 expert-level injection으로 확장되어 다섯 차원의 정밀 protocol이 가능해지며 expert-level robustness profile이라는 새로운 평가 항목이 추가됩니다.

  

이 정밀화는 학술적 차별성을 강화하지만 학습 데이터 요구량과 구현 복잡도를 증가시키므로, **분리 헤드 구조 → MoE 구조의 단계적 진화**가 본 과제의 4년 일정에서 가장 안전한 경로입니다. 1-2차년도는 분리 헤드 구조로 안정적 산출물을 확보하고, 3-4차년도에 MoE 구조로 확장하여 위 다섯 차원의 정밀화를 데이터셋 공개와 함께 최종 형태로 제시하는 진화 경로가 권고됩니다.