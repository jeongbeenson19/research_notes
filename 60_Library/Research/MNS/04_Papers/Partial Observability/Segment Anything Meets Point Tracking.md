---
alias:
  - SAM-PT
  - Segment Anything Meets Point Tracking
type: paper
tags:
  - DeepLearning
  - Paper
  - VideoSegmentation
  - ZeroShot
  - PartialObservability
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: Segment Anything Meets Point Tracking
authors:
  - Frano Rajič
  - Lei Ke
  - Yu-Wing Tai
  - Chi-Keung Tang
  - Martin Danelljan
  - Fisher Yu
year: 2023
venue: arXiv
paper_url: https://arxiv.org/abs/2307.01197
topics:
  - Video Segmentation
  - Zero-shot Learning
  - Point Tracking
  - Foundation Models
  - SAM
---

## **📄 Segment Anything Meets Point Tracking 개요**

- **발표 논문**: Segment Anything Meets Point Tracking (SAM-PT) by Frano Rajič et al., arXiv 2023.[1][2][3]
- **핵심 아이디어**:
    [[Segment Anything Model]](SAM)의 강력한 제로샷(zero-shot) 이미지 분할 능력을 활용하여 비디오 분할(video segmentation)로 확장하는 새로운 방법론인 [[SAM-PT]]를 제안한다.[1][2][4][3] 기존 비디오 분할 방법론들이 마스크 주석(mask annotation) 및 전파(propagation)에 초점을 맞추는 것과 달리, SAM-PT는 **점 중심(point-centric)**의 상호작용 비디오 분할을 위해 [[장기 점 추적(long-term point tracking)]]을 활용한다.[1][2][5][4][3] 이는 객체 의미론(object semantics)에 구애받지 않고 지역 구조 정보(local structure information)를 활용하기 위해 점 전파(point propagation)를 사용하는 독특한 접근 방식이다.[1][2][4]
- **주요 성과**:
    - Davis, YouTube-VOS, BDD100K와 같은 인기 있는 비디오 객체 분할(Video Object Segmentation) 및 다중 객체 분할 추적(Multi-Object Segmentation Tracking) 벤치마크에서 기존 SOTA(State-of-the-Art) 방법론들과 비교하여 더 나은 제로샷 성능과 효율적인 상호작용을 제공한다.[1][2][4]
    - 특히, 비디오 분할 데이터에 대한 훈련 없이도 강력한 제로샷 성능을 달성한다.[6][2][7][8]
    - UVO(Unidentified Video Objects) 벤치마크에서 점 기반 추적의 장점을 입증했다.[1][2][4]

---

## **🏗 아키텍처 개요**

[[SAM-PT]]는 [[Segment Anything Model]](SAM)의 기능을 동적 비디오에서 추적 및 분할하도록 확장하며, 주로 네 가지 단계로 구성된다.[1][6][5][7]

### **0. 기호/차원**
- $P$: 쿼리 포인트(Query Points) 집합
- $M$: 분할 마스크(Segmentation Mask)
- $T$: 비디오 프레임 수
- $h$: 예측 재초기화(reinitialization) 주기 (예: $h=8$ 프레임)[7]

### **1. 쿼리 포인트 선택 (Query Points Selection)**
- **구성**: 첫 번째 비디오 프레임에서 대상 객체(positive points) 또는 비대상 세그먼트(negative points)를 나타내는 쿼리 포인트를 선택한다.[1][6][5][7]
- **각 층**:
    1. **[[랜덤 샘플링 (Random Sampling)]]**: 그라운드 트루스 마스크(ground truth mask)에서 무작위로 쿼리 포인트를 선택한다.[1][5][7]
    2. **[[K-Medoids 샘플링 (K-Medoids Sampling)]]**: K-Medoids 클러스터링의 중심을 쿼리 포인트로 사용하여 객체의 다양한 부분을 잘 커버하고 노이즈 및 이상치에 강건하게 만든다.[1][5][7][4]
    3. **[[Shi-Tomasi 샘플링 (Shi-Tomasi Sampling)]]**: 마스크 아래 이미지에서 Shi-Tomasi 코너 포인트를 추출한다.[1][5][7]
    4. **[[혼합 샘플링 (Mixed Sampling)]]**: 위 기술들을 결합한 하이브리드 방식이다.[1][5][7]
- **특이 사항**: K-Medoids 샘플링이 가장 좋은 결과를 보였다.[7]

### **2. 점 추적 (Point Tracking)**
- **구성**: 선택된 쿼리 포인트를 사용하여 [[점 추적기(point tracker)]]를 통해 비디오의 모든 프레임에 걸쳐 포인트를 전파한다.[1][6][5][7]
- **각 층**:
    1. **[[PIPS]]**: 장기 추적 문제(long-term tracking challenges)에 대한 견고성 때문에 PIPS [11]와 같은 최신 점 추적기를 사용한다.[7]
- **특이 사항**: 예측된 궤적(trajectories)과 폐색 점수(occlusion scores)를 생성한다.[1][5][7]

### **3. 분할 (Segmentation)**
- **구성**: 전파된 궤적에서 폐색되지 않은(non-occluded) 포인트를 [[SAM]]에 프롬프트(prompt)로 제공하여 각 비디오 프레임에 대한 분할 마스크를 생성한다.[1][6][5][7]
- **특이 사항**: SAM은 초기 패스에서 양성 포인트(positive points)로 프롬프트되고, 두 번째 패스에서는 양성 및 음성 포인트(negative points)와 이전 마스크 예측을 사용하여 마스크를 정제한다.[9][7][4]

### **4. 점 추적 재초기화 (Point Tracking Reinitialization)**
- **구성**: 선택적으로, 예측된 마스크를 사용하여 쿼리 포인트를 재초기화하고 프로세스를 다시 시작한다.[1][6][5][7]
- **특이 사항**: 예측 주기 $h$에 도달하면 재초기화를 수행하여 신뢰할 수 없는 포인트를 제거하고 새로 보이는 객체 부분의 포인트를 추가하여 추적 정확도를 향상시킨다.[7][4]

---

## **🎯 주요 구성 요소**

### **1. [[쿼리 포인트 샘플링 (Query Point Sampling)]]**
- 입력/출력 및 작동 원리 설명: 첫 번째 프레임에서 객체를 나타내는 점들을 선택하는 과정. 랜덤, K-Medoids, Shi-Tomasi, 혼합 샘플링 방식이 있다. K-Medoids는 객체의 넓은 영역을 커버하는 데 효과적이다.[1][5][7][4]
- $$P_{query} = \text{SamplePoints}(M_{GT})$$

### **2. [[장기 점 추적 (Long-term Point Tracking)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 선택된 쿼리 포인트를 비디오의 모든 프레임에 걸쳐 추적하여 궤적($P_{trajectory}$)과 폐색 점수($S_{occlusion}$)를 생성한다. PIPS와 같은 견고한 추적기를 활용한다.[1][5][7]
- 설정 값 (논문 기준): PIPS [11] 사용.[7]

### **3. [[SAM 프롬프팅 및 마스크 정제 (SAM Prompting and Mask Refinement)]]**
- [[SAM]]은 폐색되지 않은 추적된 점들을 프롬프트로 받아 각 프레임의 분할 마스크를 생성한다.[1][7] 초기 마스크 생성 후, 양성 및 음성 포인트를 활용한 반복적인 마스크 디코딩 패스(mask decoding passes)를 통해 마스크를 정제한다.[9][7][4] 음성 포인트는 배경 및 인접 객체로부터 잘못 분할된 영역을 제거하는 데 도움을 준다.[7]

---

## **⚖️ [SAM-PT] vs [기존 모델]**

| **비교 항목** | **[SAM-PT]** | **[기존 마스크 전파 방식]** |
| :--- | :--- | :--- |
| **전파 기술** | 희소 점 전파 (Sparse Point Propagation) | 밀집 객체 마스크 전파 (Dense Object Mask Propagation) |
| **훈련 데이터** | 비디오 분할 데이터 불필요 (Zero-shot) | 비디오 분할 데이터 필요 |
| **객체 표현** | 압축된 점 표현 (Compact Point Representation) | 마스크 기반 표현 |
| **일반화 능력** | 높은 제로샷 일반화 (High Zero-shot Generalization) | 도메인 외 데이터에 성능 저하 가능 |
| **SAM 호환성** | 본질적으로 호환 (Naturally Compatible) | SAM과 직접적인 호환성 낮음 |
| **복잡도** | $O(\text{points} \times \text{frames})$ (추정) | $O(\text{pixels} \times \text{frames})$ (추정) |

- [[SAM-PT]]는 기존의 객체 중심 마스크 전파 전략과 달리, 객체 의미론에 독립적인 지역 구조 정보를 활용하는 점 전파를 사용한다.[1][2][7][4] 이는 제로샷 일반화 능력, 압축된 객체 표현, 그리고 [[SAM]]과의 자연스러운 호환성 측면에서 장점을 가진다.[2][7]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 점 중심(point-centric)의 제로샷 비디오 분할.[1][2][5]
- **특징**:
    - 첫 프레임에서 쿼리 포인트를 선택한다.[1][6][5][7]
    - 이 점들을 비디오 전체 프레임에 걸쳐 추적한다.[1][6][5][7]
    - 추적된 점들을 [[SAM]]에 프롬프트로 제공하여 각 프레임의 분할 마스크를 생성한다.[1][6][5][7]
    - 필요에 따라 예측된 마스크에서 새로운 쿼리 포인트를 샘플링하여 재초기화한다.[1][6][5][7]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - [[SAM-PT]]는 비디오 분할 데이터에 대한 훈련을 요구하지 않는다.[6][2][7][8]
    - 평가는 Davis 2016, Davis 2017, YouTube-VOS 2018, BDD100K, MOSE 2023, UVO 벤치마크에서 수행되었다.[1][2][7][4]
- **하드웨어**: (정보 없음)
- **학습 시간**: (정보 없음)
- **옵티마이저**: (정보 없음)
- **규제(Regularization)**: (정보 없음)

---

## **⚠️ 한계**
- 비디오 분할 훈련 데이터를 활용하는 기존 SOTA 방법론들에 비해 성능 격차가 존재한다.[9][7]
- 제안된 방법론이 다소 복잡하고 발견적(heuristic)일 수 있다.[9]

---

## **📊 주요 실험 결과**

### **메인 태스크 성능 (제로샷 비디오 객체 분할)**

| **모델** | **J&F (DAVIS 2016)** | **J&F (DAVIS 2017)** | **J&F (YouTube-VOS)** |
|---|---|---|---|
| SegGPT | 82.3 | 75.6 | - |
| **SAM-PT (ours)** | **83.1** | **76.6** | **-** |
| XMem | - | 87.7 | - |
| DeAOT | - | 86.2 | - |

- [[SAM-PT]]는 비디오 분할 훈련 데이터를 사용하지 않는 방법론들 중에서 Davis 2016 및 2017 검증 세트에서 가장 높은 J&F 점수를 달성했다.[7]
- UVO 벤치마크에서도 점 기반 추적의 효과를 입증했다.[1][2][4]

---

## **🔮 향후 연구 방향**
- [[SAM-PT]]의 잠재력은 비디오 객체 분할을 넘어 [[비디오 인스턴스 분할 (Video Instance Segmentation, VIS)]]과 같은 다른 작업으로 확장될 수 있다.[6][7]
- 더 발전된 점 추적기(point trackers)의 통합을 통해 [[SAM-PT]]의 성능을 더욱 향상시킬 수 있다.[8]

---

## **🔗 관련 링크**
- [[Segment Anything Model]]
- [[Video Object Segmentation]]
- [[Point Tracking]]
- [[Zero-shot Learning]]

## **📌 참고 링크**
- **논문 원문**: [https://arxiv.org/abs/2307.01197](https://arxiv.org/abs/2307.01197)[1][6][10][3]
- **코드**: [https://github.com/SysCV/sam-pt](https://github.com/SysCV/sam-pt)[1][4]

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
