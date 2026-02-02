## **🧠 기본 개요**

|**항목**|**내용**|
|---|---|
|이름|**Mask R‑CNN**|
|발표|**ICCV 2017 (Marr Prize, Best Paper)**|
|저자|Kaiming He, Georgia Gkioxari, Piotr Dollár, Ross Girshick (FAIR)|
|논문|_Mask R‑CNN_ (arXiv:1703.06870)|
|핵심 아이디어|**[[Faster R-CNN]]**에 **병렬 mask 분기(FCN head)**와 **RoIAlign**을 추가하여 **instance segmentation**을 End‑to‑End로 수행|

근거: 논문 원문 요약 및 저자/연도, 5fps 언급. Marr Prize(최우수논문상) 수상.

---

## **📌 문제 설정과 한계**

- **Instance segmentation**은 객체 탐지(bounding box)와 시맨틱 분할(pixel-level classification)을 결합한 고난도 문제입니다. 각 인스턴스의 정확한 픽셀 단위 마스크를 예측해야 합니다.
- [[Faster R-CNN]]과 같은 2-stage detector는 RoI(Region of Interest)를 추출한 후, RoIPool을 사용하여 고정된 크기의 feature map을 만듭니다.
- **RoIPool의 한계**: RoIPool은 RoI의 좌표를 feature map의 grid에 맞추기 위해 **두 번의 양자화(quantization)** 를 수행합니다.
    1.  RoI 경계를 정수로 변환
    2.  정수 경계의 RoI를 고정된 수($k \times k$)의 bin으로 분할할 때, bin 경계를 다시 정수로 변환
- 이 과정에서 발생하는 **위치 불일치(misalignment)** 는 픽셀 단위의 정밀한 마스크 예측에 치명적인 오차를 유발합니다.

---

## **🚀 핵심 아이디어**

> **(1) RoIAlign으로 정밀한 특성 정렬** + **(2) 분류/박스 분기와 병렬인 마스크 분기**
> **(3) 클래스 예측과 마스크 예측을 분리(decouple)** → 각 클래스별 **이진 마스크**를 독립적으로 예측

- **RoIAlign**: 양자화를 제거하고 **[[Bilinear Interpolation|쌍선형 보간법(bilinear interpolation)]]** 을 사용하여 RoI 내의 각 샘플링 포인트에서 feature 값을 정밀하게 계산합니다. 이를 통해 입력과 추출된 feature 간의 공간적 정합성을 완벽하게 보존합니다.
- **병렬 마스크 분기**: 기존 Faster R-CNN의 분류 및 박스 회귀 헤드에 병렬로 마스크 예측을 위한 작은 FCN(Fully Convolutional Network)을 추가합니다. 이는 멀티태스크 학습을 효율적으로 만듭니다.
- **분리된 예측(Decoupled Prediction)**: 클래스 예측과 마스크 예측을 분리합니다. 마스크 분기는 클래스에 상관없이 K개의 이진 마스크(클래스당 1개)를 생성합니다. 이는 클래스 간 경쟁을 없애고 학습을 안정화시켜 성능을 크게 향상시킵니다.

---

## **🏗️ 전체 구조 (모듈 요약)**

```
[Input Image]
   ↓
[Backbone (ResNet-50/101) + FPN 권장]
   ↓
[Feature Pyramid Maps]
   ├─ RPN → Proposals
   └─ RoIAlign → RoI Features (e.g., 7x7x256)
          ├─ Detection Head (Cls + Box)
          └─ Mask Head (FCN: conv×4 → deconv → m×m mask per class)
```

- **Backbone**: ResNet, ResNeXt 등 다양한 아키텍처를 사용할 수 있으며, **FPN(Feature Pyramid Network)** 과 함께 사용하는 것이 성능과 속도 면에서 가장 권장됩니다.
- **Head**: 각 RoI에 대해 분류(classification), 박스 회귀(box regression), 마스크 예측(mask prediction)을 동시에 수행합니다.

---

## **🔍 구성요소 상세**

### **1) [[Faster R-CNN#^e27b20|RPN (Region Proposal Network)]]

- [[Faster R-CNN]]과 동일한 프로토콜을 사용합니다. 앵커(5가지 scale, 3가지 비율)를 사용하여 RoI 후보를 생성하고 NMS를 적용합니다.

### **2) RoIAlign vs. RoIPool**

**RoIAlign**은 Mask R-CNN의 핵심 혁신 중 하나로, RoIPool의 양자화 오차를 해결합니다.

| 특징            | **RoIPool**            | **RoIAlign**                                                     |     |
| ------------- | ---------------------- | ---------------------------------------------------------------- | --- |
| **좌표 처리**     | **양자화 (Quantization)** | **연속 좌표 (Floating-point)**                                       |     |
| **값 계산**      | Max Pooling            | **[[Bilinear Interpolation\|쌍선형 보간법 (Bilinear Interpolation)]]** |     |
| **정렬**        | 입력-특성 불일치 발생           | **완벽한 정렬 (Perfect Alignment)**                                   |     |
| **성능 (Mask)** | 낮음 (특히 작은 객체)          | **높음 (AP 10-50% 상대적 향상)**                                        |     |

#### 💡 "Bin"이란?
"Bin"은 RoI pooling 과정에서 RoI를 고정된 크기(e.g., $k \times k$)로 나누었을 때 생기는 각각의 작은 사각형 구역(sub-region or cell)을 의미합니다. 예를 들어, $100 \times 100$ 크기의 RoI를 $7 \times 7$ 크기의 feature map으로 만들고 싶다면, RoI를 $7 \times 7=49$개의 bin으로 나눕니다. 그리고 각 bin으로부터 하나의 대표 값(e.g., max value)을 추출하여 최종 $7 \times 7$ feature map의 한 픽셀 값을 구성하게 됩니다.

- **RoIAlign 작동 방식**:
    1.  양자화 없이 RoI를 그대로 사용합니다.
    2.  RoI를 $k \times k$ 개의 bin으로 나눕니다 (bin 경계도 float).
    3.  각 bin에서 4개의 샘플링 포인트를 규칙적으로 선택합니다.
    4.  각 샘플링 포인트의 값은 feature map에서 가장 가까운 4개 픽셀 값을 사용하여 **[[Bilinear Interpolation|쌍선형 보간법]]** 으로 계산합니다.
    5.  각 bin의 값은 4개 샘플링 포인트 값의 평균 또는 최댓값(max/average pooling)으로 결정됩니다.


### **3) Detection Head (Cls/Box)**

- [[Faster R-CNN]]의 헤드와 거의 동일한 구조를 가집니다. RoIAlign으로 추출된 feature를 받아 분류 점수와 박스 오프셋을 예측합니다.

### **4) Mask Head (FCN)**

- **구조**: RoIAlign으로 추출된 $14 \times 14$ feature map에 대해 4개의 3x3 Conv 레이어(256 채널)를 순차적으로 적용한 후, 2x2 Deconv(Upsampling) 레이어를 통해 최종적으로 $28 \times 28$ 크기의 마스크를 출력합니다.
- **출력**: RoI당 **K개의 이진 마스크**($K$는 클래스 수)를 출력합니다. 각 마스크는 특정 클래스에 대한 예측을 나타냅니다.
- **활성화 함수**: 클래스 간 독립적인 예측을 위해 **per-pixel sigmoid**를 사용합니다. (Softmax는 클래스 간 경쟁을 유발하여 부적합)
- **학습**: Ground-truth 클래스가 **k**일 경우, 오직 **k번째 마스크**에 대해서만 손실을 계산합니다. 이는 **클래스 예측과 마스크 생성을 분리**하는 핵심적인 설계입니다.

---

## **🧮 손실 함수 (Multi-task)**

$$
\mathcal{L} = \mathcal{L}_{cls} + \mathcal{L}_{box} + \mathcal{L}_{mask} $$

- $\mathcal{L}_{cls}$: 분류 손실 (Cross-Entropy)
- $\mathcal{L}_{box}$: 박스 회귀 손실 (Smooth L1)
- $\mathcal{L}_{mask}$: **평균 이진 교차 엔트로피 (Average Binary Cross-Entropy)**
    - RoI가 ground-truth 클래스 $k$와 매칭되면, $\mathcal{L}_{mask}$는 $k$번째 마스크에 대해서만 계산됩니다.
    - $m \times m$ 크기의 마스크에 대해 픽셀 단위로 sigmoid를 적용하고 BCE 손실을 계산합니다.

이러한 손실 함수 설계는 클래스 예측과 마스크 예측의 의존성을 제거하여 각 태스크가 전문화되도록 유도하고, 결과적으로 전체 성능을 향상시킵니다.

---

## **📈 성능 및 지표**

- **COCO test-dev (ResNet-101-FPN)**: **Mask AP 35.7**, AP50 58.0, AP75 37.8을 기록하며 당시 모든 instance segmentation 모델을 압도하는 SOTA 성능을 달성했습니다.
- **객체 탐지 성능 향상**: 멀티태스크 학습의 부가 효과로, 동일한 백본을 사용하는 Faster R-CNN보다 **박스 탐지 AP(Box AP)도 향상**되었습니다.
- **속도**: ResNet-101-FPN 백본과 NVIDIA Tesla M40 GPU 사용 시, 이미지당 **~195ms (약 5 fps)**의 추론 속도를 보입니다.

---

## **📊 주요 실험 분석 (Ablation Analysis)**

|실험|설정|Mask AP|결론|
|---|---|---|---|
|**정렬 방식**|RoIPool vs. **RoIAlign**|~3%p 향상|**RoIAlign**의 효과가 결정적임|
|**마스크 예측**|MLP vs. **FCN**|~2%p 향상|**FCN**이 공간 구조 유지에 유리|
|**활성화 함수**|Softmax vs. **Sigmoid**|~0.5%p 향상|**Sigmoid**를 통한 클래스 분리가 효과적|
|**멀티태스크**|Mask R-CNN vs. 독립 모델|~1.5%p 향상|**공동 학습(Joint Training)**이 성능 향상에 기여|

---

## **🤸‍♀️ 확장성: 사람 자세 추정 (Human Pose Estimation)**

Mask R-CNN 프레임워크는 instance segmentation 외 다른 태스크로도 쉽게 확장될 수 있습니다.

- **Keypoint 예측**: 마스크 분기를 약간 수정하여 사람의 신체 부위(keypoint) 위치를 예측하는 태스크에 적용할 수 있습니다.
- **방법**: 마스크처럼 각 keypoint($K$개)에 대해 one-hot 인코딩된 $m \times m$ 마스크를 예측하도록 학습합니다.
- **결과**: COCO keypoint 데이터셋에서 추가적인 기법 없이도 SOTA 경쟁력을 보여주며 프레임워크의 **일반성과 유연성**을 입증했습니다.

---

## **✅ 한 문장 요약**

> **Mask R‑CNN은 RoIAlign과 per‑class 이진 마스크 분기를 더한 Faster R‑CNN 기반의 단순·강력한 프레임워크로, 탐지/분할을 통합한 인스턴스 수준 인식에서 당시 SOTA를 달성했다.**

---

## **📌 요약 정리**

|**항목**|**설명**|
|---|---|
|구조|**Backbone(+FPN)** + **RPN** + **RoIAlign** + **[Cls/Box] Head** + **[Mask] FCN Head**|
|핵심 혁신|**RoIAlign(정밀 정렬)**, **클래스·마스크 예측 분리**, **per‑pixel sigmoid**|
|속도|**~5 fps**(ResNet‑101‑FPN, Tesla M40)|
|정확도|**Mask AP 35.7 (COCO test‑dev, R‑101‑FPN)**|
|End‑to‑End|✔️ (탐지/분할 멀티태스크)|
|확장성|**Keypoint(포즈) 예측**으로도 손쉽게 확장 (동일 프레임워크)|

근거: 논문 본문/표/섹션(구조/손실/속도/성능/확장성).

---

## **🔁 후속 발전(참고)**

- **Mask Scoring R‑CNN**(마스크 품질 추정), **HTC(Hybrid Task Cascade)**, **Detectron2 구현체** 등 다양한 변종/프레임워크로 파생. _(요약 참고용)_
