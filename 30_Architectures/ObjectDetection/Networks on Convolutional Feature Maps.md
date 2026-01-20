
## ✅ 1. 용어 그대로 해석하면?

- **Convolutional Feature Maps**: CNN의 중간 레이어에서 추출된 **특징 맵(Feature Map)**  
    (예: VGG, ResNet의 conv3_x, conv4_x 출력 등)
    
- **Networks on Convolutional Feature Maps**:  
    이 **중간 feature map을 입력으로 다시 네트워크(추가 CNN, RNN 등)** 를 학습하는 방식
    

즉, **이미 학습된 CNN의 출력 특징 맵 위에서 별도의 네트워크를 구성**하는 걸 뜻합니다.

---

## ✅ 2. 왜 이런 접근을 사용하나?

### 🔹 이유

1. **전이 학습(Transfer Learning)**:  
    CNN이 추출한 feature map은 **일반적인 시각적 표현**이므로,  
    이를 기반으로 **다른 task(Detection, Segmentation 등)**를 쉽게 학습 가능
    
2. **다양한 비전 응용**
    
    - **Faster R-CNN**:  
        Region Proposal Network(RPN)을 **CNN의 feature map 위에서 작동**
        
    - **FCN (Fully Convolutional Network)**:  
        분할(Segmentation)을 위해 CNN feature map 위에 upsampling 네트워크 추가
        

---

## ✅ 3. ResNet 논문에서의 맥락

ResNet 논문에서는 **classification뿐 아니라 object detection, segmentation 등** 다양한 task에서 ResNet이 **백본(backbone)** 역할로 사용될 수 있음을 강조하며, 관련 연구를 언급합니다.

예:

- **“Networks on Convolutional Feature Maps”**는 주로 **Faster R-CNN**과 같은 detection pipeline을 지칭
    
- 즉, **ResNet의 convolutional feature map**을 기반으로 추가 네트워크를 얹어 **detection 성능을 향상**시킬 수 있다는 뜻
    

---

## ✅ 4. 한마디 요약

> **“Networks on Convolutional Feature Maps” =  
> CNN이 추출한 중간 feature map을 입력으로 사용하는 후속 네트워크(Detection, Segmentation, RNN 등)를 지칭하는 용어**

즉, **ResNet은 단순 분류기뿐 아니라 다양한 비전 task의 backbone으로 활용 가능**하다는 것을 Related Work에서 강조하기 위해 언급된 것입니다.

---
