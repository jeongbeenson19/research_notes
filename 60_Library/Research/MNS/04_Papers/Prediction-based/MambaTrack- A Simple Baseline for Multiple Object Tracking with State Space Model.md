---
aliases: ["MambaTrack"]
type: paper
tags:
  - DeepLearning
  - Paper
  - MultipleObjectTracking
  - Mamba
  - StateSpaceModel
status: 🟧 Reading
rating: 0
date: 2026-02-04
title: "MambaTrack: A Simple Baseline for Multiple Object Tracking with State Space Model"
authors: ["Changcheng Xiao", "Qiong Cao", "Zhigang Luo", "Long Lan"]
year: 2024
venue: "ACM MM '24 (arXiv)"
paper_url: https://doi.org/10.1145/3664647.3680944
topics: ["Multiple Object Tracking (MOT)", "State Space Model (SSM)", "Mamba", "Motion Prediction", "Occlusion Handling", "Data Association"]
---

## **📄 MambaTrack: A Simple Baseline for Multiple Object Tracking with State Space Model 개요**

- **발표 논문**: MambaTrack: A Simple Baseline for Multiple Object Tracking with State Space Model (Changcheng Xiao, Qiong Cao, Zhigang Luo, Long Lan, ACM MM '24)
- **핵심 아이디어**:
    [[Multiple Object Tracking (MOT)]] 분야에서 기존 [[Kalman Filter]] 기반 방법론들이 선형 모션(linear motion)을 가정하여 복잡한 비선형 모션(nonlinear motion)에 취약하다는 한계점을 극복하고자 한다[1][2]. 이를 위해 [[State Space Model (SSM)]] 기반의 [[Mamba]]를 활용한 데이터 기반 모션 예측기(data-driven motion predictor)인 [[Mamba Motion Predictor (MTP)]]를 제안한다[1][2]. 또한, 실시간 환경에서 발생하는 객체 손실(missing observations) 및 궤적 단절(premature termination of trajectories) 문제를 해결하기 위해 [[Tracklet Patching Module (TPM)]]을 도입하여 일관된 궤적을 생성한다[3][1][4].
- **주요 성과**:
    - [[DanceTrack]] 및 [[SportsMOT]] 벤치마크에서 [[State-of-the-Art (SOTA)]] 성능을 달성했다[1].
    - 특히 [[DanceTrack]]에서 HOTA 점수를 OC_SORT 대비 2.2%p, IDF1 점수를 다음 최고 방법론 대비 3.2%p 높은 57.8을 기록하며 우수한 성능을 보였다[3].
    - 복잡한 비선형 모션 및 잦은 [[Occlusion]] 환경에서 강건한(robust) 추적 성능을 입증했다[3][1][4].

---

## **🏗 아키텍처 개요**

[[MambaTrack]]은 [[Mamba Motion Predictor (MTP)]]와 [[Tracklet Patching Module (TPM)]]으로 구성된 온라인 모션 기반 트래커(online motion-based tracker)이다[1][4].

### **0. 기호/차원**
- 바운딩 박스: $B = (x, y, w, h)$
- 시퀀스 길이: $N$

### **1. Mamba Motion Predictor (MTP)**
- **구성**:
    - Input Temporal Tokenization: 과거 바운딩 박스 정보($B_{t-N}, ..., B_{t-1}$)를 입력 토큰(input tokens)으로 변환한다[3].
    - Bi-Mamba Encoding Layer: 여러 개의 [[Bi-Mamba Block]]으로 구성되어 객체의 시간적 동역학(temporal dynamics)을 추출한다[3][4].
    - Prediction Head: 바운딩 박스 오프셋(offsets of bounding boxes)에 대한 회귀(regression)를 통해 다음 모션을 예측한다[3].
- **특이 사항**: [[Mamba]]의 단방향(unidirectional) 처리 한계를 극복하기 위해 양방향 정보 흐름을 가능하게 하는 [[Bi-Mamba Encoding Layer]]를 사용한다[3].

### **2. Tracklet Patching Module (TPM)**
- **구성**: [[MTP]]를 [[Auto-regressive]] 방식으로 활용하여 손실된 트랙렛(lost tracklets)의 움직임을 예측하고 보상한다[1][4].
- **세부 구성 요소**: [[MTP]]의 예측 결과를 다음 시점의 입력으로 사용하여 손실된 트랙렛의 모션을 지속적으로 예측한다[1][4].

### **3. 주요 수식 요약**
- **MTP 예측**:
  - $B_{t} = MTP(B_{t-N}, ..., B_{t-1})$
- **TPM 자기회귀**:
  - $P_{t} = MTP(P_{t-N}, ..., P_{t-1})$ (손실된 트랙렛의 예측)

---

## **🎯 주요 구성 요소**

### **1. [[Mamba Motion Predictor (MTP)]]**
- 입력/출력 및 작동 원리 설명: 객체의 시공간적 위치 동역학(spatial-temporal location dynamics)을 입력으로 받아 [[Bi-Mamba Encoding Layer]]를 통해 복잡한 모션 패턴을 학습하고 다음 시점의 모션을 예측한다[4].
- $$B_{t} = f_{MTP}(B_{t-N}, ..., B_{t-1})$$

### **2. [[Tracklet Patching Module (TPM)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: [[Occlusion]]이나 검출기 실패(detector failure)로 인해 발생한 관측치 손실(missing observations)을 보상하기 위해 [[MTP]]를 자기회귀(auto-regressive) 방식으로 사용하여 일관된 궤적(consistent trajectories)을 생성한다[1][4]. 이 모듈은 손실된 트랙렛의 예측을 통해 궤적의 연속성을 유지하는 데 기여한다[1][4].

---

## **⚖️ MambaTrack vs 기존 모델**

| **비교 항목** | **MambaTrack** | **Kalman Filter 기반 (예: ByteTrack)** |
| :--- | :--- | :--- |
| **모션 모델링** | [[State Space Model (SSM)]] 기반 [[Mamba]]를 사용하여 복잡한 비선형 모션(nonlinear motion)을 효과적으로 모델링[1][2]. | 선형 모션(linear motion)을 가정하여 비선형 모션에 취약[2]. |
| **Occlusion 처리** | [[Tracklet Patching Module (TPM)]]을 통해 손실된 관측치를 자기회귀 방식으로 보상하여 궤적 일관성 유지[1][4]. | 관측치 손실에 취약하며 궤적 단절 발생 가능성 높음. |
| **복잡도** | [[Mamba]]의 선형 시간 복잡도(linear-time complexity)를 활용하여 효율적인 추론 및 학습 가능[1]. | 일반적으로 낮은 계산 복잡도를 가지나, 복잡한 시나리오에서 정확도 저하. |

- [[MambaTrack]]은 기존 [[Kalman Filter]] 기반의 [[MOT]] 방법론들이 가지는 비선형 모션 모델링 및 [[Occlusion]] 처리의 한계를 극복하며, 특히 [[DanceTrack]] 및 [[SportsMOT]]와 같이 복잡하고 역동적인 환경에서 우수한 성능을 보인다[3][1][2][4].

---

## **🧠 추론/디코딩/생성 과정**
- **방식**: 온라인(online) 추적 방식[4].
- **특징**:
    1.  [[MTP]]를 사용하여 활성 트랙렛(active tracklets)의 다음 프레임 바운딩 박스($\hat{B}_t$)를 예측한다[3].
    2.  예측된 바운딩 박스와 현재 프레임의 검출 결과($B_t$)를 [[Intersection-over-Union (IoU)]] 유사도 기반으로 매칭한다[3].
    3.  [[TPM]]이 손실된 트랙렛($P$)의 바운딩 박스를 자기회귀 방식으로 예측하고, 이를 나머지 검출 결과($B_u$)와 페어링한다[3].
    4.  이러한 매칭 결과를 결합하여 최종 추적 결과($T$)를 도출한다[3].

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - [[DanceTrack]] (복잡한 댄스 시나리오)[1]
    - [[SportsMOT]] (다양하고 빠른 스포츠 시나리오)[1]
- **하드웨어**: (논문 본문 확인 필요)
- **학습 시간**: (논문 본문 확인 필요)
- **옵티마이저**: (논문 본문 확인 필요)
- **규제(Regularization)**: (논문 본문 확인 필요)

---

## **⚠️ 한계**
- (논문 본문 확인 필요. 일반적으로 모션 기반 트래커는 외형 정보(appearance information)를 활용하는 트래커에 비해 객체 간 유사성이 높은 경우에 취약할 수 있다.)

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**HOTA**|**IDF1**|**AssA**|
|---|---|---|---|
| OC_SORT (DanceTrack) | (수치) | (수치) | (수치) |
| **MambaTrack (DanceTrack)** | **OC_SORT 대비 2.2%p 높음** | **57.8 (다음 최고 대비 3.2%p 높음)** | (수치) |
| ByteTrack (SportsMOT) | (수치) | (수치) | (수치) |
| **MambaTrack (SportsMOT)** | **ByteTrack 대비 약 10%p 높음** | **향상** | **향상** |

- [[MambaTrack]]은 [[DanceTrack]] 및 [[SportsMOT]] 벤치마크에서 기존 [[State-of-the-Art]] 방법론들을 능가하는 성능을 보여주며, 특히 복잡한 모션 패턴과 잦은 [[Occlusion]] 상황에서 궤적 일관성 유지 및 손실된 트랙렛 재확립 능력에서 강점을 보인다[3].

---

## **🔮 향후 연구 방향**
- (논문 본문 확인 필요. 현재 검색 결과에서는 명시적인 향후 연구 방향은 없음.)

---

## **🔗 관련 링크**
- [[Multiple Object Tracking]]
- [[State Space Model]]
- [[Mamba]]
- [[Kalman Filter]]
- [[Occlusion]]

## **📌 참고 링크**
- **논문 원문**: https://doi.org/10.1145/3664647.3680944
- **코드**: (만약 공개되었다면 URL)

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics[0]) AND file.name != this.file.name
SORT year desc
```
