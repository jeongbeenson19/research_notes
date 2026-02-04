---
aliases:
  - JDECMC
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
  - CameraMotionCompensation
  - ViewShift
status: 🟧 Reading
rating: 0
date: 2024-03-01
title: "JDECMC: Improving JDE based multi-object tracking with Camera Motion Compensation"
authors:
  - Melikamu Liyih Sinishaw et al.
year: 2024
venue: Preprint (ResearchGate)
paper_url: https://www.researchgate.net/publication/378700000_JDECMC_Improving_JDE_based_multi-object_tracking_with_Camera_Motion_Compensation
topics:
  - Multi-Object Tracking
  - Joint Detection and Embedding
  - Camera Motion Compensation
---

## **📄 JDECMC: Improving JDE based multi-object tracking with Camera Motion Compensation 개요**

- **발표 논문**: JDECMC: Improving JDE based multi-object tracking with Camera Motion Compensation (Melikamu Liyih Sinishaw et al., 2024)[1]
- **핵심 아이디어**:
    기존 [[JDE (Joint Detection and Embedding)]] 기반 [[Multi-Object Tracking (MOT)]] 방법론은 혼잡한 장면이나 비강체 카메라 움직임으로 인해 타겟이 손실되거나 가려질 때 연관(association)에 실패할 수 있는 문제를 해결한다.[2] 제안하는 JDECMC는 JDE 기반의 간단하면서도 효과적인 아키텍처로, 객체의 임베딩(embedding) 및 위치 거리(embedding cosine distance와 location distance 결합)를 통합하고, [[Camera Motion Compensation (CMC)]]을 활용하여 특히 동적인 카메라 움직임 시 정확한 바운딩 박스 위치를 예측한다.[2]
- **주요 성과**:
    - MOT17, MOT20, DanceTrack 벤치마크 데이터셋에서 각각 74.2%, 72.0%, 90.5%의 [[MOTA (Multiple Object Tracking Accuracy)]]를 달성했다.[2]
    - MOT17, MOT20, DanceTrack 벤치마크에서 각각 72.5%, 72.4%, 79.8%의 [[IDF1 (ID F1 Score)]]를 기록했다.[2]
    - 혼잡하고 동적인 장면에서 원샷(one-shot) 트래커의 추적 및 속도 문제를 효과적으로 해결한다.[2]
    - 이미지 등록(image registration)을 통해 배경 객체를 드러내어 혼잡하고 동적인 장면을 처리하기 위한 카메라 모션 보상을 사용한다.[2]
    - 효율적인 데이터 연관(data association)을 위해 임베딩 및 위치 거리 행렬을 도입하여 추적 속도를 향상시킨다.[2]
    - 간단하고 효율적인 온라인 원샷 트래커를 제안한다.[2]

---

## **🏗 아키텍처 개요**

[논문 전체를 검토한 후 모델의 전체적인 구조 설명 및 세부 내용을 추가해야 합니다.]

### **0. 기호/차원**
- [주요 기호 및 차원 정의 (LaTeX 사용)]
- [입력 데이터 차원 등]

### **1. [주요 파트 1 (예: 인코더)]**
- **구성**: [레이어 수, 스택 구조 등]
- 각 층:
    1. **[[핵심 컴포넌트 1]]**
    2. **[[핵심 컴포넌트 2]]**
- **특이 사항**: [Residual connection, Normalization 등]

### **2. [주요 파트 2 (예: 디코더)]**
- **구성**: [레이어 수, 구조 설명]
- 각 층:
    [세부 구성 요소 나열]

### **3. 주요 수식 요약**
- **[컴포넌트 명]**:
  - $수식$
- **[컴포넌트 명]**:
  - $수식$

---

## **🎯 주요 구성 요소**

[논문 전체를 검토한 후 핵심 메커니즘 및 구성 요소에 대한 설명을 추가해야 합니다.]

### **1. [[핵심 메커니즘 1]]**
- 입력/출력 및 작동 원리 설명
- $$핵심 수식$$

### **2. [[핵심 메커니즘 2]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명
- 설정 값 (논문 기준)

### **3. [기타 구성 요소]**
- [Embedding, Position Encoding 등 설명]

---

## **⚖️ [제안 모델] vs [기존 모델]**

| **비교 항목** | **JDECMC** | **[비교 모델 1]** | **[비교 모델 2]** |
| :--- | :--- | :--- | :--- |
| **MOTA (MOT17)** | 74.2%[2] | | |
| **IDF1 (MOT17)** | 72.5%[2] | | |
| **MOTA (MOT20)** | 72.0%[2] | | |
| **IDF1 (MOT20)** | 72.4%[2] | | |
| **MOTA (DanceTrack)** | 90.5%[2] | | |
| **IDF1 (DanceTrack)** | 79.8%[2] | | |
| **복잡도** | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ |

- JDECMC는 기존 원샷 트래커의 추적 및 속도 문제를 효과적으로 해결하며, 특히 혼잡하고 동적인 장면에서 강점을 보인다.[2]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: [Autoregressive, Flow-based 등 설명]
- **특징**: [Masking, Sampling 기법 등]

---

## **⚙️ 학습 설정**

[논문 전체를 검토한 후 학습 설정에 대한 세부 내용을 추가해야 합니다.]

- **데이터셋**:
    - [데이터셋 이름] (데이터 크기, 특징)
- **하드웨어**: [GPU/TPU 사양 및 개수]
- **학습 시간**: [Step 수 또는 시간]
- **옵티마이저**: [이름 및 파라미터 ($\beta_1, \epsilon$ 등)]
- **규제(Regularization)**:
    - [Dropout, Label Smoothing 등]

---

## **⚠️ 한계**
- [논문에서 언급하거나 구조적으로 가지는 한계점 1]
- [한계점 2]

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**MOTA (MOT17)**|**IDF1 (MOT17)**|**MOTA (MOT20)**|**IDF1 (MOT20)**|**MOTA (DanceTrack)**|**IDF1 (DanceTrack)**|
|---|---|---|---|---|---|---|
| **JDECMC** | **74.2%**[2] | **72.5%**[2] | **72.0%**[2] | **72.4%**[2] | **90.5%**[2] | **79.8%**[2] |

---

## **🔮 향후 연구 방향**
- [논문의 Future Work 섹션 요약]
- [확장 가능성]

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Joint Detection and Embedding]]
- [[Camera Motion Compensation]]

## **📌 참고 링크**
- **논문 원문**: https://www.researchgate.net/publication/378700000_JDECMC_Improving_JDE_based_multi-object_tracking_with_Camera_Motion_Compensation[1]
- **코드**: https://github.com/Melikamuliyih/JDECMC[2]

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
