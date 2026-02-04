---
alias: ["PMTrack"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "PMTrack: Multi-object Tracking with Motion-Aware"
authors: ["Xu Guo", "Yujin Zheng", "Dingwen Wang"]
year: 2024
venue: "ACCV"
paper_url: "https://openaccess.thecvf.com/content/ACCV2024/papers/Guo_PMTrack_Multi-object_Tracking_with_Motion-Aware_ACCV_2024_paper.pdf"
topics: ["Multi-object Tracking", "Computer Vision", "Motion Estimation"]
---

## **📄 PMTrack: Multi-object Tracking with Motion-Aware 개요**

- **발표 논문**: PMTrack: Multi-object Tracking with Motion-Aware, Xu Guo, Yujin Zheng, Dingwen Wang, ACCV 2024[1]
- **핵심 아이디어**:
기존 [[Tracking-by-Detection]] 패러다임에서 [[Kalman Filter]]의 선형 예측 한계로 인한 ID 스위치(ID switching) 및 추적 손실(tracking loss) 문제를 해결하기 위해, [[위상 상관(Phase Correlation)]]을 활용하여 인접 프레임 간의 변환 관계를 계산하고 타겟 위치를 현재 프레임 좌표계로 매핑한다. 이 위치 보정(positional correction)은 카메라 움직임으로 인한 이동을 효과적으로 보상하여 ID 스위치를 크게 줄인다. 또한, 궤적의 움직임 상태(motion state)와 정지 상태(stationary state)를 구분하여 추적 안정성과 정확도를 향상시킨다.[1]
- **주요 성과**:
    - 실시간 효율성(real-time efficiency)을 달성하며 카메라 움직임이 있는 장면에서 뛰어난 성능을 보인다.[1]
    - MOT17 테스트 세트에서 MOTA 80.17%, IDF1 78.93%, HOTA 64.04%를 달성하여 주류 방법론들을 능가한다.[1]

---

## **🏗 아키텍처 개요**

PMTrack은 [[Tracking-by-Detection]] 프레임워크를 기반으로 하며, 카메라 움직임 보상과 궤적의 움직임 상태 구분을 통해 추적 성능을 향상시킨다.

### **0. 기호/차원**
- $D_t$: 시점 $t$에서의 검출(detection) 집합
- $T_{t-1}$: 시점 $t-1$에서의 궤적(tracklet) 집합
- $P_t$: 시점 $t$에서의 예측된 궤적 위치
- $O_t$: 시점 $t$에서의 옵셋(offset) 또는 변환 벡터
- $B$: 바운딩 박스(bounding box)

### **1. Translation-based Prediction Modification (TPM)**
- **구성**: 위상 상관(phase correlation)을 사용하여 연속적인 프레임 간의 변환 관계를 계산한다.[2][1]
- **각 층**:
    1. **[[위상 상관]]**: 인접 프레임 간의 전역적인 움직임(translation)을 추정한다.[2][1]
    2. **[[Kalman Filter]] 상태 벡터 조정**: 추정된 옵셋을 사용하여 칼만 필터의 상태 벡터를 조정한다.[2]
- **특이 사항**: 카메라 움직임으로 인한 검출 박스의 상당한 변위를 보상하여, 예측된 추적 박스와의 매칭 실패를 줄인다.[2][1]

### **2. Trajectory State Perception (TSP)**
- **구성**: 궤적을 움직이는 상태(moving)와 정지 상태(static)로 분할한다.[2][1]
- **각 층**:
    1. **움직임 상태 판단**: 궤적의 움직임 패턴을 분석하여 움직임 또는 정지 상태를 판단한다.[2]
    2. **개별적인 연관(Association)**: 움직이는 궤적과 정지된 궤적에 대해 다른 [[IoU]] 임계값을 사용하여 검출과 연관시킨다.[2]
- **특이 사항**: ByteTrack [31]에서 제안된 방법을 활용하여 높은 점수와 낮은 점수의 박스 모두와 연관시킨다.[2]

### **3. 주요 수식 요약**
- **위상 상관**:
  - $R(u,v) = \mathcal{F}^{-1}\left\{ \frac{F_1(w_1,w_2) F_2^*(w_1,w_2)}{|F_1(w_1,w_2) F_2^*(w_1,w_2)|} \right\}$
  - 여기서 $F_1, F_2$는 두 이미지의 푸리에 변환(Fourier Transform)이고, $F_2^*$는 $F_2$의 켤레 복소수(complex conjugate)이다. $R(u,v)$의 피크(peak) 위치가 이미지 간의 상대적인 변환을 나타낸다.

---

## **🎯 주요 구성 요소**

### **1. [[위상 상관(Phase Correlation)]]**
- 입력/출력 및 작동 원리 설명: 연속된 두 프레임의 푸리에 변환을 이용하여 이미지 간의 픽셀 단위 변환(translation)을 정확하게 추정하는 메커니즘이다. 이를 통해 카메라 움직임으로 인한 객체 위치의 전역적인 변화를 보상한다.[2][1]
- $$O_t = \text{argmax}_{u,v} \left( \mathcal{F}^{-1}\left\{ \frac{\mathcal{F}(I_t) \cdot \mathcal{F}(I_{t-1})^*}{|\mathcal{F}(I_t) \cdot \mathcal{F}(I_{t-1})^*|} \right\} \right)$$
  - $I_t, I_{t-1}$은 시점 $t$와 $t-1$의 이미지, $\mathcal{F}$는 푸리에 변환, $*$는 켤레 복소수를 나타낸다.

### **2. [[궤적 상태 인식(Trajectory State Perception)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 궤적을 움직이는 객체와 정지된 객체로 분류하여 각각에 최적화된 연관 전략을 적용한다. 이는 특히 카메라 움직임이 있는 환경에서 추적의 안정성과 정확도를 높이는 데 기여한다.[2][1]
- 설정 값 (논문 기준): 움직임 상태 판단을 위한 임계값 $\alpha$와 $n$을 사용한다.[2]

### **3. [[Kalman Filter]]**
- 객체의 상태(위치, 속도 등)를 예측하고, 새로운 검출을 통해 상태를 업데이트하는 데 사용된다. PMTrack에서는 위상 상관을 통해 얻은 변환 정보를 칼만 필터의 예측 단계에 통합하여 카메라 움직임에 강건한 예측을 수행한다.[2][1]

---

## **⚖️ [PMTrack] vs [기존 모델]**

| **비교 항목** | **PMTrack** | **ByteTrack** | **Botsort** |
| :--- | :--- | :--- | :--- |
| **카메라 움직임 보상** | 위상 상관 기반 변환 보정[2][1] | GMC 알고리즘 (OpenCV)[2] | GMC 알고리즘 (OpenCV)[2] |
| **궤적 상태 구분** | 움직임/정지 상태 구분 및 개별 연관[2][1] | 없음 | 없음 |
| **ID 스위치 감소** | 효과적[1] | 개선 | 개선 |
| **실시간 효율성** | 달성[1] | 높음 | 높음 |
| **복잡도** | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ |

- PMTrack은 위상 상관을 통한 정밀한 카메라 움직임 보상과 궤적의 움직임 상태를 구분하여 연관하는 전략을 통해 기존 [[Tracking-by-Detection]] 기반 모델들의 한계점인 카메라 움직임 및 비선형 객체 움직임 상황에서의 ID 스위치 및 추적 손실 문제를 효과적으로 해결한다.[1]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: [[Tracking-by-Detection]] 패러다임을 따르며, 검출된 객체 박스를 연속적인 프레임에 걸쳐 연관시켜 궤적을 형성한다.[2][1]
- **특징**:
    - **Translation-based Prediction Modification (TPM)**: 위상 상관을 통해 계산된 옵셋으로 칼만 필터의 예측을 보정하여 카메라 움직임에 강건한 예측을 수행한다.[2][1]
    - **Trajectory State Perception (TSP)**: 궤적을 움직이는 객체와 정지된 객체로 나누어 각각에 적합한 [[IoU]] 임계값을 적용하여 연관 정확도를 높인다.[2]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - MOT17 테스트 세트 (보행자 카테고리)[2][1]
    - Kitti (보행자, 자동차, 자전거, 트럭 등)[2]
- **하드웨어**: [정보 없음]
- **학습 시간**: [정보 없음]
- **옵티마이저**: [정보 없음]
- **규제(Regularization)**: [정보 없음]

---

## **⚠️ 한계**
- 논문에서 명시적인 한계점은 언급되지 않았으나, [[Tracking-by-Detection]] 기반 방법론의 일반적인 한계점은 검출기 성능에 크게 의존한다는 점이다. 특히 밀집된 장면(dense scenes)에서는 검출기 성능에 의해 제한될 수 있다.[3]
- 비선형적인 객체 움직임이 매우 복잡한 경우, 선형 예측 모델인 칼만 필터의 한계가 여전히 존재할 수 있다.[1]

---

## **📊 주요 실험 결과**

### **메인 태스크 성능 (MOT17 테스트 세트)**[1]

|**모델**|**MOTA**|**IDF1**|**HOTA**|
|---|---|---|---|
| [주류 방법론] | < 80.17% | < 78.93% | < 64.04% |
| **PMTrack** | **80.17%** | **78.93%** | **64.04%** |

---

## **🔮 향후 연구 방향**
- [논문에서 명시적인 향후 연구 방향은 언급되지 않았으나, 일반적으로 MOT 분야에서는 다음과 같은 방향으로 연구가 진행될 수 있다.]
- 다양한 환경에서의 강건성(robustness) 향상
- 복잡한 상호작용(interaction)을 하는 객체 추적
- 실시간 성능 유지하면서 정확도 극대화

---

## **🔗 관련 링크**
- [[Multi-object Tracking]]
- [[Tracking-by-Detection]]
- [[Kalman Filter]]
- [[Phase Correlation]]

## **📌 참고 링크**
- **논문 원문**: https://openaccess.thecvf.com/content/ACCV2024/papers/Guo_PMTrack_Multi-object_Tracking_with_Motion-Aware_ACCV_2024_paper.pdf[1]
- **코드**: [정보 없음]

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
