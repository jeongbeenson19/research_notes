---
alias:
  - Deep OC-SORT
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
  - PedestrianTracking
  - ReIdentification
  - Long-gap
  - ViewShift
  - in-process
  - post
status: 🟩 Done
rating: 0
date: 2026-02-03
title: "Deep OC-SORT: Multi-Pedestrian Tracking by Adaptive Re-Identification"
authors:
  - Gerard Maggiolino
  - Adnan Ahmad
  - Jinkun Cao
  - Kris Kitani
year: 2023
venue: arXiv
paper_url: https://arxiv.org/abs/2302.11813
topics:
  - Multi-Object Tracking (MOT)
  - Pedestrian Tracking
  - Re-Identification
  - Computer Vision
comment: Cost에 영향을 줄 feature 도입 시 DA와 AW의 방식으로 soft한 fusion 방식으로 주입할 가능성 발견
Keyword:
  - DA
  - AW
  - CMC
  - Appearance Cost
  - Adaptive Fusion
  - View-shift Robustness
---

## **📄 Deep OC-SORT: Multi-Pedestrian Tracking by Adaptive Re-Identification 개요**

- **발표 논문**: "Deep OC-SORT: Multi-Pedestrian Tracking by Adaptive Re-Identification" by Gerard Maggiolino, Adnan Ahmad, Jinkun Cao, and Kris Kitani, 2023 (arXiv)[1][2][3]
- **핵심 아이디어**:
기존 모션 기반 [[Object Tracking#^730413|MOT]] 방법론, 특히 [[Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking|OC-SORT]]에 객체의 외형(appearance) 정보를 적응적으로 통합하여 추적 정확도와 강건성(robustness)을 향상시키는 새로운 접근 방식을 제안한다.[4][3][5] 이는 외형 정보 활용이 부족했던 기존 모션 기반 방법론의 한계를 극복하고, [[Object Tracking#^d379bd|Occlusion]], 조명 변화 등으로 인한 특징 저하(feature degradation)에 대한 강건성을 높이는 것을 목표로 한다.[4][3][5] 특히, 복잡한 폐색 상황에서 강건한 외형 특징 추출, 효율적인 탐지 결과 후처리, 그리고 폐색 정도에 따른 특징 가중치 적응적 조정을 강조한다.[6]
- **주요 성과**:
    - MOT20 벤치마크에서 1위, MOT17 벤치마크에서 2위를 달성했다 (HOTA 기준 각각 63.9 및 64.9).[1][3][5]
    - 도전적인 DanceTrack 벤치마크에서 61.3 HOTA를 달성하며, 기존의 더 복잡한 방법론들과 비교해도 새로운 SOTA(State-of-the-Art)를 기록했다.[3][5]
    - OC-SORT 대비 DanceTrack에서 약 6 HOTA 향상을 보였다.[1]
    - ID 스위치(identity switches)를 효과적으로 감소시켰다.[2][7][5]

---

## **🏗 아키텍처 개요**

Deep OC-SORT는 기존 고성능 모션 기반 추적 방법론에 외형 매칭을 적응적으로 통합하는 방식으로 작동한다. 특히 [[Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking|OC-SORT]] 프레임워크를 기반으로 하며, 외형 정보를 활용하기 위한 모듈과 폐색 상황에 대응하기 위한 후처리 모듈을 포함한다.

### **0. 기호/차원**
- $D$: 탐지(Detection) 결과
- $T$: 트랙(Track)
- $F_{motion}$: 모션 특징
- $F_{appearance}$: 외형 특징
- $C$: 비용 행렬 (Cost Matrix)

### **1. Re-identification 모듈**
- **구성**: 동적 [[Object Tracking#^d379bd|Occlusion]] 인식을 통합하여 폐색된 보행자로부터 고품질 외형 특징(appearance features)을 추출한다.[6]
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

### **2. [[Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking|OC-SORT]] 기반 모션 추적**
- 병렬 처리, 분할, 혹은 특수 기능 설명: Deep OC-SORT는 [[Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking|OC-SORT]]의 효율적이고 고성능 모션 기반 추적 프레임워크를 기반으로 한다.[3][5] OC-SORT는 강력한 객체 탐지기(object detectors)의 발전과 함께 다시 주목받는 [[Object Tracking#^730413|MOT]] 방법론으로, 주로 모션 정보를 사용하여 객체를 연관시킨다.[3][5]
- 설정 값 (논문 기준): (구체적인 설정 값은 논문 본문에 명시될 것으로 예상되나, 검색 결과에서는 확인되지 않음)

### **3. 데이터 연관 (Data Association)**
- 폐색 정도에 따라 비용 행렬(cost matrix)에서 모션 및 외형 특징의 가중치를 적응적으로 조정하는 메커니즘을 포함한다.[6] 이는 다양한 환경 조건에서 추적의 강건성을 보장한다.

### **4. [[CMC(Camera Motion Compensation)]]**
- Camera Motion Compensation은 연속 프레임 사이의 전역 2D 유사변환(스케일·회전)과 평행이동을 추정해, 카메라 움직임으로 인한 겉보기 이동을 추정하고 이를 추적 파이프라인에 명시적으로 보정하는 모듈입니다. 핵심 목적은 탐지-기반 칼만 예측과 관측 보정이 “고정 카메라” 가정에 끌려가지 않도록, 프레임 간 카메라 변화를 먼저 제거해 물체 자체의 운동 신호를 더 깨끗하게 쓰게 만드는 것입니다.


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
## 🔮 향후 연구 방향
- (검색 결과에서 구체적인 정보는 확인되지 않음)
- 외형 정보와 모션 정보의 적응적 통합에 대한 추가 연구, 다양한 환경 및 시나리오에서의 강건성 향상, 그리고 실시간 성능 최적화 등이 예상될 수 있다.

---
## 🔁 내 연구와의 매핑 (Deep OC-SORT)

- 파이프라인 위치: **in-process(camera motion compensation, DA, AW)
  - 기존 OC-SORT 요소에 카메라 모션 보정을 명시적으로 추가(`OpenCV.contrib.VidStab`)
  - tracklet 연결 시 dynamic apprearance로 외형 임베딩에 임계값 설정(좋은 프레임은 re-id 신호, 나쁜 프레임은 노이즈가 연결 결정을 흐리지 않게 모션 기반 연관을 보호)

### State 대응

- location
  - **표현(Representation)**: handcrafted camera motion estimation
  - **핵심 메커니즘(CMC)**: `OpenCV.contirb.VidStab`을 이용한 카메라 모션 추정
  - **내 아이디어와의 대응**:
    - View-shift 발생시 해결 방안으로 사용 가능

- appearance
  - **사용 여부**: appearance 사용(appearance embedding에 dynamic appearance와 adaptive weighting으로 가중치 부여)
  - **내 아이디어와의 대응**: 다른 embedding의 영향력을 훼손하지 않는 기법으로 도입 가능

- semantic
  - **사용 여부**:  **명시적 semantic state 사용 언급 없음**
  - **내 아이디어와의 대응**:

- uncertainty
  - **표현 후보**: appearance embedding conf_score로 조절(DA), 행(특정 트랙)과 열(특정 박스)의 1, 2등 마진을 구해 각 트랙-박스 쌍 마다 보정 가중치 상출(AW)
  - **내 아이디어와의 대응**: 특정 context의 불확실성에 따라 영향력을 조절함


### 키워드 연결(주축 1 + 부축 1)

- 주축: **out-of-view reactivation / view-shift 대응**
  - ORU가 “재활성화 시 과거 추정 오차 수정”을 명시 
- 부축: **appearance를 이용한 robustness 강화**
  - appearance embedding의 불확실성을 이용하여 re-activation 강건성을 부여


### 판정(1~2분 결론)

- 유사:
  - “관측 단절/재등장” 상황에서 appearance를 활용하여 **재활성화 안정화**를 직접 겨냥(DA/AW)
  - View-shift 상황에서 안정화를 위해 보정을 수행함
- 차용:
  - **CMC(Camera Motion Compensation)** 은 View-shift 상황에서 적은 연산량으로 도입할 가능성이 있음
  - **DA(Dynamic Appearance) & AW(Adaptive Weighting)** 은 Appearance를 활용한다는 측면에서 context 주입 방식으로 활용될 가능성이 있으며, 상보적인 구조 설계에 아이디어를 제공
- 충돌/빈칸:
  - 네 아이디어의 핵심인 **semantic state / belief(분포) 명시**는 이 노트 기준 Deep OC-SORT가 직접 제공하지 않음 → 너의 novelty(또는 추가 기여) 영역으로 남음

---

## 🧩 구현 체크리스트(차용 가능성)

- CMC (View-shift 상황에서 입력 보정)
  - 입력: 
  - 출력:
  - 구현 관문: 

- DA (Appearance Cost에 새 임베딩의 기여도를 동적 alpha로 조정, 쓸때만 쓰기)
  - 입력:
  - 출력:
  - 구현 관문: 

- AW (Appearance Cost에 트랙-박스 마진으로 가중치 부여)
  - 입력: 
  - 출력: 
  - 구현 관문: 

---

## 📌 Decision Log 영향(네 D1~D3 기준)

- D1(Fusion):
  - Deep OC-SORT는 “학습 기반 feature injection”이 아니라 **cost항에 embedding이 미치는 영향력 조절(DA) appearance와 motion/IOU의 비율 조절** 쪽에 가까움 
  - → 너의 설계에서도 “강주입(injection)보다 score-fusion”이 안전하다는 근거로 사용 가능

- D2(Location belief):  

- D3(Semantic):

---

## **🔗 관련 링크**
-  [[Object Tracking#^730413|MOT]]
- [[Re-Identification]]
- [[Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking|OC-SORT]]
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