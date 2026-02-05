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
status: 🟧 Reading
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

- 파이프라인 위치: **in-process, post(camera motion compensation, DA, AW)
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
  - **표현 후보**: appearance embedding conf_score로 조절(DA)
  - **내 아이디어와의 대응**:
    - 네가 목표로 하는 belief-state(분포) 관점에서는 “공분산 증가/감쇠, update freeze/decay” 규칙을 **명시적으로 추가 설계**


### 키워드 연결(주축 1 + 부축 1)

- 주축: **out-of-view reactivation / view-shift 대응**
  - ORU가 “재활성화 시 과거 추정 오차 수정”을 명시 
- 부축: **visibility-aware(occlusion robustness)**
  - 논문(노트)이 폐색(occlusion) 강건성을 핵심 목표로 둠 


### 판정(1~2분 결론)

- 유사:
  - “관측 단절/재등장” 상황에서 **재활성화 안정화**를 직접 겨냥(ORU/OCR)  [oai_citation:7‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)
- 차용:
  - **ORU(재활성화 시 관측 기반 re-update)** 는 네 모듈의 “location state 재고정” 파트에 그대로 차용 후보  [oai_citation:8‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
  - **OCM(방향 일관성 cost 항)** 은 네 association cost에 “motion-based context prior”로 붙이기 쉬움  [oai_citation:9‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)
- 충돌/빈칸:
  - 네 아이디어의 핵심인 **appearance memory / semantic state / belief(분포) 명시**는 이 노트 기준 OC-SORT가 직접 제공하지 않음 → 너의 novelty(또는 추가 기여) 영역으로 남음

---

## 🧪 Assumptions → 테스트 케이스(재현 조건으로)

- 가정 A: KF + Hungarian 기반의 온라인 추적 프레임워크 유지  [oai_citation:10‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
  - 깨지는 상황: 비선형/급가속 + 긴 gap에서 모션만으로 재연결 어려움(이때 ORU/OCM이 얼마나 버티는지)
- 가정 B: off-the-shelf detections 사용(학습 없는 필터링 기반)  [oai_citation:11‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
  - 깨지는 상황: detector miss가 잦은 도메인(저조도/블러/군중)에서 OCR이 “잘못된 IOU 복구”로 false merge 유발 가능

---

## 💥 Failure Modes(추정, 실험으로 확인할 것)

1) **긴 gap(재등장)에서 wrong reactivation**
   - 조건: gap↑, 다수 객체 근접, 유사 궤적
   - 오류 유형: IDSW / false merge
   - 점검: ORU가 “과거를 관측으로 재업데이트”하더라도, 관측 자체가 잘못 연결되면 오히려 확정 오류가 될 수 있음  [oai_citation:12‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)

2) **stationary object에서 track fragmentation**
   - 조건: 정지/저속 + detector jitter
   - OCR이 단기 occlusion/정지 객체에 도움을 주도록 설계되었다고 노트에 명시  [oai_citation:13‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
   - 점검: IOU 기반 복구가 오히려 다른 객체와 붙는지(군중/밀집에서)

3) **비선형 motion 구간에서 cost 불안정**
   - 조건: 급회전/급정지/방향 전환
   - OCM이 “direction consistency를 cost matrix에 통합”  [oai_citation:14‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
   - 점검: 방향 일관성이 깨지는 스포츠 상황(컷인/턴)이 많은 경우 오히려 페널티가 될 수 있음

---

## 🧩 구현 체크리스트(차용 가능성)

- ORU (location 재고정 모듈)
  - 입력: (재활성화된 track, 최신 observation, gap 구간)
  - 출력: virtual trajectory + 과거 KF 파라미터 re-update  [oai_citation:15‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
  - 구현 관문: “어떤 시점부터 과거를 되감아 업데이트하는가”, “virtual trajectory 생성 규칙”

- OCM (association cost 항)
  - 입력: track motion 방향/velocity, observation motion(프레임 간 변화)
  - 출력: cost matrix 항(방향 일관성 반영)  [oai_citation:16‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
  - 구현 관문: direction consistency 정의(각도/내적/정규화), 노이즈 완화 방식(스무딩/클램핑)

- OCR (post-recovery)
  - 입력: 1차 매칭에서 남은 unmatched tracks & detections
  - 출력: IOU 기반 2차 연결(복구)  [oai_citation:17‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
  - 구현 관문: 수행 조건(언제만 실행?), IOU threshold, false merge 방지 게이트

---

## 📌 Decision Log 영향(네 D1~D3 기준)

- D1(Fusion):
  - OC-SORT는 “학습 기반 feature injection”이 아니라 **cost 항 추가(OCM) + post heuristic(OCR)** 쪽에 가까움  [oai_citation:18‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
  - → 너의 설계에서도 “강주입(injection)보다 gating/score-fusion”이 안전하다는 근거로 사용 가능

- D2(Location belief):
  - ORU는 “belief를 퍼뜨려 유지”라기보다 “관측으로 재정렬(re-update)”이 핵심  [oai_citation:19‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
  - → 네 belief-state를 하고 싶다면, OC-SORT 위에 **gap에 따른 공분산 증가/decay 규칙**을 추가하는 방향이 자연스러움

- D3(Semantic):
  - 본 노트 기준 semantic은 비어있음 → semantic을 넣는다면 **추가 기여(차별점)**로 남음

---

## ✅ 다음 행동(OC-SORT에서 파생되는 다음 스텝)

1) **사건 중심 평가 프로토콜로 ORU/OCR의 효과를 분리**
   - reactivation 사건(gap-bucket)에서: ORU on/off, OCR on/off로 IDS/false merge 비교

2) **네 모듈 MVP 정의**
   - OC-SORT(모션/관측 중심) + 네 추가(appearance memory or belief rule) 중 “하나만” 얹어서 ablation 가능하게 설계

3) **OC-SORT를 베이스라인으로 삼을지 결정**
   - 스포츠/유니폼 유사 도메인이라면 “appearance 없는 강건성”이 장점일 수 있으니, 네 아이디어의 위치를
     - (A) OC-SORT + belief/uncertainty 확장
     - (B) OC-SORT + appearance memory(단, 업데이트 규칙 엄격)
     중 하나로 좁히는 게 다음 단계
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