---
aliases: ["QQ-STR", "Invisible Object Tracking"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "Where is the Invisible: Spatial-Temporal Reasoning with Object Permanence"
authors: ["Zijian Wang", "Fangwei Zhong", "Hai Ci", "Wei Wang", "Yizhou Wang"]
year: 2023
venue: "ICLR 2024 Conference (Withdrawn Submission)"
paper_url: "https://openreview.net/forum?id=9071"
topics: ["Object Tracking", "Spatial-Temporal Reasoning", "Object Permanence", "Computer Vision"]
---

## **📄 Where is the Invisible: Spatial-Temporal Reasoning with Object Permanence 개요**

- **발표 논문**: "Where is the Invisible: Spatial-Temporal Reasoning with Object Permanence" by Zijian Wang, Fangwei Zhong, Hai Ci, Wei Wang, Yizhou Wang (ICLR 2024 Conference Withdrawn Submission)[1]
- **핵심 아이디어**:
    기존의 2D 바운딩 박스 기반 객체 추적(object tracking) 방법론의 한계, 특히 [[가려짐 (occlusion)]] 및 [[포함 (containment)]] 상황에서 객체가 보이지 않게 되는 문제를 해결하기 위해 [[객체 영속성 (object permanence)]] 개념에서 영감을 받은 [[정성적-정량적 시공간 추론 (Qualitative-Quantitative Spatial-Temporal Reasoning, QQ-STR)]] 프레임워크를 제안한다.[1] 이 프레임워크는 보이지 않는 객체의 궤적을 추적하는 데 중점을 둔다.[1]
- **주요 성과**:
    - 제안된 QQ-STR 방법론은 합성(synthetic) 및 실제(real) 데이터셋 모두에서 기존 [[객체 추적 (object tracking)]] 베이스라인 모델들보다 우수한 성능을 달성했다 (mIoU 지표 기준).[1]
    - 실제 환경의 RGB-D 데이터를 포함하는 새로운 [[iVOT (invisible Object Tracking)]] 데이터셋을 구축하고 공개했다.[1]

---

## **🏗 아키텍처 개요**

QQ-STR 프레임워크는 크게 세 가지 모듈로 구성되어 있다.[1]

### **0. 기호/차원**
- 논문 원문 참조 필요

### **1. 시각 인식 모듈 (Visual Perception Module)**
- **구성**: 프레임별 [[객체 탐지 (object detection)]] 및 [[인체 자세 추정 (human pose estimation)]]을 위해 상용(off-the-shelf) 방법을 사용한다.[1]
- **특이 사항**: 이 모듈은 QQ-STR 프레임워크의 입력 데이터를 생성하는 역할을 한다.

### **2. 정성적 공간 관계 추론기 (Qualitative Spatial Relation Reasoner, SRR)**
- **구성**: 현재 및 과거 관측치를 기반으로 각 객체와 대상 객체 간의 정성적 관계를 추론한다.[1]
- **특이 사항**: 여러 가능한 객체 관계를 그래프(graph) 형태로 유지하며 잠재적 후보들을 고려한다.[1]

### **3. 정량적 관계 조건부 시공간 관계 분석기 (Quantitative Relation-conditioned Spatial-Temporal Relation Analyst, SRA)**
- **구성**: 시간에 대한 고려를 도입하여 객체의 궤적을 분석하고 오류를 수정한다.[1]
- **특이 사항**: 완전히 보이지 않는 객체를 추적하는 데 특히 유용하다.[1]

### **3. 주요 수식 요약**
- 논문 원문 참조 필요

---

## **🎯 주요 구성 요소**

### **1. [[정성적 공간 관계 추론기 (SRR)]]**
- 입력/출력 및 작동 원리 설명: 각 프레임에서 객체 간의 공간적 관계(예: 'A가 B 안에 있다', 'A가 B 뒤에 있다')를 질적으로 파악한다.[1]
- $$핵심 수식$$ (논문 원문 참조 필요)

### **2. [[정량적 관계 조건부 시공간 관계 분석기 (SRA)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: SRR에서 추론된 정성적 관계를 조건으로 사용하여 객체의 정량적인 위치를 예측하고, 시간적 정보를 통합하여 궤적을 보정한다.[1]
- 설정 값 (논문 기준): 논문 원문 참조 필요

### **3. 기타 구성 요소**
- 논문 원문 참조 필요

---

## **⚖️ QQ-STR vs 기존 모델**

| **비교 항목** | **QQ-STR (제안 모델)** | **OPNet** | **PA** | **RAM** | **AAPA** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **핵심 접근 방식** | 정성적-정량적 시공간 추론, 객체 영속성 | 객체 영속성 기반 | 논문 원문 참조 | 논문 원문 참조 | 논문 원문 참조 |
| **주요 목표** | 가려진/포함된 객체 추적 | 가려진 객체 추적 | 논문 원문 참조 | 논문 원문 참조 | 논문 원문 참조 |
| **성능** | 베이스라인 대비 우수 (mIoU) | 베이스라인 | 베이스라인 | 베이스라인 | 베이스라인 |
| **복잡도** | $O(\dots)$ (논문 원문 참조) | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ |

- QQ-STR은 [[객체 영속성 (object permanence)]] 개념을 활용하여 보이지 않는 객체의 추적 문제를 해결하며, 특히 정성적 관계 추론과 정량적 위치 분석을 결합하여 기존 방법론보다 향상된 성능을 보인다.[1]

---

## **🧠 추론/디코딩/생성 과정**
- **방식**: 논문 원문 참조 필요
- **특징**: 논문 원문 참조 필요

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - [[LA-CATER]][1]
    - Liang et al. (2018) 데이터셋[1]
    - **[[iVOT (invisible Object Tracking)]]**: 저자들이 직접 수집한 RGB-D 데이터셋. 49개의 비디오, 각 0.5~1.5분 길이, 12개 장면, 31,000 프레임, 171개의 주석 처리된 궤적을 포함한다.[1] Intel Realsense D435i를 사용하여 RGB (1920x1080), Depth (1280x720) 해상도, 30fps로 수집되었다.[1]
- **하드웨어**: 논문 원문 참조 필요
- **학습 시간**: 논문 원문 참조 필요
- **옵티마이저**: 논문 원문 참조 필요
- **규제(Regularization)**:
    - 논문 원문 참조 필요

---

## **⚠️ 한계**
- 현재 프레임워크는 격렬한 흔들림(violent shaking)이 있는 비디오에 대한 확장이 향후 연구 과제로 언급되었다.[1]

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**mIoU (예시)**|
|---|---|
| OPNet | 수치 (논문 원문 참조) |
| PA | 수치 (논문 원문 참조) |
| RAM | 수치 (논문 원문 참조) |
| AAPA | 수치 (논문 원문 참조) |
| **QQ-STR** | **수치 (논문 원문 참조)** |

- QQ-STR은 기존 베이스라인 모델들 대비 mIoU 지표에서 우수한 성능을 보였다.[1]

---

## **🔮 향후 연구 방향**
- 격렬한 흔들림이 있는 비디오에서도 프레임워크를 확장하여 적용하는 것이 향후 연구 과제이다.[1]
- 새로운 정성적-정량적 추론 프레임워크는 객체 영속성 문제를 해결하는 새로운 시각을 제공할 수 있다.[1]

---

## **🔗 관련 링크**
- [[객체 추적]]
- [[객체 영속성]]
- [[시공간 추론]]

## **📌 참고 링크**
- **논문 원문**: [https://openreview.net/forum?id=9071](https://openreview.net/forum?id=9071)[1]
- **코드**: (논문에서 코드 링크는 명시되지 않음)

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
