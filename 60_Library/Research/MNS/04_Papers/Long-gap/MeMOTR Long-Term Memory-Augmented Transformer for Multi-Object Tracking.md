---
alias:
  - MeMOTR
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
  - Transformer
  - MemoryAugmented
  - Long-gap
  - PartialObservability
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "MeMOTR: Long-Term Memory-Augmented Transformer for Multi-Object Tracking"
authors:
  - Ruopeng Gao
  - Limin Wang
year: 2023
venue: ICCV
paper_url: https://arxiv.org/abs/2307.15700
topics:
  - Multi-Object Tracking
  - Transformer
  - Long-Term Memory
  - Deep Learning
  - Computer Vision
---

## **📄 MeMOTR: Long-Term Memory-Augmented Transformer for Multi-Object Tracking 개요**

- **발표 논문**: MeMOTR: Long-Term Memory-Augmented Transformer for Multi-Object Tracking (Ruopeng Gao, Limin Wang), ICCV 2023[1]
- **핵심 아이디어**:
기존 다중 객체 추적(Multi-Object Tracking, MOT) 방법론들이 인접 프레임 간의 객체 특징만을 활용하여 장기적인 시간 정보를 모델링하는 데 한계가 있다는 문제점을 해결하기 위해 [[MeMOTR]]을 제안한다.[2][3][4] 이 모델은 장기 기억(long-term memory)을 활용하여 동일 객체의 트랙 임베딩(track embedding)을 더욱 안정적이고 구별 가능하게 만들며, 맞춤형 메모리-어텐션 레이어(customized memory-attention layer)를 통해 장기 기억 주입(long-term memory injection)을 수행한다.[2][3][4] 또한, 탐지 디코더(Detection Decoder)와 결합 디코더(Joint Decoder)를 분리하여 탐지 쿼리(detect query)와 트랙 쿼리(track query) 간의 의미론적 불일치(semantic misalignment) 문제를 완화하고, 적응형 통합(adaptive aggregation) 전략을 통해 인접 프레임의 객체 특징을 융합하여 추적 견고성(tracking robustness)을 향상시킨다.[3][5][6]
- **주요 성과**:
    - DanceTrack 데이터셋에서 기존 SOTA(State-of-the-Art) 방법론 대비 HOTA 지표 7.9%, AssA 지표 13.0% 향상을 달성했다.[2][3][4][6]
    - MOT17 데이터셋에서 다른 [[Transformer]] 기반 방법론들보다 연관성(association) 성능이 우수함을 입증했다.[2][3]
    - BDD100K 데이터셋에서도 우수한 일반화 성능(generalization performance)을 보였다.[2][3]

---

## **🏗 아키텍처 개요**

[[MeMOTR]]은 [[ResNet-50]] 백본과 [[Transformer]] 인코더를 사용하여 입력 이미지 $I^t$의 2D 표현을 학습한다. 학습 가능한 탐지 쿼리 $Q_{det}$는 탐지 디코더($\mathcal{D}_{det}$)에 입력되어 현재 프레임의 탐지 임베딩 $E_{det}^t$를 생성한다. 이후 $E_{det}^t$와 이전 프레임의 트랙 임베딩 $E_{tck}^t$를 결합 디코더($\mathcal{D}_{joint}$)에 쿼리하여 출력 $\hat{O}_{det}^t$와 $\hat{O}_{tck}^t$를 생성한다. 마지막으로, 장기 기억 $M_{tck}^t$와 인접 프레임의 출력 $O_{tck}^t$, $O_{tck}^{t-1}$을 [[Temporal Interaction Module]]에 입력하여 다음 트랙 임베딩 $E_{tck}^{t+1}$ 및 장기 기억 $M_{tck}^{t+1}$을 업데이트한다.[3]

### **0. 기호/차원**
- $I^t$: 입력 프레임[3]
- $Q_{det}$: 학습 가능한 탐지 쿼리[3]
- $\mathcal{D}_{det}$: 탐지 디코더[3]
- $E_{det}^t$: 현재 프레임의 탐지 임베딩[3]
- $E_{tck}^t$: 이전 프레임의 트랙 임베딩[3]
- $\mathcal{D}_{joint}$: 결합 디코더[3]
- $\hat{O}_{det}^t$: 탐지 디코더 출력 (신규 객체)[3]
- $\hat{O}_{tck}^t$: 트랙 디코더 출력 (추적 객체)[3]
- $O_{tck}^t$: 현재 프레임의 객체 출력 (신규 + 추적 객체 병합)[3]
- $M_{tck}^t$: 장기 기억[3]
- $c_i^t$: $i$-번째 객체의 예측 분류 신뢰도[3]
- $b_i^t$: $i$-번째 객체의 예측 바운딩 박스[3]
- $\lambda$: 기억 업데이트 비율 (실험적으로 0.01로 설정)[3]
- $W_{tck}^t$: 채널별 가중치[3]
- $\tau_{det}, \tau_{tck}, \tau_{next}$: 신뢰도 임계값 (0.5로 설정)[3]
- $\mathcal{T}_{miss}$: 객체 손실 후 제거까지의 프레임 수 (DanceTrack: 30, MOT17: 15, BDD100K: 10)[3]

### **1. [[분리된 탐지 디코더]]**
- **구성**: 기존 [[Transformer]] 디코더를 두 부분으로 분리하며, 첫 번째 디코더 레이어는 탐지에 사용된다.[3]
- **특이 사항**: 학습 가능한 탐지 쿼리 $Q_{det}$를 입력으로 받아 의미론적 정보가 충분한 탐지 임베딩 $E_{det}^t$를 생성한다. 이는 기존 방법론에서 탐지 쿼리와 트랙 쿼리 간의 의미론적 불일치 문제를 해결한다.[3][5]

### **2. [[결합 디코더]]**
- **구성**: 나머지 5개 레이어는 결합 탐지 및 추적에 사용된다.[3]
- **특이 사항**: 탐지 임베딩 $E_{det}^t$와 트랙 임베딩 $E_{tck}^t$를 연결하여 입력으로 받는다.[3]

### **3. 주요 수식 요약**
- **장기 기억 업데이트**:
  - $M_{tck}^{t+1} = (1 - \lambda) \cdot M_{tck}^t + \lambda \cdot O_{tck}^t$[3]
- **채널별 가중치 생성**:
  - $W_{tck}^t = \mathrm{Sigmoid}(\mathrm{MLP}(O_{tck}^t))$[3]
- **트랙 임베딩 및 장기 기억 업데이트 조건**:
  - $[E_i^{t+1}, M_i^{t+1}] = \begin{cases} [\tilde{E}_i^{t+1}, \tilde{M}_i^{t+1}], & c_i^t > \tau_{next} \\ [E_i^t, M_i^t], & c_i^t \le \tau_{next} \end{cases}$[3]

---

## **🎯 주요 구성 요소**

### **1. [[장기 기억]] (Long-Term Memory)**
- 입력/출력 및 작동 원리 설명: 기존 방법론과 달리 장기적인 시간 정보를 유지하기 위해 명시적으로 도입된다. 신규 객체가 탐지되면 현재 출력으로 장기 기억을 초기화하며, 객체의 의미론적 특징이 짧은 시간 동안 미미하게 변한다는 가정하에 지수 가중 이동 평균(exponentially decaying weights)을 사용하여 부드럽게 업데이트된다.[3][6]
- $$M_{tck}^{t+1} = (1 - \lambda) \cdot M_{tck}^t + \lambda \cdot O_{tck}^t$$[3]

### **2. [[Temporal Interaction Module]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명:
    - **적응형 통합 (Adaptive Aggregation)**: 블러링(blurring)이나 가려짐(occlusion)과 같은 문제 해결을 위해 다중 프레임 특징을 활용한다. 현재 프레임의 출력 $O_{tck}^t$가 신뢰할 수 없을 수 있으므로, 채널별 가중치 $W_{tck}^t$를 생성하여 현재 출력에 곱하고 이전 프레임의 출력 $O_{tck}^{t-1}$과 연결한 후 MLP를 통해 융합한다.[3][6]
    - **메모리-어텐션 레이어 (Memory-Attention Layer)**: 유사한 객체가 많은 프레임에서 더 구별 가능한 표현을 학습하기 위해 Multi-Head Attention 구조를 사용한다. 장기 기억 $M_{tck}^t$를 Key로, 통합된 출력 $\hat{O}_{tck}^t$를 Query로, 현재 출력 $O_{tck}^t$를 Value로 사용하여 상호작용한다.[3][5][6]
- 설정 값 (논문 기준): 기억 업데이트 비율 $\lambda = 0.01$.[3]

### **3. [[분리된 탐지 디코더]] (Separated Detection Decoder)**
- 설명: 기존 [[Transformer]] 기반 MOT 방법론에서 탐지 쿼리와 트랙 쿼리 간의 의미론적 불일치 문제를 해결하기 위해 도입된다. 학습 가능한 탐지 쿼리 $Q_{det}$를 먼저 처리하여 충분한 의미론적 정보를 가진 탐지 임베딩 $E_{det}^t$를 생성한 후, 이를 트랙 임베딩과 함께 결합 디코더에 입력한다.[3][5][6]

---

## **⚖️ [[MeMOTR]] vs 기존 모델**

| **비교 항목** | **[[MeMOTR]]** | **[[MOTR]]** | **[[ByteTrack]]** |
| :--- | :--- | :--- | :--- |
| **핵심 아이디어** | 장기 기억 증강 [[Transformer]] | End-to-end [[Transformer]] | Robust Detector (YOLOX) + Low-confidence detections 재활용 |
| **장기 시간 정보** | 명시적 활용 (장기 기억) | 인접 프레임 정보 위주 | 인접 프레임 정보 위주 |
| **탐지/추적 쿼리** | 분리된 디코더로 정렬 | 단일 디코더에서 공동 처리 | Tracking-by-detection (별도) |
| **DanceTrack HOTA** | **68.5**[3] | 54.2[3] | 47.7[3] |
| **DanceTrack AssA** | **58.4**[3] | 40.2[3] | 32.1[3] |
| **복잡도** | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ |

- [[MeMOTR]]은 장기 기억과 [[Temporal Interaction Module]]을 통해 복잡한 움직임과 유사한 외형을 가진 객체들의 연관성(association) 문제를 효과적으로 해결한다. 특히 DanceTrack 데이터셋에서 HOTA 및 AssA 지표에서 뛰어난 성능을 보여, 기존 방법론들이 어려움을 겪던 장기적인 객체 추적 및 ID 유지 능력을 크게 향상시켰다.[2][4][6]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**:
    - 시간 $t$에서 학습 가능한 탐지 쿼리 $Q_{det}$와 트랙 임베딩 $E_{tck}^t$를 모델에 공동 입력하여 탐지 및 추적 결과를 생성한다.[3]
    - 탐지 결과 중 신뢰도 점수 $\tau_{det}$ 이상인 객체는 신규 객체로 전환된다.[3]
    - 추적 객체가 현재 프레임에서 손실(신뢰도 $\le \tau_{tck}$)되면 즉시 제거하지 않고 'inactive'로 표시하며, $\mathcal{T}_{miss}$ 프레임 이후 완전히 제거된다.[3]
- **특징**:
    - 모든 시간 단계에서 모든 객체의 트랙 임베딩과 장기 기억을 업데이트하지 않고, 높은 신뢰도를 가진 트랙 임베딩만 업데이트한다.[3]
    - 업데이트 임계값 $\tau_{next}$를 사용하여 업데이트 여부를 결정한다.[3]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - DanceTrack[3] (주요 평가 데이터셋, 연관성 문제 심각)
    - MOT17[3] (전통적인 보행자 추적 데이터셋)
    - BDD100K[3] (다중 카테고리 추적 데이터셋)
    - CrowdHuman[3] (MOT17 학습 시 오버피팅 방지를 위해 추가 사용)
- **하드웨어**: 8 NVIDIA Tesla V100 GPUs[3]
- **학습 시간**:
    - DanceTrack: 18 에포크 (12번째 에포크에서 학습률 1/10 감소)[3]
    - MOT17: 130 에포크 (120번째 에포크에서 학습률 1/10 감소)[3]
    - BDD100K: 14 에포크 (12번째 에포크에서 학습률 1/10 감소)[3]
- **옵티마이저**: AdamW (초기 학습률 $2.0 \times 10^{-4}$)[3]
- **규제(Regularization)**:
    - 데이터 증강 (random resize, random crop)[3]
    - PyTorch gradient checkpoint 기술을 활용한 메모리 최적화 버전 구현[3]

---

## **⚠️ 한계**
- 여전히 어려운 시퀀스(challenging sequences)에서는 객체 연관성(object association) 성능 개선의 여지가 남아있다.[7]

---

## **📊 주요 실험 결과**

### **메인 태스크 성능 (DanceTrack Test Set)**[3]

|**모델**|**HOTA**|**DetA**|**AssA**|**MOTA**|**IDF1**|
|---|---|---|---|---|---|
| MOTR[3] | 54.2 | 73.5 | 40.2 | 79.7 | 51.5 |
| ByteTrack[3] | 47.7 | 71.0 | 32.1 | 89.6 | 53.9 |
| MOTRv2[3] | 69.9 | 83.0 | 59.0 | 91.9 | 71.7 |
| **[[MeMOTR]] (ours)**[3] | **68.5** | **80.5** | **58.4** | **89.9** | **71.2** |

---

## **🔮 향후 연구 방향**
- 장기 기억 업데이트 전략을 다양한 데이터셋에 대해 최적화하는 연구.[6]
- 대체 메모리 구조를 탐색하여 성능을 더욱 향상시키는 연구.[6]
- 모션 추정 모델과 같은 추가적인 단서(cues)를 통합하여 추적 정확도를 높이는 연구.[6]
- [[MeMOTR]] 프레임워크를 다른 객체 탐지 패러다임 또는 백본 아키텍처와 통합하여 적용 가능성을 확장하는 연구.[6]

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Transformer]]
- [[Deep Learning]]
- [[Computer Vision]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2307.15700[3]
- **코드**: https://github.com/MCG-NJU/MeMOTR[3][1]

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics[0]) AND file.name != this.file.name
SORT year desc
```

```