
# RoIAlign (Region of Interest Align)

---

## **🧠 기본 개념**

**RoIAlign**은 [[RoIPool]]의 양자화(quantization)로 인한 위치 불일치(misalignment) 문제를 해결하기 위해 [[Mask R-CNN]]에서 제안된 feature 추출 방식입니다. 양자화를 수행하지 않고 **[[Bilinear Interpolation|쌍선형 보간법(bilinear interpolation)]]** 을 사용하여 픽셀 수준의 정밀한 정렬(alignment)을 구현합니다.

- **목적**: RoI와 추출된 feature 간의 공간적 위치를 정확하게 정렬하여 고품질의 feature map 생성.
- **핵심 아이디어**: **"양자화 없는(quantization-free)"** RoI pooling.
- **적용 모델**: [[Mask R-CNN]] 및 후속 모델들.

---

## **⚙️ 작동 방식**

RoIAlign은 [[RoIPool]]의 양자화 단계를 제거하고 다음과 같이 작동합니다.

1.  **RoI Projection**: 원본 이미지의 RoI를 feature map 좌표계로 투영합니다. 이때 좌표는 **소수점(floating-point)을 그대로 유지**합니다.
2.  **Grid Division**: 투영된 RoI를 목표 크기(e.g., $k 	imes k$)의 bin으로 나눕니다. bin의 경계 역시 소수점 좌표를 유지합니다.
3.  **Sampling Points**: 각 bin 내에서 4개(또는 그 이상)의 샘플링 포인트를 규칙적으로 선택합니다. 이 포인트들의 좌표 또한 소수입니다.
4.  **Bilinear Interpolation**: 각 샘플링 포인트의 값은 feature map 상에서 가장 가까운 4개의 픽셀 값을 사용하여 **[[Bilinear Interpolation|쌍선형 보간법]]**으로 계산합니다. 이를 통해 정수 grid에 얽매이지 않는 정확한 feature 값을 얻을 수 있습니다.
5.  **Aggregation**: 각 bin의 최종 값은 4개 샘플링 포인트 값의 평균(average pooling) 또는 최댓값(max pooling)으로 결정됩니다.

---

## **✅ 장점**

- **완벽한 정렬(Perfect Alignment)**: 입력 RoI와 추출된 feature 간의 픽셀 단위 정렬을 보장합니다.
- **성능 향상**: 위치 불일치 문제를 해결함으로써, 특히 **인스턴스 분할(instance segmentation)**과 같이 픽셀 수준의 정밀도가 요구되는 태스크에서 큰 성능 향상(Mask AP 기준 10-50% 상대적 향상)을 가져옵니다.
- **일반성**: 객체 탐지(object detection)와 같은 다른 태스크의 성능도 소폭 향상시킵니다.

---

## **🆚 RoIPool vs. RoIAlign**

|특징|[[RoIPool]]|**RoIAlign**|
|---|---|---|
|**좌표 처리**|양자화 (Quantization)|**연속 좌표 (Floating-point)**|
|**값 계산**|Max Pooling|**[[Bilinear Interpolation|쌍선형 보간법 (Bilinear Interpolation)]]**|
|**정렬**|불일치 발생 (Misaligned)|**완벽한 정렬 (Perfectly Aligned)**|
|**주요 사용처**|객체 탐지|**인스턴스 분할**, 고정밀 탐지|

---

## **📌 요약**

|항목|설명|
|---|---|
|**목적**|위치 불일치 없이 가변 크기 RoI → 고정 크기 Feature Map|
|**핵심 연산**|[[Bilinear Interpolation|쌍선형 보간법 (Bilinear Interpolation)]]|
|**장점**|**픽셀 단위의 완벽한 정렬**, 분할 태스크 성능 대폭 향상|
|**단점**|RoIPool 대비 약간의 계산량 증가|
