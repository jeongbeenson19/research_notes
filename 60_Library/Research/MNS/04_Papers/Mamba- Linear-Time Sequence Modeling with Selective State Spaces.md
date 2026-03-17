---
aliases: ["Mamba: Linear-Time Sequence Modeling with Selective State Spaces", "Mamba"]
type: paper
tags:
  - DeepLearning
  - Paper
  - StateSpaceModel
  - Mamba
  - SequenceModeling
status: 🟩 Done
rating: 5
date: 2026-03-17
title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
authors: ["Albert Gu", "Tri Dao"]
year: 2023
venue: "arXiv"
paper_url: "https://arxiv.org/abs/2312.00752"
code_url: "https://github.com/state-spaces/mamba"
topics: ["State Space Models", "Selective Scan", "Long Sequence Modeling", "Hardware-aware Parallelism"]
---

## Paper
- Title: Mamba: Linear-Time Sequence Modeling with Selective State Spaces
- Venue/Year: arXiv 2023
- Link: https://arxiv.org/abs/2312.00752
- 역할(문제정의/방법/평가/반박): 방법 + 이론적 기준선 + 효율성 비교축

## Extract
- Task: 범용 시퀀스 모델링. 특히 긴 컨텍스트 언어 모델링, 오디오, 유전체학처럼 sequence length가 매우 긴 문제를 대상으로 한다.
- Unobserved interval: 비디오 occlusion처럼 명시적 비가시 구간을 다루는 논문은 아니다. 대신 "먼 과거 정보가 현재에 다시 필요해지는 상황"을 긴 시퀀스 의존성 문제로 다룬다.
- Memory unit: 레이어별 잠재 상태 `h_t`를 갖는 [[Selective State Space Models (SSMs)]].
- State: 고정 파라미터 SSM이 아니라 입력 `x_t`에 따라 달라지는 `Δ_t`, `B_t`, `C_t` 및 이산화된 recurrent state.
- Update rule: `h_t = A_bar_t h_{t-1} + B_bar_t x_t`, `y_t = C_t h_t + D x_t`. 핵심은 `A_bar_t, B_bar_t, C_t`가 입력 의존적이라는 점이다.
- Reactivation: 명시적 re-detection은 없고, selective scan이 필요한 정보는 state에 오래 보존하고 불필요한 정보는 빠르게 감쇠시켜 간접적으로 "재활성화" 효과를 낸다.
- Fusion: 입력 투영 후 SSM 경로와 gate 경로를 결합한다. causal depthwise conv와 gating이 selective SSM 앞뒤에 들어가 정보 흐름을 제어한다.
- Assumptions: 긴 문맥에서 모든 token-token pair를 명시적으로 비교하지 않아도, 입력 조건부 recurrent state만으로 충분한 추론력을 만들 수 있다는 가정.
- Evaluation: 언어 모델링(The Pile, LAMBADA 등), 오디오, 유전체학. 정확도뿐 아니라 throughput과 long-context scaling을 핵심 지표로 본다.
- Failure modes: attention처럼 명시적 pairwise alignment score를 바로 꺼내기 어렵다. 시각 데이터처럼 scan order가 중요한 문제는 별도 설계가 필요하다.

## Takeaway
- 내 설계에 적용(1줄): 장기 메모리를 반드시 attention cache로 구현할 필요는 없고, 입력 조건부 recurrent state로도 충분히 강한 기억 메커니즘을 만들 수 있다.
- D1/D2/D3에 미치는 영향: `D1`은 feature injection보다 state update rule 설계가 더 중요하다는 근거를 준다. `D2`는 location/appearance를 고정 벡터가 아닌 입력 조건부 belief state로 유지할 수 있음을 시사한다. `D3`는 semantic을 무작정 늘리기보다 "언제 유지/망각할지"를 배우는 선택성이 먼저라는 쪽으로 기운다.

## 개요

Mamba는 [[Transformer]]의 핵심 장점인 content-based reasoning을 유지하면서, attention의 `O(L^2)` 비용을 `O(L)` 수준으로 낮추는 것을 목표로 한다. 기존 SSM은 길이 효율성은 좋지만 입력 내용에 따른 선택성이 약해서 텍스트 같은 정보 밀도가 높은 이산 시퀀스에 약했다. Mamba는 이 문제를 "파라미터를 입력 의존적으로 만들자"는 방식으로 해결한다.

논문의 포지션은 단순한 SSM 변형이 아니라, "attention 없이도 foundation model 급 시퀀스 백본을 만들 수 있는가"에 대한 직접적인 답이다. 공식 저장소 기준으로 Mamba와 Mamba-2 계열은 현재도 `state-spaces/mamba`에서 유지되고 있으며, 공개된 pretrained LM도 함께 제공된다.

## 핵심 아이디어

### 1. 선택적 상태 업데이트
- 기존 SSM은 시간 불변 파라미터를 사용해 모든 token을 비슷한 방식으로 처리한다.
- Mamba는 현재 입력 `x_t`를 보고 `Δ_t`, `B_t`, `C_t`를 동적으로 생성해, 어떤 정보는 오래 보존하고 어떤 정보는 즉시 버리도록 만든다.
- 이 선택성 덕분에 "지금 들어온 token이 중요한가"를 attention 없이도 판단할 수 있다.

### 2. Selective Scan
- 입력 의존적 recurrence는 순진하게 구현하면 병렬화가 어렵다.
- 논문은 GPU 친화적 prefix-scan 스타일 알고리즘을 사용해 recurrent 계산을 병렬화한다.
- 학습 시에는 하드웨어 인지 병렬 scan을 사용하고, 추론 시에는 KV cache 없이 recurrent 모드로 한 스텝씩 진행한다.

### 3. 단순한 블록 구조
- Mamba block은 대략 `입력 투영 -> local mixing(depthwise conv) -> selective SSM -> gate 결합 -> 출력 투영` 흐름으로 이해하면 된다.
- Transformer처럼 `Attention block + MLP block`을 따로 두지 않고 하나의 통합 블록으로 처리한다.
- 이 구조 때문에 depth가 깊어져도 구현이 단순하고, 메모리 사용량이 비교적 예측 가능하다.

## 아키텍처 상세

### 블록 수준 동작
1. 입력 토큰을 선형 투영해 SSM branch와 gate branch로 분기한다.
2. SSM branch는 causal depthwise convolution으로 짧은 구간 local mixing을 먼저 수행한다.
3. 이후 선형층이 입력 의존적 `Δ`, `B`, `C`를 생성하고 selective scan이 recurrent update를 실행한다.
4. gate branch는 SSM 출력에 elementwise gate를 걸어 정보량을 조절한다.
5. 마지막 선형 투영과 residual 연결로 다음 블록에 전달한다.

### 수식 관점

```text
h_t = A_bar_t h_{t-1} + B_bar_t x_t
y_t = C_t h_t + D x_t
A_bar_t, B_bar_t, C_t = f(x_t, Δ_t)
```

- 여기서 핵심은 `A_bar_t, B_bar_t, C_t`가 고정값이 아니라 현재 입력의 함수라는 점이다.
- 즉, Mamba의 메모리는 "고정 메모리"가 아니라 "현재 입력에 의해 재설정되는 메모리"에 가깝다.

### 왜 attention을 대체할 수 있는가
- attention은 token 간 pairwise 비교를 통해 중요한 과거 정보를 꺼낸다.
- Mamba는 동일한 pairwise score를 만들지는 않지만, state update를 입력 조건부로 조정함으로써 중요한 과거 정보를 state 안에 남겨 둔다.
- 따라서 random access memory라기보다, "선택적으로 압축된 지속 상태"를 유지하는 구조라고 보는 편이 정확하다.

## 학습과 추론

### 학습
- 논문은 언어 모델링, 오디오, 유전체학 등 서로 다른 시퀀스 도메인에서 Mamba를 검증한다.
- 공식 저장소에는 pretrained LM 체크포인트(`130M`, `370M`, `790M`, `1.4B`, `2.8B`)가 제공된다.
- 저장소 README 기준으로 이 모델들은 `The Pile` 300B tokens 학습 레시피를 따른다.

### 추론
- Transformer와 달리 KV cache를 시퀀스 길이만큼 유지할 필요가 없다.
- 한 스텝당 recurrent state만 갱신하면 되므로 긴 시퀀스에서 메모리 이점이 커진다.
- 논문/공식 페이지 기준 주장은 다음과 같다.
  - 동일 크기 Transformer 대비 약 5배 높은 추론 throughput
  - 백만 길이 수준까지 성능 개선이 유지되는 long-context scaling
  - Mamba-3B가 동급 Transformer를 넘고, 약 2배 큰 Transformer와 경쟁

## 실험과 결과

### 언어 모델링
- 로컬 노트에 정리된 논문 표 기준으로 `Mamba-1.4B`는 Pile perplexity `6.80`, LAMBADA perplexity `5.04`, LAMBADA accuracy `59.7%`를 기록한다.
- 핵심 메시지는 "linear-time인데도 Transformer 급 품질을 낸다"는 점이다.

### 장문 컨텍스트
- Mamba는 긴 길이에서 context window가 길어질수록 성능이 계속 좋아지는 경향을 보인다.
- 이는 attention 모델이 비용 때문에 context를 제한하는 상황과 대비된다.

### 도메인 일반성
- 텍스트만이 아니라 오디오와 유전체학에서도 강한 결과를 보였다는 점이 중요하다.
- 즉, selective SSM이 특정 모달리티 전용 트릭이 아니라 범용 sequence operator로 작동함을 보여준다.

## MNS 관점에서 중요한 이유

### 1. 메모리 업데이트 규칙을 직접 설계하게 만든다
- MNS 문제에서는 "state에 무엇을 넣을 것인가" 못지않게 "언제 갱신하고 언제 유지할 것인가"가 중요하다.
- Mamba는 이 질문에 대해 gating이 아니라 입력 조건부 동역학 자체를 배우는 해법을 준다.

### 2. object permanence를 recurrent state로 해석할 수 있다
- 가려진 객체를 유지하는 문제를 attention retrieval가 아니라 latent state 유지 문제로 재정의할 수 있다.
- 이는 occlusion gap 동안 location, appearance, uncertainty를 어떻게 감쇠시킬지 설계하는 데 직접 연결된다.

### 3. 비디오 쪽 확장 방향이 명확하다
- 다만 원 논문은 1D sequence 중심이라, 비디오에서는 scan order와 spatial aggregation이 추가로 필요하다.
- 그래서 후속작인 [[VideoMamba- State Space Model for Efficient Video Understanding]]와 [[Snakes and Ladders- Two Steps Up for VideoMamba]]가 중요해진다.

## 한계와 주의점

- attention score가 없으므로 "왜 이 과거 정보를 썼는가"를 바로 해석하기는 어렵다.
- 시각 문제에서는 sequence ordering이 성능에 직접 영향을 주므로 naive flattening이 최선이 아닐 수 있다.
- recurrent dynamics는 precision에 민감할 수 있어, 공식 저장소도 AMP/파라미터 재초기화 이슈를 따로 안내한다.
- pairwise relation을 직접 비교해야 하는 문제에서는 pure SSM만으로 부족할 수 있어 hybrid 설계가 필요하다.

## 참고 링크
- 논문: https://arxiv.org/abs/2312.00752
- 코드: https://github.com/state-spaces/mamba
- 관련 노트: [[Selective State Space Models (SSMs)]]
