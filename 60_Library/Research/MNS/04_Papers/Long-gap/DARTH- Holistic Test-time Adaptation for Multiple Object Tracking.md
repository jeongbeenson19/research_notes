---
alias:
  - "DARTH: MOT를 위한 전체론적 테스트 시간 적응"
type: paper
tags:
  - DeepLearning
  - Paper
  - MultipleObjectTracking
  - TestTimeAdaptation
  - DomainAdaptation
  - Long-gap
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "DARTH: Holistic Test-time Adaptation for Multiple Object Tracking"
authors:
  - Mattia Segu
  - Bernt Schiele
  - Fisher Yu
year: 2023
venue: ICCV
paper_url: https://arxiv.org/abs/2310.01926
topics:
  - Multiple Object Tracking (MOT)
  - Test-time Adaptation (TTA)
  - Domain Shift
  - Self-supervised Learning
  - Object Detection
  - Instance Association
---

## **📄 DARTH: Holistic Test-time Adaptation for Multiple Object Tracking 개요**

- **발표 논문**: DARTH: Holistic Test-time Adaptation for Multiple Object Tracking by Mattia Segu et al. (ICCV 2023) [1, 8]
- **핵심 아이디어**: 기존 [[Multiple Object Tracking (MOT)]] 모델이 새로운 환경(domain shift)에 직면했을 때 성능 저하를 겪는 문제를 해결하기 위해, [[Test-time Adaptation (TTA)]] 프레임워크인 DARTH를 제안한다. 이 프레임워크는 추가적인 레이블링된 데이터 없이 추론 시점에 모델을 적응시킨다. 특히, 객체 탐지(object detection)를 위한 [[Detection Consistency Formulation]]과 인스턴스 외형 표현(instance appearance representations) 적응을 위한 새로운 [[Patch Contrastive Loss]]를 통해 MOT의 다양한 구성 요소를 전체론적으로(holistically) 적응시킨다. [1, 2, 3, 4]
- **주요 성과**:
    - Sim-to-real, outdoor-to-indoor, indoor-to-outdoor 등 다양한 도메인 변화(domain shifts)에서 기존 모델의 성능을 모든 지표에서 크게 향상시켰다. [2, 3, 4]
    - MOT의 도메인 변화 적응 문제에 대한 최초의 테스트 시간 적응 솔루션을 제공한다. [2, 3]
    - 레이블링된 데이터에 대한 의존도를 줄이면서도 기존 전이 학습(transfer learning)과 유사한 성능 향상을 달성한다. [1]

---

## **🏗 아키텍처 개요**

DARTH는 MOT의 다면적인 특성을 다루는 전체론적 테스트 시간 적응 프레임워크이다. 이는 객체 탐지 및 인스턴스 연관(instance association) 구성 요소를 모두 적응시킨다. [2, 3]

### **0. 기호/차원**
- $ \theta $: 학생 모델(student model)의 가중치 [3]
- $ \xi $: 교사 모델(teacher model)의 가중치 [3]
- $ \tau $: EMA(Exponential Moving Average) 업데이트의 모멘텀 [3]
- $ \phi_T, \phi_S, \phi_C $: 이미지 변환(image transformations) [3]

### **1. Detection Consistency Formulation**
- **구성**: DARTH는 객체 탐지를 자기 지도(self-supervised) 방식으로 적응시키기 위한 탐지 일관성 공식(detection consistency formulation)을 제안한다. [3, 4]
- **특이 사항**: 인접 프레임(adjacent frames)에서의 탐지 결과 일관성을 강화하고, 광도 변화(photometric changes)에 대한 강건성(robustness)을 확보한다. [3] 교사 모델은 학생 모델의 EMA로 업데이트되며, 이 교사 모델은 일관성 손실(consistency loss)을 위한 타겟을 제공한다. [3]

### **2. Patch Contrastive Loss**
- **구성**: 인스턴스 외형 표현을 적응시키기 위한 새로운 패치 대조 손실(patch contrastive loss)을 도입한다. [2, 3, 4]
- **특이 사항**: 더 나은 데이터 연관(data association)을 위해 판별적인 외형 표현(discriminative appearance representations) 학습을 가능하게 한다. [3]

### **3. 주요 수식 요약**
- **교사 모델 업데이트**:
  - $ \xi \leftarrow \tau\xi + (1 - \tau)\theta $ [3]

---

## **🎯 주요 구성 요소**

### **1. [[Detection Consistency Formulation]]**
- 입력/출력 및 작동 원리 설명: DARTH는 두 가지 다른 증강(augmented) 버전의 동일 이미지에서 교사 및 학생 탐지 출력 간의 탐지 일관성 손실을 통해 객체 탐지를 적응시킨다. 이는 광도 변화에 대한 강건성을 보장하고 인접 프레임에서 탐지 결과의 일관성을 강화한다. [3]
- $$ L_{DC} = \text{ConsistencyLoss}(\text{TeacherOutput}(\phi_T(I)), \text{StudentOutput}(\phi_S(I))) $$

### **2. [[Patch Contrastive Loss]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 시아미즈 학생(siamese student) 구조를 활용하여 동일 이미지의 두 가지 뷰(views)에서 탐지된 객체들 간의 패치 대조 손실 $L_{PCL}$을 통해 판별적인 외형 표현을 학습한다. 이는 데이터 연관(data association) 성능을 향상시킨다. [3]
- $$ L_{PCL} = \text{PatchContrastiveLoss}(\text{StudentEmbeddings}(\phi_S(I)), \text{StudentEmbeddings}(\phi_C(I))) $$

### **3. [[Momentum Teacher]]**
- EMA(Exponential Moving Average) 방식으로 학생 모델의 가중치를 사용하여 업데이트되는 교사 모델이다. 이 교사 모델은 탐지 일관성 손실을 위한 안정적인 타겟을 제공하여 학습 과정을 점진적으로 개선한다. [3]

---

## **⚖️ DARTH vs 기존 모델**

| **비교 항목** | **DARTH** | **기존 전이 학습 (Traditional Transfer Learning)** | **기존 MOT 적응 방법 (Existing MOT Adaptation Methods)** |
| :--- | :--- | :--- | :--- |
| **적응 시점** | 테스트 시간 (inference time) [1] | 학습 시간 (training time) [1] | 학습 시간 또는 사후 적응 (post-hoc adaptation) [1] |
| **레이블 데이터 요구** | 추가 레이블 데이터 불필요 [1] | 새로운 도메인에 대한 광범위한 레이블 데이터 필요 [1] | 특정 도메인에 대한 상당한 세분화된 인스턴스 주석 필요 [1] |
| **적응 범위** | MOT의 전체 구성 요소 (탐지 및 연관) [2, 3] | 주로 특징 분포 편향 [1] | 제한적, 주로 탐지 또는 연관 중 하나 [2] |
| **도메인 일반화** | 다양한 도메인 변화에 강건 [2, 3] | 제한적 [1] | 제한적 [1] |
| **복잡도** | 효율적인 적응 [1] | 시간 소모적, 비용 발생 [1] | 복잡하고 비효율적일 수 있음 [1] |

- DARTH는 기존 전이 학습 방식과 비교하여 고품질 레이블 데이터에 대한 의존도를 줄이면서도 유사한 성능 향상을 달성한다. [1] 또한, MOT의 도메인 적응 문제에 대한 최초의 테스트 시간 솔루션이라는 점에서 차별점을 가진다. [3] 기존의 객체 탐지만을 적응시키는 방법(예: SFOD)은 추적 관련 지표를 악화시킬 수 있지만, DARTH는 MOT 시스템의 모든 구성 요소를 향상시킨다. [2]

---

## **🧠 추론 과정**
- **방식**: DARTH로 적응된 모델은 객체를 탐지하고 인스턴스 임베딩(instance embeddings)을 추출한다. 이후, 표준 QDTrack 추론 전략을 적용하여 비디오 내 객체를 추적한다. [3]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - 운전 데이터셋: SHIFT, BDD100K [3]
    - 보행자 데이터셋: MOT17, DanceTrack [3]
- **하드웨어**: (정보 없음)
- **학습 시간**: (정보 없음)
- **옵티마이저**: (정보 없음)
- **규제(Regularization)**: (정보 없음)

---

## **⚠️ 한계**
- 제공된 검색 결과에서는 DARTH 모델 자체의 명시적인 한계점은 언급되지 않았다.

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

- DARTH는 sim-to-real, outdoor-to-indoor, indoor-to-outdoor를 포함한 다양한 도메인 변화에서 소스 모델 성능을 모든 지표에서 크게 향상시킨다. [2, 3, 4]
- 비지도 설정(unsupervised settings)에서, TTA 프레임워크는 탐지 정확도를 20.6% 향상시켰으며, 10,000개의 레이블링된 이미지를 사용한 전이 학습의 93.09% 정확도를 달성했다. [1]
- MOT17 모델을 BDD100K에 적응시킬 때, DARTH는 Oracle 모델과의 격차를 크게 줄였으며, MOTA는 Oracle 모델을 능가하기도 했다. [2]
- MOT17에서 DanceTrack으로의 변화에서, DARTH는 초기 연관 정확도(AssA)를 거의 두 배로 높였고, MOTA와 HOTA를 각각 +12.9 및 +10.1 증가시켜 Oracle 모델과의 격차를 상당히 좁혔다. [2]
- QDTrack 모델(Faster R-CNN with ResNet-50 backbone 기반)에 대한 성능 평가가 이루어졌다. [3]

---

## **🔮 향후 연구 방향**
- 제공된 검색 결과에서는 명시적인 향후 연구 방향은 언급되지 않았다.

---

## **🔗 관련 링크**
- [[Multiple Object Tracking]]
- [[Test-time Adaptation]]
- [[Domain Adaptation]]
- [[Self-supervised Learning]]
- [[Object Detection]]
- [[Instance Association]]

## **📌 참고 링크**
- **논문 원문**: [https://arxiv.org/abs/2310.01926](https://arxiv.org/abs/2310.01926) [1]
- **코드**: [https://github.com/darth-mot/darth-mot.github.io](https://github.com/darth-mot/darth-mot.github.io) [8]
- **프로젝트 페이지**: [https://www.vis.xyz/pub/darth](https://www.vis.xyz/pub/darth) [4]

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
