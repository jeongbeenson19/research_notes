---
alias: ["TCOW"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟧 Reading
rating: 0
date: 2023-05-04
title: "Tracking Through Containers and Occluders in the Wild"
authors: ["Basile Van Hoorick", "Pavel Tokmakov", "Simon Stent", "Jie Li", "Carl Vondrick"]
year: 2023
venue: "CVPR"
paper_url: "https://arxiv.org/abs/2305.03052"
topics: ["Object Tracking", "Occlusion", "Containment", "Object Permanence", "Video Segmentation", "Computer Vision"]
---

## **📄 Tracking Through Containers and Occluders in the Wild 개요**

- **발표 논문**: Tracking Through Containers and Occluders in the Wild (Basile Van Hoorick 외, CVPR 2023)[1][2]
- **핵심 아이디어**:
기존 객체 추적(object tracking) 모델들은 객체가 가려지거나(occlusion) 다른 객체 안에 있을 때(containment) 추적에 어려움을 겪는다. 본 논문은 **TCOW** (Tracking through Containers and Occluders in the Wild)라는 모델을 제안하여, 객체가 시야에서 사라져도 존재한다는 [[객체 영속성 (Object Permanence)]] 개념을 기반으로 비디오 내 객체를 분할(segmentation)하고 추적한다[3]. TCOW는 추적 대상 객체뿐만 아니라, 객체를 가리는 [[가림막 (Occluder)]] 또는 객체를 담는 [[컨테이너 (Container)]]를 명시적으로 마스킹(masking)하도록 학습된다[3]. 이를 위해 Kubric 시뮬레이터를 활용하여 가림 및 포함 이벤트에 대한 정확한 레이블이 있는 합성 데이터셋을 생성한다[3].
- **주요 성과**:
    - 가림 및 포함 상황에서의 시각적 추적을 위한 새로운 벤치마크와 모델인 TCOW를 제안하였다[1][2].
    - 합성 데이터셋과 실제 데이터셋의 혼합을 통해 지도 학습(supervised learning) 및 모델 성능 평가를 지원한다[1][2].
    - 합성 데이터로만 훈련되었음에도 불구하고, 실제 환경에서 간단한 가림 및 포함 사례에 대해 우수한 일반화 성능을 보인다[4].
    - 복잡한 도메인 적응(domain adaptation) 기술 없이도 시뮬레이션에서 실제 환경으로 직접 전이(sim-to-real transfer)가 가능하다[3].
    - Kubric Random 합성 테스트 세트에서 대상 객체에 대해 53.0%의 Jaccard 지수를 달성하여, 기존 AOT(41.3%)를 크게 능가한다[5].

---

## **🏗 아키텍처 개요**

TCOW 모델은 비디오의 시작 부분에서 대상 객체에 대한 포인터(query)가 주어지면, 이후 모든 프레임에 대해 세 가지 마스크를 생성한다[3].

### **0. 기호/차원**
- $\hat{m}_t \in \mathbb{R}^{T \times H \times W}$: 추적되는 대상 객체 인스턴스 마스크[6]
- $\hat{m}_o \in \mathbb{R}^{T \times H \times W}$: 대상 객체의 가장 앞쪽 가림막(occluder) 마스크 (존재할 경우)[6]
- $\hat{m}_c \in \mathbb{R}^{T \times H \times W}$: 대상 객체의 가장 바깥쪽 컨테이너(container) 마스크 (존재할 경우)[6]
- $T$: 비디오 프레임 수
- $H$: 비디오 높이
- $W$: 비디오 너비

### **1. 비디오 트랜스포머 모델 (Video Transformer Model)**
- **구성**: 비디오 트랜스포머(video transformer) 모델을 기반으로 한다[3].
- **특이 사항**: 주어진 비디오 클립의 모든 프레임에 대해 대상, 가림막, 컨테이너의 세 가지 마스크를 생성한다[3].

---

## **🎯 주요 구성 요소**

### **1. [[객체 영속성 (Object Permanence)]] 모델링**
- 입력/출력 및 작동 원리 설명: 모델은 객체가 시야에서 사라져도 존재한다는 개념을 학습하여, 대상 객체, 가림막, 컨테이너를 동시에 분할한다[3].
- $L_{BCE}$: 출력 채널 $\hat{m}$과 해당 그라운드 트루스 $m$ 사이의 이진 교차 엔트로피(binary cross-entropy) 목적 함수를 사용한다[4].

### **2. [[Kubric 시뮬레이터]] 기반 합성 데이터 생성**
- 병렬 처리, 분할, 혹은 특수 기능 설명: Kubric 시뮬레이터를 활용하여 가림 및 포함 이벤트에 대한 정확한 레이블을 가진 포토리얼리스틱(photorealistic) 합성 훈련 세트를 생성한다[3].
- 설정 값 (논문 기준):
    - Kubric Random 데이터셋은 4,000개의 비디오로 구성되며, 각 비디오는 36프레임, 공간 해상도는 $480 \times 360$이다[4].
    - RGB 정보, 깊이 맵(depth maps) 등을 포함한다[4].
    - X-ray 분할 마스크 $m_a$를 생성하여 모든 인스턴스의 픽셀을 가림 여부와 관계없이 노출시킨다[4].

---

## **⚖️ TCOW vs 기존 모델**

| **비교 항목** | **TCOW** | **AOT (Baseline)** |
| :--- | :--- | :--- |
| **핵심 아이디어** | 객체 영속성 기반, 대상/가림막/컨테이너 마스크 동시 예측[3] | 일반적인 비디오 객체 분할[5] |
| **Kubric Random (Jaccard Index)** | 대상: 53.0%, 가림막: 70.5%, 컨테이너: 71.6%[5] | 대상: 41.3%, 가림막: 5.1%, 컨테이너: 4.9%[5] |
| **실제 환경 일반화** | 합성 데이터로 훈련 후 실제 환경에서 간단한 가림/포함 사례에 대해 우수한 성능[4] | 실제 환경에서 성능 저하[5] |

- TCOW는 Kubric Random 합성 테스트 세트에서 대상 객체, 가림막, 컨테이너 분할 모두에서 AOT 베이스라인을 크게 능가한다[5]. 이는 TCOW의 특화된 트랜스포머 아키텍처가 복잡한 상호작용을 효과적으로 학습함을 시사한다[5]. 그러나 실제 환경 데이터셋에서는 성능 격차가 여전히 존재한다[5].

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 비디오 트랜스포머 모델을 통해 주어진 비디오 클립의 모든 프레임에 대해 대상, 가림막, 컨테이너의 세 가지 마스크를 생성한다[3].
- **특징**: 대상 객체가 비디오의 첫 프레임에서 쿼리(query)로 주어지면, 모델은 이후 프레임에서 해당 객체를 추적하며 마스크를 예측한다[3].

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - Kubric Random: 4,000개의 비디오, 각 36프레임, $480 \times 360$ 해상도, RGB 정보 및 깊이 맵 포함[4].
    - 훈련 시, 첫 프레임에서 보이는 모든 인스턴스에 대해 난이도 점수를 할당하고, 추적하기 어려운 대상 객체에 우선순위를 두어 쿼리를 샘플링한다[4].
- **하드웨어**: NVIDIA RTX A6000 GPU를 사용하였다[4].
- **학습 시간**: (정보 없음)
- **옵티마이저**: (정보 없음)
- **규제(Regularization)**:
    - 훈련 중 다양한 데이터 증강(augmentation) 기법을 적용한다: 무작위 색상 지터링(hue, saturation, brightness), 무작위 그레이스케일(grayscale), 무작위 비디오 반전(reversal), 무작위 팔린드롬(palindromes), 무작위 수평 뒤집기(horizontal flipping), 무작위 크롭(cropping)[4].

---

## **⚠️ 한계**
- [[객체 영속성 (Object Permanence)]]의 고급 사례에서는 여전히 실패가 발생한다[4].
- 주요 실패 사례: 동일한 컨테이너가 섞이는 경우, 중첩된 포함(nested containment), 시각적으로 매우 유사한 가림막과 가려지는 객체[4].
- 실제 환경의 시각적 사실성(visual realism)과 복잡성은 여전히 상당한 도전 과제를 제시하며, [[Sim2Real Gap]]이 존재한다[5].
- 진정한 객체 영속성을 획득했다고 주장하기에는 여전히 상당한 성능 격차가 남아있다[1][2].

---

## **📊 주요 실험 결과**

### **메인 태스크 성능 (Jaccard Index)**

|**모델**|**대상 객체**|**가림막**|**컨테이너**|
|---|---|---|---|
| AOT (Baseline) | 41.3% | 5.1% | 4.9% |
| **TCOW (Kubric Random)** | **53.0%** | **70.5%** | **71.6%** |
| TCOW (Rubric Office) | 69.4% | 30.1% | 11.7% |
| TCOW (Rubric Cup Games) | 38.3% | (정보 없음) | (정보 없음) |
| TCOW (Rubric DAV/YTB) | 52.8% | (정보 없음) | (정보 없음) |

---

## **🔮 향후 연구 방향**
- 동일한 컨테이너가 섞이는 경우, 중첩된 포함, 시각적으로 유사한 가림막과 가려지는 객체와 같은 현재 모델의 한계점을 해결하는 연구가 필요하다[4].
- 실제 환경에서의 객체 영속성 과제를 위한 [[Sim2Real Gap]]을 줄이는 노력이 필요하다[5].

---

## **🔗 관련 링크**
- [[객체 영속성 (Object Permanence)]]
- [[비디오 객체 분할 (Video Object Segmentation)]]
- [[트랜스포머 (Transformer)]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2305.03052[1]
- **코드**: https://github.com/basilevh/tcow[4]

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics[0]) AND file.name != this.file.name
SORT year desc
```

```