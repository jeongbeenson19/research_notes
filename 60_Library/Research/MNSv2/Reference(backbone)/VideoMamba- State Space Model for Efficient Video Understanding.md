---
aliases: ["VideoMamba: State Space Model for Efficient Video Understanding", "VideoMamba"]
type: paper
tags:
  - DeepLearning
  - Paper
  - VideoUnderstanding
  - StateSpaceModel
  - Mamba
status: 🟩 Done
rating: 5
date: 2026-03-17
title: "VideoMamba: State Space Model for Efficient Video Understanding"
authors: ["Kunchang Li", "Xinhao Li", "Yi Wang", "Yinan He", "Yali Wang", "Limin Wang", "Yu Qiao"]
year: 2024
venue: "ECCV 2024"
paper_url: "https://arxiv.org/abs/2403.06977"
code_url: "https://github.com/OpenGVLab/VideoMamba"
topics: ["Video Understanding", "State Space Models", "Long Video Modeling", "Masked Modeling"]
---

## Paper
- Title: VideoMamba: State Space Model for Efficient Video Understanding
- Venue/Year: ECCV 2024
- Link: https://arxiv.org/abs/2403.06977
- 역할(문제정의/방법/평가/반박): 방법 + 비디오 백본 비교기준 + 장기 문맥 효율성 기준선

## Extract
- Task: 일반 비디오 이해. short-term action recognition, long-term understanding, video-text retrieval까지 포함하는 범용 비디오 백본을 목표로 한다.
- Unobserved interval: explicit occlusion을 직접 다루기보다 긴 시간 축에서 필요한 정보가 멀리 떨어져 있는 long-range temporal dependency를 다룬다.
- Memory unit: bidirectional Mamba block이 유지하는 latent SSM state. 토큰 단위로는 frame patch sequence 전체가 state update 대상이다.
- State: 비디오 patch token, positional embedding, block 내부 recurrent hidden state.
- Update rule: bidirectional selective scan으로 forward/backward 방향 temporal dependency를 모두 반영한다.
- Reactivation: 별도 re-identification 단계는 없고, 장기 문맥을 recurrent state에 유지한 뒤 classifier/retrieval head가 필요한 정보를 읽는다.
- Fusion: 3D patch embedding으로 영상 정보를 token화하고, spatial-first scan order와 bidirectional Mamba stack으로 공간-시간 정보를 통합한다.
- Assumptions: 비디오를 attention 없이도 순차 state update로 충분히 모델링할 수 있으며, scan order 설계가 성능에 직접적인 영향을 준다.
- Evaluation: ImageNet 사전학습, Kinetics-400, Something-Something V2, Breakfast, COIN, 다수 video-text retrieval 벤치마크.
- Failure modes: scan order가 부적절하면 공간 정보가 무너질 수 있다. 큰 모델은 단순 supervised pretraining만으로는 충분히 최적화되지 않아 self-distillation이나 masked modeling이 필요하다.

## Takeaway
- 내 설계에 적용(1줄): 비디오 메모리를 attention map 대신 bidirectional recurrent state로 유지해도 장기 문맥과 효율성을 동시에 잡을 수 있다.
- D1/D2/D3에 미치는 영향: `D1`은 frame-level late fusion보다 백본 내부의 temporal state update가 더 중요할 수 있음을 보여준다. `D2`는 belief state를 token 집합이 아니라 scan-friendly latent state로 유지하는 설계 근거가 된다. `D3`는 semantic을 많이 넣기 전에 scan order와 memory path를 먼저 고정해야 함을 시사한다.

## 개요

VideoMamba는 Mamba 계열 SSM을 비디오 도메인에 본격적으로 가져온 초기 대표작이다. 논문의 핵심 질문은 간단하다. "Transformer가 사실상 표준이 된 비디오 이해에서, linear-time SSM이 정말 경쟁력이 있는가?" 저자들의 답은 yes이며, 단순한 백본 교체가 아니라 비디오에 맞는 tokenization, scan order, self-distillation, masked pretraining까지 포함한 패키지로 제시한다.

공식 ECCV 페이지와 저장소 기준으로 이 논문은 네 가지 역량을 전면에 둔다.
- scalability
- short-term sensitivity
- long-term superiority
- multi-modal compatibility

즉, "길기만 한 모델"이 아니라 짧은 동작 인식부터 긴 영상, 심지어 video-text retrieval까지 모두 먹히는 범용 operator인지 검증하려는 설계다.

## 아키텍처

### 1. 입력 토큰화
- 비디오를 non-overlapping spatio-temporal patch로 나눈다.
- 논문 HTML 기준 patch embedding은 `3D convolution` 기반이며, ViT처럼 token sequence를 만든 뒤 백본에 넣는다.
- 중요한 점은 토큰을 만드는 순간부터 비디오가 "frame grid"가 아니라 "긴 시퀀스"로 바뀐다는 것이다.

### 2. Bidirectional Mamba Block
- 단방향 Mamba는 과거에서 현재로만 정보가 흐른다.
- 비디오 이해는 동일 clip 안에서 양방향 문맥이 필요하므로, VideoMamba는 `bi-directional Mamba block`을 사용한다.
- 논문 기준 vanilla ViT 구조를 따르되 attention block을 bi-directional Mamba block으로 치환한 형태로 이해하면 된다.

### 3. Scan Order
- 저자들은 temporal-first, spatial-first, spatio-temporal 등 여러 scan order를 비교한다.
- 공식 HTML 본문 기준 가장 좋은 성능은 `spatial-first`에서 나온다.
- 해석하면, frame 내부 spatial structure를 먼저 잘 정리한 뒤 시간 축으로 state를 넘기는 편이 비디오에서 더 안정적이라는 뜻이다.

### 4. 모델 스케일
- 공개된 기본 모델 스케일은 `Ti`, `S`, `M`, `B`이며, 본문 기준 `B`는 최적화 난이도 때문에 핵심 비교에서 제외되기도 한다.
- 논문에 명시된 대표 크기는 다음과 같다.
  - `VideoMamba-Ti`: 24 layers, 192 dim, 약 7M params
  - `VideoMamba-S`: 24 layers, 384 dim, 약 26M params
  - `VideoMamba-M`: 32 layers, 576 dim, 약 74M params
  - `VideoMamba-B`: 24 layers, 768 dim, 약 98M params

## 학습 전략

### ImageNet 사전학습
- 논문 HTML 기준 ImageNet-1K에서 300 epochs 사전학습을 수행한다.
- optimizer는 `AdamW`, initial learning rate는 `1e-3`, weight decay는 `0.05`, total batch size는 `1024`다.
- mixed precision(`bfloat16`)를 사용한다.

### 비디오 파인튜닝
- Kinetics-400은 50 epochs, Something-Something V2는 30 epochs 파인튜닝 설정이 제시된다.
- 학습률은 `2e-4`, weight decay는 `0.05`, repeated augmentation을 사용한다.
- 큰 모델일수록 supervised pretraining만으로는 최적화가 부족해 self-distillation이 성능 향상에 중요하다.

### Masked Modeling
- 논문은 Mamba가 masked pretraining과도 잘 결합됨을 보여준다.
- 특히 Something-Something V2처럼 motion-sensitive한 데이터셋에서 masked pretraining 효과가 크다.

## 실험과 결과

### 1. ImageNet-1K
- 공식 HTML 본문 기준 `VideoMamba-M`은 `84.0` top-1 정확도를 기록한다.
- 이는 "비디오용 SSM이 이미지 사전학습 단계에서도 충분히 경쟁력 있다"는 점을 보여준다.

### 2. Kinetics-400
- `VideoMamba-M`, `32 x 224 x 224`, ImageNet-1K pretraining 설정에서 `82.4` top-1 / `95.7` top-5를 기록한다.
- 더 큰 입력(`64 x 384 x 384`)에서는 `83.3` top-1 / `96.5` top-5까지 올라간다.
- 논문은 이 결과가 ViViT-L보다 약 2.0%p 높은 수준이라고 설명한다.

### 3. Something-Something V2
- supervised pretraining 기반 `VideoMamba-M`, `16 x 288 x 288` 설정에서 `68.4` top-1을 기록한다.
- masked pretraining을 결합하면 같은 해상도에서 `71.4` top-1까지 오른다.
- motion ordering이 중요한 데이터셋에서 Mamba류 state update가 특히 강하다는 해석이 가능하다.

### 4. Long-term Video Understanding
- Table 6 기준 end-to-end `VideoMamba-M`의 `f64` 구성은 `Breakfast 96.9`, `COIN 90.4`까지 보고된다.
- 즉, 단기 분류용 backbone이 아니라 long-form activity understanding에도 충분히 먹힌다.

### 5. 효율
- 논문은 64-frame 비디오 기준 TimeSformer 대비 약 `6x` faster, GPU memory는 약 `40%` less 사용한다고 주장한다.
- 이 포인트가 VideoMamba의 가장 실용적인 장점이다.

## 왜 중요한가

### 1. 비디오용 SSM의 첫 강한 기준점
- 이전 SSM 비디오 논의는 가능성 수준인 경우가 많았다.
- VideoMamba는 실제로 K400/SSv2/Breakfast/COIN/retrieval까지 넓게 검증하며 "SSM도 비디오 백본이 될 수 있다"를 보여준다.

### 2. scan order가 성능을 좌우한다
- vision에서 SSM은 단순히 sequence operator를 가져다 쓰는 것으로 끝나지 않는다.
- 토큰을 어떤 순서로 state에 흘릴지가 매우 중요하고, 이 지점이 이후 후속작의 출발점이 된다.

### 3. 후속작의 기준선
- [[Snakes and Ladders- Two Steps Up for VideoMamba]]는 바로 이 VideoMamba의 약점을 분석해 개선한 논문이다.
- 따라서 VideoMamba는 standalone 결과보다 "무엇이 부족했는가"까지 포함해 읽어야 한다.

## 한계

- attention처럼 명시적인 pairwise token interaction이 없어서 sparse but critical interactions를 바로 집어내는 데 약할 수 있다.
- scan order 선택이 매우 중요해 데이터셋별 튜닝 비용이 존재한다.
- 대형 모델은 학습 안정성 이슈가 있어 self-distillation이나 masked pretraining 같은 보조 전략이 필요하다.
- action recognition에서는 강하지만, localization-heavy task에서는 추가 구조가 필요할 가능성이 높다.

## MNS 관점 연결

- occlusion gap을 직접 다루는 모델은 아니지만, "긴 temporal history를 저비용으로 state에 보존한다"는 점에서 memory backbone 후보로 매우 중요하다.
- 특히 object track를 token sequence로 보고 recurrent state로 넘기는 설계는 MNS의 object memory를 clip-level SSM으로 구현할 때 직접 참고할 수 있다.
- 다만 pure VideoMamba는 explicit reactivation/mechanism이 부족하므로, MNS 쪽에서는 state update 위에 reactivation head를 추가하는 방향이 자연스럽다.

## 참고 링크
- 논문: https://arxiv.org/abs/2403.06977
- ECCV 페이지: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5647_ECCV_2024_paper.php
- 코드: https://github.com/OpenGVLab/VideoMamba
