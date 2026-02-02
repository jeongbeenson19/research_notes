
# RoIPool (Region of Interest Pooling)

---

## **🧠 기본 개념**

**RoIPool**은 다양한 크기의 RoI(Region of Interest)로부터 고정된 크기의 feature map을 추출하는 연산입니다. 이는 [[Fast R-CNN]]에서 제안되었으며, 2-stage object detector에서 RoI-specific feature를 분류 및 박스 회귀 헤드에 전달하기 위한 필수적인 과정입니다.

- **목적**: 가변적인 크기의 RoI를 고정된 크기(e.g., $7 \times 7$)의 feature representation으로 변환.
- **적용 모델**: [[Fast R-CNN]], [[Faster R-CNN]] 등

---

## **⚙️ 작동 방식**

RoIPool은 다음과 같은 순서로 작동합니다.

1.  **RoI Projection**: 원본 이미지에 있는 RoI(bounding box)를 feature map의 좌표계로 투영(projection)합니다.
2.  **Quantization (양자화)**: 투영된 RoI의 좌표를 feature map의 grid에 맞추기 위해 **정수로 변환**합니다. 이 과정에서 소수점 좌표가 버려지면서 첫 번째 위치 불일치(misalignment)가 발생합니다.
3.  **Grid Division**: 양자화된 RoI 영역을 목표하는 출력 크기(e.g., $7 \times 7$)의 bin으로 나눕니다. 이 과정에서 bin의 경계가 다시 **정수로 변환**되면서 두 번째 위치 불일치가 발생합니다.
4.  **Max Pooling**: 각 bin에 포함된 feature map 값들 중에서 최댓값을 선택(max pooling)하여 해당 bin의 대표값으로 사용합니다.

---

## **⚠️ 한계: 위치 불일치 (Misalignment)**

RoIPool의 가장 큰 단점은 **두 번의 양자화 과정**에서 발생하는 **위치 불일치**입니다.

- **원인**: 연속적인(floating-point) 좌표를 불연속적인(integer) grid에 강제로 맞추기 때문에 발생합니다.
- **문제점**:
    - 원본 RoI와 추출된 feature 간의 공간적 정합성이 깨집니다.
    - 이 오차는 객체 탐지(object detection)에서는 비교적 문제가 적을 수 있지만, 픽셀 단위의 정밀함이 요구되는 **인스턴스 분할(instance segmentation)** 에서는 치명적인 성능 저하를 유발합니다.

이러한 문제를 해결하기 위해 [[Mask R-CNN]]에서는 [[RoIAlign]]이 제안되었습니다.

---

## **📌 요약**

|항목|설명|
|---|---|
|**목적**|가변 크기 RoI → 고정 크기 Feature Map|
|**핵심 연산**|좌표 양자화 + Max Pooling|
|**장점**|간단하고 빠르며, 분류/회귀 헤드에 고정된 입력 제공|
|**단점**|**양자화로 인한 위치 불일치(Misalignment)**|
|**대안**|[[RoIAlign]] ([[Bilinear Interpolation|쌍선형 보간법]] 사용)|
