---
alias:
  - BoostTrack
type: paper
tags:
  - DeepLearning
  - Paper
  - MultipleObjectTracking
  - MOT
  - Long-gap
  - OTnContext
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "BoostTrack: Boosting the Similarity Measure and Detection Confidence for Improved Multiple Object Tracking"
authors:
  - V.D. Stanojevic
  - B.T. Todorovic
year: 2024
venue: Machine Vision and Applications, Vol. 35, p. 53
paper_url: https://arxiv.org/abs/2408.13003
topics:
  - Multiple Object Tracking (MOT)
  - Detection Confidence
  - Similarity Measure
  - Deep Learning
---

## **📄 BoostTrack 개요**

- **발표 논문**: "BoostTrack: Boosting the Similarity Measure and Detection Confidence for Improved Multiple Object Tracking" by V.D. Stanojevic and B.T. Todorovic, published in Machine Vision and Applications, Vol. 35, p. 53, 2024.[1]
- **핵심 아이디어**: BoostTrack는 다단계 연관(multi-stage association) 방식의 단점을 피하고, 낮은 신뢰도(low-confidence)의 탐지(detections)를 활용하기 위해 탐지 신뢰도 부스팅(detection confidence boosting)을 적용하는 추적-기반-탐지(tracing-by-detection) [[MOT]] 방법론입니다. 특히 혼잡한 장면이나 잦은 폐색(occlusions) 상황에서 추적 성능을 향상시키는 것을 목표로 합니다.[2][3][4][5][6][7]
- **주요 성과**:
    - 혼잡한 장면과 잦은 폐색 상황에서 추적 성능을 향상시켰습니다 (특히 MOT20 데이터셋에서 효과적).[2][3]
    - 실시간 실행 속도를 유지하면서 표준 벤치마크 솔루션과 유사한 결과를 달성했습니다.[4]
    - 외형 유사성(appearance similarity)과 결합 시 MOT17 및 MOT20 데이터셋에서 모든 표준 벤치마크 솔루션을 능가했습니다.[4]
    - MOT Challenge에서 MOT17 및 MOT20 테스트 세트의 HOTA 지표에서 온라인 방법 중 1위를 기록했습니다.[4]
    - ByteTrack 대비 MOTA에서 0.6%, IDF1에서 4.5% 향상된 성능을 보였습니다.[8]

---

## **🏗 아키텍처 개요**

BoostTrack는 추적-기반-탐지(tracing-by-detection) [[MOT]] 방법으로, 여러 경량 플러그 앤 플레이(plug and play) 추가 기능을 활용하여 MOT 성능을 향상시킵니다.[4]

### **0. 기호/차원**
- (정보 부족)

### **1. [[탐지-트랙렛 신뢰도 점수]]**
- **구성**: 탐지-트랙렛 신뢰도 점수(detection-tracklet confidence score)를 설계하여 유사성 측정(similarity measure)을 조정하고, 단일 단계 연관(one-stage association)에서 높은 탐지 신뢰도와 높은 트랙렛 신뢰도 쌍을 암묵적으로 선호합니다.[4]

### **2. [[유사성 측정 부스팅]]**
- **구성**: IoU(Intersection over Union) 사용으로 인한 모호성을 줄이기 위해, 마할라노비스 거리(Mahalanobis distance)와 형태 유사성(shape similarity)을 추가하여 전반적인 유사성 측정을 강화합니다.[4][6]

### **3. 주요 수식 요약**
- (정보 부족)

---

## **🎯 주요 구성 요소**

### **1. [[탐지 신뢰도 부스팅]] (Detection Confidence Boosting)**
- 입력/출력 및 작동 원리 설명: 낮은 탐지 점수(low-detection score) 바운딩 박스를 단일 단계 연관에서 활용하기 위해, 기존 추적 객체에 해당하는 탐지와 이전에 탐지되지 않은 객체에 해당하는 탐지라는 두 그룹의 탐지 신뢰도 점수를 높입니다.[4] 이는 DLO(Detection of Likely Objects) 신뢰도 부스팅으로 불립니다.[6]
- $$ \text{Boosted Confidence} = f(\text{Original Confidence}, \text{Similarity}) $$

### **2. [[유사성 측정 강화]] (Enhanced Similarity Measure)**
- 병렬 처리, 분할, 혹은 특수 기능 설명: IoU(Intersection over Union)만 사용하는 것에서 발생하는 모호성을 줄이기 위해, 마할라노비스 거리(Mahalanobis distance)와 형태 유사성(shape similarity)을 추가하여 전반적인 유사성 측정을 강화합니다.[4][6]
- $$ \text{Similarity} = w_1 \cdot \text{IoU} + w_2 \cdot \text{Mahalanobis} + w_3 \cdot \text{Shape} $$

### **3. [기타 구성 요소]**
- 보간(interpolation) 및 카메라 움직임 보상(camera motion compensation)과 결합하여 사용됩니다.[4]

---

## **⚖️ BoostTrack vs 기존 모델**

| **비교 항목** | **BoostTrack** | **ByteTrack** | **[비교 모델 2]** |
| :--- | :--- | :--- | :--- |
| **MOTA** | ByteTrack 대비 0.6% 향상[8] | (수치) | (수치) |
| **IDF1** | ByteTrack 대비 4.5% 향상[8] | (수치) | (수치) |
| **HOTA** | 온라인 방법 중 1위 (MOT17, MOT20)[4] | (수치) | (수치) |
| **복잡도** | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ |

- BoostTrack는 기존의 강력한 추적기인 ByteTrack에 비해 MOTA와 IDF1 지표에서 개선된 성능을 보여주며, 특히 HOTA 지표에서는 온라인 방법 중 최고 수준의 성능을 달성합니다.[4][8]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 추적-기반-탐지(tracing-by-detection) 방식입니다.[4]
- **특징**: 단일 단계 연관(one-stage association)을 사용합니다.[4]

---

## **⚙️ 학습 설정**

- **데이터셋**: MOT17, MOT20[4]
- **하드웨어**: (정보 부족)
- **학습 시간**: (정보 부족)
- **옵티마이저**: (정보 부족)
- **규제(Regularization)**: (정보 부족)

---

## **⚠️ 한계**
- 새로운 ID 증가 및 ID 전환(identity switches) 증가가 발생할 수 있으며, 이는 더 정교한 방법이 필요함을 시사합니다.[2][3][6]
- 고정된 IoU 임계값 사용 및 단순한 유사성 측정에 의존하는 한계가 있습니다.[6]

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**MOTA**|**IDF1**|**HOTA**|
|---|---|---|---|
| ByteTrack | (수치) | (수치) | (수치) |
| **BoostTrack** | ByteTrack 대비 0.6% 향상[8] | ByteTrack 대비 4.5% 향상[8] | 온라인 방법 중 1위 (MOT17, MOT20)[4] |

---

## **🔮 향후 연구 방향**
- BoostTrack++는 BoostTrack의 신뢰도 부스팅 한계를 개선하고, 더 풍부한 유사성 측정(shape, Mahalanobis distance, soft BIoU)을 제안합니다.[2][3][5][6][7]
- 소프트 탐지 신뢰도 부스팅(soft detection confidence boost) 및 트랙렛 수명에 따른 가변 유사성 임계값(varying similarity threshold based on tracklet age) 도입이 향후 연구 방향으로 제시됩니다.[6]

---

## **🔗 관련 링크**
- [[Multiple Object Tracking]]
- [[Detection Confidence]]
- [[Similarity Measure]]
- [[Tracing-by-Detection]]

## **📌 참고 링크**
- **논문 원문**: "BoostTrack: boosting the similarity measure and detection confidence for improved multiple object tracking", V.D. Stanojevic, B.T. Todorovic, Machine Vision and Applications, Vol. 35, p. 53, 2024.[1]
- **관련 arXiv 논문 (BoostTrack++)**: [2408.13003] BoostTrack++: using tracklet information to detect more objects in multiple object tracking - arXiv (https://arxiv.org/abs/2408.13003)[5]
- **코드**: https://github.com/vukasin-stanojevic/BoostTrack[2][3]

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics[0]) AND file.name != this.file.name
SORT year desc
```

```