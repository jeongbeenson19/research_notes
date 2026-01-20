
## 🧠 개요: R-CNN이란?

| 항목      | 내용                                                                                   |
| ------- | ------------------------------------------------------------------------------------ |
| 이름      | R-CNN: Regions with CNN features                                                     |
| 발표      | 2014, CVPR                                                                           |
| 제안자     | Ross Girshick et al. (UC Berkeley, Facebook AI)                                      |
| 논문      | [[Rich feature hierarchies for accurate object detection and semantic segmentation]] |
| 핵심 아이디어 | Selective Search로 추출한 Region Proposal을 CNN으로 분류 및 회귀 수행                              |

---

## 📌 배경: 왜 R-CNN이 혁신적이었나?

### 기존의 object detection (pre-2014):

- **Hand-crafted features**: HOG, SIFT + SVM
    
- **Sliding window** 방식: 전체 이미지에 걸쳐 모든 위치, 크기에 대해 brute-force 탐색 → 연산 비용 과다
    
- Detection이 분류에 비해 성능이 낮았던 이유: **특징 표현력 부족 + 연산 비효율성**
    

---

## 🧩 핵심 아이디어: CNN 기반 Region-wise Detection

### R-CNN 파이프라인

1. **Region Proposal**
    
    - Selective Search로 이미지에서 약 2000개의 **물체 후보 영역 (region proposals)** 생성
        
2. **Feature Extraction**
    
    - 각 region을 warp하여 (예: 224×224) CNN (AlexNet 등)에 입력
        
    - 마지막 FC layer의 feature vector (4096-dim) 추출
        
3. **Object Classification**
    
    - 각 region의 feature → SVM classifier (class별)로 분류
        
4. **[[Bounding box regression]]**
    
    - CNN feature 기반으로 GT box와의 offset을 학습
        


---

## 🧱 구성 요약

|단계|기술|역할|
|---|---|---|
|Region Proposal|Selective Search|후보 영역 생성|
|Feature Extractor|CNN (AlexNet)|Region별 특징 추출|
|Classifier|SVM|객체 분류|
|BBox Regressor|Linear Regression|정확한 위치 조정|

---

## 🧪 수학적 구성 요소

### [[Bounding box regression]]

목표: GT box $(x,y,w,h)(x, y, w, h)$와 예측 box의 차이를 줄이는 회귀 모델 학습

$$
t_x = (x - x_a) / w_a, \quad t_y = (y - y_a) / h_a, \ldots
$$

- 손실 함수: Smooth L1 loss
    

---

## 🧠 한계점

|문제점|설명|
|---|---|
|**속도**|각 region마다 CNN forward → 연산량 과도 (수천 번 CNN 호출)|
|**훈련 복잡성**|CNN → SVM → BBox regression 각각 따로 학습|
|**end-to-end 아님**|학습 파이프라인이 분리되어 있음|

---

## 📈 성능

|모델|mAP (PASCAL VOC 2007)|
|---|---|
|DPM (기존 방식)|~33%|
|R-CNN (AlexNet)|**~58.5%**|

→ 최초로 deep CNN을 object detection에 성공적으로 적용한 사례

---

## 🔁 이후 발전 흐름

| 모델                                                                    | 특징                               | 개선점                                 |
| --------------------------------------------------------------------- | -------------------------------- | ----------------------------------- |
| **[[30_Architectures/ObjectDetection/Fast R-CNN|Fast R-CNN]](2015)** | ROI Pooling 도입                   | CNN feature를 공유하여 속도 향상             |
| **[[Faster R-CNN]] (2015)**                                           | RPN (Region Proposal Network) 도입 | Selective Search 제거, end-to-end 구조  |
| **YOLO / SSD (2016)**                                                 | Fully convolutional detection    | Region proposal 없이 실시간 detection 가능 |

---

## ✅ 한 문장 요약

> **R-CNN은 Region Proposal과 CNN을 결합하여 객체 탐지의 표현력을 혁신적으로 끌어올린 모델이며, 이후 Fast/Faster R-CNN, YOLO 등의 기반을 마련한 딥러닝 기반 detection의 시초입니다.**

---

필요하다면:

- R-CNN vs Fast R-CNN vs Faster R-CNN 비교표,
    
- PyTorch 기반 구현 구조 설명,
    
- RPN의 수식적 설명  
    도 제공해드릴 수 있습니다.