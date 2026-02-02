---
tags:
  - MILAB
  - ComputerVision
  - CV_Task
---

# Semantic Segmentation

## 1. Semantic Segmentation이란?

> **Semantic Segmentation(의미론적 분할)** 은 이미지의 모든 픽셀을 특정 클래스(class)로 분류하는 컴퓨터 비전의 핵심 작업입니다. 즉, 이미지 내의 모든 픽셀에 대해 "이 픽셀은 자동차에 속한다", "이 픽셀은 사람에 속한다", "이 픽셀은 배경에 속한다"와 같이 의미(semantic)를 부여하는 것입니다.

- **출력**: 입력 이미지와 동일한 크기의 **세그멘테이션 맵(Segmentation Map)** 을 출력합니다. 이 맵의 각 픽셀은 해당 위치의 클래스를 나타내는 정수 값을 가집니다.
- **목표**: 이미지에 **무엇이(what)** 있는지를 픽셀 단위로 정밀하게 이해하는 것입니다.

---

## 2. 다른 객체 인식 작업과의 비교

| 작업 (Task) | 목표 | 출력 형태 |
| --- | --- | --- |
| **Classification** | 이미지 전체에 대한 단일 클래스 예측 | `"고양이"` (Label) |
| **Object Detection** | 이미지 내 객체의 위치와 클래스 예측 | `(x, y, w, h)` + `"고양이"` (Bounding Box + Label) |
| **Semantic Segmentation** | **모든 픽셀**을 해당 클래스로 분류 | `(H, W)` 크기의 **픽셀 단위 마스크** |
| **Instance Segmentation** | **개별 객체**까지 구분하여 픽셀 단위로 분류 | `(H, W)` 크기의 **객체별 마스크** |

- **vs. Object Detection**: 단순히 경계 상자(bounding box)로 객체의 위치를 대략적으로 표시하는 것을 넘어, **객체의 정확한 모양**을 픽셀 단위로 분할합니다.
- **vs. Instance Segmentation**: Semantic Segmentation은 **같은 클래스의 다른 인스턴스(instance)를 구분하지 않습니다.** 예를 들어, 이미지에 자동차 두 대가 있다면 두 대 모두 동일한 '자동차' 클래스로 라벨링합니다. 반면, Instance Segmentation은 이를 '자동차1', '자동차2'로 구분합니다.

---

## 3. 주요 아키텍처

Semantic Segmentation 모델은 일반적으로 **인코더-디코더(Encoder-Decoder)** 구조를 따릅니다.

- **인코더 (Encoder)**: 입력 이미지로부터 컨볼루션 연산을 통해 고차원의 의미 정보(semantic information)를 추출합니다. 이 과정에서 피쳐맵의 공간적 해상도는 점차 감소하고 채널 수는 증가합니다. (Downsampling)
- **디코더 (Decoder)**: 인코더가 압축한 피쳐맵을 다시 원래 이미지 크기로 복원하면서, 픽셀별 클래스 예측을 수행합니다. 이 과정에서 공간적 해상도를 높이기 위한 **Upsampling** 기법이 사용됩니다. (예: Transposed Convolution, Upsample + Convolution)

- **대표적인 모델**:
    - **FCN (Fully Convolutional Network)**: 최초로 End-to-End 방식의 Semantic Segmentation을 제안한 모델.
    - **[[U-Net]]**: 의료 이미지 분할을 위해 제안되었으며, 인코더와 디코더 간의 **Skip Connection**을 통해 저수준 특징을 효과적으로 활용하는 구조로 유명합니다.
    - **DeepLab 시리즈**: Atrous(Dilated) Convolution을 사용하여 더 넓은 receptive field를 확보하는 방식으로 높은 성능을 달성했습니다.
    - **[[HRNet]]**: 저해상도로 줄였다가 다시 키우는 대신, **고해상도 피쳐맵을 계속 유지하고 병렬로 처리**하는 방식을 사용합니다.

---

## 4. 주요 응용 분야

- **자율 주행 (Autonomous Driving)**: 도로, 차선, 보행자, 다른 차량, 신호등 등을 픽셀 단위로 정밀하게 인식하여 주행 환경을 이해하는 데 필수적입니다.
- **의료 영상 분석 (Medical Imaging)**: MRI나 CT 이미지에서 종양, 장기, 병변 등의 영역을 자동으로 분할하여 의사의 진단을 보조합니다.
- **위성 이미지 분석 (Geospatial Analysis)**: 위성 사진에서 숲, 강, 건물, 농경지 등 다양한 지형지물을 자동으로 분류하고 분석합니다.
- **증강 현실 (Augmented Reality)**: 배경과 사람, 특정 객체를 정밀하게 분리하여 가상의 객체를 자연스럽게 합성하는 데 사용됩니다.