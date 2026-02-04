---
alias:
  - TrackFlow
type: paper
tags:
  - DeepLearning
  - Paper
  - Long-gap
  - OTnContext
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "TrackFlow: Multi-Object Tracking with Normalizing Flows"
authors:
  - Gianluca Mancusi
  - Aniello Panariello
  - Angelo Porrello
  - Matteo Fabbri
  - Simone Calderara
  - Rita Cucchiara
year: 2023
venue: ICCV
paper_url: https://arxiv.org/abs/2308.11513
topics:
  - Multi-Object Tracking
  - Normalizing Flows
  - Probabilistic Fusion
  - Computer Vision
---

## **📄 TrackFlow: Multi-Object Tracking with Normalizing Flows 개요**

- **발표 논문**: TrackFlow: Multi-Object Tracking with Normalizing Flows, Gianluca Mancusi, Aniello Panariello, Angelo Porrello, Matteo Fabbri, Simone Calderara, Rita Cucchiara, ICCV 2023[1][2]
- **핵심 아이디어**:
    [[TrackFlow]]는 [[정규화 흐름 (Normalizing Flows)]]을 사용하여 [[다중 객체 추적 (Multi-Object Tracking, MOT)]]에서 연관 비용(association costs)을 학습하는 확률론적 프레임워크를 제안한다[3][4][1]. 기존의 휴리스틱 기반 또는 규칙 기반의 다중 모달(multi-modal) 정보 융합 방식의 한계를 극복하기 위해, 조건부 밀도 추정(conditional density estimation)을 통해 연관 비용을 우도(likelihood)로 모델링한다[3][5][1]. 이는 다양한 지각적 단서(시각적 외형, 모션 패턴, 3D 공간 위치 등) 간의 상호 의존성을 고려하여, 특정 장면에 적응하고 미묘한 비용 상호작용을 포착한다[3][4][1].
- **주요 성과**:
    - 기존 [[추적-탐지 (tracking-by-detection)]] 알고리즘의 성능을 일관되게 향상시킨다[5][1].
    - MOTSynth, MOT17, MOT20 데이터셋에서 HOTA 및 IDF1 지표에서 상당한 성능 향상을 보인다[6].
    - 특히, 정확한 3D 거리 정보가 통합될 때 성능 향상이 두드러지며, 합성 데이터(MOTSynth)로만 학습했음에도 실제 데이터셋(MOT17, MOT20)에서 만족스러운 결과를 달성한다[4][6].

---

## **🏗 아키텍처 개요**

[모델의 전체적인 구조 설명]

### **0. 기호/차원**
- $D_t$: 현재 프레임 $t$에서의 탐지(detections) 집합
- $T_{t-1}$: 이전 프레임 $t-1$에서의 트랙(tracks) 집합
- $c_{i,j}$: $i$-번째 탐지 $D_t^i$와 $j$-번째 트랙 $T_{t-1}^j$ 간의 연관 비용
- $\mu, \sigma^2$: 보행자의 예상 거리(expected distance) 및 불확실성(uncertainty)[4]

### **1. TrackFlow (Deep Density Estimator)**
- **구성**: [[정규화 흐름 (Normalizing Flows)]] 모델을 활용한 심층 밀도 추정기(deep density estimator)[4].
- **역할**: 다양한 입력 비용/변위(input costs/displacements)를 단일 출력 메트릭(metric)으로 요약하여 올바른 연관(correct association)의 확률을 나타낸다[4].
- **특이 사항**: 조건부 결합 확률 분포(conditional joint probability distribution)를 모델링하도록 훈련되어, 비용 간의 의존성을 내재적으로 설명하고 장면별 융합을 가능하게 한다[5][1].

### **2. DistSynth (Distance Estimator)**
- **구성**: 단안 이미지(monocular image)에서 인스턴스별 거리(per-instance distance)를 추정하기 위해 개발된 심층 신경 회귀기(deep neural regressor)[4].
- **역할**: 시간적 정보(temporal information)와 공간적 표현(spatial representations)을 통합하여 예측 신뢰도를 높인다[4].
- **특이 사항**: ConvLSTM과 FPN(Feature Pyramid Network) 브랜치를 통해 시간적 패턴을 추출하고 지역적 세부 사항을 보존한다[4].

### **3. 주요 수식 요약**
- **연관 비용**:
  - $c_{i,j}$는 $i$-번째 탐지가 $j$-번째 트랙에 속할 확률의 음의 로그 우도(negative log-likelihood)로 간주된다[5].
  - $c_{i,j} = -\log P(\text{detection } i \text{ belongs to track } j | \text{features})$ (논문에서 구체적인 수식 확인 필요)

---

## **🎯 주요 구성 요소**

### **1. [[정규화 흐름 (Normalizing Flows)]]**
- **입력/출력 및 작동 원리 설명**: TrackFlow의 핵심으로, 복잡한 분포를 간단한 분포로 변환하는 일련의 가역 변환(invertible transformations)을 학습하여 밀도 추정을 수행한다. 이를 통해 다중 모달 입력(2D 모션, 외형, 3D 정보 등)의 조건부 확률 분포를 모델링하고, 탐지-트랙 연관의 우도를 계산한다[3][4][5].
- $$P(x) = P(z) \left| \det \left( \frac{\partial f^{-1}}{\partial x} \right) \right|$$ (일반적인 정규화 흐름 수식, 논문에서 사용된 특정 형태 확인 필요)

### **2. [[DistSynth]]**
- **병렬 처리, 분할, 혹은 특수 기능 설명**: 단안 카메라 이미지에서 각 객체(pedestrian)의 3D 거리를 추정하는 모듈이다. ConvLSTM을 사용하여 시간적 정보를 통합하고, FPN을 통해 다양한 스케일의 특징을 활용하여 거리 추정의 정확도를 높인다[4].
- **설정 값 (논문 기준)**: (논문에서 구체적인 설정 값 확인 필요)

### **3. [[헝가리안 알고리즘 (Hungarian Algorithm)]]**
- **설명**: TrackFlow에서 계산된 연관 비용 행렬(cost matrix)을 사용하여 최적의 탐지-트랙 매칭을 수행하는 데 사용된다[4]. 비용 행렬은 소프트맥스 스무딩(softmax smoothing)을 거쳐 정규화된 후 헝가리안 알고리즘에 입력된다[4].

---

## **⚖️ TrackFlow vs 기존 모델**

| **비교 항목** | **TrackFlow** | **기존 휴리스틱/규칙 기반** |
| :--- | :--- | :--- |
| **비용 융합 방식** | 조건부 밀도 추정 기반 확률론적 융합[3][5] | 단순 규칙 또는 복잡한 휴리스틱[5] |
| **비용 독립성 가정** | 비용 간의 상호 의존성 고려[5][1] | 비용이 독립적이라고 가정 (현실과 다름)[5] |
| **하이퍼파라미터 튜닝** | 수동 튜닝 불필요 (데이터 기반 학습)[5] | 홀드아웃 세트(hold-out set)에 대한 신중한 튜닝 필요[5] |
| **복잡도** | $O(\dots)$ (논문에서 구체적인 복잡도 확인 필요) | $O(\dots)$ (논문에서 구체적인 복잡도 확인 필요) |

- [[TrackFlow]]는 기존 방식들이 가지는 비용 독립성 가정의 문제점과 수동 하이퍼파라미터 튜닝의 필요성을 해결하며, 데이터 기반으로 장면별 융합을 가능하게 하여 더 견고하고 정확한 추적 성능을 제공한다[5][1].

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: (논문에서 구체적인 추론 과정 확인 필요)
- **특징**: (논문에서 구체적인 특징 확인 필요)

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - MOTSynth (합성 데이터셋)[4][6]
    - MOT17, MOT20 (실제 데이터셋)[4][6]
- **하드웨어**: (논문에서 구체적인 하드웨어 사양 확인 필요)
- **학습 시간**: (논문에서 구체적인 학습 시간 확인 필요)
- **옵티마이저**: (논문에서 구체적인 옵티마이저 및 파라미터 확인 필요)
- **규제(Regularization)**:
    - (논문에서 구체적인 규제 기법 확인 필요)

---

## **⚠️ 한계**
- (논문에서 언급하거나 구조적으로 가지는 한계점 확인 필요)

---

## **📊 주요 실험 결과**

### **[메인 태스크 성능]**

|**모델**|**HOTA**|**IDF1**|
|---|---|---|
| SORT (Baseline) | (수치) | (수치) |
| ByteTrack (Baseline) | (수치) | (수치) |
| OC-SORT (Baseline) | (수치) | (수치) |
| **TrackFlow (GT) + SORT** | **5.49 (향상)** | **9.62 (향상)**[6] |
| **TrackFlow (Estimated) + SORT** | **0.54 (향상)** | **1.22 (향상)**[6] |

- [[TrackFlow]]는 [[SORT]], [[ByteTrack]], [[OC-SORT]]와 같은 기존 추적-탐지 알고리즘에 통합될 때 일관된 성능 향상을 보여준다[6]. 특히, Ground-Truth (GT) 거리를 사용할 때 HOTA 및 IDF1 지표에서 상당한 개선을 이루며, DistSynth로 추정된 거리를 사용하더라도 성능 향상이 관찰된다[6].

---

## **🔮 향후 연구 방향**
- (논문의 Future Work 섹션 요약 확인 필요)
- (확장 가능성 확인 필요)

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Normalizing Flows]]
- [[Tracking-by-Detection]]
- [[DistSynth]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2308.11402
- **코드**: (논문 또는 관련 자료에서 코드 링크 확인 필요)

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```

```