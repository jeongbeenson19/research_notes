---
aliases: ["Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality", "Transformers are SSMs", "Mamba-2"]
type: paper
tags:
  - DeepLearning
  - Paper
  - StateSpaceModel
  - Theory
  - Mamba
status: 🟩 Done
rating: 5
date: 2026-03-17
title: "Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality"
authors: ["Tri Dao", "Albert Gu"]
year: 2024
venue: "ICML 2024"
paper_url: "https://proceedings.mlr.press/v235/dao24a.html"
code_url: "https://github.com/state-spaces/mamba"
topics: ["State Space Duality", "Semiseparable Matrices", "Mamba-2", "Sequence Modeling Theory"]
---

## Paper
- Title: Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality
- Venue/Year: ICML 2024
- Link: https://proceedings.mlr.press/v235/dao24a.html
- 역할(문제정의/방법/평가/반박): 이론 + 알고리즘 통합 + Mamba-2의 기반 논문

## Extract
- Task: attention과 SSM을 하나의 이론적 프레임으로 통합하고, 그 위에서 더 빠른 범용 sequence layer를 설계하는 것.
- Unobserved interval: occlusion이나 missing observation을 직접 다루지 않는다. 대신 긴 시퀀스에서 정보를 어떻게 전달하고 압축할지를 수학적으로 다룬다.
- Memory unit: semiseparable matrix가 암묵적으로 표현하는 sequence memory, 혹은 그와 동등한 recurrent SSM hidden state.
- State: structured state space duality(SSD)로 연결되는 matrix view와 recurrent state view의 두 표현.
- Update rule: attention류 연산과 SSM recurrence를 structured semiseparable class의 서로 다른 계산 방식으로 본다. Mamba-2는 이 duality를 실제 레이어 설계로 구현한다.
- Reactivation: explicit retrieval는 없지만, matrix form에서는 pairwise interaction처럼 보이고 recurrent form에서는 compressed state propagation으로 보인다.
- Fusion: recurrent SSM 계산과 matrix multiplication 관점을 하나의 연산자 클래스로 묶는다. 실전 구현에서는 `mamba2`, `mamba2_simple`, `ssd_minimal`로 나뉜다.
- Assumptions: sequence operator의 핵심이 dense arbitrary attention 전체가 아니라, 구조화된 semiseparable family 안에 상당 부분 포함될 수 있다는 가정.
- Evaluation: 언어 모델링 중심. Mamba-2는 이전 state-space 모델보다 2-8배 빠르면서 Transformer 품질에 경쟁적이라고 주장한다.
- Failure modes: 이론은 강하지만 실험 영역은 주로 language modeling 중심이다. 모든 비전/멀티모달 attention을 그대로 대체한다고 해석하면 과장이다.

## Takeaway
- 내 설계에 적용(1줄): attention과 recurrent memory를 별개 진영으로 볼 게 아니라, 같은 정보 전달 연산의 다른 계산 방식으로 보아야 한다.
- D1/D2/D3에 미치는 영향: `D1`은 fusion을 모듈 연결 문제가 아니라 operator choice 문제로 재정의하게 만든다. `D2`는 belief state 유지와 pairwise relation modeling이 양립 불가능한 것이 아니라 dual form일 수 있음을 보여준다. `D3`는 semantic을 더 넣기보다 어떤 구조화 연산으로 state를 전달할지 먼저 정해야 함을 시사한다.

## 개요

이 논문은 Mamba-2의 기술 보고서이면서 동시에 더 큰 주장 하나를 한다. "Transformer와 SSM은 본질적으로 멀리 떨어져 있지 않다." 저자들은 attention을 행렬 연산의 관점에서, SSM을 recurrence의 관점에서 보되, 이 둘이 사실 같은 structured operator family 안에 놓일 수 있다고 주장한다. 이 프레임이 바로 `Structured State Space Duality (SSD)`다.

이 논문이 중요한 이유는 단지 Mamba-2를 소개했기 때문이 아니라, 이후 hybrid design 논의를 훨씬 정교하게 만들어 줬기 때문이다. 이제 질문은 "attention을 쓸까 SSM을 쓸까"가 아니라, "같은 연산자를 어떤 계산 모드로 실행할까"가 된다.

## 핵심 아이디어

### 1. Structured State Space Duality (SSD)
- 특정한 sequence mixing 연산은 semiseparable matrix로 표현할 수 있다.
- 이 행렬은 matrix multiplication으로 계산할 수도 있고, recurrent SSM 형태로 계산할 수도 있다.
- 즉, attention-like interaction과 SSM-like recurrence가 완전히 별개가 아니라 dual form이라는 주장이다.

### 2. 왜 중요한가
- attention은 pairwise interaction을 직접 계산하므로 해석이 쉽지만 비용이 크다.
- SSM은 state에 정보를 압축해 넣으므로 효율적이지만, attention만큼 직접적인 상호작용처럼 보이지 않는다.
- SSD는 "둘 다 같은 구조적 정보를 다른 계산 방식으로 다루고 있다"는 시각을 준다.

### 3. Mamba-2로 이어지는 이유
- 이론만으로 끝나지 않고, 저자들은 이 duality를 바탕으로 더 단순하고 빠른 Mamba-2 레이어를 설계한다.
- 공식 저장소 README 기준 Mamba-2는 이전 Mamba-1보다 더 사용하기 쉬운 구현과 더 큰 `d_state`를 채택한다.

## Mamba-2 관점에서 읽기

### 구현 레벨 포인트
- 공식 저장소에는 다음 파일이 핵심으로 명시된다.
  - `modules/mamba2.py`
  - `modules/mamba2_simple.py`
  - `modules/ssd_minimal.py`
- `ssd_minimal.py`는 논문 Listing 1에 해당하는 최소 SSD 구현이라고 README가 설명한다.
- 즉, 이 논문은 이론 논문이면서 동시에 코드 경로가 매우 명확한 실전 논문이기도 하다.

### 모델 설정
- 저장소 README 기준 Mamba-2 블록은 보통 `d_state = 64` 또는 `128`을 사용한다.
- 이는 Mamba-1보다 더 큰 state를 쓰는 쪽으로 기울어 있으며, layer 자체도 단순화되어 있다.
- 공개 체크포인트는 `130M`, `370M`, `780M`, `1.3B`, `2.7B` 크기로 제공된다.

### Hybrid baseline
- 저장소는 pure Mamba-2뿐 아니라 `mamba2attn-2.7b`, `transformerpp-2.7b` 같은 hybrid 또는 Transformer++ baseline도 함께 제공한다.
- 이는 저자들 스스로도 "완전 대체"보다 "operator family 내 비교"를 중요하게 본다는 뜻으로 해석할 수 있다.

## 알고리즘적 의미

### Matrix mode와 recurrent mode
- matrix mode는 한 번에 전체 시퀀스를 보고 block/chunk 단위로 처리하기 쉽다.
- recurrent mode는 step-by-step inference에 유리하고 메모리 사용이 예측 가능하다.
- SSD는 이 둘 사이를 오갈 수 있게 해 준다.

### 왜 이게 실전에서 유리한가
- 학습 때는 chunk 병렬화와 하드웨어 최적화가 중요하다.
- 추론 때는 latency와 cache 크기가 중요하다.
- 같은 연산자를 학습과 추론에서 다른 계산 관점으로 실행할 수 있다면 효율이 좋아진다.

### MNS에 주는 메시지
- object memory도 attention-style relation과 recurrent-style persistence를 둘 다 필요로 한다.
- SSD 관점은 이 둘을 별도 모듈로 이어 붙이는 대신, 하나의 구조화 연산자로 설계할 가능성을 준다.

## 실험과 결과

### 언어 모델링
- ICML abstract와 공식 저장소 README가 일관되게 강조하는 결과는 다음이다.
  - Mamba-2가 language modeling에서 Transformer와 경쟁적이다.
  - 이전 state-space 모델보다 `2x ~ 8x` 빠를 수 있다.
- 공개 체크포인트는 `The Pile` 300B tokens 학습 설정과 연결되어 있으며, repo에는 zero-shot evaluation 스크립트도 제공된다.

### 실전 메시지
- 이 논문이 보여주는 것은 단순 accuracy 한 줄보다 "SSM이 이제 이론적으로도, 구현적으로도 Transformer와 같은 테이블에서 비교될 수 있다"는 점이다.
- 즉, Mamba-2 이후에는 SSM이 niche model이 아니라 mainstream sequence operator 후보가 된다.

## 강점

- attention과 SSM의 논의를 하나의 언어로 정리한다.
- 이론에서 끝나지 않고 Mamba-2라는 실제 아키텍처와 코드로 이어진다.
- hybrid 설계까지 포함해 설계 공간을 넓힌다.
- 이후 비디오/비전/멀티모달 Mamba 논문들의 공통 기반 개념이 된다.

## 한계

- 논문의 직접 실험은 언어 모델링 중심이라, 비디오/비전으로의 일반화는 후속 논문을 함께 봐야 한다.
- semiseparable 구조가 설명하는 범위 밖의 dense interaction까지 모두 커버한다고 보면 과장이다.
- 실제 다운스트림 설계에서는 여전히 scan order, tokenization, residual layout 같은 도메인별 문제가 남는다.

## MNS 관점 연결

- MNS에서 중요한 질문은 "가려진 객체 정보를 latent state에 누적할 것인가, pairwise relation으로 다시 읽어올 것인가"다.
- 이 논문은 그 둘이 완전히 별개가 아니라 dual form일 수 있다고 말해 준다.
- 따라서 MNS 설계에서도 pure recurrent memory와 sparse relation module을 대립항으로 보지 말고, 하나의 구조화 연산을 서로 다른 모드로 구현하는 관점이 유용하다.
- 실전적으로는 `Mamba-2 backbone + 필요한 곳에만 explicit relation head` 같은 hybrid가 가장 설득력 있는 방향이다.

## 참고 링크
- 논문: https://proceedings.mlr.press/v235/dao24a.html
- arXiv: https://arxiv.org/abs/2405.21060
- 코드: https://github.com/state-spaces/mamba
