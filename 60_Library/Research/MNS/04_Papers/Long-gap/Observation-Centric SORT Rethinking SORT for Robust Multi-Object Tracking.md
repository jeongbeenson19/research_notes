---
aliases:
  - OC-SORT
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
  - SORT
  - Long-gap
  - OTnContext
  - in-process
  - post
status: 🟩 Done
rating: 0
date: 2026-02-03
title: "Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking"
authors:
  - Jinkun Cao
  - Xinshuo Weng
  - Rui Khirodkar
  - Jianing Pang
  - Kris Kitani
year: 2022
venue: arXiv
paper_url: https://arxiv.org/pdf/2203.14360.pdf
topics:
  - Multi-Object Tracking
  - Kalman Filter
  - Occlusion Handling
  - Non-linear Motion
Keyword:
  - ORU
  - OCM
  - Occlusion Robusteness
  - Non-linear Motion Robustness
comment: 칼만 필터를 사용할 경우 Non-linear Motion Robustness의 확보 목적으로 ORU, OCU 차용 고려할 수 있음
---

## **📄 Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking 개요**

- **발표 논문**: Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking by Jinkun Cao et al., arXiv 2022.
- **핵심 아이디어**:
    기존 [[Kalman Filter (KF)]] 기반의 [[Multi-Object Tracking (MOT)]] 방법론인 [[SORT]]의 한계점(선형 운동 가정, 추정 중심적 접근, 오차 누적)을 해결하기 위해 "관측 중심(observation-centric)" 접근 방식을 제안한다. 특히, 폐색(occlusion) 및 비선형 움직임(non-linear motion) 상황에서 추적의 강건성(robustness)을 향상시키는 데 중점을 둔다. 이를 위해 [[Observation-centric Re-Update (ORU)]]와 [[Observation-Centric Momentum (OCM)]]이라는 두 가지 주요 혁신 기법을 도입한다.
- **주요 성과**:
    - 기존 [[SORT]]의 "Simple, Online, Real-Time" 특성을 유지한다.
    - 단일 CPU에서 700+ FPS (초당 프레임 수) 이상의 빠른 속도로 동작한다. 
    - MOT17, MOT20, KITTI, DanceTrack 등 다양한 데이터셋에서 최첨단(state-of-the-art) 성능을 달성했으며, 특히 객체 움직임이 매우 비선형적인 DanceTrack에서 뛰어난 성능을 보인다.
    - MOT17에서 63.2 HOTA, MOT20에서 62.1 HOTA를 기록하여 기존 발표된 방법론들을 능가한다. [7]

---

## **🏗 아키텍처 개요**

OC-SORT는 기존 [[SORT]] 프레임워크를 기반으로 하며, 특히 폐색 기간 동안의 오차 처리 방식을 개선하는 관측 중심 메커니즘을 통합한다. [2, 6, 8]

### **0. 기호/차원**
- 일반적으로 [[Kalman Filter]]는 객체의 위치($x, y$), 크기($h, w$), 속도($v_x, v_y$) 등을 포함하는 상태 벡터($\mathbf{x}$)와 공분산 행렬($\mathbf{P}$)을 사용합니다.

### **1. 주요 파트 (관측 중심 메커니즘)**
OC-SORT는 전통적인 인코더/디코더 구조보다는 추적 파이프라인 내에서 [[Kalman Filter]]의 동작을 개선하는 데 초점을 맞춘다.

- **[[Observation-centric Re-Update (ORU)]]**
    - **구성**: 트랙이 손실된 후 재연관(re-association)될 때 활성화된다. [3, 6]
    - **특이 사항**: 과거 추정치 대신 가상 관측치(virtual observations)를 사용하여 오차 누적을 방지한다. 이 가상 관측치는 트랙이 손실되기 전 마지막으로 관측된 데이터와 트랙을 재활성화하는 최신 관측치를 앵커(anchor)로 사용하여 생성된 궤적에서 파생된다. [6]

- **[[Observation-Centric Momentum (OCM)]]**
    - **구성**: 연관성(association)을 위한 비용 행렬에 트랙의 방향 일관성(direction consistency)을 통합한다. [2, 6]
    - **특이 사항**: [[SORT]]에서 방향 추정의 높은 노이즈로 인해 방향 정보를 활용하기 어려웠던 문제를 관측 중심 방식으로 해결한다. [6]

- **[[Observation-Centric Recovery (OCR)]]**
    - **구성**: 주 트랙/탐지 연관 이후에 발생하는 IOU(Intersection Over Union) 기반의 보조 연관 단계이다. [3]
    - **특이 사항**: 손실된 트랙을 마지막으로 알려진 관측치를 사용하여 복구하는 휴리스틱 기법으로, 일시적인 폐색으로 인한 트랙 손실을 방지하는 데 도움을 준다. [3, 8]

### **3. 주요 수식 요약**
- 본 요약에 사용된 자료에서는 핵심 수식이 명시적으로 제공되지 않았습니다.

---

## **🎯 주요 구성 요소**

### **1. [[Observation-centric Re-Update (ORU)]]**
- **입력/출력 및 작동 원리**: 트랙이 손실되었다가 재활성화될 때, 과거의 추정치(estimations)를 더 정확한 관측치(observations) 기반의 데이터로 대체하여 누적된 오차를 줄인다. 이는 가상 궤적(virtual trajectory)을 생성하여 과거 시간 단계의 [[Kalman Filter]] 파라미터를 재업데이트하는 방식으로 이루어진다. [3, 6]
- **핵심 수식**: (제공되지 않음)

### **2. [[Observation-Centric Momentum (OCM)]]**
- **입력/출력 및 작동 원리**: 선형 운동 가정 하에서 객체의 움직임 방향 일관성(direction consistency)을 활용한다. 기존 [[SORT]]에서 방향 추정의 높은 노이즈로 인해 활용하기 어려웠던 이 정보를 관측 중심 방식으로 연관성 비용 행렬에 통합하여 추적의 강건성을 높인다. [2, 6]
- **핵심 수식**: (제공되지 않음)

### **3. [[Observation-Centric Recovery (OCR)]]**
- **입력/출력 및 작동 원리**: 주 연관성 단계 이후에 수행되는 휴리스틱 기법으로, 일치하지 않는 트랙과 관측치 간의 IOU 기반 연관을 통해 손실된 트랙을 복구한다. 이는 특히 단기 폐색(short-term occlusions) 및 정지 객체(stationary objects) 처리 능력을 향상시킨다. [3, 8]

---

## **⚖️ OC-SORT vs SORT**

| **비교 항목** | **OC-SORT** | **SORT** |
| :--- | :--- | :--- |
| **핵심 아이디어** | 관측 중심(Observation-Centric) [2, 4] | 추정 중심(Estimation-Centric) [2, 4] |
| **강점** | 폐색 및 비선형 움직임에 대한 강건성 향상 [1, 2, 6] | 단순성, 온라인, 실시간 처리 [1] |
| **제한 사항** | (SORT의 한계점 개선) | 상태 추정 노이즈에 민감, 오차 누적, 추정 중심적 [2, 5, 6] |
| **복잡도** | Simple, Online, Real-Time 유지, 단일 CPU 700+ FPS [1, 6, 8] | Simple, Online, Real-Time [1] |

- OC-SORT는 [[SORT]]의 기본적인 프레임워크를 유지하면서도, [[Kalman Filter]] 기반 추적의 고질적인 문제점인 폐색 시 오차 누적과 비선형 움직임에 대한 취약성을 관측 중심의 접근 방식으로 효과적으로 개선한다. 

---

## **🧠 추론/디코딩/생성 과정**
- **방식**: [[Kalman Filter]]를 이용한 객체 상태 예측과 헝가리안 알고리즘(Hungarian algorithm)을 통한 탐지(detections)와 트랙(tracks) 간의 데이터 연관(data association)을 기본으로 한다. [4] OC-SORT는 이 과정에 [[Observation-centric Re-Update (ORU)]], [[Observation-Centric Momentum (OCM)]], [[Observation-Centric Recovery (OCR)]] 메커니즘을 통합하여 추론 과정을 강화한다. [3, 6, 8]
- **특징**:
    - **ORU**: 트랙이 재활성화될 때 과거의 추정 오차를 수정하여 트랙의 정확도를 높인다. [3, 6]
    - **OCM**: 연관성 비용 계산 시 객체의 움직임 방향 일관성을 고려하여 비선형 움직임에 대한 강건성을 확보한다. [2, 6]
    - **OCR**: 일시적으로 손실된 트랙을 효과적으로 복구하여 ID 스위치(ID switches)를 줄인다. [3, 8]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - MOT17, MOT20 (Multi-Object Tracking) [1, 4, 7]
    - KITTI (Autonomous Driving) [1, 4]
    - DanceTrack (비선형 움직임이 강한 데이터셋) [1, 4]
    - Head tracking 데이터셋 [1, 4]
- **하드웨어**: 단일 CPU에서 700+ FPS (793 FPS)로 실행 가능. [1, 4, 6, 8]
- **학습 시간**: OC-SORT는 딥러닝 모델처럼 별도의 학습 과정을 거치지 않는 필터링 기반 방법론이며, 기성 탐지(off-the-shelf detections)를 입력으로 사용한다. [1]
- **옵티마이저**: 해당 없음.
- **규제(Regularization)**: 해당 없음.

---

## **⚠️ 한계**
- 기존 [[SORT]]의 세 가지 주요 한계점을 지적하고 개선한다: 상태 추정 노이즈에 대한 민감성, 시간 경과에 따른 오차 누적, 그리고 추정 중심적(estimation-centric)이라는 점.
- [[Kalman Filter]] 기반의 MOT 방법론들이 일반적으로 객체가 선형으로 움직인다는 가정을 한다는 점이 장기 폐색 시 부정확한 추정으로 이어질 수 있다.

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

| **모델** | **MOT17 HOTA** | **MOT20 HOTA** | **MOT20 IDF1** |
|---|---|---|---|
| 기존 SOTA (Published) | (OC-SORT 이전) | (OC-SORT 이전) | (OC-SORT 이전) |
| **OC-SORT** | **63.2** [7] | **62.1** (private detections) [7] | **67.0** (public detections) [8] |
| **OC-SORT (linear interpolation)** | - | **55.2** (public detections) [8] | **67.9** (public detections) [8] |

- OC-SORT는 MOT17 및 MOT20 벤치마크에서 기존 방법론들을 능가하는 최첨단 성능을 달성했다. [7, 8] 특히, 객체의 움직임이 매우 비선형적인 DanceTrack 데이터셋에서도 뛰어난 성능을 보여, 폐색 및 비선형 움직임에 대한 강건성을 입증했다. [1, 4]

---

## **🔮 향후 연구 방향**
- 본 요약에 사용된 자료에서는 논문의 "향후 연구 방향(Future Work)" 섹션에 대한 구체적인 내용이 명시적으로 제공되지 않았습니다. 그러나 OC-SORT가 기존 [[SORT]]의 한계를 재고하고 개선한 점을 고려할 때, 전통적인 필터링 기반 추적 방법론의 지속적인 개선 및 딥러닝 기반 방법론과의 통합 가능성 등이 있을 수 있습니다.

---

## 🔁 내 연구와의 매핑 (OC-SORT)

- 파이프라인 위치: **in-loop(association) + post(heuristic recovery)**
  - KF 예측 + Hungarian data association을 기본으로 하고, ORU/OCM/OCR을 **연관(association) 과정에 통합**함  [oai_citation:0‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
  - OCR은 “주 연관성 단계 이후” IOU 기반 복구 휴리스틱으로 **후처리(post 성격)** 가 강함  [oai_citation:1‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)

### State 대응

- location
  - **표현(Representation)**: KF 기반 객체 상태(추정/예측) + 관측치 기반 재업데이트
  - **핵심 메커니즘(ORU)**: 트랙이 손실→재활성화될 때, 과거의 추정치를 관측치 기반으로 대체(가상 궤적 생성 후 과거 KF 파라미터 재업데이트)  [oai_citation:2‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
  - **내 아이디어와의 대응**:
    - “out-of-view 동안 location belief 유지”에서 **belief 업데이트를 ‘관측 재주입’으로 안정화**하는 구현 레퍼런스로 사용 가능
    - 단, 이 노트 기준으로는 **분포(belief) 명시보다는 ‘관측으로 재고정’**에 가까움(uncertainty 설계는 별도 보강 필요)

- appearance
  - **사용 여부**: (이 노트 기준) **명시적 appearance/ReID 사용 언급 없음**
  - **내 아이디어와의 대응**:
    - 너의 object-state memory(appearance bank/prototype)와는 축이 다름 → “motion/observation-centric만으로 어디까지 버티는지”를 보는 **비교 기준(baseline/ablation 축)**로 적합  
    - 스포츠(유니폼 유사)처럼 appearance가 약할 때는 OC-SORT류 접근이 더 현실적일 수 있음

- semantic
  - **사용 여부**: (이 노트 기준) **명시적 semantic state 사용 언급 없음**
  - **내 아이디어와의 대응**:
    - semantic을 넣는다면 OC-SORT의 cost 항(OCM) 또는 recovery 단계(OCR)에 “soft prior”로 붙이는 형태가 자연스럽지만, 본 논문(노트) 자체의 핵심은 아님

- uncertainty
  - **표현 후보**: KF 공분산/게이팅/occlusion 시 업데이트 정책이 사실상 uncertainty 처리에 해당 가능(다만 노트에 상세 수식은 없음)
  - **내 아이디어와의 대응**:
    - 네가 목표로 하는 belief-state(분포) 관점에서는 “공분산 증가/감쇠, update freeze/decay” 규칙을 **명시적으로 추가 설계**해야 함
    - ORU는 “불확실성 누적”을 줄이기 위해 “관측으로 과거를 재정렬”하는 쪽에 가까움  [oai_citation:3‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)

### 키워드 연결(주축 1 + 부축 1)

- 주축: **out-of-view reactivation / long-gap 대응**
  - ORU가 “재활성화 시 과거 추정 오차 수정”을 명시  [oai_citation:4‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)
- 부축: **visibility-aware(occlusion robustness)**
  - 논문(노트)이 폐색(occlusion) 강건성을 핵심 목표로 둠  [oai_citation:5‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)  
- (참고) context gating은 “장면/관계”보다는 **모션 일관성(OCM) + IOU 복구(OCR)**로 후보를 조절하는 형태에 가까움  [oai_citation:6‡Observation-Centric SORT Rethinking SORT for Robust Multi-Object Tracking.md](sediment://file_000000007268720693a5383ae95a334b)

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
- [[Multi-Object Tracking]]
- [[Kalman Filter]]
- [[SORT]]
- [[Occlusion]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/pdf/2203.14360.pdf
- **코드**: https://github.com/noahcao/OC_SORT

---
