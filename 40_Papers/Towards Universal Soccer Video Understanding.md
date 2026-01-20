---
title: Towards Universal Soccer Video Understanding
aliases:
  - UniSoccer
  - SoccerReplay-1988
  - MatchVision
  - Universal Soccer Video Understanding
tags:
  - paper
  - video
  - sports
  - multimodal
  - dataset
  - encoder
year: 2024
venue: arXiv
arxiv: https://arxiv.org/abs/2410.02803
project: https://jyrao.github.io/UniSoccer/
---
# Towards Universal Soccer Video Understanding

## 한줄 요약
- **대규모 멀티모달 축구 데이터셋(SoccerReplay-1988)과 축구 특화 시각 인코더(MatchVision)를 제안해 이벤트 분류, 해설 생성, 다중 뷰 파울 인식에서 성능을 끌어올린다.**

## 핵심 기여
- **SoccerReplay-1988**: 1,988 경기로 구성된 최대 규모 멀티모달 축구 데이터셋.
- **자동화 큐레이션 파이프라인**: 시간 정렬, 이벤트 요약, 익명화.
- **MatchVision**: 축구 도메인에 맞춘 시공간 인코더 + 다양한 다운스트림 헤드.
- **통합 평가**: 이벤트 분류, 해설 생성, 멀티뷰 파울 인식에서 일관된 성능 향상.

## 데이터셋: SoccerReplay-1988
- **규모**: 1,988 경기, 총 3,323 시간 분량.
- **리그/시즌**: 유럽 6개 리그 + UEFA Champions League, 2014-15 ~ 2023-24.
- **주석**:
  - 텍스트 해설 약 150K (초 단위 타임스탬프 정렬).
  - 이벤트 주석 약 150K, 24개 이벤트 타입.
- **분할**: Train 1,488 / Val 250 / Test 250 경기.
- **품질**: 무작위 2% 샘플 수동 검증 98% 정확도.

### 이벤트 타입(24)
- corner, goal, injury, own goal, penalty, penalty missed, red card, second yellow card,
  substitution, start of game (half), end of game (half), yellow card, throw in, free kick,
  saved by goal-keeper, shot off target, clearance, lead to corner, off-side, var,
  foul (no card), statistics and summary, ball possession, ball out of play

### 자동화 큐레이션 파이프라인
1) **Temporal Alignment**: MatchTime 모델로 해설 타임스탬프와 영상 정렬
2) **Event Summarization**: LLaMA-3-70B로 이벤트 요약 및 라벨 생성
3) **Anonymization**: [PLAYER], [TEAM] 등으로 개체 익명화

### SoccerReplay-test
- SoccerReplay-1988 250경기 + SoccerNet-pro 50경기
- 더 세분화된 이벤트와 풍부한 해설을 포함하는 평가용 벤치마크

## 방법: MatchVision
### 문제 정의
- 입력 비디오 클립 $V \in \mathbb{R}^{T \times 3 \times H \times W}$
- 출력: 이벤트, 해설, 파울 타입
- 통합 표현: $E, C, F = \Psi(\Phi_{MatchVision}(V))$

### 아키텍처 요약
- **Token Embedding**: 프레임을 패치로 분할, 공간/시간 위치 임베딩 추가
- **Spatiotemporal Attention Block**: TimeSformer처럼 시간/공간 어텐션을 교차 적용
- **Aggregation**: 프레임별 [cls] 토큰을 모아 비디오 레벨 특징 생성

### 사전학습
- **Supervised Event Classification**
- **Video-Text Contrastive Learning** (SigLIP 방식)

## 다운스트림 태스크
- **Event Classification**: temporal attention으로 [cls] 토큰 집계 후 분류
- **Commentary Generation**: Perceiver + MLP로 prefix 생성 후 LLaMA-3(8B)로 생성
- **Multi-view Foul Recognition**: 다중 뷰 집계 후 파울 타입/심각도 분류

## 실험 설정(요지)
- 1 FPS로 30초 구간 샘플링
- 입력 해상도 224x224
- 초기화: SigLIP Base-16
- LLM 디코더: LLaMA-3 8B
- GPU: 4x NVIDIA H800

## 결과 요약
- MatchVision은 이벤트 분류, 해설 생성, 멀티뷰 파울 인식에서 기존 모델 대비 성능 향상.
- SoccerReplay-1988 사전학습이 다양한 태스크에서 일관된 이득을 제공.

## 의의
- 축구 도메인에 특화된 대규모 데이터와 범용 인코더를 결합한 통합 프레임워크.
- 단일 인코더로 여러 축구 이해 태스크를 지원하는 기준선 제시.

## 링크
- 프로젝트: https://jyrao.github.io/UniSoccer/
- arXiv: https://arxiv.org/abs/2410.02803
