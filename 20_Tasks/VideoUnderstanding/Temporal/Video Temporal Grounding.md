---
title: Video Temporal Grounding
aliases:
tags:
  - task
  - video
  - grounding
  - temporal
topics:
  - Video Understanding
---
**Video Temporal Grounding (VTG)** 또는 **Natural Language Video Localization (NLVL)** 은 자연어 질의(Query)가 주어졌을 때, 비디오에서 그 질의에 대응하는 정확한 **시간 구간(Temporal Segment)** 을 찾아내는 핵심 비디오 이해 작업입니다. 이는 [[Moment Retrieval]], Temporal Sentence Grounding과 거의 동일하거나 포괄하는 개념으로, 비디오 검색, 편집, 질의응답 등 다양한 응용에서 필수적입니다.

---

## 1. 핵심 개념 및 정의

### 1.1 작업 정의
주어진 비디오 $V = \{f_1, f_2, ..., f_T\}$와 자연어 질의 $Q$ (예: "남자가 공을 던지는 순간")에 대해, 질의와 가장 관련 있는 시간 구간 $[t_s, t_e]$를 예측하는 것입니다.

**입력**: 비디오 + 텍스트 질의  
**출력**: 시작 시간 $t_s$, 종료 시간 $t_e$ (또는 여러 구간)

### 1.2 핵심 특징

**[Cross-Modal Understanding (교차 모달 이해)]**  
비디오(시각)와 질의(언어)라는 서로 다른 모달리티 간의 의미적 정렬(Semantic Alignment)이 핵심입니다.

**[Temporal Reasoning (시간적 추론)]**  
"before", "after", "while" 같은 시간적 관계를 이해해야 합니다.  
예: "남자가 물을 마신 후 걷기 시작하는 순간"

**[Fine-grained Localization (세밀한 위치 추정)]**  
단순히 관련 있는 부분을 찾는 것이 아니라, 정확한 시작과 끝 지점을 프레임 단위로 예측해야 합니다.

**[Ambiguity (모호성)]**  
같은 질의라도 비디오에 여러 개의 대응 구간이 있을 수 있습니다.  
예: "사람이 웃는 장면" → 비디오 내 여러 곳에서 웃음

---

## 2. 작업 변형 (Task Variants)

### 2.1 Single-Moment Retrieval
가장 관련성 높은 **하나의 구간**만 찾습니다.

### 2.2 Multi-Moment Retrieval
질의에 대응하는 **여러 개의 구간**을 모두 찾아 순위를 매깁니다.

### 2.3 Compositional Temporal Grounding
복잡한 질의를 구성 요소로 분해하여 처리합니다.  
예: "남자가 문을 열고 안으로 들어간 후 앉는 순간" → 3개의 하위 행동으로 분해

### 2.4 Weakly-Supervised Grounding
비디오-질의 쌍만 주어지고 정확한 시간 주석(Temporal Annotation)은 없는 상황에서 학습합니다.

### 2.5 Zero-Shot Temporal Grounding
학습 시 보지 못한 새로운 도메인이나 질의 유형에 대해 일반화합니다.

---

## 3. 아키텍처 및 핵심 모듈

### 3.1 전체 파이프라인
```
비디오 인코딩 + 질의 인코딩 → 교차 모달 융합 → 시간적 모델링 → 경계 예측 → 후처리
```

### 3.2 특징 추출 (Feature Extraction)

**[비디오 인코더 (Video Encoder)]**
- **2D/3D CNN**: ResNet, I3D, C3D로 프레임별 또는 클립별 특징 추출
- **Transformer 기반**: VideoMAE, TimeSformer, ViViT
- **사전 학습 백본**: CLIP의 VisualEncoder를 활용하여 강력한 시각 표현 획득

**[질의 인코더 (Query Encoder)]**
- **BERT/RoBERTa**: 문장 임베딩 생성
- **CLIP TextEncoder**: 비디오 특징과 동일한 공간에 텍스트 매핑
- **GloVe/Word2Vec**: 단어 임베딩 (초기 방법)

### 3.3 교차 모달 융합 (Cross-Modal Fusion)

**[Early Fusion]**
비디오와 텍스트 특징을 초기 단계에서 결합:
```
Concat([video_features, query_features])
```

**[Late Fusion]**
각각 독립적으로 처리 후 최종 단계에서 결합:
```
score = MLP([video_rep, query_rep])
```

**[Cross-Modal Attention]**
가장 효과적인 방법으로, 비디오와 질의 간 상호작용을 학습:
```
Video-to-Query Attention:
v' = Attention(Q=video, K=query, V=query)

Query-to-Video Attention:
q' = Attention(Q=query, K=video, V=video)
```

**[Co-Attention]**
양방향 attention을 동시에 수행:
```
[v', q'] = CoAttention(video, query)
```

### 3.4 시간적 모델링 (Temporal Modeling)

**[Temporal Convolutional Networks (TCN)]**
1D Convolution으로 시간적 패턴 학습:
```
temporal_features = Conv1D(video_features)
```

**[LSTM/GRU]**
순차적 정보 처리:
```
h_t = LSTM(video_t, h_{t-1})
```

**[Transformer Encoder]**
Self-attention으로 장거리 시간 의존성 학습:
```
temporal_features = TransformerEncoder(video_features)
```

**[Temporal Feature Pyramid (TFP)]**
다중 스케일 시간 특징 추출:
```
pyramid = [Conv1D_k1, Conv1D_k3, Conv1D_k5](video_features)
```

### 3.5 경계 예측 (Boundary Prediction)

**[Anchor-based Methods]**
미리 정의된 앵커 박스(다양한 길이)를 사용:
```
for each anchor:
    offset_start = predict_start_offset(features)
    offset_end = predict_end_offset(features)
    confidence = predict_confidence(features)
```

**[Anchor-free Methods]**
각 시간 위치에서 직접 경계까지 거리 예측:
```
for each time step t:
    distance_to_start = predict(features_t)
    distance_to_end = predict(features_t)
```

**[DETR-based Methods]**
Detection Transformer 방식:
```
learned_queries = [q1, q2, ..., qN]
moments = Transformer(video_features, learned_queries)
```
학습 가능한 쿼리를 통해 모멘트를 직접 예측하고, Bipartite Matching으로 정답과 매칭합니다.

**[Regression-based]**
시작/끝 시간을 직접 회귀:
```
[t_start, t_end] = MLP(fused_features)
```

### 3.6 고급 모듈

**[Temporal Attention Pooling]**
질의 관련 시간 지점에 높은 가중치 부여:
```
weights = softmax(Attention(query, video))
pooled = Σ weights_i * video_i
```

**[Boundary-Aware Features]**
경계 주변 특징을 강조:
```
boundary_features = Extract_around_boundary(video, [t_s, t_e])
```

**[Contextual Modeling]**
목표 구간 전후 맥락 활용:
```
context = Concat([before_segment, target_segment, after_segment])
```

**[Multi-Scale Temporal Convolution]**
```
features = Concat([Conv1D_1, Conv1D_3, Conv1D_5](video))
```

---

## 4. 학습 전략 및 손실 함수

### 4.1 지도 학습 (Fully-Supervised)

**[Regression Loss]**
시작/끝 시간의 회귀 손실:
```
L_reg = SmoothL1(pred_start - gt_start) + SmoothL1(pred_end - gt_end)
```

**[IoU Loss]**
예측 구간과 정답 구간의 IoU 직접 최적화:
```
L_iou = 1 - IoU([pred_start, pred_end], [gt_start, gt_end])
```

**[Classification Loss (Ranking)]**
정답 구간이 다른 구간보다 높은 점수를 받도록:
```
L_rank = max(0, margin + score_neg - score_pos)
```

**[Contrastive Loss]**
관련 구간은 가깝게, 무관한 구간은 멀게:
```
L_contrastive = -log(exp(sim(v, q+)) / Σ exp(sim(v, q)))
```

### 4.2 약지도 학습 (Weakly-Supervised)

비디오-질의 쌍만 주어지고 시간 주석은 없는 경우:

**[Multiple Instance Learning (MIL)]**
```
video_score = max(segment_scores) or mean(top_k_scores)
L = CrossEntropy(video_score, label)
```

**[Reconstruction-based]**
```
reconstructed_query = Decoder(selected_segments)
L = MSE(reconstructed_query, original_query)
```

### 4.3 Zero-Shot Learning

**[Vision-Language Pre-training]**
CLIP 등 대규모 VLM의 제로샷 능력 활용:
```
similarity = CLIP_visual(video_segment) · CLIP_text(query)
```

**[Prompt Engineering]**
질의를 템플릿화하여 VLM에 입력:
```
"A video showing [query] happening at time [t_s] to [t_e]"
```

---

## 5. 평가 메트릭

### 5.1 Recall@K, IoU=θ (R@K, IoU=θ)
상위 K개 예측 중 IoU ≥ θ인 것이 있는 비율:
```
R@1, IoU=0.5: 최상위 예측이 IoU 0.5 이상일 확률
R@5, IoU=0.7: 상위 5개 예측 중 IoU 0.7 이상인 것이 있을 확률
```

### 5.2 mean IoU (mIoU)
모든 예측의 평균 IoU:
```
mIoU = (1/N) Σ IoU(pred_i, gt_i)
```

### 5.3 mean Average Precision (mAP)
다양한 IoU 임계값에서의 평균 정밀도:
```
mAP = mean(AP@IoU=0.3, AP@IoU=0.5, AP@IoU=0.7)
```

---

## 6. 주요 데이터셋

### 6.1 ActivityNet Captions
- **비디오 수**: 20,000개 (학습/검증/테스트)
- **평균 길이**: 120초
- **질의 수**: 100,000+
- **특징**: 긴 비디오, 다양한 일상 활동

### 6.2 Charades-STA
- **비디오 수**: 6,670개
- **평균 길이**: 30초
- **질의 수**: 16,000+
- **특징**: 실내 일상 활동, 짧은 비디오

### 6.3 TACoS (TextuallyAnnotated Cooking Scenes)
- **비디오 수**: 127개
- **질의 수**: 18,000+
- **특징**: 요리 활동, 세밀한 주석

### 6.4 QVHighlights
- **비디오 수**: 10,000+
- **질의 수**: 10,000+
- **특징**: Moment Retrieval + Highlight Detection 통합

### 6.5 DiDeMo (Distinct Describable Moments)
- **비디오 수**: 10,000+
- **특징**: Flickr 비디오, 다양한 장면

---

## 7. 기술적 도전 과제

### 7.1 장시간 비디오 처리
- **문제**: 메모리 제약으로 전체 비디오 처리 어려움
- **해결책**: 
  - Coarse-to-Fine 전략 (CONE)
  - Hierarchical Processing
  - Sparse Sampling

### 7.2 시간적 추론
- **문제**: "before", "after", "during" 같은 복잡한 시간 관계 이해
- **해결책**:
  - Causal Event Modeling (TRACE)
  - Temporal Relation Networks
  - LLM을 활용한 추론

### 7.3 교차 모달 정렬
- **문제**: 비디오와 텍스트의 의미 공간이 다름
- **해결책**:
  - CLIP 같은 사전 학습 VLM 활용
  - Contrastive Learning
  - Cross-Modal Attention

### 7.4 경계 모호성
- **문제**: 행동의 시작/끝이 불명확
- **해결책**:
  - Soft Boundary Modeling
  - Gaussian Distribution
  - Boundary Refinement Module

### 7.5 주석 비용
- **문제**: 시간 주석은 매우 비쌈
- **해결책**:
  - Weakly-Supervised Learning
  - Point Supervision
  - Zero-Shot Methods

---

## 8. 최신 연구 동향 (2024-2026)

### 8.1 Large Vision-Language Models 통합
- **Video-LLMs**: GPT-4V, Gemini를 비디오에 적용
- **Post-Training**: Time-R1처럼 VLM을 VTG에 특화시켜 후학습
- **Instruction Tuning**: 대화형 질의응답으로 확장

### 8.2 생성형 접근법
- **Generative MLLMs**: 구간을 텍스트로 생성 ("starts at 10s, ends at 25s")
- **Autoregressive Decoding**: 여러 모멘트를 순차적으로 생성

### 8.3 추론 기반 그라운딩
- **Chain-of-Thought**: 단계별 추론을 통해 모멘트 찾기
- **Causal Reasoning**: 이벤트 간 인과관계 모델링

### 8.4 온라인/스트리밍 그라운딩
- **실시간 처리**: 전체 비디오 없이 실시간으로 그라운딩
- **Incremental Learning**: 새 프레임이 들어올 때마다 업데이트

### 8.5 통합 프레임워크
- **Multi-Task Learning**: Grounding, Highlight Detection, QA 동시 해결
- **Universal Models**: 다양한 VTG 변형을 하나의 모델로 처리

### 8.6 효율성 개선
- **Moment Quantization**: 연속적 시간을 이산화하여 효율성 향상
- **Sparse Attention**: 중요한 프레임에만 집중
- **Knowledge Distillation**: 경량 모델 생성

---

## 9. 핵심 연구 및 최신 논문

| Paper | Description | Published |
| :--- | :--- | :--- |
| [Time-R1: Post-Training Large VLM for Temporal Video Grounding](https://arxiv.org/abs/2503.13377) | 대규모 VLM을 VTG에 특화시켜 후학습한 SOTA 모델로, 장시간 비디오에서 탁월한 성능을 보입니다. | 10 months ago |
| [A Survey on Video Temporal Grounding with Multimodal LLM](https://arxiv.org/abs/2508.10922) | MLLM 시대의 VTG 연구 동향을 종합적으로 정리한 최신 서베이 논문입니다. | 5 months ago |
| [Universal Video Temporal Grounding with Generative MLLMs](https://arxiv.org/abs/2506.18883) | 생성형 MLLM으로 다양한 형태의 질의를 통합 처리하는 범용 모델입니다. | 7 months ago |
| [Grounded-VideoLLM: Sharpening Fine-grained Temporal Grounding](https://arxiv.org/abs/2410.03290) | Video-LLM의 세밀한 시간적 그라운딩 능력을 강화한 연구입니다. | a year ago |
| [TimeLens: Rethinking VTG with Multimodal LLMs](https://arxiv.org/abs/2512.14698) | VTG의 본질적 접근법을 재고하며 단순하지만 효과적인 기준선을 제시합니다. | a month ago |
| [TRACE: Temporal Grounding via Causal Event Modeling](https://arxiv.org/abs/2410.05643) | 이벤트 간 인과관계를 모델링하여 시간적 추론을 강화합니다. | a year ago |
| [Grounding-MD: Open-World Moment Detection](https://arxiv.org/abs/2504.14553) | 오픈 월드 환경에서 범용적으로 모멘트를 탐지하는 사전 학습 모델입니다. | 9 months ago |
| [UniVTG: Towards Unified Video-Language Temporal Grounding](https://arxiv.org/abs/2307.16715) | 다양한 VTG 작업을 통합된 프레임워크로 처리하는 영향력 있는 연구입니다. | 2 years ago |
| [CONE: COarse-to-fiNE Alignment for Long Video Grounding](https://arxiv.org/abs/2209.10918) | 계층적 정렬로 긴 비디오에서 효율적인 그라운딩을 수행합니다. | 3 years ago |
| [Moment Quantization for Video Temporal Grounding](https://arxiv.org/abs/2504.02286) | 시간을 양자화하여 관련/무관 구간을 효과적으로 구별합니다. | 10 months ago |

---

## 10. 응용 분야

**비디오 검색**: "특정 장면 찾기" 기능  
**비디오 편집**: 자동 클립 추출 및 하이라이트 생성  
**질의응답**: "이 비디오에서 언제 X가 발생하나요?"  
**교육**: 강의 영상에서 특정 개념 설명 부분 찾기  
**보안**: 감시 영상에서 특정 사건 순간 자동 탐지  
**스포츠 분석**: "골이 들어간 순간" 자동 표시  
**영화/드라마**: "특정 대사가 나오는 장면" 검색

---

## 11. 기술 스택 요약

**비디오 인코더**: I3D, SlowFast, VideoMAE, CLIP  
**텍스트 인코더**: BERT, RoBERTa, CLIP TextEncoder  
**융합**: Cross-Attention, Co-Attention, Transformer  
**시간 모델링**: TCN, LSTM, Temporal Transformer  
**경계 예측**: Anchor-based, Anchor-free, DETR  
**학습**: Contrastive, MIL, Reinforcement Learning

Video Temporal Grounding은 **비디오와 언어의 가교 역할**을 하는 핵심 기술입니다. 최근 **대규모 VLM/LLM**의 발전으로 인해 복잡한 시간적 추론과 제로샷 일반화가 가능해지면서, 실용적 응용 범위가 크게 확대되고 있습니다. 특히 **생성형 모델**을 활용한 접근법이 주목받고 있으며, 단순히 구간을 찾는 것을 넘어 "왜 이 구간이 질의와 관련되는지"를 설명할 수 있는 방향으로 진화하고 있습니다.