
좋아. **Cascade Pyramid Network (CPN)** 은 2018년 CVPR에서 발표된 논문  
👉 _"Cascaded Pyramid Network for Multi-Person Pose Estimation"_  
에 기반한 모델이야. COCO keypoint challenge 2017에서 **1위를 차지한 아키텍처**로, 특히 어려운 관절(hard keypoints)을 정밀하게 예측하는 데 초점을 둔 구조야.

---

## 🧠 핵심 개념 요약

> CPN은 **multi-scale feature 추출 (GlobalNet)** 과, **정교한 keypoint refinement (RefineNet)** 의 **2단계 구조**로 이루어져 있으며,  
> 특히 **어려운 관절(hard keypoints)** 을 집중 학습하기 위한 **[[Online Hard Keypoints Mining|Online Hard Keypoints Mining (OHKM)]]** 기법을 사용한다.

---

## 🏗️ 전체 아키텍처 구성

### 1. [[GlobalNet]]

- 기본적인 keypoint 히트맵을 생성하는 stage
    
- **ResNet (conv2_x ~ conv5_x)** 에서 각 해상도별 feature 추출
    
- FPN(Feature Pyramid Network)처럼 여러 스케일의 feature를 **upsample & concat** → **multi-scale feature fusion**
    

📌 목적: coarse한 keypoint 위치 예측  
📌 특징: 다양한 receptive field 정보를 융합

---

### 2. **[[RefineNet]]**

- GlobalNet이 생성한 히트맵 + feature를 입력으로 받아 **어려운 keypoint를 정교하게 보정**
    
- Residual block과 upsampling block으로 구성된 shallow한 CNN 구조
    
- **중간 히트맵에서 성능 낮은 keypoint만 집중적으로 학습**
    

📌 목적: fine-grained keypoint refinement  
📌 특징: hard keypoint에 selective하게 gradient를 전달

---

## 🔍 핵심 구성 요소 정리

|구성 요소|설명|
|---|---|
|**Backbone**|ResNet-50 / 101|
|**GlobalNet**|multi-scale feature fusion (FPN 스타일)|
|**RefineNet**|Residual block 기반 refinement head|
|**OHKM Loss**|학습 시 hard keypoint (MSE 높은 것 상위 K개)만 loss 계산|

---

## 📊 OHKM (Online Hard Keypoints Mining)

### 목적:

- 모든 keypoint를 동일하게 학습하지 않고,
    
- **정확도가 낮은 keypoint (예: 손목, 발목 등)** 에 집중 학습
    

### 방식:

- RefineNet의 output과 GT heatmap 간의 MSE를 keypoint 단위로 계산
    
- 이 중 상위 K개 (예: 8개) keypoint에 대해서만 loss를 계산
    

📌 장점: 학습 에너지를 가장 어려운 관절에 집중 → 성능 향상

---

## 📈 CPN 구조 도식화

```
Input
 ↓
[ResNet Backbone]
 ↓
[GlobalNet]
  └─ conv2_x, conv3_x, conv4_x, conv5_x → upsample & concat → heatmap1
 ↓
[RefineNet]
  └─ residual blocks + upsample
  └─ OHKM loss 적용 → refined heatmap2
```

---

## 🚀 성능

- COCO Keypoint Challenge 2017 1위 (AP: ~73.0)
    
- 특히 **복잡한 포즈, 가려진 관절**에서 강력함
    

---

## ✅ 정리 문장

> **CPN은 ResNet을 기반으로 한 2단계 구조의 포즈 추정 네트워크로, GlobalNet에서 multi-scale 정보를 추출하고, RefineNet에서 어려운 keypoint를 정교하게 보정한다. OHKM 기법을 통해 학습 효율을 극대화하며, 실전 성능에서도 우수한 정확도를 달성하였다.**

---

## 📁 옵시디언 분류 제안

- `Computer Vision > Networks > Cascade Pyramid Network`
    
- 또는 `Computer Vision > Detection & Segmentation > Human Pose Estimation`
    
