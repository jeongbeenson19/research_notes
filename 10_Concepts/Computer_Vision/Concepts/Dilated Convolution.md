---
tags:
  - MILAB
  - ComputerVision
  - CoreConcept
  - CNN
---

# Dilated Convolution (Atrous Convolution)

## 1. Dilated Convolution이란?

> **Dilated Convolution**은 **Atrous Convolution** (프랑스어로 `à trous` - 구멍이 있는)이라고도 불리며, 컨볼루션 커널(kernel) 내부에 일정한 간격(hole)을 주어 **추가적인 파라미터나 연산량 없이 Receptive Field(수용 영역)를 확장**하는 컨볼루션 기법입니다.

- **작동 원리**: **Dilation Rate**라는 새로운 하이퍼파라미터를 도입합니다.
    - **Dilation Rate (r)**: 커널의 원소들 사이에 얼마나 많은 공간을 둘지를 결정합니다.
    - `r=1`이면 표준적인(standard) 컨볼루션과 동일합니다.
    - `r > 1`이면, 커널이 `r-1`개의 픽셀을 건너뛰며 연산을 수행합니다.

- **예시**: 3x3 커널에 `dilation rate = 2`를 적용하면, 실제 커널의 가중치 수는 9개로 동일하지만, 입력 피쳐맵에서는 5x5 영역에 해당하는 Receptive Field를 갖게 됩니다.

---

## 2. 왜 Dilated Convolution을 사용하는가?

기존의 CNN에서는 Receptive Field를 넓히기 위해 주로 **Pooling Layer**를 사용하거나 **Stride**를 크게 설정했습니다. 하지만 이 방식들은 **공간적 해상도(spatial resolution)를 감소**시키는 단점이 있습니다.

> **Dilated Convolution**은 **공간적 해상도를 전혀 손상시키지 않으면서** Receptive Field를 효과적으로 넓힐 수 있는 강력한 대안입니다.

### 주요 장점

1.  **더 넓은 Receptive Field**: 파라미터 수를 늘리지 않고도 커널이 더 넓은 영역의 컨텍스트(context)를 파악할 수 있습니다.
2.  **공간 해상도 유지**: Pooling이나 Stride 없이 Receptive Field를 넓히므로, [[Semantic Segmentation]]이나 [[Pose Estimation|Pose Estimation]]처럼 픽셀 단위의 조밀한(dense) 예측이 필요한 작업에 매우 유리합니다.
3.  **효율적인 연산**: 표준 컨볼루션과 동일한 연산량으로 더 넓은 영역을 커버하므로 효율적입니다.
4.  **다중 스케일 정보 획득**: 서로 다른 Dilation Rate를 가진 여러 Dilated Convolution을 병렬로 사용하면(e.g., Atrous Spatial Pyramid Pooling - ASPP), 다양한 크기의 객체나 컨텍스트를 동시에 파악할 수 있습니다.

---

## 3. 주요 응용 분야

- **[[Semantic Segmentation|Semantic Segmentation]]**: 
    - **DeepLab 시리즈**에서 핵심적인 요소로 사용되었습니다.
    - 해상도 손실 없이 넓은 영역의 컨텍스트를 이해하여, 픽셀 단위 분류의 정확도를 크게 높였습니다.
- **실시간 오디오 생성**:
    - **WaveNet**과 같은 모델에서 이전 시간의 더 넓은 오디오 샘플을 효율적으로 참조하기 위해 사용되었습니다.
- **객체 탐지 (Object Detection)** 및 기타 조밀한 예측이 필요한 다양한 CV 작업에 널리 활용됩니다.
