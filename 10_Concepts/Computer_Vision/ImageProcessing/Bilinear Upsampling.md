# 이중선형 업샘플링 (Bilinear Upsampling)

---

**이중선형 업샘플링**은 [[Bilinear Interpolation|이중선형 보간법]]을 사용하여 이미지나 특징 맵(feature map)의 해상도를 높이는 기법입니다. 주로 딥러닝, 특히 컴퓨터 비전 분야에서 저해상도 특징 맵을 고해상도로 복원할 때 널리 사용됩니다.

## 특징

-   **작동 방식:** 출력 이미지의 각 픽셀 위치에 대응하는 원본 이미지의 좌표를 계산한 후, 해당 좌표 주변의 4개 픽셀 값을 이용하여 [[Bilinear Interpolation|이중선형 보간법]]으로 새로운 픽셀 값을 계산합니다.
-   **속도와 품질:** [[Nearest Neighbor Interpolation|최근접 이웃 보간법]]보다는 부드러운 결과를 제공하며, [[Bicubic Upsampling|바이큐빅 업샘플링]]보다는 계산 속도가 빠릅니다. 이 때문에 속도와 품질 사이의 적절한 균형을 제공합니다.
-   **학습 가능 파라미터 부재:** 이중선형 업샘플링은 고정된 연산이며, 컨볼루션 레이어와 달리 학습해야 할 가중치(weight)가 없습니다. 이는 모델의 복잡도를 낮추는 데 기여합니다.

## 주요 사용 사례

-   **Semantic Segmentation:** U-Net, FCN(Fully Convolutional Networks)과 같은 모델에서 인코더를 통해 압축된 특징 맵을 다시 원본 이미지 크기로 복원(디코딩)하는 과정에서 사용됩니다.
-   **Super-Resolution:** 저해상도 이미지를 고해상도 이미지로 변환하는 모델의 마지막 단계에서 사용될 수 있습니다.

---

## 연관 개념

-   [[Bilinear Interpolation]]
-   [[Bicubic Upsampling]]
-   [[Deconvolutional Networks|Transposed Convolution (Deconvolution)]]
