
이해해야 할 포인트는:

1. **기존 [[CNN]]의 한계 (고정 input size)**
    
2. **SPP 구조가 이를 어떻게 해결하는가**
    
3. **[[R-CNN]]과의 통합에서 어떤 계산 이득이 있었는가**
    
4. **후속 구조 ([[30_Architectures/ObjectDetection/Fast R-CNN|Fast R-CNN]], [[Faster R-CNN]])에서 어떻게 발전되었는가**
    

---

## 🧠 기본 개요

|항목|내용|
|---|---|
|이름|**SPPNet** (Spatial Pyramid Pooling Network)|
|발표|ECCV 2014|
|제안자|Kaiming He et al. (MSRA, 이후 ResNet 개발 주역)|
|논문|[Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition](https://arxiv.org/abs/1406.4729)|
|핵심 아이디어|CNN 후단에 **Multi-level pooling (SPP)**을 붙여서 **입력 이미지 크기를 고정하지 않고도** feature 추출 가능하게 만듦|

---

## 📌 문제 인식: CNN의 고정 입력 크기 문제

### CNN의 한계:

- AlexNet, VGG 등은 `224×224`처럼 고정된 입력 크기만 처리 가능
    
- Fully connected (FC) layer는 고정된 feature vector 길이 입력을 요구하기 때문
    
- 다양한 크기의 입력 이미지를 처리하려면 **crop or warp** → 정보 손실 발생
    

---

## 🧩 핵심 아이디어: [[Spatial Pyramid Pooling|Spatial Pyramid Pooling (SPP)]]

### 아이디어:

- 마지막 convolution layer의 **feature map**은 크기가 가변적
    
- 이를 다양한 크기로 **공간적으로 나눈 뒤**, 각각에서 **max pooling** 수행
    
- 결과를 flatten해서 FC에 연결 → 항상 **고정 길이의 벡터** 생성 가능
    

### 구조 요약:

SPP layer는 아래와 같은 방식으로 multi-level pooling을 수행:

|Level|Pooling size|생성되는 bin 수|
|---|---|---|
|1×1|Global pooling|1|
|2×2|4개 영역|4|
|4×4|16개 영역|16|
|총합|-|1 + 4 + 16 = 21 bins|

→ 각 bin마다 max pooling → 전체적으로 **고정된 feature vector** 생성

---

### 수식적으로 이해:

1. 입력 feature map 크기: $a \times a$
    
2. 원하는 출력 bin 개수: $n \times n$
    
3. Pooling kernel size: $k = \lceil \frac{a}{n} \rceil$
    
4. Stride: $s = \lfloor \frac{a}{n} \rfloor$
    

이렇게 하면 어떤 feature map 크기에서도 **고정된 pooling 결과**를 얻을 수 있음.

---

## 🏗️ 전체 네트워크 구조 (R-CNN과 연계)

SPPNet은 기존 R-CNN과 달리, **region마다 CNN을 반복 수행하지 않음**:

| 단계              | R-CNN                 | SPPNet                                                   |
| --------------- | --------------------- | -------------------------------------------------------- |
| Region Proposal | [[Selective Search]]  | Selective Search                                         |
| CNN 연산          | Region마다 CNN 수행       | **전체 이미지 1회 CNN 연산**                                     |
| Feature 추출      | 각각의 region warp 후 CNN | **convolution feature map 위에서 SPP로 region-wise pooling** |
| Classifier      | SVM                   | SVM                                                      |

→ 즉, SPPNet은 convolution 연산을 **공유**하고, region마다 feature map 위에서 SPP 수행하여 **속도 대폭 향상**

---

## 📈 성능 개선

|측면|R-CNN|SPPNet|
|---|---|---|
|CNN 연산 수|수천 번 (region마다)|1번 (전체 이미지 기준)|
|Detection 속도|느림|**수십 배 이상 빠름**|
|Accuracy|유사하거나 향상|✔️|

---

## 🔁 Fast R-CNN과의 관계

Fast R-CNN은 SPPNet의 단점을 보완한 구조로, 다음과 같은 차이점이 있음:

|항목|SPPNet|Fast R-CNN|
|---|---|---|
|Region feature 추출|**SPP layer**|**ROI Pooling** (SPP의 고정 grid를 단순화)|
|훈련 방식|여러 stage (CNN, SVM 분리 학습)|**End-to-end** 학습|
|Backpropagation|SPP는 Conv까지만 BP 가능|FC까지 gradient 전파 가능|

즉, **SPPNet은 R-CNN → Fast R-CNN으로 가는 중간 단계**로, 속도 향상과 variable-size input 처리를 동시에 가능케 한 과도기 모델입니다.

---

## ✅ 한 문장 요약

> **SPPNet은 입력 이미지 크기를 고정하지 않아도 되도록 Spatial Pyramid Pooling layer를 도입하여, region-based CNN detection의 효율성과 유연성을 획기적으로 개선한 모델입니다.**

---

## 📌 요약 정리

|개념|설명|
|---|---|
|Spatial Pyramid Pooling|다양한 공간 해상도에서 pooling하여 고정된 feature vector 생성|
|주요 개선점|CNN 반복 제거 → 속도 향상 / 가변 입력 이미지 처리 가능|
|한계점|end-to-end 학습 어려움 (SPP layer 이후 BP 안됨)|
|후속|Fast R-CNN (ROI Pooling + end-to-end), Faster R-CNN (RPN 도입)|

---

필요하시면:

- SPP layer 구현 코드 (PyTorch)
    
- ROI Pooling과 SPP의 비교
    
- SPPNet 이후 detection 아키텍처 발전 계보  
    도 이어서 설명해드릴 수 있습니다.