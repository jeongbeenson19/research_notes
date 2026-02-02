---
title: "C3D"
tags: [paper, architecture, video, action-recognition, spatiotemporal]
year: 2015
venue: "ICCV"
---
# C3D: 3D Convolutional Networks를 이용한 시공간 특징 학습

**저자:** Du Tran, Lubomir Bourdev, Rob Fergus, Lorenzo Torresani, Manohar Paluri  
**소속:** Facebook AI Research, Dartmouth College  
**논문:** Learning Spatiotemporal Features with 3D Convolutional Networks (ICCV 2015)

---

## 1. 들어가며: 비디오 데이터의 폭발과 분석의 필요성

인터넷상의 멀티미디어 데이터는 매 분마다 폭발적으로 증가하고 있습니다. 이러한 방대한 양의 비디오 데이터를 검색하고, 추천하고, 랭킹을 매기기 위해서는 비디오를 '제대로' 이해하고 분석하는 기술이 필수적입니다.

이미지 분야에서는 딥러닝(특히 ConvNet)이 혁신적인 성과를 거두었지만, 비디오는 이미지와 달리 **시간(Temporal)** 이라는 차원이 더해져 있어 기존의 이미지 기반 모델만으로는 움직임(Motion) 정보를 완벽하게 담아내기 어렵습니다.

오늘 소개할 논문은 2D ConvNet의 한계를 넘어, **3D ConvNet(C3D)** 을 통해 비디오의 **공간(Spatial)과 시간(Temporal) 특징**을 동시에, 그리고 효과적으로 학습하는 방법을 제안합니다.

## 2. 훌륭한 비디오 디스크립터(Video Descriptor)의 4가지 조건

이 논문에서는 좋은 비디오 특징 추출기(Descriptor)가 갖춰야 할 4가지 조건을 다음과 같이 정의합니다.

1.  **Generic (범용성):** 풍경, 스포츠, 영화, 반려동물 등 어떤 종류의 비디오라도 잘 표현할 수 있어야 합니다.
2.  **Compact (압축성):** 수백만 개의 비디오를 다루기 때문에, 특징 벡터(Feature Vector)의 차원이 작고 간결해야 저장 및 처리가 용이합니다.
3.  **Efficient (효율성):** 실시간 시스템 적용을 위해 계산 속도가 빨라야 합니다.
4.  **Simple (단순성):** 복잡한 인코딩 방식 없이, 단순한 모델(예: Linear Classifier)만 붙여도 좋은 성능을 내야 합니다.

저자들은 제안하는 **C3D**가 이 4가지 조건을 모두 만족한다고 주장합니다.

**표 1: C3D와 기존 최고 성능 연구들의 비교 (Table 1)**

| 데이터셋 (Dataset) | 태스크 (Task)                             | 기존 최고 성능 (Previous Best) | **C3D 성능 (Ours)** |
| :------------- | :------------------------------------- | :----------------------: | :---------------: |
| **Sports-1M**  | 행동 인식 (Action Recognition)             |          90.8%           |       85.2%       |
| **UCF101**     | 행동 인식 (Action Recognition)             |      75.8% (89.1%)       | **85.2% (90.4%)** |
| **ASLAN**      | 행동 유사성 판별 (Action Similarity Labeling) |          68.7%           |     **78.3%**     |
| **YUPENN**     | 장면 분류 (Scene Classification)           |          96.2%           |     **98.1%**     |
| **UMD**        | 장면 분류 (Scene Classification)           |          77.7%           |     **87.7%**     |
| **Object**     | 객체 인식 (Object Recognition)             |          12.0%           |     **22.3%**     |

---
### 💡 참고 사항 (UCF101 수치 설명)

**UCF101** 항목에 있는 괄호 안의 숫자는 다음과 같은 차이가 있습니다:

1.  **괄호 밖 (예: 75.8, 85.2):**
    *   **RGB 프레임**만 입력값으로 사용한 결과입니다.
    *   이 조건에서는 C3D(85.2%)가 기존 최고 성능(75.8%)보다 훨씬 우수한 성능을 보입니다.

2.  **괄호 안 (예: 89.1, 90.4):**
    *   RGB뿐만 아니라 **광학 흐름(Optical Flow), iDT(Improved Dense Trajectory) 등 가능한 모든 특징(feature)** 을 조합하여 사용한 결과입니다.
    *   이 경우에도 C3D를 결합한 모델(90.4%)이 기존 최고 성능(89.1%)을 앞섭니다.

**요약:** C3D는 Sports-1M을 제외한 5개의 벤치마크에서 기존의 최고 성능(SOTA)을 능가하거나 대등한 결과를 보여줍니다. 특히 장면 분류나 객체 인식에서도 단순한 선형 분류기(Linear Classifier)만으로도 뛰어난 성능을 보입니다.

## 3. 핵심 아이디어: 3D Convolution

기존의 2D ConvNet은 비디오의 프레임을 개별 이미지로 처리하기 때문에 시간적 흐름 정보를 잃어버리기 쉽습니다. 반면, **3D ConvNet**은 3차원 커널을 사용하여 비디오 볼륨(Video Volume)을 처리합니다.

$$y(x,y,z) = \sum_{i=-k}^{k} \sum_{j=-k}^{k} \sum_{t=-d}^{d} w(i,j,t) \cdot x(x+i, y+j, z+t)$$
*   **연구의 주요 발견:**
    1.  **3D ConvNet의 우수성:** 시공간(Spatiotemporal) 특징을 학습하는 데 있어 2D ConvNet보다 3D ConvNet이 더 적합합니다.
    2.  **균일한 작은 커널:** 대부분의 레이어에서 **3×3×3** 커널을 사용하는 구성이 안정적이고 성능이 좋았습니다(2D의 VGG 스타일과 유사).


## 4. 아키텍처 요약 (논문 기준)
- 입력: 보통 **16프레임 클립**, 크기 **112×112** (크롭/리사이즈 후 사용)
- 구조: 3D Conv + 3D Pooling을 반복하며 깊이 증가
- FC 레이어: fc6/fc7(4096), fc8(분류)
- 특징 추출: fc6/7을 **비디오 디스크립터**로 사용 가능

## Action Recognition([[Two-Stream Network]]와의 구조적 차이)

핵심 차이는 **"몸통(Hidden Layers)을 공유하느냐, 안 하느냐"** 입니다.

---
### 1. Two-Stream의 Multi-task Learning 구조
**"몸통은 하나인데, 머리가 두 개인 구조 (Y자 형태)"**

Two-Stream 논문에서 Temporal Net을 학습시킬 때 사용한 구조입니다. 데이터가 적은 UCF101을 보완하기 위해 큰 데이터셋(HMDB51)을 같이 씁니다.

*   **구조적 특징:**
    *   **Input:** Optical Flow (입력은 배마다 다름)
    *   **Hidden Layers (Conv1 ~ FC7):** **완전히 공유(Shared Weights)**합니다. 하나의 네트워크 파라미터 $\theta_{shared}$가 존재합니다.
    *   **Output Layer (Softmax):** 마지막에만 두 갈래로 나뉩니다.
        *   Head A: UCF101용 (101 class)
        *   Head B: HMDB51용 (51 class)
*   **작동 방식:**
    *   UCF 데이터를 넣을 땐 Head A로 Loss를 구해 몸통을 업데이트합니다.
    *   HMDB 데이터를 넣을 땐 Head B로 Loss를 구해 **같은 몸통**을 업데이트합니다.
    *   **결과:** 네트워크는 하나만 남습니다.

```text
       [ Input Image ]
             ⬇
    [ Shared Conv Layers ]  <-- 가중치(W) 하나를 공유함
             ⬇
    [ Shared FC Layers ]
             ⬇
      /-------------\
 [Head A]       [Head B]    <-- 마지막 분류기만 다름
(UCF101)       (HMDB51)
```

---
### 2. C3D의 Feature Concatenation 구조
**"완전히 남남인 세 명의 전문가가 나란히 서 있는 구조 (||| 형태)"**

이 논문(C3D)에서 "3 different nets"를 사용했다는 부분입니다.

*   **구조적 특징:**
    *   **Networks:** 물리적으로 **3개의 별도 네트워크**가 메모리에 로드됩니다.
        1.  Net 1 (I380K 학습됨)
        2.  Net 2 (Sports-1M 학습됨)
        3.  Net 3 (Fine-tuned 학습됨)
    *   **Hidden Layers:** **전혀 공유하지 않습니다.** 서로 다른 가중치 값($W_1, W_2, W_3$)을 가집니다.
    *   **Combination:** 각 네트워크의 FC6(혹은 FC7) 층에서 나온 **벡터(Vector)** 들을 가져와서 깁니다.
*   **작동 방식:**
    *   이미지 하나를 Net 1, 2, 3에 각각 넣습니다.
    *   나온 결과값(4096차원) 3개를 일렬로 붙입니다. (4096 + 4096 + 4096 = 12,288 차원)
    *   이 거대해진 벡터를 **SVM**이라는 별도의 분류기에 넣습니다.

```text
    [ Input Video ] ------------------------\
          ⬇                 ⬇               ⬇
    [ Net 1 Body ]    [ Net 2 Body ]    [ Net 3 Body ]  <-- 서로 완전히 다른 모델
    (I380K weights)   (Sports weights)  (Tuned weights)
          ⬇                 ⬇               ⬇
    [ Vector A ]      [ Vector B ]      [ Vector C ]
          ⬇                 ⬇               ⬇
    [      Concatenated Vector (A+B+C)      ]           <-- 단순히 붙임
                       ⬇
               [ Linear SVM ]                           <-- 최종 분류
```

---
### 3. 한눈에 보는 요약

| 특징 | Two-Stream (Multi-task) | C3D (Feature Concatenation) |
| :--- | :--- | :--- |
| **네트워크 개수** | **1개** (Y자 구조) | **3개** (병렬 구조) |
| **가중치(Weight)** | **공유함 (Shared)** | **독립적임 (Independent)** |
| **목적** | 학습 시 데이터 부족 해결 (Regularization) | 추론 시 성능 극대화 (Ensemble) |
| **최종 형태** | Softmax (분류기) | SVM (긴 벡터를 입력으로 받음) |

결론적으로 Two-Stream의 방식은 **"학습(Training) 테크닉"** 으로서 네트워크 내부를 튼튼하게 만드는 것이고, C3D의 방식은 **"특징 추출(Feature Extraction)"** 단계에서 여러 모델의 힘을 빌려 표현력을 넓히는 방식입니다.

## 5. 학습/추론 포인트
- 대규모 비디오로 사전학습 후 다운스트림 데이터셋에 파인튜닝
- 클립 단위 예측을 영상 전체로 집계(평균/합의)해 안정화
- 단순 선형 분류기와 결합해도 높은 성능을 달성

## 6. C3D의 성능 및 특징

논문에서는 대규모 비디오 데이터셋으로 학습된 C3D 모델의 특징을 추출하여 단순한 선형 분류기(Linear Classifier)와 결합해 성능을 테스트했습니다.

*   **강한 일반화:** 다양한 비디오 태스크에서 강한 특징 표현을 제공
*   **컴팩트한 디스크립터:** 낮은 차원에서도 의미 있는 성능 유지
*   **빠른 추론:** 3D Conv 기반이지만 클립 단위 병렬화가 가능

## 7. 한계와 후속 흐름
- 긴 시간 의존성 모델링이 제한적(클립 길이 의존)
- 연산/메모리 비용이 커서 대규모 배치 학습 부담
- 후속 연구는 I3D, SlowFast, Video Transformer 등으로 확장

## 8. 결론

이 논문은 대규모 지도 학습(Supervised Learning) 환경에서 3D ConvNet을 활용하여 비디오의 모양(Appearance)과 동작(Motion)을 동시에 모델링하는 것이 매우 효과적임을 입증했습니다.

**C3D**는 개념적으로 단순하면서도 강력하고, 효율적인 비디오 특징 추출기입니다. 복잡한 튜닝 없이도 다양한 비디오 분석 작업(객체 탐지, 장면 인식, 행동 인식 등)에 범용적으로 사용할 수 있다는 점에서 비디오 이해(Video Understanding) 분야의 중요한 이정표가 되는 연구입니다.

***

## 관련 노트
- [[3D-CNN]]
- [[20_Tasks/VideoUnderstanding/Abstract/Video Action Recognition]]
- [[Two-Stream Network]]
