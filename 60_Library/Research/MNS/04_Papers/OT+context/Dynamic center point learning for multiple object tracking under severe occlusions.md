---
aliases: ["Dynamic center point learning MOT"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "Dynamic center point learning for multiple object tracking under Severe occlusions"
authors: ["Jinqiu Sun", "Yaoqi Hu", "Axi Niu", "Yanning Zhang"]
year: 2024
venue: "Knowledge-Based Systems"
paper_url: "https://www.researchgate.net/publication/381290000_Dynamic_center_point_learning_for_multiple_object_tracking_under_Severe_occlusions"
topics: ["Multi-Object Tracking", "Occlusion Handling", "Deep Learning", "Computer Vision"]
---

## **📄 Dynamic center point learning for multiple object tracking under Severe occlusions 개요**

- **발표 논문**: Dynamic center point learning for multiple object tracking under Severe occlusions, Jinqiu Sun, Yaoqi Hu, Axi Niu, Yanning Zhang, Knowledge-Based Systems, 2024.[1][2]
- **핵심 아이디어**:
    기존 [[Multi-Object Tracking (MOT)]] 방법론들이 [[동적 배경 (dynamic backgrounds)]] 및 [[심한 가려짐 (severe occlusions)]] 상황에서 객체 영역 및 배경 내의 상세 정보를 포착하지 못하여 부정확하고 일관성 없는 추적 결과를 초래하는 문제를 해결하기 위해 새로운 접근 방식을 제안한다. 이 방법은 [[세분화된 단서 (fine-grained cues)]]를 활용하여 객체 영역과 배경의 동적 변화를 발견하고 궤적 복구 및 연관을 용이하게 한다.[1]
- **주요 성과**:
    - (구체적인 수치는 논문 전문 확인 필요)
    - [[MOT]]의 정확도와 견고성 향상 (추정)

---

## **🏗 아키텍처 개요**

[논문 전문을 통해 모델의 전체적인 구조 설명이 필요합니다. 현재는 주요 모듈만 파악됩니다.]

### **0. 기호/차원**
- (논문 전문 확인 필요)

### **1. 주요 파트 1 (예: Points Trajectories Generator)**
- **구성**: 초기 [[점 집합 (initial set of points)]]을 샘플링하고, [[점 궤적 (point trajectories)]]을 생성하며, 초기 점 집합을 정제하여 세분화된 단서를 생성한다.[1]
- 각 층:
    1. **[[Points Trajectories Generator]]**
- **특이 사항**: [[세분화된 단서 (fine-grained cues)]] 생성에 중점.[1]

### **2. 주요 파트 2 (예: Camera Motion and Occlusion Compensation)**
- **구성**: 배경 및 객체 점 궤적을 활용하여 배경 움직임을 보정하고, 가려진 객체의 [[경계 상자 (bounding boxes)]]를 복구한다.[1]
- 각 층:
    1. **[[Camera Motion and Occlusion Compensation]]**

### **3. 주요 파트 3 (예: Fine- and Coarse-grained Association)**
- **구성**: 점 궤적 단서를 활용하여 [[미세 및 거친 연관 전략 (fine-grained and coarse-grained association strategy)]]을 수립하고, 객체 경계 상자로부터 공간적 단서를 결합한다.[1]
- 각 층:
    1. **[[Fine- and Coarse-grained Association]]**

### **4. 주요 수식 요약**
- (논문 전문 확인 필요)

---

## **🎯 주요 구성 요소**

### **1. [[Points Trajectories Generator]]**
- **입력/출력 및 작동 원리 설명**: 초기 점 집합을 샘플링하고, 이 점들의 궤적을 생성한 후, 초기 점 집합을 정제하여 객체 및 배경의 세분화된 움직임 단서를 제공한다.[1]
- $$ (논문 전문 확인 필요) $$

### **2. [[Camera Motion and Occlusion Compensation]]**
- **병렬 처리, 분할, 혹은 특수 기능 설명**: 배경과 객체의 점 궤적 정보를 사용하여 카메라 움직임으로 인한 오차를 보정하고, 가려짐으로 인해 손실된 객체의 경계 상자 정보를 복구한다.[1]
- **설정 값 (논문 기준)**: (논문 전문 확인 필요)

### **3. [[Fine- and Coarse-grained Association]]**
- **설명**: 점 궤적 단서를 활용하여 객체 간의 연관성을 더욱 효과적으로 확립한다. 이는 객체 경계 상자에서 얻은 미세 및 거친 공간적 단서를 결합하는 전략을 포함한다.[1]

---

## **⚖️ [제안 모델] vs [기존 모델]**

| **비교 항목** | **[제안 모델]** | **[비교 모델 1]** | **[비교 모델 2]** |
| :--- | :--- | :--- | :--- |
| **가려짐 처리** | 세분화된 단서 및 동적 중심점 학습 | 전체적인 외형 또는 공간적 단서 | (논문 전문 확인 필요) |
| **배경 처리** | 배경 움직임 보정 | (논문 전문 확인 필요) | (논문 전문 확인 필요) |
| **복잡도** | $O(\dots)$ (논문 전문 확인 필요) | $O(\dots)$ (논문 전문 확인 필요) | $O(\dots)$ (논문 전문 확인 필요) |

- 제안 모델은 기존 방법론들이 동적 배경과 심한 가려짐 상황에서 객체 영역 및 배경의 상세 정보를 포착하지 못하는 한계를 극복하기 위해 세분화된 단서를 활용한다.[1]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: (논문 전문 확인 필요)
- **특징**: (논문 전문 확인 필요)

---

## **⚙️ 학습 설정**

- **데이터셋**: (논문 전문 확인 필요)
- **하드웨어**: (논문 전문 확인 필요)
- **학습 시간**: (논문 전문 확인 필요)
- **옵티마이저**: (논문 전문 확인 필요)
- **규제(Regularization)**: (논문 전문 확인 필요)

---

## **⚠️ 한계**
- (논문 전문 확인 필요)

---

## **📊 주요 실험 결과**

### **[메인 태스크 성능]**

|**모델**|**[지표 1]**|**[지표 2]**|
|---|---|---|
| [비교 모델 A] | 수치 | 수치 |
| [비교 모델 B] | 수치 | 수치 |
| **[제안 모델]** | **수치** | **수치** |

- (논문 전문 확인 필요)

---

## **🔮 향후 연구 방향**
- (논문 전문 확인 필요)

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Occlusion Handling]]
- [[Center Point Tracking]]

## **📌 참고 링크**
- **논문 원문**: https://www.researchgate.net/publication/381290000_Dynamic_center_point_learning_for_multiple_object_tracking_under_Severe_occlusions[1]
- **코드**: (논문 전문 확인 필요)

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
