---
alias: ["Deep OC-SORT"]
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
  - PedestrianTracking
  - ReIdentification
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "Deep OC-SORT: Multi-Pedestrian Tracking by Adaptive Re-Identification"
authors: ["Gerard Maggiolino", "Adnan Ahmad", "Jinkun Cao", "Kris Kitani"]
year: 2023
venue: "arXiv"
paper_url: https://arxiv.org/abs/2302.11813
topics: ["Multi-Object Tracking (MOT)", "Pedestrian Tracking", "Re-Identification", "Computer Vision"]
---

## **📄 Deep OC-SORT: Multi-Pedestrian Tracking by Adaptive Re-Identification 개요**

- **발표 논문**: "Deep OC-SORT: Multi-Pedestrian Tracking by Adaptive Re-Identification" by Gerard Maggiolino, Adnan Ahmad, Jinkun Cao, and Kris Kitani, 2023 (arXiv)[1][2][3]
- **핵심 아이디어**:
기존 모션 기반 [[Multi-Object Tracking (MOT)]] 방법론, 특히 [[OC-SORT]]에 객체의 외형(appearance) 정보를 적응적으로 통합하여 추적 정확도와 강건성(robustness)을 향상시키는 새로운 접근 방식을 제안한다.[4][3][5] 이는 외형 정보 활용이 부족했던 기존 모션 기반 방법론의 한계를 극복하고, [[폐색 (Occlusion)]], 조명 변화 등으로 인한 특징 저하(feature degradation)에 대한 강건성을 높이는 것을 목표로 한다.[4][3][5] 특히, 복잡한 폐색 상황에서 강건한 외형 특징 추출, 효율적인 탐지 결과 후처리, 그리고 폐색 정도에 따른 특징 가중치 적응적 조정을 강조한다.[6]
- **주요 성과**:
    - MOT20 벤치마크에서 1위, MOT17 벤치마크에서 2위를 달성했다 (HOTA 기준 각각 63.9 및 64.9).[1][3][5]
    - 도전적인 DanceTrack 벤치마크에서 61.3 HOTA를 달성하며, 기존의 더 복잡한 방법론들과 비교해도 새로운 SOTA(State-of-the-Art)를 기록했다.[3][5]
    - OC-SORT 대비 DanceTrack에서 약 6 HOTA 향상을 보였다.[1]
    - ID 스위치(identity switches)를 효과적으로 감소시켰다.[2][7][5]

---

## **🏗 아키텍처 개요**

Deep OC-SORT는 기존 고성능 모션 기반 추적 방법론에 외형 매칭을 적응적으로 통합하는 방식으로 작동한다. 특히 [[OC-SORT]] 프레임워크를 기반으로 하며, 외형 정보를 활용하기 위한 모듈과 폐색 상황에 대응하기 위한 후처리 모듈을 포함한다.

### **0. 기호/차원**
- $D$: 탐지(Detection) 결과
- $T$: 트랙(Track)
- $F_{motion}$: 모션 특징
- $F_{appearance}$: 외형 특징
- $C$: 비용 행렬 (Cost Matrix)

### **1. Re-identification 모듈**
- **구성**: 동적 [[폐색 (Occlusion)]] 인식을 통합하여 폐색된 보행자로부터 고품질 외형 특징(appearance features)을 추출한다.[6]
- **특이 사항**: 외형 특징은 대상의 ID를 유지하는 데 중요한 역할을 한다.

### **2. 후처리 모듈**
- **구성**: 폐색으로 인해 발생할 수 있는 신뢰할 수 없는 탐지(unreliable detections)를 완화하기 위해 탐지 신뢰도(detection confidence)를 향상시키는 기능을 수행한다.[6]
- **특이 사항**: 탐지 품질을 개선하여 전체 추적 성능에 긍정적인 영향을 미친다.

### **3. 주요 수식 요약**
- **비용 행렬 (Cost Matrix) 조정**:
  - 데이터 연관(data association) 단계에서 모션 특징과 외형 특징의 가중치를 폐색 정도에 따라 적응적으로 조정한다.[6]
  - $C = w_{motion} \cdot C_{motion} + w_{appearance} \cdot C_{appearance}$
  - 여기서 $w_{motion}$과 $w_{appearance}$는 폐색 정도에 따라 동적으로 변화하는 가중치이다.

---

## **🎯 주요 구성 요소**

### **1. [[적응형 Re-identification]]**
- 입력/출력 및 작동 원리 설명: Deep OC-SORT의 핵심은 객체의 외형 정보를 활용하여 기존 고성능 모션 기반 방법론에 외형 매칭을 적응적으로 통합하는 것이다.[3][5] 이는 특히 폐색 상황에서 강건한 외형 특징을 추출하고, 외형 특징 가중치를 적응적으로 조정함으로써 ID 스위치를 줄이고 추적 연속성을 높인다.[6][7]
- $$C_{appearance} = \text{ReID\_Distance}(F_{appearance}(D), F_{appearance}(T))$$

### **2. [[OC-SORT]] 기반 모션 추적**
- 병렬 처리, 분할, 혹은 특수 기능 설명: Deep OC-SORT는 [[OC-SORT]]의 효율적이고 고성능 모션 기반 추적 프레임워크를 기반으로 한다.[3][5] OC-SORT는 강력한 객체 탐지기(object detectors)의 발전과 함께 다시 주목받는 [[MOT]] 방법론으로, 주로 모션 정보를 사용하여 객체를 연관시킨다.[3][5]
- 설정 값 (논문 기준): (구체적인 설정 값은 논문 본문에 명시될 것으로 예상되나, 검색 결과에서는 확인되지 않음)

### **3. 데이터 연관 (Data Association)**
- 폐색 정도에 따라 비용 행렬(cost matrix)에서 모션 및 외형 특징의 가중치를 적응적으로 조정하는 메커니즘을 포함한다.[6] 이는 다양한 환경 조건에서 추적의 강건성을 보장한다.

---

## **⚖️ Deep OC-SORT vs 기존 모델**

| **비교 항목** | **Deep OC-SORT** | **OC-SORT** | **DeepSORT** |
| :--- | :--- | :--- | :--- |
| **외형 정보 활용** | 적응적 통합 (O) | 제한적 (X) | 딥 CNN 기반 (O)[7] |
| **폐색 강건성** | 높음 (적응형 Re-ID 및 후처리)[6] | 낮음 (모션 기반) | 향상됨 (외형 특징)[7] |
| **성능 (HOTA)** | SOTA (MOT17: 64.9, MOT20: 63.9, DanceTrack: 61.3)[1][3][5] | (Deep OC-SORT보다 낮음)[1] | (Deep OC-SORT보다 낮음) |
| **ID 스위치** | 감소[2][7][5] | 높음 | 감소[7] |
| **복잡도** | $O(\dots)$ (Re-ID 모듈 추가로 OC-SORT보다 증가 예상) | $O(\dots)$ (효율적) | $O(\dots)$ (딥 CNN으로 증가) |

- Deep OC-SORT는 순수 모션 기반 방법론인 OC-SORT의 효율성을 유지하면서도, 외형 정보를 적응적으로 통합하여 폐색과 같은 어려운 상황에서 ID 스위치를 크게 줄이고 추적 성능을 향상시켰다.[4][3][5] 특히, 외형 특징의 가중치를 동적으로 조절함으로써 다양한 환경에 대한 적응력을 높인 것이 강점이다.[6]

---

## **🧠 추론/디코딩/생성 과정**
- **방식**: 온라인(online) 추적 방식으로, 실시간 애플리케이션에 적합하도록 설계되었다.[4]
- **특징**: (구체적인 특징은 논문 본문에 명시될 것으로 예상되나, 검색 결과에서는 확인되지 않음)

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - MOT20 (매우 혼잡한 장면)[4][3][5]
    - MOT17[4][3][5]
    - DanceTrack (유사한 외형과 다양한 움직임을 가진 객체 추적에 특화)[4][3][5]
- **하드웨어**: (검색 결과에서 구체적인 정보는 확인되지 않음)
- **학습 시간**: (검색 결과에서 구체적인 정보는 확인되지 않음)
- **옵티마이저**: (검색 결과에서 구체적인 정보는 확인되지 않음)
- **규제(Regularization)**: (검
색 결과에서 구체적인 정보는 확인되지 않음)

---

## **⚠️ 한계**
- (논문에서 직접적으로 언급된 한계점은 검색 결과에서 확인되지 않으나, Deep OC-SORT는 기존 모션 기반 추적 시스템의 한계를 극복하고자 제안되었다.)
- 기존 모션 기반 추적 시스템은 다양한 외형 변화에 적응하기 어렵고, 시간이 지남에 따라 특징 저하가 발생하며, 복잡한 폐색 시나리오에서 객체 추적 손실 및 ID 스위치와 같은 문제에 직면한다.[4][6] Deep OC-SORT는 이러한 문제들을 해결하는 데 중점을 둔다.

---

## **📊 주요 실험 결과**

### **메인 태스크 성능 (Multi-Pedestrian Tracking)**

| **모델** | **HOTA (MOT17)** | **AssA (MOT17)** | **IDF1 (MOT17)** | **MOTA (MOT17)** | **IDs (MOT17)** | **Frag (MOT17)** | **HOTA (MOT20)** | **AssA (MOT20)** | **IDF1 (MOT20)** | **MOTA (MOT20)** | **IDs (MOT20)** | **Frag (MOT20)** | **HOTA (DanceTrack)** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Deep OC-SORT** | **64.9**[1][3][5] | **65.9**[1] | **80.6**[1] | **79.4**[1] | **1,950**[1] | **2,040**[1] | **63.9**[1][3][5] | **65.9**[1] | **79.2**[1] | **75.6**[1] | **779**[1] | **1,536**[1] | **61.3**[3][5] |

---

## **🔮 향후 연구 방향**
- (검색 결과에서 구체적인 정보는 확인되지 않음)
- 외형 정보와 모션 정보의 적응적 통합에 대한 추가 연구, 다양한 환경 및 시나리오에서의 강건성 향상, 그리고 실시간 성능 최적화 등이 예상될 수 있다.

---

## **🔗 관련 링크**
- [[Multi-Object Tracking (MOT)]]
- [[Re-identification (Re-ID)]]
- [[OC-SORT]]
- [[DeepSORT]]
- [[Kalman Filter]]
- [[Hungarian Algorithm]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2302.11813[1][3]
- **코드**: https://github.com/GerardMaggiolino/Deep-OC-SORT[3][5]

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```

```