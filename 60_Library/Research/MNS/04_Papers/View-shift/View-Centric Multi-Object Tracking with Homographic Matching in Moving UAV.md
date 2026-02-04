---
aliases:
  - HomView-MOT
type: paper
tags:
  - DeepLearning
  - Paper
  - ViewShift
status: 🟧 Reading
rating: 0
date: 2024-02-03
title: View-Centric Multi-Object Tracking with Homographic Matching in Moving UAV
authors:
  - Deyi Ji
  - Siqi Gao
  - Lanyun Zhu
  - Qi Zhu
  - Yiru Zhao
  - Peng Xu
  - Hongtao Lu
  - Feng Zhao
  - Jieping Ye
year: 2024
venue: arXiv
paper_url: https://arxiv.org/abs/2403.10830
topics:
  - Multi-Object Tracking
  - UAV
  - Homography
  - Computer Vision
---

## **📄 View-Centric Multi-Object Tracking with Homographic Matching in Moving UAV 개요**

- **발표 논문**: View-Centric Multi-Object Tracking with Homographic Matching in Moving UAV (Deyi Ji et al., arXiv 2024)[1][2]
- **핵심 아이디어**:
    기존의 고정 카메라 [[MOT]](Multi-Object Tracking)와 달리, 불규칙한 비행 궤적을 가진 [[UAV]](Unmanned Aerial Vehicle) 환경에서의 [[MOT]]는 배경 변화와 객체의 시점 변화로 인해 복잡성이 크게 증가한다. 이 문제를 해결하기 위해, 논문은 장면의 [[Homography]](호모그래피) 속성을 활용하여 [[Homographic Matching]] 및 [[View-Centric]] 개념을 통합한 새로운 [[HomView-MOT]] 프레임워크를 제안한다.[3][1][2]
- **주요 성과**:
    - [[VisDrone]] 및 [[UAVDT]]와 같은 주요 [[UAV MOT]] 데이터셋에서 [[State-of-the-Art]](SOTA) 성능을 달성했다.[3][1]

---

## **🏗 아키텍처 개요**

[모델의 전체적인 구조 설명은 논문 본문 참조 필요]

### **0. 기호/차원**
- [주요 기호 및 차원 정의 (LaTeX 사용) - 논문 본문 참조 필요]
- [입력 데이터 차원 등 - 논문 본문 참조 필요]

### **1. [주요 파트 1 (예: Homography Estimation)]**
- **구성**: [레이어 수, 스택 구조 등 - 논문 본문 참조 필요]
- 각 층:
    1. **[[Fast Homography Estimation (FHE)]]**
- **특이 사항**: [Residual connection, Normalization 등 - 논문 본문 참조 필요]

### **2. [주요 파트 2 (예: ID Learning & Matching)]**
- **구성**: [레이어 수, 구조 설명 - 논문 본문 참조 필요]
- 각 층:
    [세부 구성 요소 나열 - 논문 본문 참조 필요]

### **3. 주요 수식 요약**
- **[컴포넌트 명]**:
  - $수식$
- **[컴포넌트 명]**:
  - $수식$

---

## **🎯 주요 구성 요소**

### **1. [[Fast Homography Estimation (FHE) Algorithm]]**
- **입력/출력 및 작동 원리**: 비디오 프레임 간의 [[Homography]] 행렬을 빠르게 계산한다.[3][1]
- $$핵심 수식$$ (논문 본문 참조 필요)

### **2. [[View-Centric ID Learning (VCIL)]]**
- **작동 원리**: 다중 시점 [[Homography]]를 활용하여 교차 시점 [[ID]] 특징을 학습한다.[3][1]
- **설정 값 (논문 기준)**: [논문 본문 참조 필요]

### **3. [[Homographic Matching Filter (HMF)]]**
- **작동 원리**: 다른 프레임의 객체 바운딩 박스를 공통 시점 평면에 매핑하여 보다 현실적인 물리적 [[IOU]] (Intersection Over Union) 연관성을 가능하게 한다.[3][1]
- $$핵심 수식$$ (논문 본문 참조 필요)

---

## **⚖️ [HomView-MOT] vs [기존 모델]**

| **비교 항목** | **[HomView-MOT]** | **[기존 MOT 방법론]** | **[기존 UAV MOT 방법론]** |
| :--- | :--- | :--- | :--- |
| **UAV 동적 환경 처리** | [[Homography]] 및 [[View-Centric]] 개념 활용 | 비효율적 (배경 변화, 시점 변화) | 제한적 |
| **IOU 연관성** | [[HMF]]를 통한 물리적 [[IOU]] | 전통적인 프레임-투-프레임 [[IOU]] | [논문 본문 참조 필요] |
| **ID 학습** | [[VCIL]]을 통한 교차 시점 [[ID]] 특징 학습 | [논문 본문 참조 필요] | [논문 본문 참조 필요] |
| **복잡도** | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ |

- [[HomView-MOT]]는 움직이는 [[UAV]] 환경에서 발생하는 복잡한 배경 변화와 객체 시점 변화 문제를 [[Homography]]를 활용하여 효과적으로 해결함으로써 기존 [[MOT]] 방법론 대비 강점을 가진다.[3][1][2]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: [Autoregressive, Flow-based 등 설명 - 논문 본문 참조 필요]
- **특징**: [Masking, Sampling 기법 등 - 논문 본문 참조 필요]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - [[VisDrone]] (데이터 크기, 특징 - 논문 본문 참조 필요)[3][1]
    - [[UAVDT]] (데이터 크기, 특징 - 논문 본문 참조 필요)[3][1]
- **하드웨어**: [GPU/TPU 사양 및 개수 - 논문 본문 참조 필요]
- **학습 시간**: [Step 수 또는 시간 - 논문 본문 참조 필요]
- **옵티마이저**: [이름 및 파라미터 ($\beta_1, \epsilon$ 등) - 논문 본문 참조 필요]
- **규제(Regularization)**:
    - [Dropout, Label Smoothing 등 - 논문 본문 참조 필요]

---

## **⚠️ 한계**
- [논문에서 언급하거나 구조적으로 가지는 한계점 1 - 논문 본문 참조 필요]
- [한계점 2 - 논문 본문 참조 필요]

---

## **📊 주요 실험 결과**

### **[메인 태스크 성능]**

|**모델**|**[지표 1]**|**[지표 2]**|
|---|---|---|
| [비교 모델 A] | 수치 | 수치 |
| [비교 모델 B] | 수치 | 수치 |
| **[HomView-MOT]** | **SOTA 수치** | **SOTA 수치** |

---

## **🔮 향후 연구 방향**
- [논문의 Future Work 섹션 요약 - 논문 본문 참조 필요]
- [확장 가능성 - 논문 본문 참조 필요]

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[UAV]]
- [[Homography]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2403.10830
- **코드**: [URL - 논문 본문 참조 필요]

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
