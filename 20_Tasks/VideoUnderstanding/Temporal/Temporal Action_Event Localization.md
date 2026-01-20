---
title: Temporal Action/Event Localization
aliases:
  - Temporal Action Localization
  - Temporal Event Localization
tags:
  - task
  - video
  - localization
topics:
  - Video Understanding
---
**Temporal Action Localization (TAL)** 또는 **Temporal Action Detection (TAD)** 은 편집되지 않은(Untrimmed) 긴 비디오에서 행동(Action)이 발생하는 정확한 시간 구간을 찾아내고(Localization), 해당 행동의 카테고리를 분류(Classification)하는 비디오 이해의 핵심 작업입니다. 이는 보안 감시, 스포츠 분석, 자율주행, 비디오 검색 등 다양한 실세계 응용에서 필수적인 기술입니다.

---

## 1. 핵심 개념 및 정의

### 1.1 작업 정의
TAL은 주어진 비디오 $V = \{f_1, f_2, ..., f_T\}$에서 각 행동 인스턴스 $a_i$에 대해:
- **시작 시간(Start time)** $t_s^i$
- **종료 시간(End time)** $t_e^i$
- **행동 카테고리(Action class)** $c_i$

를 예측하는 것입니다. 이는 이미지의 객체 탐지(Object Detection)를 시간 축으로 확장한 것으로 볼 수 있습니다.

### 1.2 핵심 특징

**[다중 스케일 문제]**  
행동은 몇 초에서 몇 분까지 매우 다양한 길이를 가집니다. 예를 들어 "손 흔들기"는 2-3초이지만, "요리하기"는 수 분이 걸릴 수 있습니다.

**[경계 모호성(Boundary Ambiguity)]**  
행동의 시작과 끝은 명확하지 않은 경우가 많습니다. 예를 들어 "앉기" 행동이 정확히 언제 시작되는지 판단하기 어렵습니다.

**[행동 간 중첩(Action Overlap)]**  
실제 비디오에서는 여러 행동이 동시에 발생하거나 시간적으로 겹칠 수 있습니다.

**[배경 지배(Background Dominance)]**  
전체 비디오의 대부분은 의미 있는 행동이 아닌 배경이므로, 클래스 불균형 문제가 심각합니다.

---

## 2. 아키텍처 및 핵심 모듈

### 2.1 전체 파이프라인

TAL 시스템은 일반적으로 다음과 같은 모듈로 구성됩니다:

```
입력 비디오 → 특징 추출 → 시간적 모델링 → 제안 생성/분류 → 후처리
```

### 2.2 특징 추출(Feature Extraction)

**[사전 학습된 백본 네트워크]**
- **2D CNN 기반**: ResNet, VGG 등을 각 프레임에 적용하여 프레임 단위 특징 추출
- **3D CNN 기반**: C3D, I3D, SlowFast 등을 사용하여 시공간적 특징을 직접 추출
- **Two-Stream Networks**: RGB 스트림과 Optical Flow 스트림을 결합하여 외관(Appearance)과 움직임(Motion) 정보를 동시에 캡처
- **Transformer 기반**: Video Swin Transformer, VideoMAE 등 최신 모델 활용

**[특징의 시간적 다운샘플링]**
긴 비디오를 처리하기 위해 특징을 시간 축으로 다운샘플링합니다. 예를 들어, 30fps 비디오를 1fps 특징 시퀀스로 변환합니다.

### 2.3 시간적 모델링(Temporal Modeling)

**[Temporal Convolutional Networks (TCN)]**
- 1D Convolution을 시간 축에 적용하여 지역적 시간 패턴을 학습
- Dilated Convolution을 사용하여 넓은 수용 영역(Receptive Field) 확보
- Multi-scale TCN으로 다양한 길이의 행동 포착

**[Temporal Feature Pyramid Networks (TFPN)]**
- 이미지 객체 탐지의 FPN을 시간 축으로 적용
- 다중 스케일 특징 맵을 계층적으로 구성하여 다양한 길이의 행동 감지
- Bottom-up과 Top-down 경로를 통해 저수준과 고수준 정보 융합

**[Transformer 기반 모델링]**
- Self-Attention으로 전역적 시간 의존성 학습
- ActionFormer, TriDet 등이 대표적
- 위치 인코딩(Positional Encoding)으로 시간적 순서 정보 주입

**[Graph Neural Networks (GNN)]**
- 비디오 세그먼트를 노드로, 시간적 관계를 엣지로 모델링
- 메시지 전달(Message Passing)을 통해 문맥 정보 전파

**[State Space Models (SSM)]**
- Mamba 등 최신 SSM을 활용하여 긴 시퀀스를 효율적으로 처리
- Transformer보다 계산 복잡도가 낮으면서도 장거리 의존성 학습 가능

### 2.4 행동 탐지 방식

**[Two-Stage 접근법]**

1단계에서 Temporal Action Proposal Generation (TAPG)을 수행하고, 2단계에서 각 제안을 분류합니다.

- **제안 생성**: BMN, BSN 등
- **제안 분류**: 각 제안에 대해 행동 분류기 적용
- **장점**: 높은 재현율(Recall) 달성 가능
- **단점**: 두 단계가 독립적이어서 최적화가 어렵고 느림

**[One-Stage 접근법]**

제안 생성과 분류를 동시에 수행합니다.

- **Anchor-based**: 미리 정의된 앵커(다양한 길이의 템플릿)를 기반으로 행동 탐지
  - SSN(Single Shot Temporal Action Detection), SST 등
  - 각 앵커에서 경계 오프셋과 행동 확률을 동시에 회귀
  
- **Anchor-free**: 앵커 없이 직접 행동 경계를 예측
  - AFSD(Anchor-Free Single-stage Detector)
  - 각 시간 위치에서 행동의 시작까지 거리와 끝까지 거리를 직접 회귀
  
- **DETR 기반**: Detection Transformer 방식 적용
  - 학습 가능한 쿼리(Query)를 통해 행동 인스턴스를 직접 예측
  - Bipartite Matching으로 예측과 정답을 일대일 매칭

### 2.5 핵심 기술 모듈

**[Actionness 모델링]**
- 각 시간 위치에서 "행동이 발생하고 있을 확률" 추정
- Background Suppression을 통해 배경 영역에서 잘못된 탐지 억제
- Foreground-Background Separation으로 행동 영역 강조

**[Boundary Regression]**
- 행동의 시작과 끝 경계를 정밀하게 조정
- Distance-based Regression: 현재 위치에서 경계까지 거리 예측
- IoU-based Regression: 예측 구간과 실제 구간의 IoU를 직접 회귀

**[Boundary-Matching]**
- 시작 경계와 끝 경계를 독립적으로 예측한 후 매칭
- BMN(Boundary-Matching Network)이 대표적
- Temporal Evaluation Module로 각 조합의 품질 평가

**[Multi-Scale Modeling]**
- Pyramid 구조로 다양한 시간 해상도에서 특징 추출
- Short, Medium, Long 행동을 각각 다른 스케일에서 처리
- Feature Aggregation으로 다중 스케일 정보 통합

**[Contextual Modeling]**
- 행동 전후의 문맥 정보 활용
- Pre-action과 Post-action 정보로 경계 정밀화
- Temporal Causality: 행동 간 인과 관계 학습 (예: "공을 던지다" → "공을 받다")

**[Attention Mechanisms]**
- Temporal Self-Attention: 비디오 내 모든 시간 위치 간 관계 학습
- Cross-Modal Attention: RGB와 Optical Flow 등 다중 모달리티 융합
- Boundary-Aware Attention: 경계 주변 정보에 집중

---

## 3. 학습 전략 및 손실 함수

### 3.1 지도 학습(Fully-Supervised)

**[분류 손실(Classification Loss)]**
```
L_cls = CrossEntropy(predicted_class, ground_truth_class)
```
행동 카테고리 분류를 위한 표준 교차 엔트로피 손실

**[위치 회귀 손실(Localization Loss)]**
```
L_loc = SmoothL1(predicted_boundaries, ground_truth_boundaries)
```
경계 위치를 정확하게 예측하기 위한 회귀 손실

**[IoU 손실]**
```
L_iou = 1 - IoU(predicted_segment, ground_truth_segment)
```
예측 구간과 실제 구간의 중첩도를 직접 최적화

**[Focal Loss]**
```
L_focal = -α(1-p_t)^γ log(p_t)
```
클래스 불균형 문제(배경 vs 행동) 해결을 위한 손실

**[전체 손실]**
```
L_total = λ_cls * L_cls + λ_loc * L_loc + λ_iou * L_iou
```

### 3.2 약지도 학습(Weakly-Supervised)

비디오 레벨 라벨만 주어지고 시간적 경계는 없는 상황에서 학습합니다.

**[Multiple Instance Learning (MIL)]**
- 비디오를 여러 세그먼트(Instance)의 집합(Bag)으로 간주
- 적어도 하나의 세그먼트가 긍정적이면 전체 비디오가 긍정적
- Top-K MIL: 가장 높은 점수를 가진 K개 세그먼트의 평균으로 비디오 점수 계산

**[Attention-based Localization]**
- Temporal Class Activation Mapping (T-CAM)
- 분류 네트워크의 attention weight로 행동 위치 근사

**[Contrastive Learning]**
- 같은 행동의 세그먼트는 가깝게, 다른 행동은 멀게 임베딩

### 3.3 Zero-shot 및 Open-Vocabulary

**[Vision-Language Models (VLM) 활용]**
- CLIP과 같은 VLM의 zero-shot 능력 활용
- 텍스트 쿼리로 새로운 행동 카테고리 탐지
- Prompt Engineering으로 행동 설명 최적화

**[Self-Training]**
- VLM으로 pseudo label 생성 후 self-training
- Confidence Threshold로 신뢰도 높은 pseudo label만 사용

---

## 4. 평가 메트릭

### 4.1 mAP (mean Average Precision)

다양한 IoU 임계값에서 평균 정밀도를 계산합니다.
```
mAP = (1/N) Σ AP@IoU_threshold
```
- **mAP@0.5**: IoU ≥ 0.5일 때 정답으로 간주
- **mAP@0.75**: 더 엄격한 기준
- **Average mAP**: 여러 임계값(0.5, 0.55, ..., 0.95)의 평균

### 4.2 Temporal IoU (tIoU)

예측 구간과 실제 구간의 교집합 비율:
```
tIoU = (overlap_duration) / (union_duration)
```

### 4.3 Recall@IoU

특정 IoU 임계값에서 실제 행동 중 몇 개를 찾았는지 측정:
```
Recall@0.5 = (정답으로 간주된 예측 수) / (전체 ground truth 수)
```

---

## 5. 주요 데이터셋

### 5.1 THUMOS14
- **특징**: 스포츠 행동, 200+ 시간의 비디오
- **행동 수**: 20개 카테고리
- **난이도**: 중간, 행동 간 중첩 많음

### 5.2 ActivityNet
- **특징**: 일상 행동, 매우 긴 비디오
- **행동 수**: 200개 카테고리
- **난이도**: 높음, 평균 비디오 길이 10분 이상

### 5.3 FineAction
- **특징**: 세밀한(Fine-grained) 행동
- **행동 수**: 100+ 카테고리
- **난이도**: 매우 높음, 유사한 행동 구별 필요

### 5.4 MultiTHUMOS
- **특징**: 다중 라벨(Multi-label) 환경
- **특성**: 한 시점에 여러 행동 동시 발생

---

## 6. 기술적 도전 과제

### 6.1 긴 비디오 처리
- **문제**: 메모리 제약으로 전체 비디오를 한 번에 처리 불가
- **해결책**: Sliding window, Feature caching, Streaming processing

### 6.2 다중 스케일
- **문제**: 짧은 행동과 긴 행동을 동시에 잘 탐지해야 함
- **해결책**: Multi-scale feature pyramid, Adaptive temporal sampling

### 6.3 경계 모호성
- **문제**: 행동의 시작/끝이 주관적이고 불명확
- **해결책**: Boundary-sensitive feature learning, Gaussian smoothing

### 6.4 클래스 불균형
- **문제**: 배경이 대부분, 행동은 일부 구간에만 존재
- **해결책**: Focal loss, Hard negative mining, Balanced sampling

### 6.5 계산 효율성
- **문제**: 실시간 응용에서 빠른 처리 필요
- **해결책**: Knowledge distillation, Network pruning, Early exit

---

## 7. 최신 연구 동향

### 7.1 Transformer 통합
- Self-attention으로 전역 문맥 학습
- DETR 스타일의 end-to-end 학습
- Query-based detection

### 7.2 인과 관계 모델링
- 행동 간 시간적 인과성 학습
- 행동 전이(Transition) 예측
- 미래 행동 예측(Anticipation)

### 7.3 멀티모달 학습
- Vision-Language Models 통합
- Open-vocabulary detection
- Zero-shot generalization

### 7.4 온라인/스트리밍 탐지
- 실시간 처리 요구사항 대응
- Causal convolution (미래 정보 없이 탐지)
- Incremental learning

### 7.5 약지도/자기지도 학습
- 주석 비용 절감
- Pseudo labeling
- Self-training with VLMs

---

## 8. 핵심 연구 및 최신 논문

| Paper | Description | Published |
| :--- | :--- | :--- |
| [Harnessing Temporal Causality for Advanced Temporal Action Detection](https://arxiv.org/abs/2407.17792) | 행동 간 시간적 인과관계를 모델링하여 정확도를 크게 향상시킨 SOTA 연구입니다. | a year ago |
| [ActionFormer: Localizing Moments of Actions with Transformers](https://arxiv.org/abs/2202.07925) | Transformer를 TAL에 적용하여 지역-전역 문맥을 효과적으로 학습한 영향력 있는 연구입니다. | 3 years ago |
| [TriDet: Temporal Action Detection with Relative Boundary Modeling](https://arxiv.org/abs/2303.07347) | 상대적 경계 모델링으로 모호한 경계 문제를 해결한 one-stage detector입니다. | 3 years ago |
| [TimeLoc: Unified End-to-End Framework for Precise Timestamp Localization](https://arxiv.org/abs/2503.06526) | TAD, Moment Retrieval 등 여러 시간적 위치 추정 작업을 통합한 범용 프레임워크입니다. | 10 months ago |
| [FDDet: Frequency-Decoupling for Boundary Refinement](https://arxiv.org/abs/2504.00647) | 주파수 영역 분석으로 경계를 정밀하게 개선한 최신 연구입니다. | 10 months ago |
| [MS-Temba: Multi-Scale Temporal Mamba for Long Untrimmed Videos](https://arxiv.org/abs/2501.06138) | Mamba SSM을 활용하여 긴 비디오를 효율적으로 처리하는 최신 접근법입니다. | a year ago |
| [DyFADet: Dynamic Feature Aggregation for Temporal Action Detection](https://arxiv.org/abs/2407.03197) | 동적 특징 집계로 다양한 길이의 행동을 효과적으로 모델링합니다. | 2 years ago |
| [Training-Free Zero-Shot TAD with Vision-Language Models](https://arxiv.org/abs/2501.13795) | VLM을 활용한 학습 없는 zero-shot TAD를 제안한 최신 연구입니다. | a year ago |
| [Boundary-Recovering Network for Temporal Action Detection](https://arxiv.org/abs/2408.09354) | 다중 스케일 행동의 경계를 복구하는 특화된 네트워크를 제안합니다. | a year ago |

---

## 9. 응용 분야

**보안 감시**: 이상 행동 자동 탐지  
**스포츠 분석**: 주요 플레이 자동 하이라이트  
**자율주행**: 보행자/차량 행동 예측  
**의료**: 수술 과정 자동 기록 및 분석  
**비디오 검색**: 특정 행동 순간 검색  
**로봇 공학**: 인간 행동 이해 및 모방

Temporal Action Localization은 비디오 이해의 가장 기초적이면서도 도전적인 작업으로, 최근 Transformer와 VLM의 발전으로 인해 큰 도약을 이루고 있습니다. 특히 **zero-shot generalization**, **실시간 처리**, **장시간 비디오 이해** 방향으로 빠르게 발전하고 있습니다.