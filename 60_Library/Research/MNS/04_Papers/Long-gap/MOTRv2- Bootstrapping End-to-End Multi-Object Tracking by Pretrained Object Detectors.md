---
alias: ["MOTRv2"]
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
status: 🟩 Done
rating: 0
date: 2026-02-03
title: "MOTRv2: Bootstrapping End-to-End Multi-Object Tracking by Pretrained Object Detectors"
authors: ["Yuang Zhang", "Tiancai Wang", "Xiangyu Zhang"]
year: 2022
venue: "arXiv"
paper_url: https://arxiv.org/abs/2211.09791
topics: ["End-to-End Multi-Object Tracking", "Object Detection", "Transformer"]
---

## **📄 MOTRv2: Bootstrapping End-to-End Multi-Object Tracking by Pretrained Object Detectors 개요**

- **발표 논문**: "MOTRv2: Bootstrapping End-to-End Multi-Object Tracking by Pretrained Object Detectors" by Yuang Zhang, Tiancai Wang, Xiangyu Zhang (arXiv, 2022)[1][2][3]
- **핵심 아이디어**: 기존 End-to-End Multi-Object Tracking (MOT) 방법론인 [[MOTR]] 및 [[TrackFormer]]의 낮은 탐지(detection) 성능 문제를 해결하기 위해, 사전 학습된 [[객체 탐지기 (Object Detector)]]를 활용하여 End-to-End MOT를 부트스트랩하는 간단하면서도 효과적인 파이프라인인 MOTRv2를 제안한다.[4][1][2][3] 특히, 앵커(anchor) 형태의 쿼리(queries)를 채택하고 외부 객체 탐지기(예: [[YOLOX]])를 사용하여 제안(proposals)을 앵커로 생성함으로써, [[MOTR]]에 탐지 사전 정보(detection prior)를 제공한다.[4][1][2][5][3] 이는 [[MOTR]]에서 탐지(detection)와 연관(association) 작업 간의 충돌을 크게 완화한다.[4][1][2][5][3]
- **주요 성과**:
    - DanceTrack 벤치마크에서 73.4% HOTA (Higher Order Tracking Accuracy)로 1위를 달성했다.[4][1][2][3]
    - BDD100K 데이터셋에서 최첨단(state-of-the-art) 성능을 기록했다.[1][2][3]
    - End-to-End 특성을 유지하며 대규모 벤치마크에서 잘 확장된다.[4][1][2][3]

--- 

## **🏗 아키텍처 개요**

MOTRv2는 기존 [[MOTR]] 아키텍처를 기반으로 하며, 사전 학습된 객체 탐지기(예: [[YOLOX]])에서 생성된 제안(proposals)을 활용하여 쿼리(queries)를 생성한다.[5] 이 제안 쿼리(proposal queries)는 [[MOTR]]의 탐지 쿼리(detect queries)를 대체하여 새로 나타나는 객체를 탐지한다.[5] 이전 프레임에서 전달된 트랙 쿼리(track queries)는 추적되는 객체의 바운딩 박스(bounding boxes)를 예측하는 데 사용된다.[5] 제안 쿼리와 트랙 쿼리의 연결(concatenation) 및 이미지 특징(image features)이 [[MOTR]]에 입력되어 프레임별 예측을 생성한다.[5]

### **0. 기호/차원**
- $I_t$: 시각 $t$에서의 입력 이미지 (Input Image at time $t$)
- $Q_{prop}$: 제안 쿼리 (Proposal Queries)
- $Q_{track}$: 트랙 쿼리 (Track Queries)
- $B_t$: 시각 $t$에서의 예측된 바운딩 박스 (Predicted Bounding Boxes at time $t$)
- $HOTA$: Higher Order Tracking Accuracy (추적 성능 지표)

### **1. 인코더 (Encoder)**
- **구성**: [[Transformer]] 인코더는 입력 이미지 특징을 처리하여 시각적 특징을 추출한다. (세부 구성은 논문 본문 확인 필요)
- 각 층:
    1. **[[Self-Attention]]**
    2. **[[Feed-Forward Network]]**
- **특이 사항**: [[Residual Connection]], [[Layer Normalization]] 등 포함.

### **2. 디코더 (Decoder)**
- **구성**: [[Transformer]] 디코더는 제안 쿼리 및 트랙 쿼리와 인코더 특징을 사용하여 객체 바운딩 박스와 ID를 예측한다.[5]
- 각 층:
    1. **[[Self-Attention]]** (쿼리 간)
    2. **[[Cross-Attention]]** (쿼리와 이미지 특징 간)
    3. **[[Feed-Forward Network]]**

### **3. 주요 수식 요약**
- **쿼리 전파 (Query Propagation)**:
  - $Q_{track}^{t} = f(Q_{track}^{t-1}, B_{t-1})$ (이전 프레임의 트랙 쿼리와 바운딩 박스를 기반으로 업데이트)
- **탐지 사전 정보 활용**:
  - $Q_{prop} = \text{Detector}(I_t)$ (사전 학습된 탐지기에서 제안 생성)

--- 

## **🎯 주요 구성 요소**

### **1. [[사전 학습된 객체 탐지기 (Pretrained Object Detector)]]**
- 입력/출력 및 작동 원리 설명: [[YOLOX]]와 같은 외부 객체 탐지기를 사용하여 이미지에서 객체 제안(object proposals)을 생성한다. 이 제안들은 [[MOTR]]의 탐지 쿼리를 대체하는 앵커 역할을 하여, 모델이 새로운 객체를 더 정확하게 탐지할 수 있도록 돕는다.[5]
- $$Q_{prop} = \text{Detector}(I_t)$$

### **2. [[앵커 형태의 쿼리 (Anchor Formulation of Queries)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 외부 탐지기에서 생성된 제안을 앵커로 사용하여 쿼리를 초기화한다. 이는 [[Transformer]] 디코더가 이 앵커에 대한 상대적인 오프셋(relative offsets)을 예측하도록 하여 탐지 최적화를 단순화한다.[5]
- 설정 값 (논문 기준): (논문 본문 확인 필요)

### **3. [[쿼리 전파 (Query Propagation)]]**
- 이전 프레임의 바운딩 박스 정보를 사용하여 트랙 쿼리를 업데이트한다. 이는 연관(association) 성능을 크게 향상시킨다.[1][2][5][3]

--- 

## **⚖️ MOTRv2 vs 기존 모델**

| **비교 항목** | **MOTRv2** | **MOTR** | **TrackFormer** |
| :--- | :--- | :--- | :--- |
| **탐지 성능** | 사전 학습된 탐지기 활용으로 우수[4][1][2][5][3] | 상대적으로 낮음[4][1][2][3] | 상대적으로 낮음[4][1][2][3] |
| **탐지-연관 충돌** | 탐지 작업 분리로 완화[4][1][2][5][3] | 존재[4][1][2][3] | 존재[4][1][2][3] |
| **End-to-End** | 유지[4][1][2][3] | End-to-End[4][1][2][3] | End-to-End[4][1][2][3] |
| **복잡도** | $O(\dots)$ (논문 본문 확인 필요) | $O(\dots)$ (논문 본문 확인 필요) | $O(\dots)$ (논문 본문 확인 필요) |

- MOTRv2는 사전 학습된 객체 탐지기를 통합하여 [[MOTR]] 및 [[TrackFormer]]와 같은 기존 End-to-End MOT 방법론의 주요 약점인 낮은 탐지 성능을 효과적으로 개선한다.[4][1][2][5][3] 이를 통해 탐지 및 연관 작업 간의 내재된 충돌을 완화하고, End-to-End 특성을 유지하면서도 추적 성능을 크게 향상시킨다.[4][1][2][5][3]

--- 

## **🧠 추론/디코딩/생성 과정**
- **방식**: 프레임별로 객체 탐지 및 추적을 수행하는 방식으로 작동한다.
- **특징**: 이전 프레임의 트랙 쿼리를 다음 프레임으로 전파하고, 새로운 객체는 사전 학습된 탐지기의 제안을 통해 탐지한다.[5]

--- 

## **⚙️ 학습 설정**

- **데이터셋**:
    - DanceTrack (데이터 크기, 특징은 논문 본문 확인 필요)[4][1][2][3]
    - BDD100K (데이터 크기, 특징은 논문 본문 확인 필요)[1][2][3]
- **하드웨어**: (논문 본문 확인 필요)
- **학습 시간**: (논문 본문 확인 필요)
- **옵티마이저**: (논문 본문 확인 필요)
- **규제(Regularization)**:
    - (논문 본문 확인 필요)

--- 

## **⚠️ 한계**
- 사전 학습된 탐지기를 사용함으로써 End-to-End 추적의 자율적인(self-contained) 특성을 일부 훼손할 수 있다.[6]

--- 

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**HOTA (DanceTrack)**|**성능 (BDD100K)**|
|---|---|---|
| MOTR | (논문 본문 확인 필요) | (논문 본문 확인 필요) |
| TrackFormer | (논문 본문 확인 필요) | (논문 본문 본문 확인 필요) |
| **MOTRv2** | **73.4% (1위)**[4][1][2][3] | **SOTA**[1][2][3] |

--- 

## **🔮 향후 연구 방향**
- 이 간단하고 효과적인 파이프라인이 End-to-End MOT 커뮤니티에 새로운 통찰력을 제공할 수 있기를 기대한다.[1][2][3]
- (논문 본문 확인 필요)

--- 

## **🔗 관련 링크**
- [[MOTR]]
- [[TrackFormer]]
- [[YOLOX]]
- [[Multi-Object Tracking]]
- [[Object Detection]]
- [[Transformer]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2211.09791[2]
- **코드**: https://github.com/megvii-research/MOTRv2[1][2][3]

--- 

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```

```