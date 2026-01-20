---
title: Object Tracking
aliases:
  - Video Object Tracking
tags:
  - task
  - video
  - tracking
topics:
  - Video Understanding
  - Computer Vision
---

객체 추적(Object Tracking)은 비디오 시퀀스의 **연속적인 프레임에서 특정 대상의 위치를 식별**하고 시간 흐름에 따라 **그 궤적을 유지**하는 컴퓨터 비전의 핵심 기술입니다.

이 기술은 크게 **단일 객체 추적(Single Object Tracking, SOT)** 과 **다중 객체 추적(Multi-Object Tracking, MOT)** 으로 분류됩니다. 
**단일 객체 추적**은 첫 번째 프레임에서 **지정된 하나의 대상만을 정밀하게 쫓는 방식**인 반면 **다중 객체 추적**은 화면에 나타나는 **여러 유동적인 대상들을 동시에 감지**하고 **각각에게 고유한 식별자(ID)를 부여하여 관리**합니다.

현대의 객체 추적 기술은 딥러닝의 발전과 함께 비약적인 성장을 이루었으며 특히 **검출 기반 추적(Tracking-by-Detection) 방식**이 주류를 이루고 있습니다.
이 방식은 **매 프레임마다 객체를 먼저 검출한 뒤 이전 프레임의 정보와 현재의 검출 결과 사이의 유사도를 계산**하여 **동일 인물이나 물체인지를 판단하는 데이터 연관(Data Association)** 과정을 거칩니다.

데이터 연관 과정에서는 **객체의 이동 경로를 예측하는 칼만 필터(Kalman Filter)** 와 같은 **모션 모델**과 **객체의 외형 특징을 추출하여 비교**하는 **외관 모델**이 함께 사용됩니다.

최근에는 **트랜스포머(Transformer) 구조를 도입하여 감지와 추적을 하나의 엔드투엔드(End-to-End) 네트워크로 통합**하려는 시도가 활발히 이루어지고 있습니다.
이러한 모델들은 **어텐션 메커니즘을 통해 프레임 간의 긴밀한 관계를 파악**하며 가려짐(Occlusion)이나 조명 변화와 같은 **복잡한 환경에서도 안정적인 추적 성능**을 보여줍니다.

객체 추적의 성능을 평가할 때는 추적 대상과 예측된 상자 사이의 겹침 정도를 나타내는 $IoU$ 지표가 자주 활용됩니다. $IoU$는 두 영역의 교집합을 합집합으로 나눈 값으로 정의되며 수식으로는 $IoU = \frac{|A \cap B|}{|A \cup B|}$와 같이 표현됩니다. 이 지표가 높을수록 추적기가 대상의 위치를 정확하게 포착하고 있음을 의미합니다.

---
## 1. 핵심 개념 및 정의

### 1.1 작업 정의

주어진 비디오 $V = \{f_1, f_2, ..., f_T\}$에서:

- **초기화**: 첫 프레임에서 추적할 객체를 지정 (바운딩 박스, 마스크, 언어 설명 등)
- **추적**: 이후 프레임에서 객체의 위치를 예측하고 업데이트
- **ID 유지**: 동일 객체는 모든 프레임에서 같은 ID를 가져야 함

### 1.2 핵심 도전 과제

- **Occlusion (가림)**: 객체가 다른 객체나 배경에 가려짐
- **Appearance Change (외관 변화)**: 조명, 시점, 자세 변화
- **Motion Blur (모션 블러)**: 빠른 움직임으로 인한 흐릿함
- **Similar Distractors (유사 방해 객체)**: 목표와 비슷한 다른 객체
- **Scale Variation (크기 변화)**: 객체와 카메라 간 거리 변화
- **Out-of-View (시야 이탈)**: 객체가 프레임 밖으로 나갔다 돌아옴

---

## 2. 작업 유형별 분류

### 2.1 Single Object Tracking (SOT)

**정의**: 초기 프레임에서 지정된 하나의 객체를 추적합니다.

**초기화 방식**:

- Bounding Box: 첫 프레임에서 박스로 지정
- Mask: 픽셀 단위 마스크 제공
- Language: "빨간 셔츠를 입은 사람"

**특징**:

- 단일 객체에 집중하므로 정밀한 추적 가능
- 클래스 무관(Class-agnostic): 어떤 객체든 추적 가능
- Re-detection 불필요

**대표 데이터셋**:

- LaSOT, TrackingNet, GOT-10k, VOT

### 2.2 Multiple Object Tracking (MOT)

**정의**: 비디오에서 여러 객체를 동시에 탐지하고 추적하며, 각 객체에 고유 ID를 할당합니다.

**하위 작업**:

- **Multi-Pedestrian Tracking (MPT)**: 보행자 추적에 특화
- **Multi-Vehicle Tracking**: 차량 추적
- **Generic MOT**: 다양한 객체 카테고리

**특징**:

- Data Association 문제가 핵심
- 새 객체 등장/퇴장 처리
- ID Switch 최소화가 중요

**대표 데이터셋**:

- MOT Challenge (MOT15, MOT16, MOT17, MOT20)
- DanceTrack, SportsMOT

### 2.3 Video Object Segmentation & Tracking (VOS)

**정의**: 픽셀 단위로 객체를 분할하며 추적합니다.

**유형**:

- **Semi-supervised VOS**: 첫 프레임에서 마스크 제공
- **Unsupervised VOS**: 자동으로 주요 객체 찾아 추적
- **Interactive VOS**: 사용자가 중간에 개입 가능

**대표 데이터셋**:

- DAVIS, YouTube-VOS, MOSE

### 2.4 3D Object Tracking

**정의**: 3D 공간에서 객체의 위치, 방향, 크기를 추적합니다.

**입력**:

- Point Cloud (LiDAR)
- RGB-D
- Stereo Vision

**응용**: 자율주행, 로봇공학

**대표 데이터셋**:

- KITTI, nuScenes, Waymo

### 2.5 Referring Object Tracking

**정의**: 자연어 설명으로 지정된 객체를 추적합니다.

**예시**: "왼쪽에서 두 번째 파란 차", "안경 쓴 남자"

**특징**: Vision-Language 이해 필요

---

## 3. 아키텍처 및 핵심 모듈

### 3.1 Single Object Tracking 아키텍처

#### **3.1.1 Siamese Networks**

두 입력(템플릿과 탐색 영역)의 유사도를 측정합니다.

**구조**:

```
Template Branch: φ(template)
Search Branch: φ(search_region)
Similarity Map: Correlation(φ(template), φ(search_region))
```

**대표 모델**:

- **SiamFC**: Fully Convolutional Siamese
- **SiamRPN**: Region Proposal Network 통합
- **SiamMask**: 마스크 예측 추가

**장점**:

- 빠른 속도 (실시간 가능)
- End-to-end 학습
- 강력한 일반화

#### **3.1.2 Transformer-based Trackers**

Attention 메커니즘으로 템플릿과 탐색 영역 간 관계 학습합니다.

**구조**:

```
Template Encoding: Transformer(template)
Search Encoding: Transformer(search_region)
Cross-Attention: Attend(template, search)
Prediction: Head(attended_features)
```

**대표 모델**:

- **TransT**: Pure Transformer tracking
- **OSTrack**: One-Stream Transformer
- **SeqTrack**: Sequence-to-Sequence tracking

**장점**:

- 전역적 문맥 파악
- 장거리 의존성 학습
- SOTA 성능

#### **3.1.3 Correlation Filter-based**

주파수 도메인에서 효율적인 상관 연산을 수행합니다.

**원리**:

```
Response = F^-1(F(template) ⊙ F(patch))
```

**대표 모델**:

- **KCF**: Kernelized Correlation Filters
- **ECO**: Efficient Convolution Operators
- **ATOM**: Accurate Tracking by Overlap Maximization

**장점**:

- 매우 빠른 속도
- 메모리 효율적

### 3.2 Multiple Object Tracking 아키텍처

#### **3.2.1 Tracking-by-Detection (TbD)**

가장 전통적이고 널리 사용되는 패러다임입니다.

**파이프라인**:

```
1. Detection: 각 프레임에서 객체 탐지
2. Feature Extraction: 각 탐지에서 특징 추출 (외관, 위치)
3. Data Association: 프레임 간 탐지 매칭
4. Trajectory Management: ID 할당 및 궤적 업데이트
```

**Data Association 방법**:

**[Hungarian Algorithm (헝가리안 알고리즘)]** 비용 행렬을 최적 할당으로 해결합니다:

```
Cost Matrix C[i,j] = distance(track_i, detection_j)
Assignment = Hungarian(C)
```

**[IoU Matching]**

```
IoU(box1, box2) = Area(Intersection) / Area(Union)
```

IoU가 높으면 같은 객체로 판단합니다.

**[Appearance-based Matching]**

```
similarity = cosine(feature_track, feature_detection)
```

Re-ID (Re-Identification) 특징을 사용합니다.

**[Motion-based Matching]** Kalman Filter로 다음 위치 예측:

```
Predicted_position = Kalman_predict(previous_states)
Distance = ||Predicted - Detected||
```

#### **3.2.2 대표 TbD 모델**

**[SORT (Simple Online and Realtime Tracking)]**

```
1. Kalman Filter로 위치 예측
2. IoU 기반 매칭
3. Hungarian Algorithm으로 할당
```

- 장점: 매우 빠름, 단순
- 단점: 가림에 약함

**[DeepSORT]** SORT에 외관 특징(Re-ID) 추가:

```
Cost = λ_iou * IoU_cost + λ_app * Appearance_cost
```

- 장점: ID Switch 감소
- 단점: Re-ID 모델 필요

**[ByteTrack]** 낮은 confidence 탐지도 활용:

```
High-conf detections: Primary association
Low-conf detections: Secondary association (recover occluded)
```

- SOTA급 성능

**[OC-SORT / Deep OC-SORT]**

```
Observation-Centric momentum + Re-ID
```

- 복잡한 움직임 처리
- 장기간 가림 복구

**[BoT-SORT]**

```
BoT (Bag of Tricks):
- Camera Motion Compensation
- Interpolation
- Re-ID features
```

#### **3.2.3 End-to-End Transformer-based MOT**

**[MOTR (MOT with Transformer)]** DETR을 MOT에 적용:

```
Learned Track Queries → Transformer → Object Detections + IDs
```

- 각 쿼리가 하나의 객체 추적
- Temporal Aggregation으로 프레임 간 연결

**[TransTrack]**

```
Frame-to-Frame Association via Transformer
```

- Query: 이전 프레임 객체
- Key/Value: 현재 프레임 특징

**[MeMOTR]**

```
Long-Term Memory + Transformer
```

- 과거 정보를 메모리에 저장
- 장기간 가림 후 재등장 처리

#### **3.2.4 Segmentation-driven MOT**

**[SAM2MOT]** Segment Anything 2 (SAM2)를 MOT에 활용:

```
Segmentation → Tracking
```

- 픽셀 단위 정확도
- 복잡한 형태의 객체 추적

---

## 4. 핵심 기술 모듈

### 4.1 외관 모델링 (Appearance Modeling)

**[Re-Identification (Re-ID)]** 같은 객체를 다른 프레임에서 다시 식별하는 능력:

```
Feature Extractor: ResNet, OSNet, ViT
Metric Learning: Triplet Loss, Contrastive Loss
```

**[Template Update]** 템플릿을 지속적으로 업데이트하여 외관 변화 적응:

```
template_t = α * template_{t-1} + (1-α) * current_appearance
```

### 4.2 움직임 모델링 (Motion Modeling)

**[Kalman Filter]**

```
Prediction:
  x̂_{t|t-1} = F * x_{t-1}
  P_{t|t-1} = F * P_{t-1} * F^T + Q

Update:
  K_t = P_{t|t-1} * H^T * (H * P_{t|t-1} * H^T + R)^{-1}
  x̂_t = x̂_{t|t-1} + K_t * (z_t - H * x̂_{t|t-1})
```

**[Learning-based Motion]**

- LSTM/GRU로 움직임 패턴 학습
- Transformer로 궤적 예측
- Mamba (State Space Model) 활용

### 4.3 Data Association

**[Bipartite Matching]**

```
minimize Σ C[i,j] * x[i,j]
subject to: Σ_j x[i,j] ≤ 1, Σ_i x[i,j] ≤ 1
```

**[Graph Neural Networks]**

```
Nodes: Detections
Edges: Similarity
Message Passing: Update node features
Classification: Edge is match or not
```

### 4.4 Occlusion Handling

**[Tracklet Recovery]** 가려진 객체를 잠시 메모리에 보관:

```
if no_match for tracklet in N frames:
    mark as lost
if reappears within M frames:
    recover ID
else:
    terminate
```

**[Interpolation]** 가림 구간의 궤적을 보간:

```
Linear: position = interpolate(pos_before, pos_after)
Polynomial: fitting higher-order curves
```

---

## 5. 학습 전략 및 손실 함수

### 5.1 SOT 학습

**[Classification Loss]**

```
L_cls = CrossEntropy(predicted_class, ground_truth_class)
```

**[Regression Loss]** 바운딩 박스 좌표 회귀:

```
L_reg = SmoothL1(pred_bbox - gt_bbox)
```

**[Contrastive Loss]**

```
L_contrastive = -log(exp(sim(anchor, positive)) / Σ exp(sim(anchor, samples)))
```

### 5.2 MOT 학습

**[Detection Loss]**

```
L_det = L_cls + λ * L_bbox
```

**[Re-ID Loss]**

```
L_reid = TripletLoss(anchor, positive, negative)
```

**[Association Loss]**

```
L_assoc = CrossEntropy(predicted_match, gt_match)
```

**[End-to-End Loss (MOTR)]**

```
L_total = L_det + L_track + L_association
```

---

## 6. 평가 메트릭

### 6.1 SOT 메트릭

**[Success Rate]** IoU > threshold인 프레임 비율:

```
Success = (# frames with IoU > 0.5) / (total frames)
```

**[Precision]** 중심점 오차 < threshold인 프레임 비율:

```
Precision = (# frames with center error < 20px) / (total frames)
```

**[AUC (Area Under Curve)]** 다양한 임계값에서 Success Rate 적분

### 6.2 MOT 메트릭

**[MOTA (Multiple Object Tracking Accuracy)]**

```
MOTA = 1 - (FN + FP + ID_Switch) / GT
```

- FN: False Negatives (놓친 객체)
- FP: False Positives (잘못된 탐지)
- ID_Switch: ID 전환 횟수

**[MOTP (Multiple Object Tracking Precision)]** 매칭된 객체들의 평균 IoU

**[IDF1 (ID F1 Score)]**

```
IDF1 = 2 * IDTP / (2 * IDTP + IDFP + IDFN)
```

ID 일관성 측정

**[HOTA (Higher Order Tracking Accuracy)]**

```
HOTA = √(Detection_Accuracy × Association_Accuracy)
```

탐지와 연결을 균형있게 평가

---

## 7. 주요 데이터셋

### 7.1 SOT 데이터셋

- **LaSOT**: 1,400 비디오, 평균 2,500 프레임, 70개 카테고리
- **TrackingNet**: 30,000+ 비디오
- **GOT-10k**: Generic Object Tracking, 10,000+ 비디오
- **VOT (Visual Object Tracking)**: 매년 챌린지 개최

### 7.2 MOT 데이터셋

- **MOT Challenge**: MOT15~MOT20, 보행자 중심
- **DanceTrack**: 복잡한 움직임, 유사한 외관
- **SportsMOT**: 스포츠 장면
- **BDD100K**: 자율주행 멀티 카테고리

### 7.3 VOS 데이터셋

- **DAVIS**: Dense Annotations in Video Segmentation
- **YouTube-VOS**: 4,000+ 비디오
- **MOSE**: Complex Scenarios

---

## 8. 최신 연구 동향 (2024-2026)

### 8.1 Foundation Models for Tracking

- **SAM2 통합**: Segment Anything 2를 추적에 활용
- **CLIP 기반**: Zero-shot 및 언어 기반 추적
- **Video LLMs**: 추론 능력으로 복잡한 추적 시나리오 처리

### 8.2 Language-guided Tracking

- **Referring Tracking**: "빨간 모자 쓴 사람" 추적
- **ReferGPT**: GPT를 활용한 zero-shot referring MOT
- **ReasoningTrack**: Chain-of-Thought로 추적 결정

### 8.3 End-to-End Learning

- Transformer 기반 통합 프레임워크
- Detection + Tracking joint optimization
- Online learning and adaptation

### 8.4 3D and Multi-Modal Tracking

- **3D MOT**: LiDAR + Camera 융합
- **MCTrack**: Multi-Camera Tracking
- **Event Camera**: 고속 움직임 추적

### 8.5 Efficiency and Real-time

- Knowledge Distillation
- Lightweight Architectures
- Hardware Acceleration

핵심 연구 및 동향
---
객체 추적 분야에서 획기적인 변화를 이끌어낸 논문들은 주로 프레임 간 **데이터 연관(Data Association)의 효율성을 극대화**하거나, 딥러닝 아키텍처를 **추적 작업에 최적화하여 설계**한 것들입니다.

초기에는 **칼만 필터와 헝가리안 알고리즘을 결합한 단순한 구조**가 주를 이뤘으나, 이후 **객체의 외형 특징을 학습하는 Re-ID** 기술, 그리고 **최근에는 어텐션 메커니즘을 활용한 트랜스포머 기반의 엔드투엔드 모델**로 패러다임이 전환되었습니다.
특히 ByteTrack은 검출 점수가 낮은 박스까지 추적에 활용함으로써 기존 방식의 한계를 극복하며 큰 반향을 일으켰으며, Siamese 계열의 논문들은 단일 객체 추적에서 템플릿 매칭의 새로운 기준을 제시했습니다.

| Paper | Description | Publication Time |
| :--- | :--- | :--- |
| [ByteTrack: Multi-Object Tracking by Associating Every Detection Box](https://arxiv.org/abs/2110.06864) | 검출 점수가 낮은 박스도 배경으로 버리지 않고 추적에 활용하여 저조도나 가려짐 상황에서 성능을 극대화한 핵심 논문입니다. | 4 years ago |
| [Simple Online and Realtime Tracking](https://arxiv.org/abs/1602.00763) | SORT로 알려진 이 논문은 실시간 MOT의 표준이 된 칼만 필터 기반 추적-바이-검출 프레임워크를 정립했습니다. | 9 years ago |
| [Tracking Objects as Points](https://arxiv.org/abs/2004.11177) | 객체를 박스가 아닌 중심점으로 파악해 추적하는 CenterTrack 방식을 제안하여 시스템 복잡도를 획기적으로 낮췄습니다. | 5 years ago |
| [Deep OC-SORT: Multi-Pedestrian Tracking by Adaptive Re-Identification](https://arxiv.org/abs/2302.11813) | 모션 기반 추적의 한계를 외형 재식별 기술로 보완하여 비선형적인 움직임도 효과적으로 추적할 수 있게 했습니다. | 3 years ago |
| [MOTR: End-to-End Multiple-Object Tracking with Transformer](https://arxiv.org/abs/2105.03247) | 수동적인 연관 과정 없이 트랜스포머의 질의(Query) 구조를 통해 객체를 추적하는 엔드투엔드 모델의 시대를 열었습니다. | 4 years ago |
| [StrongSORT: Make DeepSORT Great Again](https://arxiv.org/abs/2202.13514) | 고전적인 DeepSORT 알고리즘을 최신 검출기 및 특징 추출 기술로 업그레이드하여 강력한 성능 기준점을 제시했습니다. | 3 years ago |
| [A Twofold Siamese Network for Real-Time Object Tracking](https://arxiv.org/abs/1802.08817) | 의미적 특징과 외형 특징을 동시에 활용하는 Siamese 구조를 통해 실시간 단일 객체 추적의 정확도를 크게 높였습니다. | 8 years ago |

최근 객체 추적 연구는 메타(Meta)의 SAM 2(Segment Anything Model 2)를 활용한 **비디오 세그멘테이션 기반 추적**과 **트랜스포머의 연산 효율성을 극대화한 맘바(Mamba) 아키텍처의 도입**, 그리고 자율 주행을 위한 **3D 공간 추적 기술의 고도화**라는 세 가지 큰 흐름으로 요약됩니다.

특히 SAM 2의 등장은 단순히 박스 형태의 위치를 찾는 것을 넘어 **객체의 정교한 마스크(Mask)를 프레임 간에 유지**하는 새로운 패러다임을 제시했습니다. 또한 맘바 구조는 트랜스포머의 성능을 유지하면서도 **긴 비디오 시퀀스를 선형적인 복잡도로 처리**할 수 있게 하여 실시간 성능을 비약적으로 향상시켰습니다.

| Paper                                                                                                                 | Description                                                                 | Publication Time |
| :-------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------- | :--------------- |
| [SAM2MOT: A Novel Paradigm of Multi-Object Tracking by Segmentation](https://arxiv.org/abs/2504.04519)                | SAM 2의 강력한 세그멘테이션 능력을 다중 객체 추적에 통합하여 기존의 검출 기반 방식에서 벗어난 새로운 표준을 제시했습니다.     | 9 months ago     |
| [S3MOT: Monocular 3D Object Tracking with Selective State Space Model](https://arxiv.org/abs/2504.18068)              | 단안 카메라 환경에서 맘바(Mamba)의 선택적 상태 공간 모델을 활용해 3D 객체 추적의 효율성을 극대화했습니다.            | 9 months ago     |
| [SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking](https://arxiv.org/abs/2411.11922)            | SAM 2를 모션 인식 메모리 구조와 결합하여 학습하지 않은 객체에 대해서도 제로샷(Zero-shot) 추적이 가능하도록 개선했습니다. | a year ago       |
| [MCTrack: A Unified 3D Multi-Object Tracking Framework for Autonomous Driving](https://arxiv.org/abs/2409.16149)      | KITTI, nuScenes 등 주요 자율주행 벤치마크에서 SOTA를 달성한 통합 3D 추적 프레임워크입니다.               | a year ago       |
| [MambaTrack: A Simple Baseline for Multiple Object Tracking with State Space Model](https://arxiv.org/abs/2408.09178) | 기존 칼만 필터 대신 맘바 구조를 모션 예측기로 사용하여 복잡한 움직임도 선형 시간 안에 추적할 수 있음을 입증했습니다.         | a year ago       |
| [MCTR: Multi Camera Tracking Transformer](https://arxiv.org/abs/2408.13243)                                           | 여러 대의 카메라가 겹치는 환경에서 트랜스포머를 이용해 객체의 신원을 일관되게 유지하는 기술을 제안했습니다.                | a year ago       |
| [Leveraging Vision-Language Models for Open-Vocabulary Tracking](https://arxiv.org/abs/2503.16538)                    | 시각-언어 모델(VLM)을 결합하여 텍스트 설명만으로 새로운 객체를 인식하고 추적하는 오픈 보캐브러리 성능을 확보했습니다.        | 10 months ago    |
| [TrackOcc: Camera-based 4D Panoptic Occupancy Tracking](https://arxiv.org/abs/2503.08471)                             | 카메라 입력만으로 3D 공간의 점유 상태와 객체의 궤적을 4D 관점에서 동시에 추적하는 최신 기술입니다.                  | 10 months ago    |

객체 추적(Object Tracking) 분야는 최근 거대 멀티모달 모델(LMM)과 시각-언어 모델(VLM)의 발전과 궤를 같이하며, **단순히 위치를 찾는 단계를 넘어 객체의 의미를 이해하고 자연어 지시문을 따르는 방향으로 진화**하고 있습니다.
2026년 1월 현재 기준으로도 최신 논문들이 꾸준히 발표되고 있으며, 특히 **멀티모달 데이터를 통합하여 추적의 한계를 극복**하려는 시도가 두드러집니다. 아래는 2025년 말에서 2026년 초 사이에 발표된 가장 근접한 시기의 핵심 연구들입니다.

| Paper | Description | Publication Time |
| :--- | :--- | :--- |
| [AR-MOT: Autoregressive Multi-object Tracking](https://arxiv.org/abs/2601.01925) | 자기회귀(Autoregressive) 방식을 도입하여 더 일반적이고 멀티모달 시나리오에 대응 가능한 유연한 추적 아키텍처를 제안했습니다. | 14 days ago |
| [LLMTrack: Semantic Multi-Object Tracking with Multi-modal Large Language Models](https://arxiv.org/abs/2601.06550) | 대규모 언어 모델(LLM)을 활용해 객체의 단순 위치뿐만 아니라 시맨틱한 의미까지 파악하며 추적하는 새로운 시도입니다. | 9 days ago |
| [Detector-Augmented SAMURAI for Long-Duration Drone Tracking](https://arxiv.org/abs/2601.04798) | SAMURAI 모델에 검출기를 보완하여 드론과 같은 장기 추적이 필요한 시나리오에서의 안정성을 강화했습니다. | 11 days ago |
| [AerialMind: Towards Referring Multi-Object Tracking in UAV Scenarios](https://arxiv.org/abs/2511.21053) | 드론 영상에서 자연어 명령(Referring)을 통해 특정 다중 객체를 정밀하게 찾아내고 추적하는 모델을 제안했습니다. | 2 months ago |
| [Tracking and Segmenting Anything in Any Modality](https://arxiv.org/abs/2511.19475) | 다양한 모달리티 환경에서도 객체를 추적하고 세그멘테이션할 수 있는 범용적인 프레임워크를 탐구한 연구입니다. | 2 months ago |
| [MANTA: Physics-Informed Generalized Underwater Object Tracking](https://arxiv.org/abs/2511.23405) | 물리 법칙을 반영하여 수중의 빛 산란이나 왜곡 환경에서도 객체를 안정적으로 추적할 수 있는 기법을 소개했습니다. | 2 months ago |
| [PlugTrack: Multi-Perceptive Motion Analysis for Adaptive Fusion in Multi-Object Tracking](https://arxiv.org/abs/2511.13105) | 칼만 필터의 한계를 극복하기 위해 다각적 모션 분석을 통한 적응형 융합 추적 방식을 제안했습니다. | 2 months ago |
| [Tracking spatial temporal details in ultrasound long video](https://arxiv.org/abs/2512.15066) | 의료용 초음파 영상과 같은 특수 도메인에서 장기적인 시공간 정보를 유지하며 추적하는 기술입니다. | a month ago |

---

