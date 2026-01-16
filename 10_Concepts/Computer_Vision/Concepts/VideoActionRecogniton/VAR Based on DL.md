---
title: "A Survey of Video Action Recognition Based on Deep Learning"
source_pdf: "A Survey of Video Action Recognition Based on Deep Learning.pdf"
venue: "Knowledge-Based Systems (2025)"
tags: [paper, survey, video-action-recognition, deep-learning]
---

# A Survey of Video Action Recognition Based on Deep Learning

## 한줄 요약
딥러닝 기반 VAR(Video Action Recognition)의 핵심 아키텍처 계열(두-스트림, 3D-CNN, RNN/LSTM, Attention/Transformer, 멀티모달, 포즈/그래프)을 구조 중심으로 정리하고, 대표 데이터셋/지표/응용/과제를 체계적으로 정리한 서베이.

## 핵심 요약
- **문제 정의**: 비디오에서 인간 행동을 분류/인식하는 VAR은 시간적 맥락과 공간적 단서를 동시에 다뤄야 함.
- **모델 계열**: 두-스트림(공간+모션), 3D-CNN, RNN/LSTM 기반 시계열 모델, Attention/Transformer 계열, 2D/멀티스트림 CNN, GCN, 하이브리드, 멀티모달, 포즈 기반(HPE) 모델이 주요 축.
- **데이터셋**: UCF101, HMDB51, Kinetics, ActivityNet, Sports-1M, Something-Something V1/V2, NTU RGB+D 60/120, JHMDB, Charades, AVA, KTH, UCF50 등 다양한 벤치마크가 사용됨.
- **평가지표**: Accuracy(Top-1/Top-5), mAP, Precision/Recall/F1, IoU 등이 사용되며 데이터/과제 특성에 따라 선택됨.
- **응용 분야**: 감시/보안, HCI, 스포츠 분석, 의료/헬스케어, 교육, 스마트홈 등.
- **과제/미래 방향**: 계산 비용, 대규모 라벨 데이터 의존, 장기 시간 의존성 모델링, 도메인 일반화/강건성, 실시간성, 해석가능성, 멀티모달 정합/융합이 핵심 이슈.

## 모델 계열 정리 (요점)
- **Two-Stream**: RGB(공간) + Optical Flow(모션) 분리 후 결합. 강력하지만 계산 비용과 플로우 의존이 단점.
- **3D-CNN**: 시공간 컨볼루션으로 직접 모션을 포착. 성능 좋지만 메모리/연산 부담 큼.
- **RNN/LSTM**: 프레임/클립 특징을 시계열로 모델링. 장기 의존성 표현에 도움, 하지만 학습/추론 비용과 안정성 이슈.
- **Attention/Transformer**: 중요한 프레임/영역에 집중. Self-Attention, Spatiotemporal Attention, Video Transformer 계열이 대표.
- **GCN/포즈 기반**: 스켈레톤을 그래프로 모델링해 동작 구조를 학습. 시점 변화에 강하나 포즈 품질 의존.
- **멀티모달/하이브리드**: RGB+Flow+Skeleton+Audio 등 결합. 성능은 상승하지만 정합/동기화 비용 증가.

## 학습 로드맵 (Video Action Recognition)

### 0) 기초 준비
- 비전/딥러닝 기본기: CNN, 시계열 모델(RNN/LSTM), 기본 최적화/정규화.
- 비디오 처리: 프레임 샘플링, 클립 구성, Optical Flow 개념.

### 1) 데이터셋/평가지표 이해
- **입문용**: UCF101, HMDB51.
- **대규모/다양성**: Kinetics, ActivityNet, Sports-1M.
- **미세 동작/컨텍스트**: Something-Something, Charades, AVA.
- **스켈레톤 기반**: NTU RGB+D 60/120, Kinetics Skeleton.
- **지표**: Accuracy(Top-1/Top-5), mAP, Precision/Recall/F1, IoU.

### 2) 기본 베이스라인 구축
- 2D-CNN 프레임 분류 → TSN류 시간 샘플링 전략 적용.
- 투-스트림(Spatial+Flow) 모델로 모션 정보 추가.

### 3) 시공간 모델링 심화
- 3D-CNN 계열로 시공간 특징 직접 학습.
- RNN/LSTM으로 클립 특징 시계열 모델링.

### 4) Attention/Transformer 확장
- Spatiotemporal Attention 도입으로 중요한 구간/영역 강조.
- Video Transformer 계열로 장기 의존성 모델링.

### 5) 멀티모달/포즈/그래프 확장
- RGB+Flow+Skeleton+Audio 등 멀티모달 융합.
- 스켈레톤 기반 GCN, 포즈 추정(HPE) 파이프라인 적용.

### 6) 현실 적용과 최적화
- 경량화/실시간성: 모델 압축, 프레임 샘플링 최적화.
- 일반화/강건성: 도메인 이동, 약지도/자기지도 학습 실험.
- 해석가능성: Attention 시각화, 실패 사례 분석.

## 실습 체크리스트 (권장)
- UCF101에서 Two-Stream vs 3D-CNN 간 성능/비용 비교.
- HMDB51에서 RNN/LSTM 기반 시간 모델링 효과 측정.
- Something-Something에서 Attention 도입 전/후 성능 비교.
- NTU RGB+D에서 Skeleton-GCN 적용 및 RGB 융합 실험.
- 동일 모델의 Accuracy와 mAP 비교 리포트 작성.

## 참고
- 원문 PDF: `A Survey of Video Action Recognition Based on Deep Learning.pdf`
- [[A Survey of Video Action Recognition Based on Deep Learning.pdf]]
