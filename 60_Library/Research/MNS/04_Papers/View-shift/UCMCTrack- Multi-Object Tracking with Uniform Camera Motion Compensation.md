---
aliases:
  - UCMCTrack
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
  - CameraMotionCompensation
  - ViewShift
status: 🟩 Done
rating: 0
date: 2026-02-03
title: "UCMCTrack: Multi-Object Tracking with Uniform Camera Motion Compensation"
authors:
  - Kefu Yi
  - Kai Luo
  - Xiaolei Luo
  - Jiangui Huang
  - Hao Wu
  - Rongdong Hu
  - Wei Hao
year: 2024
venue: AAAI
paper_url: https://arxiv.org/abs/2312.08952
topics:
  - Multi-Object Tracking (MOT)
  - Camera Motion Compensation (CMC)
  - Motion Model
  - Kalman Filter
---

## **📄 UCMCTrack: Multi-Object Tracking with Uniform Camera Motion Compensation 개요**

- **발표 논문**: UCMCTrack: Multi-Object Tracking with Uniform Camera Motion Compensation, Kefu Yi et al., AAAI 2024.[1][2][3]
- **핵심 아이디어**:
    UCMCTrack은 기존의 [[IoU (Intersection over Union)]] 기반 방법론에 의존하지 않고, 카메라 움직임과 흔들림에 강건한 단순하면서도 효과적인 [[Multi-Object Tracking (MOT)]] 방법론을 제안합니다.[4][5] 이 모델은 비디오 시퀀스 전체에 걸쳐 동일한 보정 파라미터를 적용하는 [[Uniform Camera Motion Compensation (UCMC)]]을 사용하며, 이는 프레임별로 보정 파라미터를 계산하는 기존 CMC 방식과 차별화됩니다.[6][5] 지면(ground plane)에 투영된 확률 분포를 활용하여 움직임 패턴을 효율적으로 포착하고, [[Homography]] 투영으로 인한 불확실성을 관리합니다.[6]
- **주요 성과**:
    - 단일 CPU 사용 시 1000 FPS를 초과하는 매우 빠른 속도로 동작합니다.[4][5]
    - MOT17, MOT20, DanceTrack, KITTI 등 다양한 챌린징 데이터셋에서 최첨단(state-of-the-art, SOTA) 성능을 달성했습니다.[6]
    - DanceTrack 데이터셋에서 UCMCTrack+는 HOTA를 2.3, IDF1을 3.4, AssA를 5.5 향상시켰습니다.[2]
    - MOT17 데이터셋에서 기존 SOTA 트래커 대비 HOTA 0.9, IDF1 0.5, AssA 0.7의 성능 향상을 보였습니다.[2]
    - 불규칙한 움직임(DanceTrack) 및 고속 움직임, 낮은 프레임 속도 감지(KITTI)와 같은 어려운 조건에서도 강력한 일반화 능력을 보여줍니다.[2]

---

## **🏗 아키텍처 개요**

UCMCTrack은 [[Tracking-by-Detection]] 패러다임을 따르며, 다음 단계를 포함합니다.[4]

### **0. 기호/차원**
- $x, y$: 2D 이미지 평면상의 좌표
- $X, Y, Z$: 3D 공간상의 좌표
- $H$: Homography 행렬
- $\Sigma$: 공분산 행렬

### **1. 주요 파트**
- **구성**:
    1. **[[Homography Transformation]]**: 감지된 바운딩 박스를 지면(ground plane)으로 매핑합니다.[7]
    2. **[[Correlated Measurement Distribution (CMD)]] 계산**: 지면으로 매핑된 후 타겟의 상관 측정 분포를 계산합니다.[7]
    3. **[[Kalman Filter]]**: [[Constant Velocity (CV) motion model]]과 [[Process Noise Compensation (PNC)]]이 적용된 칼만 필터에 CMD 분포를 입력합니다.[7]
    4. **[[Mapped Mahalanobis Distance (MMD)]] 계산**: 매핑된 측정값과 예측된 트랙 상태를 사용하여 MMD를 계산합니다.[7]
    5. **[[Hungarian Algorithm]]**: 최종적으로 헝가리안 알고리즘을 통해 트랙과 감지(detection)를 연결(association)합니다.[7]

### **2. 주요 수식 요약**
- **Mapped Mahalanobis Distance (MMD)**:
  - $D_{MMD}(i, j) = \sqrt{(\mathbf{x}_i - \mathbf{y}_j)^T \Sigma_{ij}^{-1} (\mathbf{x}_i - \mathbf{y}_j)}$
  (여기서 $\mathbf{x}_i$는 트랙 $i$의 예측 상태, $\mathbf{y}_j$는 감지 $j$의 매핑된 측정값, $\Sigma_{ij}$는 이들의 결합 공분산)
- **Correlated Measurement Distribution (CMD)**:
  - $P(\mathbf{y} | \mathbf{x}) \sim \mathcal{N}(\mathbf{y}; H\mathbf{x}, H\Sigma_x H^T + \Sigma_y)$
  (여기서 $H$는 호모그래피 행렬, $\Sigma_x$는 상태 공분산, $\Sigma_y$는 측정 노이즈 공분산)

---

## **🎯 주요 구성 요소**

### **1. [[Uniform Camera Motion Compensation (UCMC)]]**
- **입력/출력 및 작동 원리**: 기존 CMC가 프레임별로 보정 파라미터를 계산하는 것과 달리, UCMCTrack은 비디오 시퀀스 전체에 걸쳐 동일한 보정 파라미터를 일관되게 적용합니다.[6][5] 이는 실시간 MOT의 계산 부담을 크게 줄여줍니다.[6][5]
- **핵심 수식**: (논문 원문 참조 필요)

### **2. [[Mapped Mahalanobis Distance (MMD)]]**
- **병렬 처리, 분할, 혹은 특수 기능 설명**: 기존의 [[IoU]] 기반 거리 측정 방식의 대안으로 도입된 새로운 모션 기반 거리 측정 방식입니다.[2][6] 카메라 흔들림이나 낮은 샘플링 속도로 인해 바운딩 박스가 겹치지 않는 경우 IoU가 비효율적인 문제를 해결합니다.[5]
- **설정 값 (논문 기준)**: (논문 원문 참조 필요)

### **3. [[Process Noise Compensation (PNC)]]**
- [[Kalman Filter]]와 함께 사용되어, 움직임 모델의 불확실성을 보상하고 트래킹의 정확도를 높입니다.[2][7]

---

## **⚖️ UCMCTrack vs 기존 모델**

| **비교 항목** | **UCMCTrack** | **기존 CMC** | **IoU 기반 MOT** |
| :--- | :--- | :--- | :--- |
| **카메라 모션 보정** | 비디오 전체에 균일한 파라미터 적용[6][5] | 프레임별 파라미터 계산[6][5] | (주로 추가적인 CMC 필요) |
| **거리 측정** | [[Mapped Mahalanobis Distance (MMD)]][6] | (해당 없음) | [[IoU]][5] |
| **계산 복잡도** | 매우 빠름 (단일 CPU 1000 FPS 이상)[4][5] | 높은 계산 부담[6][5] | 높은 계산 부담 (외형 단서, CMC 추가 시)[6][5] |
| **외형 단서 사용** | 사용하지 않음 (순수 모션 기반)[6][8] | (주로 사용) | (주로 사용) |
| **강건성** | 카메라 움직임 및 흔들림에 강건함[4][5] | 부정확한 파라미터로 인해 성능 저하 가능[2] | 카메라 움직임 시 IoU 비효율적[5] |
| **복잡도** | $O(N)$ (추정) | $O(N)$ (추정) | $O(N)$ (추정) |

- UCMCTrack은 기존의 프레임별 CMC 방식이 가지는 계산 부담과 IoU 기반 방법론이 카메라 움직임에 취약한 한계를 극복합니다.[6][5] 순수 모션 기반임에도 불구하고 다양한 데이터셋에서 SOTA 성능을 달성하며, 실시간 처리에 매우 효율적입니다.[4][6][8][5]

---

## **🧠 추론 과정**
- **방식**: [[Tracking-by-Detection]] 패러다임을 따르며, 감지된 객체와 기존 트랙 간의 연관성(association)을 위해 [[Hungarian Algorithm]]을 사용합니다.[7]
- **특징**: 지면(ground plane)으로의 매핑과 [[Kalman Filter]]를 통해 객체의 움직임을 예측하고, [[Mapped Mahalanobis Distance (MMD)]]를 사용하여 트랙과 감지 간의 거리를 측정합니다.[7][6]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - MOT17, MOT20, DanceTrack, KITTI[6]
- **하드웨어**: 단일 CPU 환경에서 1000 FPS 이상의 속도를 달성합니다.[4][5]
- **학습 시간**: (논문 원문 참조 필요)
- **옵티마이저**: (논문 원문 참조 필요)
- **규제(Regularization)**: (논문 원문 참조 필요)

---

## **⚠️ 한계**
- 논문 자체에서 UCMCTrack의 명시적인 한계점은 언급되지 않았지만, 기존 CMC의 경우 부정확한 파라미터로 인해 성능 저하가 발생할 수 있다고 지적하며 UCMCTrack이 이를 극복했음을 강조합니다.[2]

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**HOTA**|**IDF1**|**AssA**|
|---|---|---|---|
| 기존 SOTA (DanceTrack) | - | - | - |
| **UCMCTrack+ (DanceTrack)** | **+2.3** | **+3.4** | **+5.5** |
| 기존 SOTA (MOT17) | - | - | - |
| **UCMCTrack+ (MOT17)** | **+0.9** | **+0.5** | **+0.7** |

---

## **🔮 향후 연구 방향**
- (논문 원문 참조 필요)

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Camera Motion Compensation]]
- [[Kalman Filter]]
- [[Homography]]
- [[IoU]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2312.08952[3]
- **코드**: https://github.com/corfyi/UCMCTrack[6]

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
