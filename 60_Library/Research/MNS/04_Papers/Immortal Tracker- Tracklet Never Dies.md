---
aliases: ["Immortal Tracker"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟧 Reading
rating: 0
date: 2026-02-04
title: "Immortal Tracker: Tracklet Never Dies"
authors: ["Qitai Wang", "Yuntao Chen", "Ziqi Pang", "Naiyan Wang", "Zhaoxiang Zhang"]
year: 2021
venue: "arXiv"
paper_url: https://arxiv.org/abs/2111.13672
topics: ["3D Multi-Object Tracking", "Trajectory Prediction", "Kalman Filter", "Identity Switch"]
---

## **📄 Immortal Tracker: Tracklet Never Dies 개요**

- **발표 논문**: Immortal Tracker: Tracklet Never Dies (Qitai Wang et al., arXiv 2021)[1]
- **핵심 아이디어**:
    기존 3D 다중 객체 추적(3DMOT) 시스템에서 발생하는 [[Tracklet]]의 조기 종료(premature tracklet termination)로 인한 [[Identity Switch]] 문제를 해결하기 위해 제안된 간단한 추적 시스템입니다. 이 시스템은 객체가 일시적으로 시야에서 사라지거나(gone dark) 가려질 때 [[Trajectory Prediction]](궤적 예측)을 활용하여 [[Tracklet]]을 유지합니다.[2][3][4]
- **주요 성과**:
    - 조기 [[Tracklet]] 종료로 인한 차량 [[Identity Switch]]를 96% 감소시켰습니다.[2][3][4]
    - 학습된 파라미터 없이(without any learned parameters) 0.0001 수준의 낮은 불일치율(mismatch ratio)을 달성했으며, 이는 기존 방법론보다 수십 배 낮은 수치입니다.[2][3][4]
    - Waymo Open Dataset 테스트 세트에서 차량 클래스에 대해 경쟁력 있는 MOTA(Multi-Object Tracking Accuracy)를 기록했습니다.[2][3][4]
    - nuScenes 데이터셋에서도 유사한 결과를 보였습니다.[2][3][4]

---

## **🏗 아키텍처 개요**

Immortal Tracker는 객체가 보이지 않을 때 [[Trajectory Prediction]]을 통해 [[Tracklet]]을 유지하는 간단한 추적 시스템입니다.[2][3][4]

### **0. 기호/차원**
- $X_t$: 시간 $t$에서의 객체 상태 (위치, 속도 등)
- $Z_t$: 시간 $t$에서의 객체 관측(detection)

### **1. Tracklet 관리**
- **구성**: [[Immortal Tracker]]의 핵심은 한 번 생성된 [[Tracklet]]이 절대 사라지지 않도록(never die) 하는 것입니다.[1]
- 각 층:
    1. **[[Kalman Filter]]**: 객체의 궤적을 예측하는 데 사용됩니다.[2][3][4]
    2. **[[Data Association]]**: 3D IoU/GIoU(Intersection over Union/Generalized Intersection over Union) 지표를 사용하여 현재 관측과 기존 [[Tracklet]]을 연결합니다.[1]
- **특이 사항**: 객체가 보이지 않을 때 [[Kalman Filter]]를 통해 예측된 궤적으로 [[Tracklet]]을 유지하며, 객체가 다시 나타나면 예측된 궤적 근처에서 해당 [[Tracklet]]과 다시 연결됩니다.[1]

### **2. 주요 수식 요약**
- **Kalman Filter Prediction**:
  - $x_k = F_k x_{k-1} + B_k u_k + w_k$
  - $P_k = F_k P_{k-1} F_k^T + Q_k$
- **Kalman Filter Update**:
  - $K_k = P_k H_k^T (H_k P_k H_k^T + R_k)^{-1}$
  - $x_k = x_k + K_k (z_k - H_k x_k)$
  - $P_k = (I - K_k H_k) P_k$
  (여기서 $x_k$는 상태 벡터, $P_k$는 공분산 행렬, $F_k$는 상태 전이 행렬, $B_k$는 제어 입력 행렬, $u_k$는 제어 벡터, $w_k$는 프로세스 노이즈, $H_k$는 관측 행렬, $R_k$는 관측 노이즈, $z_k$는 관측 벡터, $K_k$는 칼만 이득입니다.)

---

## **🎯 주요 구성 요소**

### **1. [[Kalman Filter]] 기반 궤적 예측**
- 입력/출력 및 작동 원리 설명: [[Kalman Filter]]는 객체의 과거 움직임 정보를 바탕으로 현재 상태(위치, 속도 등)를 추정하고 미래 궤적을 예측하는 데 사용됩니다. 객체가 감지되지 않을 때, 이 예측된 궤적을 사용하여 [[Tracklet]]을 계속 유지합니다.[2][3][4]
- $$x_k = F_k x_{k-1} + w_k$$

### **2. [[Tracklet]] 불멸성(Immortality)**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 한 번 생성된 [[Tracklet]]은 객체가 시야에서 사라지더라도 종료되지 않고, 예측된 위치를 따라 계속 "살아있는" 상태로 유지됩니다. 이는 기존 방법론에서 객체가 잠시 가려지거나 시야를 벗어났을 때 [[Tracklet]]이 조기 종료되어 새로운 [[Identity]]가 할당되는 문제를 방지합니다.[1]

### **3. [[Data Association]] (데이터 연결)**
- 3D IoU/GIoU 지표를 사용하여 현재 프레임의 객체 감지(detection)와 기존 [[Tracklet]] 간의 연결을 수행합니다.[1]

---

## **⚖️ Immortal Tracker vs 기존 모델**

| **비교 항목** | **Immortal Tracker** | **기존 3DMOT 모델** |
| :--- | :--- | :--- |
| **Tracklet 수명** | 한 번 생성되면 영구 유지 (Immortal)[1] | 일정 시간 미관측 시 조기 종료[3][4] |
| **Identity Switch** | 96% 감소[2][3][4] | 조기 종료로 인한 빈번한 발생[3][4] |
| **학습 파라미터** | 없음 (No learned parameters)[2][3][4] | 일반적으로 학습 기반 모델 사용 |
| **복잡도** | $O(N)$ (N은 Tracklet 수, 간단한 Kalman Filter 사용) | $O(N \log N)$ 또는 그 이상 (복잡한 학습 모델의 경우) |

- Immortal Tracker는 간단한 [[Kalman Filter]] 기반의 궤적 예측을 통해 [[Tracklet]]의 불멸성을 보장함으로써, 기존 3DMOT 시스템의 주요 문제점인 [[Identity Switch]]를 획기적으로 줄였습니다.[2][3][4] 특히, 학습된 파라미터 없이 이러한 성능을 달성했다는 점이 큰 장점입니다.[2][3][4]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 온라인(online) 추적 방식. 각 프레임에서 객체 감지(detection)를 기반으로 [[Tracklet]]을 업데이트하거나 새로 생성합니다.
- **특징**: 객체가 감지되지 않는 경우, [[Kalman Filter]]를 통해 예측된 위치를 사용하여 [[Tracklet]]을 계속 유지합니다. 이후 객체가 다시 감지되면, 예측된 궤적과 가장 가까운 감지를 해당 [[Tracklet]]에 재연결합니다.[1]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - [[Waymo Open Dataset]] (차량, 보행자, 자전거 탑승자 클래스에 대한 3D 박스 및 포인트 클라우드 제공)[2][3][1][4]
    - [[nuScenes]][2][3][4]
- **하드웨어**: (논문 스니펫에서 특정 하드웨어 정보는 제공되지 않음)
- **학습 시간**: (Immortal Tracker는 학습된 파라미터가 없으므로 별도의 학습 시간이 필요하지 않음)
- **옵티마이저**: (해당 없음)
- **규제(Regularization)**: (해당 없음)

---

## **⚠️ 한계**
- 논문 스니펫에서 명시적인 한계점은 언급되지 않았으나, "Immortal Tracker"의 원리는 객체가 "gone dark" 상태일 때 예측에 의존하므로, 장기간의 복잡한 가려짐이나 예측 불가능한 움직임에는 한계가 있을 수 있습니다. 또한, "Once Detected, Never Lost"와 같은 후속 연구에서 Immortal Tracker가 "forward-only" 방식으로 작동하며, 객체가 처음 감지되기 전의 과거를 추적하지 못한다는 점이 언급됩니다.[5]

---

## **📊 주요 실험 결과**

### **차량 클래스 3D Multi-Object Tracking 성능**

|**모델**|**Mismatch Ratio**|**Identity Switches 감소**|**MOTA**|
|---|---|---|---|
| 기존 방법론 | 높음 | 높음 | 경쟁력 낮음 |
| **Immortal Tracker** | **0.0001 수준**[2][3][4] | **96% 감소**[2][3][4] | **경쟁력 있는 수준**[2][3][4] |

---

## **🔮 향후 연구 방향**
- Immortal Tracker는 3DMOT의 한계를 극복하기 위한 간단하면서도 강력한 솔루션을 제공합니다.[2][3][4] 향후 연구는 예측 모델의 정교화나 다양한 시나리오에서의 강건성 확보에 초점을 맞출 수 있습니다.

---

## **🔗 관련 링크**
- [[3D Multi-Object Tracking]]
- [[Kalman Filter]]
- [[Trajectory Prediction]]
- [[Identity Switch]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2111.13672[2]
- **코드**: https://github.com/ImmortalTracker/ImmortalTracker[3][4]

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
