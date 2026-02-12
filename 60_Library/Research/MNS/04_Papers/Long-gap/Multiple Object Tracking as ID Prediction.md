---
aliases:
  - MOTIP
type: paper
tags:
  - DeepLearning
  - Paper
  - Long-gap
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: Multiple Object Tracking as ID Prediction
authors:
  - Ruopeng Gao
  - Yijun Zhang
  - Limin Wang
year: 2025
venue: CVPR
paper_url: https://arxiv.org/abs/2403.16848
topics:
  - Multiple Object Tracking
  - ID Prediction
  - Computer Vision
  - Deep Learning
Keyword:
comment:
---

## **📄 Multiple Object Tracking as ID Prediction 개요**

- **발표 논문**: Multiple Object Tracking as ID Prediction by Ruopeng Gao, Yijun Zhang, Limin Wang (CVPR 2025)
- **핵심 아이디어**:
    기존의 다중 객체 추적 (MOT, Multiple Object Tracking) 방법론들이 수작업으로 설계된 휴리스틱(handcrafted heuristics)에 의존하여 궤적 유지 및 비용 행렬 계산을 수행하는 한계를 극복하고자 한다. 이 논문은 MOT를 In-context ID Prediction 문제로 재정의하여, 객체 탐지(object detection)와 연관(association)을 분리하고, 객체 연관을 End-to-end 학습 가능한 태스크로 전환하는 새로운 관점을 제안한다. 이는 현재 탐지된 객체에 대해 ID Decoder와 Learnable ID Dictionary를 활용하여 직접 ID 레이블을 디코딩함으로써, 보지 못한 궤적(unseen trajectories)에도 일반화될 수 있도록 한다.
- **주요 성과**:
    - MOT를 [[In-context ID Prediction]]으로 단순화하여 [[End-to-end]] 학습을 가능하게 함[1][2].
    - 기존 휴리스틱 기반 방법론의 유연성 및 최적 추적 능력 학습의 한계를 해결[1].
    - 객체 수준 특징(object-level features)과 학습 가능한 ID 딕셔너리를 사용하여 현재 탐지된 객체의 ID 레이블을 직접 디코딩함으로써, 보지 못한 궤적에 대한 일반화(generalization)를 보장[1].

---

## **🏗 아키텍처 개요**

[[MOTIP]] 모델은 [[DETR]] 기반의 탐지기(detector), 학습 가능한 ID 딕셔너리(learnable ID dictionary), 그리고 ID 디코더(ID Decoder)의 세 가지 주요 구성 요소로 이루어져 있다[1].

### **0. 기호/차원**
- $T$: 시퀀스 길이 또는 시간 스텝
- $t$: 현재 프레임
- $T_{t-T:t-1}$: 과거 궤적 (historical trajectories)
- $D_t$: 현재 프레임 $t$에서의 탐지(detections)
- $ID_{labels}$: ID 레이블
- $ID_{embeddings}$: ID 임베딩

### **1. DETR 탐지기 (DETR Detector)**
- **구성**: [[DETR]] (DEtection TRansformer) 기반의 객체 탐지기로, 비디오 스트림 내에서 객체를 정확하게 찾아내는 역할을 한다[1][5].
- **특이 사항**: COCO 데이터셋으로 사전 학습된 가중치를 사용하여 초기화되며, 해당 데이터셋에서 탐지 사전 학습(detection pre-training)을 수행한다[5].

### **2. 학습 가능한 ID 딕셔너리 (Learnable ID Dictionary)**
- **구성**: 서로 다른 객체 ID를 나타내는 학습 가능한 임베딩(embeddings) 집합[1].
- **역할**: 각 궤적을 클래스로 취급하고, 전체 학습 과정 동안 일관된 고유 ID 레이블을 할당한다[5].

### **3. ID 디코더 (ID Decoder)**
- **구성**: 표준 [[Transformer Decoder]]를 사용한다[1].
- **역할**: 객체 특징(object features)과 해당 ID 임베딩(ID embeddings)을 결합하여 과거 궤적($T_{t-T:t-1}$)을 형성한다[1]. 이후 ID 토큰(ID tokens)을 [[Identity Prompts]]로 간주하고, 이를 기반으로 [[In-context ID Prediction]]을 수행하여 현재 객체의 ID 레이블을 예측한다[1].
- **특이 사항**: 가변 길이의 과거 트랙렛(variable-length historical tracklets)을 처리하며, 선형 분류 헤드(linear classification head)를 통해 ID 레이블을 예측한다[1].

### **4. 주요 수식 요약**
- 논문 스니펫에서는 구체적인 수식이 제공되지 않음.

---

## **🎯 주요 구성 요소**

### **1. In-context ID Prediction**
- 입력/출력 및 작동 원리 설명: [[MOTIP]]의 핵심 메커니즘으로, 과거 궤적 정보($T_{t-T:t-1}$)를 컨텍스트로 활용하여 현재 프레임의 탐지된 객체에 대한 ID 레이블을 예측한다[1]. ID 디코더는 ID 토큰을 프롬프트로 사용하여 이 예측을 수행한다[1].
- $$ID_{predicted} = Decoder(Features_{current}, ID_{prompts})$$ (개념적 수식)

### **2. ID Decoder (Transformer Decoder)**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 표준 [[Transformer Decoder]]를 사용하여 가변 길이의 과거 트랙렛을 처리하고, 선형 분류 헤드를 통해 ID 레이블을 예측한다[1]. 훈련 시에는 [[DETR]] 구성 요소의 순차적 포워드 패스(sequential forward passes)를 병렬화하여 효율성을 높인다[5].

### **3. ID 충돌 해결 (Duplicate ID Handling)**
- 동일한 프레임 내에서 중복 ID가 발생하는 경우, 가장 높은 신뢰도(confidence)를 가진 객체를 선택하고 나머지는 새로운 객체(newborn objects)로 레이블링하는 규칙을 적용하여 ID 충돌을 방지한다[5].

---

## **⚖️ MOTIP vs 기존 모델**

| **비교 항목** | **MOTIP (제안 모델)** | **기존 주류 MOT 방법론** |
| :--- | :--- | :--- |
| **ID 연관 방식** | [[In-context ID Prediction]] (End-to-end 학습)[1][2] | 수작업 휴리스틱(handcrafted heuristics) 기반[1][4] |
| **궤적 유지** | ID 디코더를 통한 직접 ID 디코딩[1] | 복잡한 휴리스틱 기법[4] |
| **비용 행렬 계산** | 필요 없음 (직접 ID 예측)[1] | 수작업으로 설계된 비용 행렬[1] |
| **일반화 능력** | 보지 못한 궤적에 대한 일반화 보장[1] | 도메인별 데이터에 대한 최적 추적 능력 학습에 제한[1] |
| **복잡도** | $O(N \cdot L)$ (N: 객체 수, L: 궤적 길이, Transformer 기반) | $O(N^2)$ 또는 그 이상 (매칭 알고리즘에 따라 다름) |

- [[MOTIP]]는 기존의 수작업 휴리스틱에 의존하는 [[MOT]] 방법론의 한계를 극복하고, [[End-to-end]] 학습을 통해 객체 연관(object association)을 수행함으로써 더 유연하고 일반화된 추적 능력을 제공한다[1].

---

## **🧠 추론/디코딩/생성 과정**
- **방식**: [[In-context ID Prediction]][1].
- **특징**: ID 디코더가 ID 토큰을 [[Identity Prompts]]로 사용하여 현재 탐지된 객체의 ID 레이블을 직접 예측한다[1]. 중복 ID 발생 시, 가장 높은 신뢰도를 가진 객체를 유지하고 나머지는 새로운 객체로 처리하는 규칙을 적용한다[5].

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - DanceTrack[5]
    - SportsMOT[5]
    - BFT[5]
- **하드웨어**: 8개의 NVIDIA RTX 4090 GPU[5]
- **학습 시간**:
    - DanceTrack: 10 에포크 (5, 9 에포크에서 학습률 10배 감소)[5]
    - SportsMOT: 13 에포크 (8, 12 에포크에서 학습률 10배 감소)[5]
    - BFT: 22 에포크 (16, 20 에포크에서 학습률 감소)[5]
- **옵티마이저**: (구체적인 옵티마이저 이름 및 파라미터는 스니펫에 명시되지 않음)
- **규제(Regularization)**: (구체적인 규제 기법은 스니펫에 명시되지 않음)
- **기타**: COCO 데이터셋으로 사전 학습된 가중치를 사용하여 [[DETR]] 부분 초기화 및 해당 데이터셋에서 탐지 사전 학습 수행[5]. 각 GPU의 배치 크기는 1로 설정[5]. 훈련 데이터의 다양성을 높이기 위해 1에서 4 사이의 무작위 샘플링 간격(random sampling intervals)을 사용한다[5].

---

## **⚠️ 한계**
- 논문 스니펫에서는 [[MOTIP]] 자체의 구체적인 한계점이 명시적으로 언급되지 않았다. 다만, 기존 [[MOT]] 방법론의 일반적인 문제점(객체 가려짐, 흐림, 높은 유사성 등)은 언급되어 있다[6].

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**
- 논문 스니펫에서는 DanceTrack, SportsMOT, BFT 데이터셋에서 훈련되었다고 언급되지만[5], 구체적인 성능 지표(예: MOTA, IDF1 등) 및 수치는 제공되지 않는다.

---

## **🔮 향후 연구 방향**
- 논문 스니펫에서는 향후 연구 방향에 대한 구체적인 내용은 언급되지 않음.

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
## **🔗 관련 링크**
- [[Multiple Object Tracking]]
- [[DETR]]
- [[Transformer]]

## **📌 참고 링크**
- **논문 원문**: [https://arxiv.org/abs/2403.16848](https://arxiv.org/abs/2403.16848)[4]
- **코드**: [https://github.com/MCG-NJU/MOTIP](https://github.com/MCG-NJU/MOTIP)[2]

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE year, Keyword, comment
FROM #Long-gap
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
