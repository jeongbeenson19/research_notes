# 1-2차년도 아키텍처 요약본

  

## 한 줄 정의

  

본 연구는 고속 격투형 인체 상호작용 영상에서 접촉 추정 오류가 시간적으로 누적되어 메쉬 복원을 망가뜨리는 문제를 줄이기 위한 구조를 설계한다. 1차년도는 접촉 후보와 evidence별 confidence를 안정적으로 추정하고, 2차년도는 4-gate 메모리 제어와 self-correction으로 오류 전파를 차단하는 단계다.

  

## 전체 방향

  

핵심 입력은 두 인체의 close-interaction video frame sequence이며, 모델은 접촉 후보, 접촉 상태, SMPL/mesh 복원 결과를 출력한다. 접촉 판단에는 네 종류의 evidence를 사용한다.

  

| Evidence | 의미 | 역할 |

|---|---|---|

| E: Visual evidence | 영상에서 직접 보이는 접촉 단서 | 접촉 여부의 직접 관찰 신호 |

| M: Motion discontinuity | 상대 속도 급변, 운동 불연속성 | 접촉 시작/해제 같은 이벤트 감지 |

| S: Part prior | 어떤 신체 부위가 접촉하기 쉬운지에 대한 사전 정보 | 격투 동작별 접촉 부위 prior 제공 |

| G: Geometry evidence | mesh surface 거리, normal, SDF 등 | 접촉의 물리적 타당성 보조 |

  

본 연구의 차별성은 evidence를 하나의 feature로 뭉개지 않고, evidence별 신뢰도와 시간 이벤트를 분리해서 다룬다는 점이다. 일반적인 EMA, GRU, LSTM, Kalman filter는 시간축에서 부드러운 평균을 내는 방식이라, 시각 evidence가 약해졌을 때 그것이 실제 접촉 해제인지 occlusion인지 구분하기 어렵다. 본 연구는 이 구분을 구조적으로 해결하려 한다.

  

## 1차년도 목표

  

1차년도의 목표는 2차년도 4-gate 메커니즘이 신뢰할 수 있는 입력을 받도록, evidence별 접촉 신호와 confidence를 안정적으로 추정하는 것이다.

  

주요 산출물은 다음과 같다.

  

- Evidence별 출력: E_t, M_t, S_t, G_t

- Evidence별 confidence: alpha_E, alpha_M, alpha_S, alpha_G

- Confidence-weighted contact proposal: C_hat_t

- 후속 4-gate 입력으로 사용할 uncertainty-aware contact proposal

  

### 1차년도 분리 헤드 구조

  

분리 헤드 구조는 하나의 image backbone을 공유하고, 그 위에 E/M/S/G별 head를 따로 붙이는 방식이다. Backbone은 D2FP pretrained weight로 초기화하고, 각 head는 자기 evidence를 추출한다.

  

장점은 구현과 학습이 안정적이라는 점이다. Pilot 데이터 규모가 작아도 backbone을 공유하므로 학습 부담이 낮고, 1차년도 baseline을 빠르게 확보할 수 있다. Confidence-guided fusion도 비교적 단순하게 구현할 수 있다.

  

단점은 evidence 분리가 head 단계에서만 일어나기 때문에, backbone representation은 네 evidence의 평균적인 신호에 맞춰질 가능성이 높다. 따라서 evidence별 특화나 corruption injection 분석의 깊이는 제한된다.

  

분리 헤드 구조의 핵심 메시지는 다음과 같다.

  

- 1차년도 안정적 baseline에 적합하다.

- Evidence별 confidence를 통해 motion blur, occlusion, 정적 접촉 유지 상황을 구분할 수 있다.

- 2차년도 4-gate가 작동하기 위한 최소한의 evidence 분리 구조를 제공한다.

- 다만 MoE에 비해 mechanistic 분석력과 evidence 특화도는 낮다.

  

### 1차년도 MoE 구조

  

MoE 구조는 E/M/S/G별 expert를 독립적으로 두고, gating network가 현재 입력에 따라 어느 expert를 얼마나 활성화할지 결정하는 방식이다. 분리 헤드 구조와의 가장 큰 차이는 evidence 분리가 backbone 단계부터 시작된다는 점이다.

  

MoE에서는 각 expert가 자기 evidence에 특화된 representation을 학습한다.

  

| Expert | 역할 |

|---|---|

| E-expert | visual contact cue 추출 |

| M-expert | short-window temporal backbone으로 motion discontinuity 추출 |

| S-expert | body-part prior 추출, 내부적으로 part-level sub-MoE 가능 |

| G-expert | 이전 시점 mesh 기반 SDF/geometry evidence 추출 |

  

MoE의 핵심은 confidence와 gating이 서로 다른 역할을 한다는 점이다. Confidence는 해당 evidence가 얼마나 믿을 만한지를 추정하고, gating은 현재 입력에서 어떤 expert에 계산 자원을 줄지 결정한다. 예를 들어 motion blur가 있으면 E-expert confidence는 낮아지고, gating은 M-expert 쪽으로 더 기울 수 있다.

  

장점은 학술적 차별성이 강하다는 점이다. Expert-level corruption injection, evidence-level asymmetry 분석, expert별 robustness profile 같은 정밀 분석이 가능하다. AvatarMoE의 gating 자산도 구조적으로 활용하기 쉽다.

  

단점은 학습 안정성과 데이터 요구량이다. 1차년도 30-50 clips 규모에서 네 expert와 gating을 동시에 안정적으로 학습하기는 어렵다. Gating collapse, pseudo GT noise, expert별 pretraining 부담이 주요 위험이다.

  

MoE 구조의 핵심 메시지는 다음과 같다.

  

- Evidence 특화와 mechanistic 분석에는 가장 강하다.

- Gating + confidence의 이중 비대칭 처리가 가능하다.

- 3차년도 이후 deployment constraint 분석과도 잘 연결된다.

- 하지만 1차년도부터 주 구조로 쓰기에는 학습 안정성 위험이 크다.

  

## 2차년도 목표

  

2차년도 목표는 1차년도에서 얻은 contact proposal과 evidence confidence를 이용해, 접촉 오류가 시간적으로 누적되는 현상을 차단하는 것이다.

  

여기서 오류 누적은 단순히 한 프레임의 오류가 크다는 뜻이 아니다. t 시점의 오류가 t+1, t+2 시점의 오류 발생 확률을 높이는 시간적 의존 관계를 의미한다.

  

본 연구가 다루는 대표 오류 패턴은 세 가지다.

  

| 오류 패턴 | 설명 | 주된 대응 |

|---|---|---|

| Contact hysteresis | 실제 접촉이 끝났는데 메모리에 접촉이 남아 있는 현상 | Offset-reset gate |

| Mesh drift cascade | 잘못된 접촉이 mesh를 왜곡하고, 왜곡된 mesh가 다시 evidence를 망가뜨리는 루프 | Self-correction, drift detection |

| Occlusion-induced memory corruption | 가림을 접촉 해제로 오해해 메모리가 잘못 초기화되는 현상 | Occlusion-decay gate |

  

### 2차년도 분리 헤드 구조

  

분리 헤드 기반 2차년도 구조는 1차년도 출력인 E/M/S/G와 confidence를 받아 Event Detection, 4-Gate Memory Control, Online Self-Correction을 수행한다.

  

4-gate의 역할은 다음과 같다.

  

| Gate | 활성 조건 | 메모리 동작 |

|---|---|---|

| Onset-write | M_t 급증 + E_t 급증 + S_t 부위 prior 일치 | 새 contact를 빠르게 기록 |

| Offset-reset | 분리 운동 + visual separation 단서 | contact memory를 즉시 초기화 |

| Occlusion-decay | E_t 급감 + M_t는 안정적 + pose 변화 작음 | 메모리를 천천히 감쇠, 초기화하지 않음 |

| Maintain | 위 세 이벤트가 아닌 안정 상태 | 기존 메모리 유지 |

  

Online Self-Correction은 mesh sequence에서 drift를 감지하고, 필요하면 4-gate에 교정 신호를 보낸다. 교정 신호는 메모리 정리, 누락된 onset 재기록, 심하게 오염된 메모리 재초기화로 나뉜다.

  

보조 감독은 세 가지로 구성된다.

  

- Drift prediction head: 현재 evidence와 memory로 미래 drift를 예측

- Inconsistency detection head: t-1, t, t+1 mesh sequence의 시간 일관성 판단

- Onset/offset event consistency loss: onset, offset, occlusion이 서로 다른 메모리 동작을 갖도록 강제

  

이때 oracle event timing에 과도하게 의존하지 않는 것이 중요하다. 정답 onset/offset timing은 학습 안정화나 상한 비교에 제한적으로만 쓰고, 최종 보고는 모델이 예측한 이벤트 시점 기준으로 수행해야 한다.

  

### 2차년도 MoE 구조

  

MoE 기반 2차년도 구조는 2차년도 전체 골격은 동일하게 유지하되, expert 단위로 더 정밀해진다.

  

분리 헤드 구조와 달라지는 핵심은 다음이다.

  

- 4-gate가 expert별 출력에 selective cross-attention을 수행한다.

- Gating weight와 gate activation이 서로 일관되는지 확인하는 이중 비대칭 구조가 생긴다.

- Self-correction이 단순 memory correction을 넘어 expert-specific routing 재결정까지 수행한다.

- Drift detection을 expert별로 분해할 수 있다.

- Auxiliary supervision에 expert-specific consistency loss와 gating stability under corruption이 추가된다.

  

예를 들어 onset gate는 M-expert와 E-expert를 강하게 보고, S-expert를 보조적으로 참고할 수 있다. Occlusion gate는 E-expert 약화와 M-expert 안정성을 동시에 본다. 이런 expert별 의존성은 attention weight와 gating weight로 직접 측정 가능하기 때문에, evidence-level asymmetry 분석이 훨씬 명확해진다.

  

다만 MoE 기반 2차년도는 1차년도 MoE의 학습 안정성이 확보되어야 의미가 있다. 1차년도에서 expert가 충분히 특화되지 않았거나 gating이 collapse되면, 2차년도 expert-level 분석도 신뢰하기 어렵다.

  

## 평가 계획 요약

  

2차년도의 평가는 단순 정확도보다 오류 전파 차단을 직접 보여주는 지표가 핵심이다.

  

| 지표 | 측정 대상 |

|---|---|

| Contact Hysteresis Error | 접촉 종료 이후 contact memory가 얼마나 남는지 |

| Post-Contact MPJPE Drift | 접촉 종료 이후 mesh error가 얼마나 누적되는지 |

| Contact-Conditioned MPJPE | 접촉/비접촉/transition 구간별 mesh error |

| Interpenetration Volume / Depth | 두 mesh가 서로 침투하는 정도 |

| Onset-Offset Asymmetry Score | onset, offset, occlusion이 서로 다른 메모리 동작을 갖는지 |

  

핵심 평가 protocol은 contact-corruption injection이다. 정상 모델에 의도적으로 잘못된 접촉 정보를 주입하고, 이후 프레임에서 오류가 얼마나 빠르게 회복되는지를 측정한다. 비교 baseline은 EMA, GRU, Kalman filter, symmetric temporal gate 등 일반 시간 모델이다.

  

MoE 구조에서는 이 protocol을 expert-level로 확장할 수 있다. E-expert만 오염, M-expert만 오염, 두 expert 동시 오염, gating weight 오염, 단일 spike/burst/지속 오염 등으로 나누어 robustness profile을 만들 수 있다.

  

## 구조 선택 관점

  

현재 문서 기준으로는 1-2차년도에는 분리 헤드 구조를 주 아키텍처로 두고, MoE는 후속 확장 또는 3-4차년도 고도화로 두는 전략이 가장 안정적이다.

  

| 기준 | 분리 헤드 구조 | MoE 구조 |

|---|---|---|

| 1차년도 구현 안정성 | 높음 | 낮음-중간 |

| 작은 pilot 데이터 적합성 | 높음 | 낮음 |

| Evidence 특화도 | 중간 | 높음 |

| Mechanistic 분석 깊이 | 중간 | 높음 |

| PI 자산 활용 | D2FP, confidence-guided pattern 중심 | D2FP, AvatarMoE, gating 구조까지 활용 |

| 2차년도 4-gate 연결성 | 충분함 | 더 정밀함 |

| 학회 차별성 | 중간 | 강함 |

| 리스크 | 낮음 | gating collapse, pseudo GT noise, pretraining 부담 |

  

권고 방향은 다음과 같다.

  

1. 1차년도는 D2FP pretrained backbone 기반의 분리 헤드 구조로 안정적인 baseline을 확보한다.

2. 2차년도는 분리 헤드 기반 4-gate, self-correction, corruption injection 평가 protocol을 완성한다.

3. MoE는 즉시 주 구조로 밀기보다, expert별 pretraining과 pseudo GT 안정화가 준비된 뒤 부분 MoE부터 단계적으로 확장한다.

4. 3차년도 이후 M-expert 또는 S-expert부터 분리하는 partial MoE를 도입하고, 최종적으로 full MoE와 expert-level robustness profile로 확장한다.

  

## 팀 공유용 핵심 메시지

  

현재 연구계획의 핵심 주장은 "일반 시간 평활화 모델보다 정확하다"가 아니라, "접촉 오류가 다음 프레임으로 전파되는 구조적 루프를 차단한다"는 것이다.

  

따라서 문서와 실험 설계에서 강조해야 할 점은 다음이다.

  

- 1차년도는 contact proposal 자체보다 evidence별 confidence를 신뢰 가능하게 만드는 단계다.

- 2차년도는 contact memory를 단순히 부드럽게 유지하는 것이 아니라, onset/offset/occlusion/maintain을 다르게 처리하는 단계다.

- 평가도 평균 정확도 중심이 아니라 contact corruption 이후 회복 속도와 오류 전파 차단 능력 중심이어야 한다.

- 분리 헤드 구조는 안정적이고 현실적인 주 경로다.

- MoE 구조는 학술적 차별성과 분석력은 강하지만, 데이터와 학습 안정성 리스크가 크므로 단계적 확장으로 두는 편이 안전하다.

  

## 팀 논의가 필요한 결정 사항

  

- 1차년도 주 구조를 분리 헤드로 확정할지, MoE까지 pilot에 포함할지

- 2차년도 4-gate의 주 contribution을 알고리즘으로 둘지, 평가 protocol까지 포함해 강조할지

- Contact-corruption injection을 어느 데이터셋과 어느 frame rate 조건에서 우선 검증할지

- MoE 확장을 3차년도 partial MoE로 둘지, 2차년도 말 ablation으로 일부 포함할지

- Pseudo GT 생성과 confidence filtering을 어느 수준까지 1차년도 범위에 포함할지