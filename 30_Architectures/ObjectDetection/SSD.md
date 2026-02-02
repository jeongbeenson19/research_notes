# SSD (Single Shot MultiBox Detector)

---

**SSD**는 [[YOLOv1]]과 같이 제안(Proposal) 단계를 제거하고 하나의 네트워크에서 직접 위치 추정(Localization)과 분류(Classification)를 수행하는 **1-Stage Detector**입니다. YOLO의 속도 이점을 유지하면서 정확도를 크게 개선한 모델로, 2016년에 발표되었습니다.

핵심 아이디어는 **다양한 스케일의 특징 맵(Multi-scale Feature Maps)** 을 사용하여 여러 크기의 객체를 효과적으로 탐지하는 것입니다.

## 1. 핵심 특징

### **1) 다중 스케일 특징 맵 (Multi-scale Feature Maps)**

SSD의 가장 중요한 특징은 VGG-16과 같은 기본 네트워크(Base Network)의 중간 특징 맵과, 그 뒤에 추가된 여러 컨볼루션 레이어들의 특징 맵을 모두 예측에 사용한다는 점입니다.

-   **고해상도 특징 맵 (앞쪽 레이어)**: 상대적으로 해상도가 높은 초기 특징 맵에서는 **작은 객체**를 탐지합니다. 풍부한 공간 정보를 가지고 있기 때문입니다.
-   **저해상도 특징 맵 (뒤쪽 레이어)**: 깊은 레이어를 통과하며 압축된 저해상도 특징 맵에서는 **큰 객체**를 탐지합니다. 수용 영역(Receptive Field)이 넓어 이미지의 전역적인 문맥을 파악하기 유리하기 때문입니다.

이 구조 덕분에 SSD는 YOLO와 달리 다양한 크기의 객체에 강건하게 대응할 수 있습니다.
*<p align="center">SSD의 다중 스케일 특징 맵 구조</p>*

### **2) 디폴트 박스 (Default Boxes)와 종횡비 (Aspect Ratios)**

SSD는 [[Faster R-CNN]]의 앵커 박스(Anchor Box)와 유사한 개념인 디폴트 박스(Default Box)를 사용합니다.

-   각 특징 맵의 모든 위치(셀)마다, 미리 정의된 여러 크기(scale)와 종횡비(aspect ratio)를 가진 디폴트 박스를 생성합니다.
-   네트워크는 이 디폴트 박스를 기준으로 실제 객체의 위치와 얼마나 차이가 나는지(offset)와 클래스 확률을 예측합니다.
-   예를 들어, 특정 특징 맵에서는 `{1, 2, 1/2}` 와 같은 종횡비를, 다른 특징 맵에서는 `{1, 2, 3, 1/2, 1/3}` 과 같은 다양한 종횡비를 적용하여 여러 형태의 객체를 탐지할 수 있도록 설계합니다.

### **3) 완전 컨볼루션 구조 (Fully Convolutional)**

기본 네트워크(VGG-16)에서 FC 레이어를 컨볼루션 레이어로 변환하고, 그 뒤에 탐지를 위한 보조 컨볼루션 레이어들을 추가하여 완전 컨볼루션 네트워크(FCN) 형태를 가집니다. 이로 인해 어떤 크기의 입력 이미지에도 대응할 수 있으며, 계산 효율성이 높습니다.

## 2. 학습 과정

### **1) 매칭 전략 (Matching Strategy)**

학습 시, 각 Ground-Truth 박스를 어떤 디폴트 박스와 매칭시켜 학습할지 결정해야 합니다.

1.  **Jaccard Overlap (IoU)**: 먼저, 각 Ground-Truth 박스에 대해 가장 IoU가 높은 디폴트 박스를 positive 샘플로 매칭합니다.
2.  **임계값 (Threshold)**: 그 후, 아직 매칭되지 않은 디폴트 박스들 중에서 특정 Ground-Truth 박스와의 IoU가 0.5 이상인 것들을 모두 positive 샘플로 추가합니다.

이를 통해 하나의 Ground-Truth 박스가 여러 개의 디폴트 박스에 할당될 수 있어 학습을 용이하게 합니다.

### **2) 손실 함수 (Loss Function)**

손실은 **위치 손실(Localization Loss)** 과 **분류 손실(Confidence Loss)** 의 합으로 구성됩니다.

-   **위치 손실 (L_loc)**: Positive로 매칭된 디폴트 박스들에 대해서만 계산됩니다. Smooth L1 Loss를 사용하여 박스의 중심 좌표(cx, cy)와 너비/높이(w, h)의 차이를 최소화합니다.
-   **분류 손실 (L_conf)**: Positive와 Negative 샘플 모두에 대해 계산됩니다. Softmax Loss를 사용하여 각 박스의 클래스(배경 포함)를 예측합니다.

$$ L(x, c, l, g) = \frac{1}{N}(L_{conf}(x, c) + \alpha L_{loc}(x, l, g)) $$

-   `N`: 매칭된 디폴트 박스의 수
-   `α`: 두 손실의 가중치를 조절하는 파라미터 (보통 1로 설정)

### **3) 하드 네거티브 마이닝 (Hard Negative Mining)**

객체가 없는 배경(Negative) 디폴트 박스의 수가 객체가 있는(Positive) 박스 수보다 압도적으로 많습니다. 이 클래스 불균형 문제를 해결하기 위해, 분류 손실이 높은 Negative 샘플들만 골라 학습에 사용합니다. 보통 Positive와 Negative 샘플의 비율을 1:3 정도로 유지합니다.

## 3. 장단점

### **장점**

-   **빠른 속도**: 1-Stage Detector로서 실시간 탐지가 가능할 정도로 빠릅니다. (VOC2007 test 기준, 59 FPS)
-   **높은 정확도**: 다중 스케일 특징 맵 덕분에 YOLOv1보다 훨씬 높은 정확도(mAP)를 달성했습니다.
-   **유연성**: 기본 네트워크를 다른 모델(e.g., ResNet)로 교체하여 성능을 조절하기 용이합니다.

### **단점**

-   **작은 객체 탐지 성능**: 다중 스케일 구조에도 불구하고, 여전히 매우 작은 객체에 대한 탐지 성능은 2-Stage Detector에 비해 상대적으로 낮습니다. 이는 초기 레이어의 특징이 충분히 정제되지 않았기 때문일 수 있습니다.
-   **복잡한 하이퍼파라미터**: 디폴트 박스의 크기, 종횡비, 개수 등을 데이터셋에 맞춰 신중하게 설계해야 하는 번거로움이 있습니다.

---

## 연관 개념

-   [[30_Architectures/ObjectDetection/YOLOv1]]
-   [[Faster R-CNN]]
-   [[30_Architectures/Components/Feature Pyramid Network|Feature Pyramid Network]]
