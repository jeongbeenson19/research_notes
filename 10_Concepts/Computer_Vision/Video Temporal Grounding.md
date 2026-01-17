---
title: Video Grounding
aliases:
  - Temporal Video Grounding
  - Video Temporal Localization
  - 비디오 그라운딩
  - 비디오 시점 정합
  - 비디오 순간 탐색
  - 텍스트-비디오 정합
  - Moment Retrieval
  - Temporal Sentence Grounding
tags:
  - computer-vision
  - video
  - grounding
  - temporal-localization
  - multimodal
topics:
  - text-video
  - moment-retrieval
  - temporal-boundary
---
# Video Temporal Grounding

## 1. 한줄 요약
- **Video Grounding은 텍스트 질의와 대응되는 비디오 구간(시작/종료 시점)을 찾는 문제**다.

## 2. 문제 정의
- 입력: 비디오 $V$, 텍스트 질의 $q$.
- 출력: 시간 구간 $[t_s, t_e]$ 또는 관련 스코어를 가진 여러 구간.
- 목표: 텍스트 의미와 가장 잘 일치하는 비디오 순간을 정확히 локализ레이션.

## 3. 과업 유형
- **Moment Retrieval**: 텍스트에 맞는 단일 구간 예측.
- **Dense Grounding**: 여러 문장/질의에 대해 다중 구간 예측.
- **Narration Grounding**: 내러티브 문장과 연속 구간 정렬.

## 4. 핵심 접근법
### 4.1 Two-Stage (Proposal + Ranking)
- 1단계: 후보 구간 생성(temporal proposals).
- 2단계: 텍스트-비디오 매칭 점수로 랭킹.
- 장점: 강력한 성능, 단점: 계산 비용.

### 4.2 One-Stage (Direct Regression)
- 텍스트-비디오 표현을 통해 **직접 경계 회귀**.
- 장점: 단순/빠름, 단점: 후보 다양성 부족 가능.

### 4.3 Boundary-aware Modeling
- 시작/끝 경계의 확률 분포를 분리해 예측.
- 경계 예측을 위한 별도 헤드 사용.

### 4.4 Transformer 기반
- 텍스트/비디오를 공통 임베딩 공간에서 교차 어텐션.
- 멀티모달 상호작용 강화.

## 5. 대표적 모델(요약 비교)
| 모델 | 접근 | 핵심 아이디어 | 비고 |
| --- | --- | --- | --- |
| TALL (2017) | Two-Stage | 슬라이딩 윈도우 + 텍스트-비디오 매칭 | 초기 대표 모델 |
| 2D-TAN (2020) | Two-Stage | 2D Temporal Map에서 관계 학습 | 강력한 성능 |
| Moment-DETR (2021) | One-Stage | DETR식 엔드-투-엔드 구간 예측 | 단순 구조 |

## 6. 대표 모델 상세
### 6.1 TALL (Temporal Activity Localization via Language)
- 슬라이딩 윈도우로 후보 구간 생성 후 랭킹.
- 텍스트/비디오 feature를 매칭해 점수화.
- Two-Stage의 대표적 기준선.

### 6.2 2D-TAN
- 시간 구간을 2D 매트릭스로 구성.
- 각 구간 간 관계를 학습해 더 정밀한 локализ레이션 수행.

### 6.3 Moment-DETR
- DETR 구조를 차용해 **proposal 없이 직접 구간 예측**.
- 텍스트와 비디오를 Transformer에서 융합.

## 7. 학습 목표
- 회귀 손실: $L_1$ / Smooth $L_1$ / IoU loss.
- 분류 손실: Cross-Entropy.
- 대조 학습: 텍스트-비디오 정합을 위한 contrastive loss.

## 8. 평가 지표
- **R@k, IoU@\tau**: top-k 결과 중 IoU가 임계값 이상인 비율.
- **mIoU**: 예측 구간과 정답 구간의 평균 IoU.
- **mAP**: 여러 IoU 기준에서 평균 정밀도.

## 9. 주요 벤치마크 성능(요약)
- Charades-STA, ActivityNet Captions, TACoS, DiDeMo에서
  - 2D-TAN 계열이 강한 성능을 보임.
  - DETR 계열은 간단한 구조로 경쟁력 있는 결과를 달성.
- 벤치마크별 세부 수치는 논문/리더보드에 따라 업데이트 필요.

## 10. 데이터셋
- **Charades-STA**: 문장-비디오 구간 매칭.
- **ActivityNet Captions**: 장면 설명과 시간 구간.
- **TACoS**: 요리 동영상 기반 내러티브 정렬.
- **DiDeMo**: 텍스트-비디오 클립 정합.

## 11. 난점과 연구 방향
- 긴 비디오에서 효율적 검색.
- 질의-구간의 미세한 시간 정렬.
- 멀티모달 표현의 시간 정합.
- 대규모 사전학습(영상-텍스트) 활용.

## 12. 관련 개념
- [[Video Retrieval]]
- [[Moment Retrieval]]
- [[Temporal Action Localization]]
- [[Vision Transformer]]
- [[Transformer]]

## 13. 참고 문헌
- Gao, J. et al. (2017). *TALL: Temporal Activity Localization via Language*. https://arxiv.org/abs/1705.02101
- Hendricks, L. et al. (2017). *Localizing Moments in Video with Natural Language*. https://arxiv.org/abs/1708.01641
- Yuan, J. et al. (2019). *Semantic Conditioned Dynamic Modulation for Temporal Sentence Grounding in Videos*. https://arxiv.org/abs/1910.06069
- Zhang, D. et al. (2020). *Temporal Grounding of Natural Language in Video: A Review*. https://arxiv.org/abs/1909.06404
- Zhang, S. et al. (2020). *2D-TAN: Task-Driven Temporal Video Grounding*. https://arxiv.org/abs/1911.09489
- Lei, J. et al. (2020). *Moment-DETR: End-to-End Video Moment Localization*. https://arxiv.org/abs/2105.08745
