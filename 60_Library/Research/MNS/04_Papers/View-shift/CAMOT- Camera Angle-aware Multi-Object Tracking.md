---
aliases:
  - CAMOT
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
  - CameraAngle
  - ViewShift
status: 🟧 Reading
rating: 0
date: 2024-09-26
title: "CAMOT: Camera Angle-aware Multi-Object Tracking"
authors:
  - Felix Limanta
  - Kuniaki Uto
  - Koichi Shinoda
year: 2024
venue: WACV
paper_url: https://arxiv.org/abs/2409.17533
topics:
  - Multi-Object Tracking
  - Camera Angle Estimation
  - Depth Estimation
---

## **📄 CAMOT: Camera Angle-aware Multi-Object Tracking 개요**

- **발표 논문**: CAMOT: Camera Angle-aware Multi-Object Tracking by Felix Limanta, Kuniaki Uto, Koichi Shinoda, WACV 2024.
- **핵심 아이디어**: [[CAMOT]]은 [[Multi-Object Tracking]] (MOT)에서 발생하는 [[Occlusion]] (가려짐) 및 부정확한 [[Depth Estimation]] (깊이 추정) 문제를 해결하기 위해 간단한 [[Camera Angle Estimation]] (카메라 각도 추정기)를 제안합니다. 이 방법은 여러 객체가 각 비디오 프레임에서 평평한 평면에 위치한다는 가정 하에 [[Object Detection]] (객체 감지)를 활용하여 카메라 각도를 추정합니다. 이를 통해 각 객체의 깊이 정보를 제공하여 [[Pseudo-3D MOT]]를 가능하게 합니다.[1][2][3][4]
- **주요 성과**:
    - MOT17 및 MOT20 데이터셋에서 다양한 2D MOT 방법론에 적용하여 효과를 입증했습니다.[1][2][3][4]
    - ByteTrack에 적용했을 때 MOT17에서 63.8% HOTA, 80.6% MOTA, 78.5% IDF1의 [[State-of-the-Art]] (최고 성능) 결과를 달성했습니다.[1][2][3][4]
    - 기존 딥러닝 기반 깊이 추정기에 비해 계산 비용이 현저히 낮습니다 (단일 A100 GPU에서 24.92 FPS로, 기존 방법의 10 FPS 미만보다 높음).[1][4]

---

## **🏗 아키텍처 개요**

CAMOT는 기존 2D MOT 방법론에 플러그인으로 활용될 수 있는 경량 [[Camera Angle Estimation]] 모듈입니다. 객체 감지 위치를 활용하여 카메라 각도를 추정하며, 이를 통해 각 객체의 깊이 정보를 제공하여 [[Pseudo-3D MOT]]를 가능하게 합니다.[1][4]

### **0. 기호/차원**
- (제공된 정보 없음)

### **1. [주요 파트 1 (예: 인코더)]**
- (제공된 정보 없음)

### **2. [주요 파트 2 (예: 디코더)]**
- (제공된 정보 없음)

### **3. 주요 수식 요약**
- (제공된 정보 없음)

---

## **🎯 주요 구성 요소**

### **1. [[카메라 각도 추정기]] (Camera Angle Estimator)**
- **입력/출력 및 작동 원리**: 객체 감지(Object Detection) 결과를 입력으로 받아 카메라의 각도를 추정합니다. 이는 여러 객체가 평평한 평면에 존재한다는 가정을 기반으로 합니다.[1][2][3][4]
- (핵심 수식은 제공된 정보 없음)

### **2. [[깊이 정보 제공]] (Depth Information Provision)**
- **특징**: 추정된 카메라 각도를 활용하여 각 객체의 깊이(depth)를 제공합니다. 이 깊이 정보는 [[Occlusion]] 문제를 해결하고, 깊이 방향에서의 거리 측정을 가능하게 하여 다른 프레임 간의 [[Object Association]] (객체 연관)을 더욱 정확하게 만듭니다.[1][4]
- **설정 값 (논문 기준)**: (제공된 정보 없음)

### **3. [기타 구성 요소]**
- (제공된 정보 없음)

---

## **⚖️ CAMOT vs 기존 모델**

| **비교 항목** | **CAMOT** | **기존 딥러닝 기반 깊이 추정기** |
| :--- | :--- | :--- |
| **목표 문제** | [[Occlusion]], 부정확한 깊이 추정 | [[Occlusion]], 부정확한 깊이 추정 |
| **접근 방식** | 간단한 [[Camera Angle Estimation]] 기반 [[Pseudo-3D MOT]] | 딥러닝 기반 [[Depth Estimation]] |
| **계산 비용** | 현저히 낮음 (24.92 FPS on A100 GPU)[4] | 높음 (10 FPS 미만)[4] |
| **복잡도** | 경량 (Lightweight)[4] | (제공된 정보 없음) |

- CAMOT는 기존 딥러닝 기반 깊이 추정기에 비해 훨씬 낮은 계산 비용으로 유사한 문제들을 효과적으로 해결하며, 다양한 2D MOT 방법론에 플러그인으로 쉽게 통합될 수 있는 장점이 있습니다.[1][4]

---

## **🧠 [추론/디코딩/생성] 과정**
- CAMOT는 기존 2D MOT 방법론에 깊이 정보를 추가하여 객체 연관(Object Association)의 정확도를 높이는 방식으로 추론 과정에 기여합니다.[1][4]
- **특징**: (제공된 정보 없음)

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - [[MOT17]] (Multi-Object Tracking 2017)[1][2][3][4]
    - [[MOT20]] (Multi-Object Tracking 2020)[1][2][3][4]
- **하드웨어**: 단일 [[NVIDIA A100 GPU]] (성능 측정 시)[4]
- **학습 시간**: (제공된 정보 없음)
- **옵티마이저**: (제공된 정보 없음)
- **규제(Regularization)**: (제공된 정보 없음)

---

## **⚠️ 한계**
- CAMOT의 핵심 가정은 "여러 객체가 각 비디오 프레임에서 평평한 평면에 위치한다"는 것입니다.[1][2][3][4] 이 가정은 객체가 평평하지 않은 지형이나 다양한 높이에 위치하는 시나리오에서는 한계로 작용할 수 있습니다.

---

## **📊 주요 실험 결과**

### **[메인 태스크 성능]**

|**모델**|**HOTA**|**MOTA**|**IDF1**|
|---|---|---|---|
| ByteTrack + CAMOT (MOT17) | **63.8%** | **80.6%** | **78.5%** |

---

## **🔮 향후 연구 방향**
- (제공된 정보 없음)

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Camera Angle Estimation]]
- [[Depth Estimation]]
- [[Occlusion]]
- [[Object Association]]
- [[Pseudo-3D MOT]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2409.17533
- **코드**: (제공된 정보 없음)

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```
