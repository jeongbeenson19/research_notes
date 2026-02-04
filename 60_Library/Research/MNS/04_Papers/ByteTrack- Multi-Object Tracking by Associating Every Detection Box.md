---
alias: ["ByteTrack"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟩 Done
rating: 5
date: 2026-02-04
title: "ByteTrack: Multi-Object Tracking by Associating Every Detection Box"
authors: ["Yifu Zhang", "Pei Sun", "Jing Shao", "Yi-Cong Chen", "Zhuofan Zong", "Guanhong Meng", "Xinshuo Weng", "Ping Luo", "Zhen Lei"]
year: 2021
venue: "ECCV"
paper_url: https://arxiv.org/abs/2110.06864
topics: ["Multi-Object Tracking", "Data Association", "Computer Vision"]
---

## **📄 ByteTrack: Multi-Object Tracking by Associating Every Detection Box 개요**

- **발표 논문**: ByteTrack: Multi-Object Tracking by Associating Every Detection Box, Yifu Zhang et al., ECCV 2021[1]
- **핵심 아이디어**:
기존의 다중 객체 추적(Multi-Object Tracking, [[MOT]]) 방법론들은 낮은 점수(low detection scores)를 가진 탐지 박스(detection boxes)들을 단순히 버려, 가려진(occluded) 객체나 움직임이 빠른 객체들의 궤적(trajectories)이 끊기거나 사라지는 문제를 야기했습니다. [[ByteTrack]]은 이러한 문제를 해결하기 위해 높은 점수의 탐지 박스뿐만 아니라 **거의 모든 탐지 박스(almost every detection box)**를 연관(associate)시켜 추적 성능을 향상시키는 간단하고 효과적인 데이터 연관(data association) 방법을 제안합니다. 낮은 점수의 탐지 박스에 대해서는 트랙렛(tracklets)과의 유사도를 활용하여 실제 객체를 복구하고 배경 탐지를 걸러냅니다.[1][2][3]
- **주요 성과**:
    - MOT20, HiEve, BDD100K 추적 벤치마크에서 [[State-of-the-Art (SOTA)]] 성능을 달성했습니다.[1][2]
    - MOT17 테스트 세트에서 단일 V100 GPU로 30 FPS의 속도로 80.3 MOTA, 77.3 IDF1, 63.1 HOTA를 달성했습니다.[1][2][3]
    - 9가지 다른 SOTA 트래커에 적용했을 때 IDF1 점수에서 1~10점의 일관된 성능 향상을 보였습니다.[1][2][3]

---

## **🏗 아키텍처 개요**

[[ByteTrack]]은 BYTE라는 데이터 연관 알고리즘을 기반으로 하며, 두 단계의 연관 과정을 통해 객체를 추적합니다.[4][3]

### **0. 기호/차원**
- $D$: 탐지 박스 집합 (Set of detection boxes)
- $T$: 트랙렛 집합 (Set of tracklets)
- $D_{high}$: 높은 점수의 탐지 박스 집합 (High-score detection boxes, score > 0.6)[4]
- $D_{low}$: 낮은 점수의 탐지 박스 집합 (Low-score detection boxes, 0.1 < score $\le$ 0.6)[4]
- $T_{unmatched}$: 연관되지 않은 트랙렛 집합 (Unmatched tracklets)
- $K$: 칼만 필터 (Kalman Filter)

### **1. 첫 번째 연관 (First Association)**
- **구성**: 높은 점수의 탐지 박스($D_{high}$)와 기존 트랙렛($T$) 간의 연관을 수행합니다.[4]
- 각 층:
    1. **[[유사도 측정]]**: 탐지 박스와 트랙렛 간의 유사도를 계산합니다. 구현에서는 주로 [[IoU (Intersection over Union)]]를 사용합니다.[4]
    2. **[[매칭]]**: 계산된 유사도를 바탕으로 최적의 매칭을 찾습니다.
- **특이 사항**: 매칭된 트랙렛의 상태 벡터(state vector)는 [[칼만 필터 (Kalman Filter)]]를 사용하여 업데이트됩니다. 연관되지 않은 높은 점수 탐지 박스와 연관되지 않은 트랙렛은 다음 단계로 전달됩니다.[4]

### **2. 두 번째 연관 (Second Association)**
- **구성**: 첫 번째 단계에서 연관되지 않은 트랙렛($T_{unmatched}$)과 낮은 점수의 탐지 박스($D_{low}$) 간의 연관을 수행합니다.[4]
- 각 층:
    1. **[[유사도 측정]]**: 낮은 점수 탐지 박스와 연관되지 않은 트랙렛 간의 유사도를 계산합니다. 이 단계에서도 [[IoU]]가 주로 사용됩니다.[4]
    2. **[[매칭]]**: 최적의 매칭을 찾습니다.
- **특이 사항**: 연관되지 않은 낮은 점수 탐지 박스는 버려집니다. 이는 배경 탐지를 걸러내는 데 도움이 됩니다.[4]

### **3. 주요 수식 요약**
- **칼만 필터 상태 업데이트**:
  - $x_k = F_k x_{k-1} + B_k u_k + w_k$ (상태 예측)
  - $z_k = H_k x_k + v_k$ (측정 업데이트)
  - (논문에서 구체적인 수식은 제시되지 않았으나, 칼만 필터 사용 명시)[4]
- **IoU (Intersection over Union)**:
  - $IoU(B_1, B_2) = \frac{Area(B_1 \cap B_2)}{Area(B_1 \cup B_2)}$

---

## **🎯 주요 구성 요소**

### **1. [[BYTE 데이터 연관 (BYTE Data Association)]]**
- 입력/출력 및 작동 원리 설명: BYTE는 모든 탐지 박스를 활용하여 객체 궤적을 유지하는 핵심 메커니즘입니다. 높은 점수 탐지 박스와 트랙렛을 먼저 연관시키고, 남은 트랙렛과 낮은 점수 탐지 박스를 연관시켜 가려짐 등으로 인해 점수가 낮아진 실제 객체를 복구합니다.[4][3]
- $$ \text{BYTE}(D, T) = \text{Associate}(D_{high}, T) \cup \text{Associate}(D_{low}, T_{unmatched}) $$

### **2. [[칼만 필터 (Kalman Filter)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 객체의 움직임을 예측하고, 탐지 결과를 바탕으로 트랙렛의 상태(위치, 속도 등)를 업데이트하는 데 사용됩니다. 이는 객체의 갑작스러운 움직임이나 짧은 시간 동안의 사라짐에 대응하는 데 도움을 줍니다.[4]
- 설정 값 (논문 기준): 구체적인 파라미터는 논문에 명시되어 있지 않으나, 일반적인 MOT 설정에 따라 사용됩니다.

### **3. [[유사도 측정 (Similarity Metric)]]**
- [[IoU]]와 [[Re-ID (Re-Identification)]] 특징을 유사도 측정에 활용할 수 있습니다. 구현에서는 주로 IoU가 사용되며, 특히 낮은 점수 탐지 박스의 경우 외형 특징(appearance features)이 신뢰할 수 없으므로 IoU가 더 적합하다고 언급됩니다.[4]

---

## **⚖️ ByteTrack vs 기존 모델**

| **비교 항목** | **ByteTrack** | **기존 MOT 모델 (일반적)** |
| :--- | :--- | :--- |
| **탐지 박스 활용** | 거의 모든 탐지 박스 (높은 점수 + 낮은 점수)[1][2][3] | 높은 점수의 탐지 박스만 활용[1][2][3] |
| **가려짐/저점수 객체 처리** | 낮은 점수 탐지 박스를 통해 궤적 복구[1][2][3] | 낮은 점수 객체는 버려져 궤적 끊김 발생[1][2][3] |
| **궤적 연속성** | 향상된 궤적 연속성 | 궤적 단편화 가능성 높음 |
| **복잡도** | $O(N \log N)$ (일반적인 매칭 알고리즘 기준) | $O(N \log N)$ (일반적인 매칭 알고리즘 기준) |

- [[ByteTrack]]은 낮은 점수의 탐지 박스를 활용하여 기존 모델들이 겪던 객체 누락 및 궤적 단편화 문제를 효과적으로 해결합니다. 이는 특히 가려짐(occlusion)이 심하거나 객체가 빠르게 움직이는 상황에서 강점을 가집니다.[1][2][3]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: [[Tracking-by-detection]] 패러다임을 따르며, 각 프레임에서 탐지된 객체들을 기존 트랙렛과 연관시키는 방식으로 추론이 진행됩니다.
- **특징**: 두 단계의 데이터 연관 과정을 통해 탐지 점수가 낮은 객체들도 추적에 포함시켜 궤적의 견고함(robustness)을 높입니다.[4]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - MOT17, MOT20, HiEve, BDD100K 등 다양한 다중 객체 추적 벤치마크 데이터셋에서 평가되었습니다.[1][2]
- **하드웨어**: NVIDIA V100 GPU (단일 GPU에서 30 FPS 성능 달성)[1][2][3]
- **학습 시간**: 구체적인 학습 시간은 명시되지 않았습니다.
- **옵티마이저**: (논문에서 구체적으로 언급되지 않음)
- **규제(Regularization)**: (논문에서 구체적으로 언급되지 않음)

---

## **⚠️ 한계**
- 논문에서 명시적인 한계점 섹션은 없으나, 기존 MOT 방법론의 한계점(낮은 점수 탐지 박스 폐기)을 해결하는 데 중점을 두었으므로, 이는 기존 방법론의 한계이자 ByteTrack이 개선한 부분으로 볼 수 있습니다.[1][2][3]

---

## **📊 주요 실험 결과**

### **[메인 태스크 성능]**

|**모델**|**MOTA**|**IDF1**|**HOTA**|**FPS**|
|---|---|---|---|---|
| [비교 모델 A] | - | - | - | - |
| [비교 모델 B] | - | - | - | - |
| **ByteTrack (MOT17)** | **80.3** | **77.3** | **63.1** | **30** |[1][2][3]

---

## **🔮 향후 연구 방향**
- [[ByteTrack]]의 데이터 연관 알고리즘인 BYTE는 간단하고 효과적이며 일반적인 방법론으로, 다양한 기존 트래커에 적용하여 성능을 향상시킬 수 있음을 보여주었습니다.[4][1][2][3] 이는 향후 다중 객체 추적 연구에서 데이터 연관의 중요성을 강조하며, 더 효율적이고 견고한 연관 방법론 개발의 가능성을 시사합니다.

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Data Association]]
- [[Kalman Filter]]
- [[IoU]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2110.06864[5]
- **코드**: https://github.com/ifzhang/ByteTrack[1][2][3]

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics[0]) AND file.name != this.file.name
SORT year desc
```

