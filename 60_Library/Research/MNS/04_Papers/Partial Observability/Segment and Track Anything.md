---
aliases:
  - SAMTrack
type: paper
tags:
  - DeepLearning
  - Paper
  - VideoSegmentation
  - ObjectTracking
  - PartialObservability
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: Segment and Track Anything
authors:
  - Yangming Cheng
  - et al.
year: 2023
venue: arXiv
paper_url: https://arxiv.org/abs/2305.06558
topics:
  - Video Object Segmentation
  - Object Tracking
  - Foundation Models
  - Multimodal Interaction
---

## **📄 Segment and Track Anything 개요**

- **발표 논문**: Segment and Track Anything (SAMTrack) by Yangming Cheng et al., arXiv 2023.[1]
- **핵심 아이디어**: 비디오 내 모든 객체를 정확하고 효과적으로 분할하고 추적하는 프레임워크인 [[SAMTrack]]을 제안한다. 이 프레임워크는 [[Segment Anything Model (SAM)]]과 AOT 기반 추적 모델인 [[DeAOT]]를 통합하며, 텍스트 기반 상호작용을 위해 [[Grounding-DINO]]를 포함한다. 사용자는 클릭, 스트로크, 텍스트와 같은 다중 모달 상호작용 방식을 통해 객체를 선택하고 추적할 수 있다.[1]
- **주요 성과**:
    - DAVIS-2016 Val에서 92.0%, DAVIS-2017 Test에서 79.2%의 성능을 달성했다.[1]
    - [[DeAOT]]는 VOT 2022 챌린지의 4개 트랙에서 1위를 차지했다.[1]
    - 드론 기술, 자율 주행, 의료 영상, 증강 현실, 생물학적 분석 등 다양한 분야에 적용 가능하다.[1]

---

## **🏗 아키텍처 개요**

SAMTrack은 [[Segment Anything Model (SAM)]], [[DeAOT]] (AOT 기반 추적 모델), 그리고 [[Grounding-DINO]]를 통합하여 비디오 객체 분할 및 추적을 수행한다.[1]

### **0. 기호/차원**
- (정보 부족)

### **1. 주요 파트 1 (예: 인코더)**
- **[[Segment Anything Model (SAM)]]**
- **구성**: 대화형 키프레임 분할을 담당한다.[1]
- **특이 사항**: 사용자의 프롬프트(클릭, 스트로크, 텍스트)에 따라 이미지 내 객체를 분할한다.[1]

### **2. 주요 파트 2 (예: 디코더)**
- **[[DeAOT]] (AOT-based tracking model)**
- **구성**: AOT(Associating Objects with Transformers) 기반의 추적 모델로, 비디오 내 객체 추적을 용이하게 한다.[1]
- **[[Grounding-DINO]]**
- **구성**: 텍스트 기반 상호작용을 지원하여 사용자가 텍스트 프롬프트를 통해 객체를 지정할 수 있게 한다.[1]

### **3. 주요 수식 요약**
- (정보 부족)

---

## **🎯 주요 구성 요소**

### **1. [[Segment Anything Model (SAM)]]**
- **입력/출력 및 작동 원리 설명**: 이미지 내에서 프롬프트(클릭, 박스 등)에 따라 객체를 분할하는 모델이다. SAMTrack에서는 키프레임 분할에 활용되어 사용자가 지정한 객체의 초기 마스크를 생성한다.[1]

### **2. [[DeAOT]] (AOT-based tracking model)**
- **병렬 처리, 분할, 혹은 특수 기능 설명**: VOT 2022 챌린지에서 우수한 성능을 보인 추적 모델로, SAM과 결합하여 비디오 전체에 걸쳐 객체를 일관되게 추적한다.[1]

### **3. [[Grounding-DINO]]**
- **텍스트 프롬프트 기반 객체 인식**: 텍스트 프롬프트를 통해 객체를 인식하고 분할하는 기능을 제공하여, SAMTrack의 다중 모달 상호작용을 가능하게 한다.[1]

---

## **⚖️ [제안 모델] vs [기존 모델]**

| **비교 항목** | **SAMTrack** | **[비교 모델 1]** | **[비교 모델 2]** |
| :--- | :--- | :--- | :--- |
| **상호작용 방식** | 클릭, 스트로크, 텍스트[1] | (정보 부족) | (정보 부족) |
| **기반 모델** | SAM, DeAOT, Grounding-DINO[1] | (정보 부족) | (정보 부족) |
| **복잡도** | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ |

- SAMTrack은 [[SAM]], [[DeAOT]], [[Grounding-DINO]]의 통합을 통해 비디오 객체 분할 및 추적에서 강력한 성능과 유연한 다중 모달 상호작용을 제공한다.[1]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 사용자의 클릭, 스트로크, 또는 텍스트 입력을 통해 객체를 선택하면, [[SAM]]이 키프레임에서 객체를 분할하고, [[DeAOT]]가 이를 비디오 전체에 걸쳐 추적한다.[1]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - (정보 부족)
- **하드웨어**: (정보 부족)
- **학습 시간**: (정보 부족)
- **옵티마이저**: (정보 부족)
- **규제(Regularization)**:
    - (정보 부족)

---

## **⚠️ 한계**
- (정보 부족)

---

## **📊 주요 실험 결과**

### **[메인 태스크 성능]**

|**모델**|**DAVIS-2016 Val (J&F Mean)**|**DAVIS-2017 Test (J&F Mean)**|
|---|---|---|
| **SAMTrack** | **92.0%** | **79.2%** |[1]

---

## **🔮 향후 연구 방향**
- (정보 부족)

---

## **🔗 관련 링크**
- [[Segment Anything Model (SAM)]]
- [[Grounding-DINO]]
- [[Video Object Segmentation]]
- [[Object Tracking]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2305.06558[1]
- **코드**: https://github.com/z-x-yang/Segment-and-Track-Anything[2]

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
