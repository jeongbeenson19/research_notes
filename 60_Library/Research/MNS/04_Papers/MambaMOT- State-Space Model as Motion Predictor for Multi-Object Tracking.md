---
alias: ["MambaMOT"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟧 Reading
rating: 0
date: 2026-02-04
title: "MambaMOT: State-Space Model as Motion Predictor for Multi-Object Tracking"
authors: ["Hsiang-Wei Huang et al."]
year: 2025
venue: "ICASSP 2025"
paper_url: "https://arxiv.org/abs/2403.10826"
topics: ["Multi-Object Tracking", "State-Space Models", "Motion Prediction", "Deep Learning"]
---

## **📄 MambaMOT: State-Space Model as Motion Predictor for Multi-Object Tracking 개요**

- **발표 논문**: MambaMOT: State-Space Model as Motion Predictor for Multi-Object Tracking (Hsiang-Wei Huang et al., ICASSP 2025)[1][2]
- **핵심 아이디어**:
기존 [[Multi-Object Tracking (MOT)]] 방법론들이 [[Kalman Filter]]를 이용한 선형 모션 예측에 의존하여 복잡하고 비선형적인 움직임 및 잦은 [[Occlusion (오클루전)]]이 발생하는 환경(예: 스포츠, 댄스)에서 한계를 보이는 문제를 해결한다[3][1][4]. 이 논문은 [[Kalman Filter]]를 학습 기반의 모션 모델로 대체하여 추적 정확도와 적응성을 향상시키는 가능성을 탐구한다[5][4]. 특히, [[State-Space Model (SSM)]]인 [[Mamba]]를 활용하여 트랙릿(tracklet)의 모션 예측을 수행하는 [[MambaMOT]]를 제안하며, 트랙토리(trajectory) 특징을 추출하여 추적 성능을 더욱 향상시키는 [[MambaMOT+]]를 소개한다[3][5].
- **주요 성과**:
    - DanceTrack 및 SportsMOT와 같은 도전적인 MOT 데이터셋에서 기존 방법론보다 향상된 성능을 달성했다[3][1][4].
    - 복잡하고 비선형적인 모션 패턴과 잦은 오클루전을 기존 방법보다 효과적으로 처리한다[3][1][4].
    - 다양한 추적 평가 지표에서 상당한 성능 향상을 보이며, 여러 공개 벤치마크에서 최신 기술(state-of-the-art)과 견줄만한 성능을 달성했다[5].
    - MambaMOT+는 HOTA 56.1, DetA 80.8, AssA 39.0, IDF1 54.9, MOTA 90.3을 기록했다[5].

---

## **🏗 아키텍처 개요**

[[MambaMOT+]] 아키텍처는 동일한 트랙에서 얻은 바운딩 박스(bounding box) 시퀀스를 선형 투영 레이어(linear projection layer)를 통해 처리하여 모션 모델링을 수행한다[3]. 모델은 예측(predictions)과 임베딩(embeddings)을 생성하며, 각 시간 프레임에서 은닉 상태($h_T$)를 업데이트한다[3]. 이러한 예측은 트랙 감지 및 매칭에 사용되며, 트랙토리 임베딩은 트랙릿 병합에 도움을 준다[3]. [[Mamba]] 블록의 상세 구조는 이 프레임워크의 핵심적인 부분이다[3].

### **0. 기호/차원**
- $h_T$: 특정 시간 $T$에서의 은닉 상태 (hidden state)[3]
- $\mathcal{L}_{\text{pred}}=\mathcal{L}_{\text{giou}}+\mathcal{L}_{\text{mse}}$: 예측 손실 함수 (prediction loss function)[5]

### **1. 주요 파트 1 (예: 모션 예측기)**
- **구성**: [[Mamba]] 기반의 모션 모델인 [[Mamba Motion Predictor (MTP)]]는 객체의 시공간적 위치 역학(spatial-temporal location dynamics)을 입력으로 받는다[6][7].
- 각 층:
    1. **[[Bi-Mamba Encoding Layer]]**: 모션 패턴을 포착하는 데 사용된다[6][7].
- **특이 사항**: MTP는 다음 모션을 예측하며, 오클루전이나 모션 블러로 인해 관측값이 누락될 경우 자체 예측을 입력으로 사용하여 누락된 관측값을 보상하는 자기회귀(autoregressive) 방식으로 적용될 수 있다[6][7].

### **2. 주요 파트 2 (예: 트랙릿 병합)**
- **구성**: [[MambaMOT+]]는 [[State-Space Model]]의 능력을 활용하여 트랙토리 특징(trajectory features)을 추출하고, 유사한 트랙토리 특징을 가진 트랙릿들을 연결하여 추적 성능을 향상시킨다[3][5].

### **3. 주요 수식 요약**
- **예측 손실**:
  - $\mathcal{L}_{\text{pred}}=\mathcal{L}_{\text{giou}}+\mathcal{L}_{\text{mse}}$[5]

---

## **🎯 주요 구성 요소**

### **1. [[State-Space Model (SSM)]] (Mamba)**
- 입력/출력 및 작동 원리 설명: [[Mamba]]는 긴 시퀀스 모델링에서 거의 선형적인 복잡도(near-linear complexity)를 가지는 [[State-Space Model]]로, 트랙릿 모션 예측을 위해 뛰어난 컨텍스트 추론(context reasoning) 능력을 활용한다[5].
- $$h_t = A h_{t-1} + B x_t$$
  $$y_t = C h_t + D x_t$$
  (일반적인 SSM 수식, 논문에서 구체적인 Mamba 수식은 제시되지 않음)

### **2. [[Mamba Motion Predictor (MTP)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: MTP는 댄서나 운동선수와 같이 복잡한 모션 패턴을 모델링하도록 설계되었다[6][7]. 객체의 시공간적 위치 역학을 입력으로 받아 [[Bi-Mamba Encoding Layer]]를 사용하여 모션 패턴을 포착하고 다음 모션을 예측한다[6][7].

### **3. [[Trajectory Embeddings]]**
- [[MambaMOT+]]에서 생성되는 임베딩으로, 유사한 트랙릿들을 병합하여 추적 성능을 높이는 데 사용된다[3].

---

## **⚖️ MambaMOT vs 기존 모델**

| **비교 항목** | **MambaMOT / MambaMOT+** | **Kalman filter-based (e.g., ByteTrack)** | **Learning-based (e.g., OC-SORT)** |
| :--- | :--- | :--- | :--- |
| **모션 모델** | [[State-Space Model]] (Mamba)[5] | [[Kalman Filter]][5][4] | 다양함 (예: Transformer)[5] |
| **복잡한 모션 처리** | 우수 (비선형 모션, 오클루전)[3][1][4] | 한계 (선형 모션 가정)[3][1][4] | 모델에 따라 다름 |
| **성능 (HOTA)** | **56.1 (MambaMOT+)**[5] | 54.6 (OC-SORT)[5] | 52.9 (MotionTrack)[5] |
| **데이터셋 적응성** | 각 데이터셋의 모션 패턴에 더 잘 적응[5] | 선형 모션에 최적화[4] | 모델에 따라 다름 |

- [[MambaMOT]]는 [[ByteTrack]]에서 제안된 데이터 연관(data-association) 방법인 BYTE를 통합하지만, [[Kalman Filter]] 대신 [[Mamba]]를 모션 모델로 사용한다[5]. 이는 학습 기반 모션 모델이 [[Kalman Filter]]보다 더 나은 모션 모델링을 수행할 수 있음을 보여준다[5].

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 온라인 및 실시간(online and real-time) MOT 접근 방식[5].
- **특징**: [[MambaMOT+]]는 각 시간 프레임에서 은닉 상태($h_T$)를 업데이트하며 예측과 임베딩을 생성한다[3]. 예측은 트랙 감지 및 매칭에, 트랙토리 임베딩은 트랙릿 병합에 활용된다[3].

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - [[DanceTrack]] (복잡한 모션과 오클루션이 특징)[3][1][4]
    - [[SportsMOT]] (다양하고 불규칙한 모션이 특징)[3][1][4]
- **하드웨어**: (정보 없음)
- **학습 시간**: (정보 없음)
- **옵티마이저**: (정보 없음)
- **규제(Regularization)**: (정보 없음)

---

## **⚠️ 한계**
- 논문 자체의 명시적인 한계점은 검색 결과에서 직접적으로 언급되지 않았지만, 이 연구는 기존 [[Kalman Filter]] 기반 MOT 방법론의 한계점(복잡하고 비선형적인 모션, 잦은 오클루션 처리의 어려움)을 극복하는 데 초점을 맞추고 있다[3][1][4].

---

## **📊 주요 실험 결과**

### **[메인 태스크 성능]**

|**모델**|**HOTA**|**DetA**|**AssA**|**IDF1**|**MOTA**|
|---|---|---|---|---|---|
| OC-SORT[5] | 54.6 | 80.4 | 40.2 | 54.6 | 89.6 |
| MotionTrack[5] | 52.9 | 80.9 | 34.7 | 53.8 | 91.3 |
| **MambaMOT**[5] | **55.5** | **80.8** | **38.3** | **53.9** | **90.1** |
| **MambaMOT+**[5] | **56.1** | **80.8** | **39.0** | **54.9** | **90.3** |

---

## **🔮 향후 연구 방향**
- (검색 결과에서 명시적인 향후 연구 방향은 언급되지 않음)

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[State-Space Model]]
- [[Mamba]]
- [[Kalman Filter]]
- [[DanceTrack]]
- [[SportsMOT]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2403.10826[1]
- **코드**: (정보 없음, GitHub 저장소는 TrackSSM이라는 다른 프로젝트와 관련되어 있을 수 있음)[8]

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
