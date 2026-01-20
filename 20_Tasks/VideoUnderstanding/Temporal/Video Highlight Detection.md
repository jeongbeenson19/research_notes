---
title: Video Highlight Detection
aliases:
tags:
  - task
  - video
  - highlight
topics:
  - Video Understanding
---
**Video Highlight Detection (VHD)** 은 긴 비디오에서 사용자가 가장 관심을 가질 만한 중요하고 흥미로운 순간(Highlight)을 자동으로 찾아내고 순위를 매기는 작업입니다. 이는 비디오 요약(Video Summarization)과 밀접하게 관련되어 있지만, 전체 스토리를 요약하는 것이 아니라 "가장 매력적인 순간"을 추출하는 데 초점을 맞춥니다.

---

## 1. 핵심 개념 및 정의

### 1.1 작업 정의

주어진 비디오 $V = \{f_1, f_2, ..., f_T\}$에서 각 시간 세그먼트 $s_i$에 대해 **중요도 점수(Saliency Score)** 또는 **하이라이트 점수(Highlight Score)** $h_i \in [0, 1]$을 예측하는 것입니다.

**목표**: 높은 점수를 받은 순간들이 실제로 시청자에게 가장 흥미롭고 중요한 부분이어야 합니다.

### 1.2 핵심 특징

**[주관성(Subjectivity)]**  
무엇이 "하이라이트"인지는 사용자마다 다릅니다. 축구 경기에서 골 장면은 대부분의 사람에게 하이라이트이지만, 특정 선수의 패스 플레이는 일부 팬에게만 중요할 수 있습니다.

**[도메인 의존성(Domain-Dependency)]**  
스포츠, 요리, 여행 등 도메인마다 하이라이트의 정의가 다릅니다. 축구 경기에서는 골/세이브가 하이라이트이지만, 요리 영상에서는 완성 장면이 하이라이트입니다.

**[시간적 밀집성(Temporal Density)]**  
하이라이트는 특정 순간에 밀집되어 있을 수 있습니다. 예를 들어, 경기 종료 직전에 여러 중요 장면이 연속으로 발생할 수 있습니다.

**[문맥 의존성(Context-Dependency)]**  
단순히 액션이 많다고 하이라이트는 아닙니다. 문맥상 중요한 순간(예: 역전 골)이 더 중요합니다.

---

## 2. 작업 유형별 분류

### 2.1 Generic (범용) Highlight Detection

**정의**: 특정 질의 없이 비디오 전체에서 일반적으로 흥미로운 순간을 찾습니다.

**평가 방법**: 여러 사람의 주석을 평균하여 "일반적 중요도" 측정

**대표 데이터셋**: 
- TVSum: 다양한 도메인의 50개 비디오
- SumMe: 사용자 생성 비디오 25개

**응용**: 자동 비디오 요약, 썸네일 생성

### 2.2 Query-Dependent (질의 기반) Highlight Detection

**정의**: 자연어 질의(Query)가 주어졌을 때, 그 질의와 관련된 하이라이트를 찾습니다.

**예시**: 
- 질의: "골키퍼의 슈퍼 세이브"
- 결과: 골키퍼가 골을 막은 순간들에 높은 점수 부여

**대표 데이터셋**:
- QVHighlights: 10,000+ 비디오-질의 쌍
- YouTube Highlights: 다양한 도메인

**응용**: 맞춤형 비디오 탐색, 질의 기반 비디오 편집

### 2.3 Domain-Specific Highlight Detection

**정의**: 특정 도메인(스포츠, 뉴스 등)에 특화된 하이라이트 탐지

**스포츠 하이라이트**:
- 골, 득점, 파울, 리플레이 등 특정 이벤트 중심
- SoccerNet, NBA Highlights 데이터셋

**자아 중심(Egocentric) 하이라이트**:
- 1인칭 카메라에서 중요한 순간 탐지
- 일상 활동, 여행 등

**응용**: 스포츠 중계, 일상 라이프로그 요약

---

## 3. 아키텍처 및 핵심 모듈

### 3.1 전체 파이프라인

```
입력 비디오 → 특징 추출 → 시간적 모델링 → 중요도 예측 → 후처리/순위화
```

### 3.2 특징 추출(Feature Extraction)

**[시각적 특징(Visual Features)]**
- **CNN 기반**: ResNet, VGG를 프레임별로 적용
- **3D CNN**: I3D, C3D로 시공간 특징 추출
- **Transformer 기반**: ViT, VideoMAE 등

**[오디오 특징(Audio Features)]**
- VGGish, PANN (Pre-trained Audio Neural Networks)
- 환호성, 음악 변화 등 오디오 단서 활용
- 특히 스포츠에서 관중 소리는 강력한 하이라이트 신호

**[멀티모달 융합(Multi-modal Fusion)]**
- Early Fusion: 초기 단계에서 시각+오디오 결합
- Late Fusion: 각각 처리 후 최종 결합
- Cross-Modal Attention: 두 모달리티 간 상호작용 학습

**[텍스트 특징(Text Features) - Query-Dependent]**
- BERT, CLIP 등으로 질의 임베딩
- Video-Text Cross-Modal Encoding

### 3.3 시간적 모델링(Temporal Modeling)

**[Recurrent Networks (RNN/LSTM)]**
초기 방법들이 주로 사용했으며, 순차적 정보를 처리합니다.

$$h_t = LSTM(x_t, h_{t-1})$$
$$score_t = MLP(h_t)$$


**[Temporal Convolutional Networks (TCN)]**
1D Convolution으로 지역적 시간 패턴을 효율적으로 학습합니다.
- Dilated Convolution으로 넓은 수용 영역 확보
- Multi-scale TCN으로 다양한 시간 스케일 포착

**[Transformer 기반 모델링]**
Self-attention으로 전역적 시간 의존성을 학습합니다.
- Positional Encoding으로 시간 순서 정보 주입
- Cross-Attention으로 Video-Query 정렬 (Query-Dependent)

**[Graph Neural Networks (GNN)]**
비디오 세그먼트를 노드로, 시간적/의미적 관계를 엣지로 모델링합니다.
- Temporal Graph: 인접 세그먼트 간 연결
- Semantic Graph: 유사한 내용의 세그먼트 간 연결

### 3.4 중요도 예측(Saliency Prediction)

**[회귀(Regression) 접근법]**
각 세그먼트에 대해 연속적인 중요도 점수 $s_i \in [0, 1]$ 예측:
```
score_i = σ(MLP(feature_i))
```
여기서 σ는 sigmoid 함수

**[랭킹(Ranking) 접근법]**
세그먼트 간 상대적 순위를 학습:
```
L_rank = max(0, margin - (score_pos - score_neg))
```
중요한 세그먼트가 덜 중요한 세그먼트보다 높은 점수를 받도록 학습

**[분류(Classification) 접근법]**
하이라이트/비하이라이트 이진 분류:
```
p_highlight = softmax(MLP(feature_i))
```

### 3.5 Query-Video 정렬 모듈 (Query-Dependent)

**[Cross-Modal Attention]**
질의와 비디오 간 상호작용을 모델링:
```
Attention(Q, K, V) = softmax(QK^T / √d_k)V
```
- Q: 질의 특징
- K, V: 비디오 특징

**[Modality-Specific Encoding]**
- Query Encoder: BERT 등으로 텍스트 인코딩
- Video Encoder: Transformer로 비디오 인코딩
- Fusion Layer: 두 모달리티 결합

**[Temporal Alignment]**
질의가 언급하는 시간 범위와 비디오 세그먼트를 정렬:
- Soft Alignment: Attention 기반
- Hard Alignment: Dynamic Programming

### 3.6 후처리 및 순위화

**[Non-Maximum Suppression (NMS)]**
유사하고 인접한 하이라이트를 병합:
```
if IoU(segment_i, segment_j) > threshold:
    keep segment with higher score
```

**[Top-K Selection]**
가장 높은 점수를 받은 K개 세그먼트 선택

**[Diversity Promotion]**
다양한 하이라이트를 선택하기 위해 유사한 세그먼트에 페널티:
```
score_final = score_importance - λ * similarity_penalty
```

---

## 4. 학습 전략 및 손실 함수

### 4.1 지도 학습(Fully-Supervised)

**[회귀 손실(Regression Loss)]**
```
L_reg = (1/N) Σ ||score_i - ground_truth_i||^2
```
평균 제곱 오차(MSE) 또는 평균 절대 오차(MAE) 사용

**[랭킹 손실(Ranking Loss)]**
```
L_rank = Σ max(0, margin + score_neg - score_pos)
```
Triplet Loss 또는 Pairwise Ranking Loss

**[결합 손실]**
```
L_total = λ_reg * L_reg + λ_rank * L_rank
```

### 4.2 약지도 학습(Weakly-Supervised)

비디오 레벨 라벨만 주어지고 세그먼트 레벨 라벨은 없는 경우:

**[Multiple Instance Learning (MIL)]**
- 비디오를 세그먼트 집합(Bag)으로 간주
- 전체 비디오 라벨에서 세그먼트 중요도 유추

**[Attention-based Weak Supervision]**
```
video_score = Σ α_i * segment_score_i
α_i = softmax(attention_i)
```
비디오 레벨 라벨로 학습하되, attention weight로 중요 세그먼트 식별

### 4.3 비지도 학습(Unsupervised)

**[Audio-Visual Recurrence]**
- 오디오와 비디오의 반복 패턴(Recurrence) 학습
- 반복되는 패턴(예: 리플레이)을 하이라이트로 간주

**[Self-Supervised Pretext Tasks]**
- Frame Order Prediction
- Speed Prediction
- Audio-Visual Correspondence

**[Clustering-based]**
- 비디오 세그먼트를 클러스터링
- 각 클러스터의 대표 세그먼트를 하이라이트로 선택

### 4.4 사용자 개인화(Personalization)

**[사용자 선호도 학습]**
- 사용자의 과거 시청 이력 분석
- 클릭, 재생, 건너뛰기 등의 암묵적 피드백 활용

**[메타 학습(Meta-Learning)]**
- 빠르게 새로운 사용자에게 적응
- Few-shot Learning으로 소수 샘플만으로 개인화

---

## 5. 평가 메트릭

### 5.1 mAP (mean Average Precision)

IoU 임계값을 사용하여 예측된 하이라이트와 실제 하이라이트의 매칭 평가:
```
mAP = (1/N) Σ AP_i
```

### 5.2 Hit@K

상위 K개 예측 중 실제 하이라이트가 포함된 비율:
```
Hit@K = (하이라이트가 포함된 비디오 수) / (전체 비디오 수)
```

### 5.3 Recall@K

전체 하이라이트 중 상위 K개 예측에서 찾은 비율:
```
Recall@K = (찾은 하이라이트 수) / (전체 하이라이트 수)
```

### 5.4 Kendall's Tau / Spearman's ρ

예측 순위와 실제 순위 간 상관관계 측정:
```
τ = (concordant pairs - discordant pairs) / total pairs
```

### 5.5 F1-Score

정밀도와 재현율의 조화 평균:
```
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

---

## 6. 주요 데이터셋

### 6.1 TVSum (TV Summarization)
- **비디오 수**: 50개
- **도메인**: 뉴스, 스포츠, 요리 등 10개 카테고리
- **주석**: 20명의 사용자가 각 비디오 세그먼트에 중요도 점수 부여
- **특징**: 다양한 도메인, 사용자 간 선호도 차이 연구 가능

### 6.2 SumMe (Summary of Me)
- **비디오 수**: 25개
- **도메인**: 사용자 생성 비디오 (휴가, 스포츠 등)
- **주석**: 15-18명 사용자가 중요 장면 선택
- **특징**: 주관성이 강한 개인 비디오

### 6.3 QVHighlights (Query-based Video Highlights)
- **비디오 수**: 10,148개
- **질의 수**: 10,310개
- **도메인**: YouTube 비디오 (다양)
- **주석**: 질의별 하이라이트 세그먼트 + 중요도 점수
- **특징**: 대규모, 질의 기반, Moment Retrieval과 Highlight Detection 동시 평가

### 6.4 YouTube Highlights
- **비디오 수**: 600+
- **도메인**: 6개 카테고리 (스케이트보드, 개, 서핑 등)
- **주석**: 도메인별 하이라이트
- **특징**: 도메인 특화 하이라이트 연구

### 6.5 SoccerNet
- **비디오 수**: 500+ 축구 경기
- **주석**: 골, 카드, 교체 등 이벤트 타임스탬프
- **특징**: 스포츠 하이라이트의 표준 벤치마크

---

## 7. 기술적 도전 과제

### 7.1 주관성 문제
- **문제**: 사용자마다 하이라이트 기준이 다름
- **해결책**: 
  - 다수 사용자 주석 평균
  - 개인화 모델 학습
  - 다양성(Diversity) 증진

### 7.2 긴 비디오 처리
- **문제**: 시간/메모리 제약으로 전체 비디오 처리 어려움
- **해결책**:
  - Hierarchical Processing
  - Feature Caching
  - Efficient Sampling

### 7.3 도메인 적응
- **문제**: 특정 도메인에서 학습한 모델이 다른 도메인에서 작동 안 함
- **해결책**:
  - Domain-Agnostic Feature Learning
  - Transfer Learning
  - Meta-Learning

### 7.4 주석 비용
- **문제**: 하이라이트 주석은 시간이 많이 걸리고 비쌈
- **해결책**:
  - Weakly-Supervised Learning
  - Unsupervised Learning
  - Active Learning

### 7.5 실시간 처리
- **문제**: 라이브 스포츠 등에서 실시간 하이라이트 생성 필요
- **해결책**:
  - Online/Streaming Algorithms
  - Lightweight Models
  - Hardware Acceleration

---

## 8. 최신 연구 동향

### 8.1 Transformer 및 DETR 기반 접근법
- Self-attention으로 장거리 의존성 학습
- Query-based Detection
- End-to-end 최적화

### 8.2 멀티모달 학습
- Vision + Audio + Text 통합
- Cross-Modal Attention
- CLIP 등 사전 학습 VLM 활용

### 8.3 사용자 개인화
- 시청 이력 기반 선호도 학습
- Few-shot Personalization
- 암묵적 피드백(Click, Skip) 활용

### 8.4 Test-Time Adaptation
- 각 테스트 비디오에 맞춰 실시간 적응
- Meta-Auxiliary Learning
- Cross-Modality Hallucinations

### 8.5 제로샷 및 오픈 어휘(Open-Vocabulary)
- 학습 시 보지 못한 도메인/카테고리에 일반화
- VLM의 강력한 제로샷 능력 활용
- 자연어로 새로운 하이라이트 정의 가능

### 8.6 Moment Retrieval과의 통합
- Highlight Detection과 Moment Retrieval을 동시 해결
- 공유 표현 학습
- 상호 보완적 작업 활용

---

## 9. 핵심 연구 및 최신 논문

| Paper | Description | Published |
| :--- | :--- | :--- |
| [QVHighlights: Detecting Moments and Highlights via Natural Language Queries](https://arxiv.org/abs/2107.09609) | 질의 기반 하이라이트 탐지의 대규모 벤치마크를 제안하고 문제를 정립한 영향력 있는 연구입니다. | 4 years ago |
| [UMT: Unified Multi-modal Transformers for Joint MR and HD](https://arxiv.org/abs/2203.12745) | Moment Retrieval과 Highlight Detection을 통합 Transformer로 동시 해결한 연구입니다. | 4 years ago |
| [Query-Dependent Video Representation for MR and HD](https://arxiv.org/abs/2303.13874) | 질의에 따라 동적으로 비디오 표현을 조정하는 효과적인 방법을 제안합니다. | 3 years ago |
| [Watch Video, Catch Keyword: Context-aware Keyword Attention](https://arxiv.org/abs/2501.02504) | 키워드 중심 attention으로 질의와 비디오를 정밀하게 정렬하는 최신 연구입니다. | a year ago |
| [VideoLights: Feature Refinement and Cross-Task Alignment](https://arxiv.org/abs/2412.01558) | 교차 작업 정렬을 통해 HD와 MR의 상호 보완성을 극대화한 Transformer 모델입니다. | a year ago |
| [MS-DETR: Joint Motion-Semantic Learning for MR and HD](https://arxiv.org/abs/2507.12062) | 움직임과 시맨틱을 결합하여 DETR 기반 프레임워크를 강화한 연구입니다. | 6 months ago |
| [MINI-Net: Multiple Instance Ranking Network](https://arxiv.org/abs/2007.09833) | 약지도 설정에서 MIL을 활용한 효율적인 하이라이트 탐지 방법입니다. | 5 years ago |
| [Unsupervised Video Highlight Detection by Audio-Visual Recurrence](https://arxiv.org/abs/2407.13933) | 비지도 방식으로 오디오-비디오 반복 패턴을 학습하여 하이라이트를 찾습니다. | 2 years ago |
| [Test-Time Adaptation for Video Highlight Detection](https://arxiv.org/abs/2508.04924) | 테스트 시점에 각 비디오에 맞춰 모델을 적응시키는 메타 학습 기반 방법입니다. | 5 months ago |

---

## 10. 응용 분야

**스포츠 중계**: 자동 하이라이트 생성으로 즉각적인 리플레이 제공  
**소셜 미디어**: 긴 비디오를 짧은 클립으로 자동 편집  
**비디오 검색**: 중요한 순간만 빠르게 찾기  
**교육**: 강의 영상에서 핵심 부분만 추출  
**감시**: 의심스러운 활동이 발생한 순간 자동 마킹  
**개인 라이프로그**: 일상 기록에서 의미 있는 순간 요약  
**영화/드라마**: 예고편 자동 생성

---

## 11. 기술 스택 요약

**특징 추출**: I3D, SlowFast, VideoMAE, VGGish  
**시간 모델링**: LSTM, TCN, Transformer, GNN  
**멀티모달**: CLIP, BERT, Cross-Modal Attention  
**학습 전략**: MIL, Self-Supervised, Meta-Learning  
**후처리**: NMS, Diversity Sampling, Top-K Selection

Video Highlight Detection은 단순히 기술적 과제를 넘어 **사용자 경험(UX)**을 크게 향상시키는 핵심 기술입니다. 최근에는 **개인화**, **실시간 처리**, **멀티모달 통합** 방향으로 빠르게 발전하고 있으며, 특히 **대규모 Vision-Language Models**의 등장으로 질의 기반 하이라이트 탐지의 성능이 비약적으로 향상되고 있습니다.