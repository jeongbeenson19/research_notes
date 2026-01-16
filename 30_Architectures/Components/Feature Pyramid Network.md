
## 📘 Feature Pyramid Network (FPN)

### 🔷 정의

> **Feature Pyramid Network (FPN)** 는 CNN에서 추출된 다양한 해상도의 feature map을 결합하여,  
> **고해상도에서의 세밀한 위치 정보와 저해상도에서의 추상적인 의미 정보를 동시에 활용**하는 구조이다.  
> Object Detection, Pose Estimation, Instance Segmentation 등에서 널리 사용된다.

---

### 🔷 설계 목적

- CNN은 레이어가 깊어질수록 feature는 **semantic-rich**해지지만 **해상도는 낮아짐**
    
- 반면 shallow한 layer는 **spatially rich**하지만 **semantic 약함**
    
- FPN은 이 두 가지 특성을 융합해 **multi-scale object / keypoint 인식** 성능을 향상시킴
    

---

### 🔷 구조 구성

#### 1. Bottom-up Pathway

- 일반적인 CNN forward pass (ex. ResNet의 `conv2_x` ~ `conv5_x`)
    
- 각 레이어에서 feature 추출 → C2, C3, C4, C5로 명명
    

#### 2. Top-down Pathway

- 높은 레벨(C5)부터 시작해서 점진적으로 **upsample**
    
- `2× upsample` → 상위 레벨 feature map을 아래로 전파
    

#### 3. Lateral Connections

- 각 레벨의 **bottom-up feature (Cℓ)**에 대해 1×1 conv 적용
    
- 이를 top-down feature와 **element-wise add**
    
- 이후 3×3 conv로 혼합된 feature를 보정
    

---

### 🔷 연산 흐름 (예: ResNet-50 기반)

|Stage|Bottom-up Feature|Top-down 처리|FPN 출력 이름|
|---|---|---|---|
|C5|7×7, 2048ch|그대로 사용|P5|
|C4|14×14, 1024ch|↑ + 1×1(C4)|P4|
|C3|28×28, 512ch|↑ + 1×1(C3)|P3|
|C2|56×56, 256ch|↑ + 1×1(C2)|P2|

각 `Pℓ`는 다양한 크기의 객체에 대응하기 위한 multi-scale feature로 사용됨.

---

### 🔷 주요 특징 요약

|항목|설명|
|---|---|
|🧠 구조|Top-down upsampling + lateral 1×1 conv|
|🧱 입력|C2~C5 (보통 ResNet 기반 feature)|
|🧩 출력|P2~P5 (같은 해상도로 정렬된 multi-scale features)|
|💡 장점|semantic-rich + spatially precise 정보 동시 활용|
|⚙️ 사용처|Mask R-CNN, RetinaNet, CPN, Detectron2 등|

---

### 🔷 대표 활용 사례

1. **RetinaNet**
    
    - P3~P7 feature pyramid 사용
        
    - Focal Loss로 class imbalance 보완
        
2. **[[Mask R-CNN]]**
    
    - P2~P5 사용
        
    - 각 scale에서 ROI Align 수행
        
3. **[[Cascaded Pyramid Network|CPN (Pose Estimation)]]**
    
    - [[GlobalNet|GlobalNe]]t에서 FPN 구조 사용 → multi-resolution keypoint 히트맵 생성
        

---

### 🔷 구현 요점 (PyTorch 개념 코드)

```python
# 예시: top-down upsampling + lateral add
P5 = conv1x1(C5)
P4 = conv1x1(C4) + F.interpolate(P5, scale_factor=2)
P3 = conv1x1(C3) + F.interpolate(P4, scale_factor=2)
P2 = conv1x1(C2) + F.interpolate(P3, scale_factor=2)

# optional: 3x3 conv after fusion
P2 = conv3x3(P2)
P3 = conv3x3(P3)
P4 = conv3x3(P4)
P5 = conv3x3(P5)
```

---

### 📌 요약 문장

> **FPN은 CNN의 계층적 구조를 활용하여 semantic-rich하면서도 spatially precise한 multi-scale feature를 생성하는 구조로**,  
> 다양한 크기의 객체를 정밀하게 인식하거나 keypoint를 정확히 추정하는 데 매우 효과적이다.

---
