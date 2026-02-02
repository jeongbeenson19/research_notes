---
tags:
  - MILAB
  - ComputerVision
  - ObjectDetection
  - CoreConcept
---

# Anchor Boxes

## 1. 앵커 박스란 무엇인가? (What is an Anchor Box?)

> **앵커 박스(Anchor Box)** 는 객체 탐지 모델, 특히 [[30_Architectures/ObjectDetection/Faster R-CNN|Faster R-CNN]]과 같은 2-stage detector나 YOLO, SSD와 같은 1-stage detector에서 **객체의 위치를 예측하기 위한 기준이 되는 상자(prior or default box)** 입니다.

- **작동 원리**: CNN을 통과한 컨볼루션 피쳐맵(feature map)의 각 위치(cell)마다, 미리 정의된 **다양한 크기(scale)와 가로세로 비율(aspect ratio)을 가진 여러 개의 가상 박스**를 설정합니다.
- **목표**: 네트워크는 이 수많은 앵커 박스들 중에서 실제 객체(Ground Truth)와 가장 근접한 앵커 박스를 찾고, 이 앵커 박스를 얼마나 이동하고 크기를 조절해야 실제 객체에 정확히 맞출 수 있는지를 학습합니다.

---

## 2. 왜 앵커 박스가 필요한가?

- **객체의 다양한 형태 대응**: 이미지 속 객체들은 크기와 형태가 매우 다양합니다. 앵커 박스는 다양한 크기와 비율의 '틀'을 미리 제공함으로써, 모델이 여러 형태의 객체를 효과적으로 탐지할 수 있게 돕습니다.
- **효율적인 후보 영역 탐색**: [[30_Architectures/ObjectDetection/R-CNN|R-CNN]]에서 사용된 Selective Search처럼 이미지 전체를 탐색하는 방식 대신, 피쳐맵 위에서 정해진 앵커들을 기준으로 후보 영역을 예측하므로 훨씬 효율적이고 빠릅니다.
- **하나의 위치에서 다중 객체 탐지**: 피쳐맵의 한 위치(cell)에서 여러 개의 앵커 박스를 사용하므로, 서로 다른 크기나 비율을 가진 여러 객체가 겹쳐 있을 때도 탐지가 가능합니다.

---

## 3. 앵커 박스의 생성 방식

- **기준**: 피쳐맵의 각 셀(cell) 위치를 중심으로 앵커 박스를 생성합니다.
- **구성 요소**: 일반적으로 **3개의 크기(scale)** 와 **3개의 비율(aspect ratio)** 을 조합하여, 각 셀마다 **k=9**개의 앵커 박스를 생성하는 것이 표준적입니다.
    - **Scale**: {128², 256², 512²}
    - **Aspect Ratio**: {1:1, 1:2, 2:1}
- **총 개수**: (피쳐맵의 가로) x (피쳐맵의 세로) x k
    - 예: 50x38 크기의 피쳐맵과 k=9를 사용하면, 총 50 * 38 * 9 = 17,100개의 앵커 박스가 생성됩니다.

---

## 4. 학습 과정에서의 역할

네트워크(특히 RPN)는 수많은 앵커 박스 각각에 대해 두 가지를 학습합니다.

1.  **객체 여부 분류 (Objectness Score)**
    - 이 앵커 박스가 **객체(positive)인지 배경(negative)인지**를 이진 분류(binary classification)합니다.
    - 이를 위해 각 앵커를 Ground Truth(GT) 박스와의 **IoU(Intersection over Union)** 를 기준으로 레이블링합니다.
        - **Positive Label**: GT 박스와의 IoU가 0.7 이상이거나, 해당 GT 박스와 가장 높은 IoU를 갖는 앵커.
        - **Negative Label**: 모든 GT 박스와의 IoU가 0.3 미만인 앵커.
        - *0.3과 0.7 사이의 애매한 앵커들은 학습에서 제외됩니다.*

2.  **경계 상자 회귀 (Bounding Box Regression)**
    - Positive로 레이블링된 앵커에 한해, 이 앵커를 실제 GT 박스에 정확히 맞추기 위한 **변환값(offset)** 을 예측합니다.
    - 예측 대상은 절대 좌표가 아닌, **앵커 박스 대비 상대적인 변환값** $(t_x, t_y, t_w, t_h)$ 입니다.

이 과정을 통해, 미리 정의된 수많은 '기준 틀'인 앵커 박스들이 점차 실제 객체의 위치와 크기에 맞는 '후보 영역'으로 정교하게 조정됩니다.