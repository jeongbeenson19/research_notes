
Pose Estimation은 이미지나 비디오에서 사람 또는 객체의 **자세(포즈)** 를 추정하는 컴퓨터 비전 작업입니다. 사람의 경우, 일반적으로 관절(joint) 위치를 2D 또는 3D 좌표로 예측하는 것이 목적입니다.

---

## 1. 정의

**Pose Estimation**은 주어진 이미지에서 객체의 형태나 구조를 파악하여, **관절 위치나 뼈대 구조(keypoints, skeleton)** 를 추정하는 문제입니다.

- **2D Pose Estimation**: 이미지 평면 상의 (x, y) 좌표
    
- **3D Pose Estimation**: (x, y, z) 좌표, 깊이까지 추정
    
- **Single Person** vs **Multi-Person**: 한 명 또는 여러 명 추정
    

---

## 2. 입력과 출력

|항목|설명|
|---|---|
|입력 (Input)|RGB 이미지 또는 비디오 프레임|
|출력 (Output)|관절별 좌표 (예: 머리, 어깨, 무릎, 발목 등)|

---

## 3. 주요 기법

### 3.1 Top-down 방식

1. 먼저 **사람 검출(Object Detection)** → 2. 각 사람마다 자세 추정
    

- 대표 모델:
    
    - **[[Cascaded Pyramid Network|CPN (Cascaded Pyramid Network)]]**
        
    - **[[Simple Baseline|Simple Baseline]]**
        
    - **HRNet**
        

> 장점: 높은 정확도  
> 단점: 사람 수에 따라 연산량 증가

---

### 3.2 Bottom-up 방식

1. 이미지 전체에서 **모든 keypoint**를 탐지 → 2. 이를 그룹핑하여 사람 별로 연결
    

- 대표 모델:
    
    - **OpenPose**
        
    - **HigherHRNet**
        
    - **CenterNet**
        

> 장점: 빠름, 사람 수와 무관  
> 단점: 포스트 프로세싱이 복잡하고 정확도 낮을 수 있음

---

## 4. 네트워크 구성 예시 (Simple Baseline)

```
[Input Image]
      ↓
[ResNet Backbone]
      ↓
[Deconv Layers (업샘플링)]
      ↓
[1x1 Conv → Heatmap 생성 (joint별)]
      ↓
[argmax → joint 좌표 추출]
```

- Output: (height, width, num_joints)의 **heatmap**
    
- 각 픽셀의 값은 해당 joint일 확률을 나타냄
    

---

## 5. 학습 방식

### **Loss Function**

#### 🔥 Heatmap 기반 Loss 사용 여부

|모델|Heatmap 기반 Loss 사용 여부|설명|
|---|---|---|
|**CPN** (Cascaded Pyramid Network)|✅ 사용함|각 관절에 대해 GT heatmap과 예측 heatmap 사이의 **MSE Loss** 사용. GlobalNet과 RefineNet 단계 모두 heatmap 예측 구조.|
|**Simple Baseline**|✅ 사용함|ResNet + Deconv 후 1×1 Conv로 **joint별 heatmap 생성**, MSE Loss 사용.|
|**HRNet** (High Resolution Net)|✅ 사용함|다양한 해상도의 feature를 유지하면서 heatmap 예측 → MSE Loss 기반 학습.|
|**OpenPose**|✅ 사용함|Part Affinity Fields(PAF)와 confidence heatmap 모두 존재. 둘 다에 대해 각각의 loss 계산 (L2 loss 등).|
|**HigherHRNet**|✅ 사용함|multi-scale feature 기반으로 여러 해상도에서 heatmap을 예측. 역시 MSE Loss 기반.|
|**CenterNet** (pose variant)|❌ 사용하지 않음 (변형)|center point를 heatmap으로 예측하지만, keypoint 좌표는 regression 방식으로 직접 예측 → **L1 또는 L2 loss 사용**.|
|**Pose2Seg**, **DETR 기반 포즈 추정** 등|❌ 사용하지 않음 (transformer 기반 등)|keypoint의 직접 regression 또는 object-centric 방식. heatmap 미사용.|
- **Top-down & Bottom-up 모델 대부분**은 **heatmap → MSE loss** 기반 구조.
    
- 하지만 **CenterNet**, **transformer 기반 모델들 (e.g. TokenPose, PoseDETR)** 등은
    
    - keypoint 위치를 직접 regression하거나
        
    - object center를 예측한 후 offset을 예측하는 방식
        
    - 따라서 **L1/L2 loss 또는 focal loss**를 사용함.
        

### **Data Augmentation**
flip, rotate, scale 등 다양하게 사용
    
### Dataset
    
    - COCO Keypoints
        
    - MPII
        
    - Human3.6M (3D)
        
    - PoseTrack (video)
        

---

## 6. 응용 분야

- 스포츠 분석 (선수 움직임 분석)
    
- 모션 캡처 (애니메이션, 게임)
    
- AR/VR 인터랙션
    
- 헬스케어 자세 분석
    
- 보행 인식 및 이상행동 탐지
    

---

## 7. 확장 주제

- **Temporal Pose Estimation**: 영상 기반으로 시간 정보를 활용
    
- **3D Pose Estimation**: 깊이 추정 포함
    
- **Pose Tracking**: 영상 속 여러 사람을 시간 축에서 추적
    
- **Mesh Estimation**: 3D 메시 구조까지 예측 (예: SMPL)
    

---

## 📌 정리


## 🔍 GT Heatmap이란?

보통 다음과 같이 생성됨:

- 관절 위치에 **2D Gaussian**을 얹어서 각 keypoint에 대해 GT heatmap 생성
    
- 예측 heatmap과의 **픽셀 단위 MSE 계산**이 주요 loss
    

---

궁금하다면 **regression 기반 포즈 추정**과 **heatmap 기반 추정**을 비교하는 문서도 만들어줄 수 있어.  
더 들어가보고 싶은 주제가 있어?