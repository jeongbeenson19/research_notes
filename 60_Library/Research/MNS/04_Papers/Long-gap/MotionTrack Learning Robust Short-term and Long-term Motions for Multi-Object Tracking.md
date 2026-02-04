---
aliases:
  - MotionTrack
type: paper
tags:
  - DeepLearning
  - Paper
  - Long-gap
status: 🟧 Reading
rating: 5
date: 2026-02-03
title: "MotionTrack: Learning Robust Short-term and Long-term Motions for Multi-Object Tracking"
authors:
  - Zheng Qin
  - S. Zhou
  - L. Wang
  - J. Duan
  - G. Hua
  - W. Tang
year: 2023
venue: CVPR
paper_url: https://arxiv.org/abs/2303.10404
topics:
  - Multi-Object Tracking
  - Motion Learning
  - Deep Learning
---

## **📄 MotionTrack: Learning Robust Short-term and Long-term Motions for Multi-Object Tracking 개요**

- **발표 논문**: MotionTrack: Learning Robust Short-term and Long-term Motions for Multi-Object Tracking (Zheng Qin 외, CVPR 2023)[1]
- **핵심 아이디어**:
    [[Multi-Object Tracking]](MOT)에서 발생하는 밀집된 군중(dense crowds) 및 극심한 가려짐(extreme occlusions)과 같은 어려운 시나리오에서 강건한 단기(short-term) 및 장기(long-term) 모션을 학습하여 객체 궤적을 효과적으로 연결하는 [[MotionTrack]]이라는 간단하면서도 효과적인 추적기를 제안한다.[2][3] 이 방법은 [[tracking-by-detection]] 패러다임을 따르며, 단거리 및 장거리 궤적 연결 문제를 해결하기 위해 [[Interaction Module]]과 [[Refind Module]]을 통합한다.[2][3]
- **주요 성과**:
    - MOT17 및 MOT20 데이터셋에서 최첨단(state-of-the-art) 성능을 달성했다.[2][3]
    - MOT17에서 IDF1, HOTA, AssA, DetA, IDs, Frag 등 대부분의 주요 지표에서 최상위 결과를 기록했으며, 두 번째로 우수한 추적기보다 IDF1에서 2.0, AssA에서 3.1 높은 성능을 보였다.[3]
    - ID 스위치(identity switches, IDs)를 최소화하여 MOT17에서 P3AFormer보다 40% 적은 IDs를, MOT20에서 두 번째로 우수한 모델보다 13% 적은 IDs를 달성했다.[3]
    - MOT20에서 ByteTrack 대비 IDF1 1.3, MOTA 0.2, HOTA 1.5 증가를 포함하여 상당한 개선을 보였다.[3]

---

## **🏗 아키텍처 개요**

MotionTrack은 [[tracking-by-detection]] 패러다임 내에서 단기 및 장기 모션을 학습하여 궤적을 연결하는 통합 프레임워크이다.[2]

### **0. 기호/차원**
- (논문 원문 참조 필요)

### **1. Interaction Module**
- **구성**: 밀집된 군중(dense crowds) 상황에서 단기 궤적(short-term trajectories)으로부터 상호작용 인식 모션(interaction-aware motions)을 학습한다.[2][3]
- **각 층**:
    1. **[[비대칭 인접 행렬]] (asymmetric adjacency matrix)**: 타겟 간의 상호작용 관계를 표현한다.[3]
    2. **[[그래프 컨볼루션 네트워크]] (graph convolution network)**: 정보 융합을 통해 다음 프레임의 위치를 예측한다.[3]
- **특이 사항**: 각 타겟의 복잡한 움직임을 추정하여 충돌을 피하고 단거리 연결 문제를 해결한다.[2][3]

### **2. Refind Module**
- **구성**: 극심한 가려짐(extreme occlusions) 상황에서 타겟의 과거 궤적(history trajectory)으로부터 신뢰할 수 있는 장기 모션(long-term motions)을 학습한다.[2][3]
- **각 층**:
    1. **[[상관 관계 계산]] (correlation calculation)**: 일치하지 않는 손실된 트랙렛(lost tracklets)과 탐지(detections) 간의 대응 관계를 분석한다.[3]
    2. **[[오류 보상]] (error compensation)**: 일치하는 쌍을 선택하여 장거리 연결을 완료한다.[3]
- **특이 사항**: 중단된 궤적을 해당 탐지와 연결하여 장거리 연결 문제를 해결한다.[2][3]

### **3. 주요 수식 요약**
- (논문 원문 참조 필요)

---

## **🎯 주요 구성 요소**

### **1. [[Interaction Module]]**
- **입력/출력 및 작동 원리 설명**: 타겟 간의 상호작용을 모델링하여 밀집된 환경에서 타겟의 복잡한 움직임을 예측하고 단거리 궤적 연결의 정확도를 높인다.[2][3]
- $$ (논문 원문 참조 필요) $$

### **2. [[Refind Module]]**
- **병렬 처리, 분할, 혹은 특수 기능 설명**: 과거 궤적 정보를 활용하여 장기 모션을 학습하고, 가려짐으로 인해 손실된 타겟을 재식별하며 중단된 경로를 보상한다.[2][3]
- **설정 값 (논문 기준)**: (논문 원문 참조 필요)

### **3. 기타 구성 요소**
- (논문 원문 참조 필요)

---

## **⚖️ MotionTrack vs 기존 모델**

| **비교 항목** | **MotionTrack** | **P3AFormer (MOT17)** | **ByteTrack (MOT20)** |
| :--- | :--- | :--- | :--- |
| **IDs (감소율)** | 40% 감소 (MOT17)[3] | - | - |
| **IDs (감소율)** | 13% 감소 (MOT20)[3] | - | - |
| **IDF1 (MOT17)** | SOTA (2.0↑)[3] | - | - |
| **AssA (MOT17)** | SOTA (3.1↑)[3] | - | - |
| **IDF1 (MOT20)** | 1.3↑[3] | - | - |
| **MOTA (MOT20)** | 0.2↑[3] | - | - |
| **HOTA (MOT20)** | 1.5↑[3] | - | - |
| **복잡도** | (논문 원문 참조 필요) | (논문 원문 참조 필요) | (논문 원문 참조 필요) |

- MotionTrack은 밀집된 군중 및 극심한 가려짐과 같은 어려운 시나리오에서 기존 모델들보다 뛰어난 성능을 보이며, 특히 ID 스위치를 크게 줄이는 데 강점을 가진다.[3]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: (논문 원문 참조 필요)
- **특징**: (논문 원문 참조 필요)

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - MOT17[2]
    - MOT20[2]
- **하드웨어**: (논문 원문 참조 필요)
- **학습 시간**: (논문 원문 참조 필요)
- **옵티마이저**: (논문 원문 참조 필요)
- **규제(Regularization)**:
    - (논문 원문 참조 필요)

---

## **⚠️ 한계**
- (논문 원문 참조 필요)

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**IDF1 (MOT17)**|**HOTA (MOT17)**|**IDs (MOT17)**|**IDF1 (MOT20)**|**HOTA (MOT20)**|**IDs (MOT20)**|
|---|---|---|---|---|---|---|
| P3AFormer | - | - | 높음 | - | - | - |
| ByteTrack | - | - | - | 낮음 | 낮음 | - |
| **MotionTrack** | **SOTA** | **SOTA** | **40% 감소** | **SOTA** | **SOTA** | **13% 감소** |

---

## **🔮 향후 연구 방향**
- (논문 원문 참조 필요)

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Tracking-by-Detection]]
- [[Interaction Module]]
- [[Refind Module]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2303.10404[1]
- **코드**: https://github.com/qwomeng/MotionTrack[2]

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
