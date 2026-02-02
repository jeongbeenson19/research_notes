---
tags:
  - ML
  - CV
  - architecture
  - neural_network
aliases:
  - CNN
  - Convolutional Neural Network
  - 합성곱 신경망
---

# Convolutional Neural Network (CNN)

**Convolutional Neural Network (CNN)**, 즉 합성곱 신경망은 인간의 시각 피질(visual cortex) 구조에서 영감을 받아 설계된 딥러닝 모델입니다. 이미지를 포함한 그리드(grid) 형태의 데이터에서 공간적 계층 구조(spatial hierarchy)를 효과적으로 학습하는 데 특화되어 있습니다.

핵심 아이디어는 **지역 수용 필드(local receptive field)**를 활용해 전체 이미지를 한 번에 보는 대신, **부분적인 특징을 추출**한 뒤 이를 계층적으로 조합해 나가는 것입니다.

## 🧱 주요 구성 요소

### 1. Convolution Layer (합성곱 계층)

입력 데이터에 **필터(Filter 또는 커널, Kernel)**를 슬라이딩하며 적용해 **특징 맵(Feature Map)**을 생성합니다.
-   **필터**: 학습 가능한 파라미터로, 특정 시각적 패턴(예: 수직선, 색상, 질감)을 감지합니다.
-   **Stride**: 필터가 한 번에 이동하는 간격입니다.
-   **Padding**: 출력 크기를 조절하거나 입력 경계의 정보 손실을 막기 위해 입력 데이터 주변을 특정 값(주로 0)으로 채우는 것입니다.

### 2. Activation Function (활성화 함수)

합성곱 계층을 통과한 결과에 비선형성(non-linearity)을 부여합니다. 주로 **ReLU(Rectified Linear Unit)**가 사용됩니다.
`ReLU(x) = max(0, x)`

### 3. Pooling Layer (풀링 계층)

특징 맵의 공간적 크기(가로, 세로)를 줄여 연산량을 감소시키고, 작은 위치 변화에 모델이 덜 민감하게(translation invariance) 만듭니다. **Max Pooling**이 가장 널리 사용됩니다.

### 4. Fully Connected Layer (완전 연결 계층)

추출된 특징들을 기반으로 최종적인 분류나 회귀 등의 작업을 수행합니다. 일반적인 [[ANN]]의 마지막 부분과 동일한 구조입니다.

---

## 🧮 합성곱 연산 예시

-   **입력 이미지 (4x4)**, **필터 (2x2)**, **Stride=1**, **Padding=0**

-   **입력**: `[[1, 2, 0, 3], [4, 5, 6, 1], [7, 8, 9, 0], [1, 2, 3, 4]]`
-   **필터**: `[[1, 0], [0, -1]]` (대각선 특징 감지)

#### 첫 번째 위치 연산:
`(1×1) + (2×0) + (4×0) + (5×-1) = 1 - 5 = -4`

이 과정을 전체 영역에 반복하면 다음과 같은 **3x3 크기의 특징 맵**이 생성됩니다.

-   **출력 특징 맵**: `[[-4, -4, -1], [-4, -4, -6], [6, 6, 5]]`

---

## ✨ CNN의 주요 특징

-   **Parameter Sharing (파라미터 공유)**: 하나의 필터를 이미지 전체에 공유하므로, 일반적인 [[ANN]]에 비해 학습할 파라미터 수가 획기적으로 줄어듭니다.
-   **Translation Invariance (이동 불변성)**: 객체가 이미지의 다른 위치에 있어도 동일한 필터로 특징을 감지할 수 있습니다.
-   **Hierarchical Feature Learning (계층적 특징 학습)**: 초기 계층에서는 선, 모서리 등 단순한 특징을, 깊은 계층으로 갈수록 눈, 코, 또는 객체의 일부와 같은 복잡하고 추상적인 특징을 학습합니다.

---

## 🏛️ 대표적인 CNN 아키텍처

| 아키텍처          | 주요 특징                                            |
| ----------------- | ---------------------------------------------------- |
| **LeNet-5** (1998)  | 최초의 성공적인 CNN, 숫자 인식에 사용                |
| **AlexNet** (2012)  | ReLU, Dropout 도입, GPU 활용으로 딥러닝 시대 개막    |
| **VGGNet** (2014)   | 3x3의 작은 필터를 반복적으로 사용하여 깊고 단순한 구조 |
| **GoogLeNet** (2014)| Inception 모듈로 다양한 크기의 특징을 병렬 추출      |
| **ResNet** (2015)   | Skip Connection으로 매우 깊은 네트워크(100층 이상) 학습 |

## 🔗 관련 개념 및 기술

-   [[Batch Normalization]]: 각 층의 입력 분포를 정규화하여 학습을 안정화하고 가속합니다.
-   [[Dropout; A Simple Way to Prevent Neural Networks from Overfitting|Dropout]]: 학습 시 뉴런을 무작위로 비활성화하여 과적합을 방지합니다.
-   **Max-norm Regularization**: 각 뉴런의 가중치 벡터 크기에 제약을 두어 과적합을 방지합니다.
-   **DropConnect**: Dropout이 뉴런을 비활성화하는 것과 달리, 개별 가중치(연결)를 무작위로 끊습니다.
-   **Stochastic Pooling**: 풀링 윈도우 내에서 확률적으로 값을 샘플링하여 과적합을 방지합니다.
-   **Maxout Networks**: 활성화 함수 자체를 학습 가능한 여러 선형 함수의 최댓값으로 구성합니다
#### 핵심 개념: 귀납적 편향 (Inductive Bias)

^0d803b

**귀납적 편향**이란 모델이 본 적 없는 데이터에 대해 예측할 때 사용하는 **'가정'이나 '사전 지식'** 을 말합니다.

- **CNN의 귀납적 편향:**
    - **국소적 연결성(Local Connectivity):** "인접한 픽셀끼리는 서로 밀접한 관계가 있다."
    - **이동 등변성(Translation Equivariance):** "물체가 이미지의 왼쪽 위에 있든 오른쪽 아래에 있든 그것은 같은 물체다."
    - **장점:** 이러한 가정 덕분에 CNN은 데이터가 적어도 효율적으로 학습하며 일반화 성능이 좋습니다.
    - **단점:** 데이터가 아주 많을 때는 이러한 고정된 가정(틀)이 오히려 더 복잡하거나 멀리 떨어진 픽셀 간의 관계를 학습하는 데 방해가 될 수 있습니다(표현력 제한).

## 📚 관련 논문

-   [[Gradient-based learning applied to document recognition]] (LeNet)
-   [[ImageNet classification with deep convolutional neural networks]] (AlexNet)
-   [[Deep Residual Learning for Image Recognition]] (ResNet)