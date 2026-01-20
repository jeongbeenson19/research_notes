
## 🔍 점 연산(Point Operation)이란?

**점 연산**은 영상의 **각 픽셀에 대해 독립적으로 수행되는 연산**입니다. 즉, 특정 픽셀의 출력값은 **오직 해당 픽셀의 입력값만을 기반으로 결정**됩니다.  
이와 달리, 공간 연산(spatial operation)은 주변 픽셀들과의 관계를 고려하므로 필터링(예: 블러, 에지 검출)과는 구별됩니다.

---

## 🎯 수학적 정의

입력 영상 $f(x, y)$에 대해 출력 영상 $g(x, y)$는 다음과 같은 함수로 정의됩니다.

$$
g(x, y) = T(f(x, y))
$$

- $T$: 단일 픽셀에 적용되는 변환 함수
    
- $(x, y)$: 영상의 공간 좌표
    
- 이 연산은 **픽셀 단위로 병렬 처리**가 가능하여 빠르게 연산됩니다.
    

---

## 🔧 주요 점 연산의 종류

### 1. **명암 조절 (Gray Level Transformation)**

픽셀 값을 일정 방식으로 변형하는 것

- **선형 변환 (Linear Scaling)**
    
    $$
    g(x, y) = a \cdot f(x, y) + b
    $$
	- $a > 1$: 대비 증가
        
    - $b > 0$: 밝기 증가
        
- **역변환 (Negative Image)**
    
    $$
    g(x, y) = L - 1 - f(x, y)
    $$
    - $L$: 영상의 최대 그레이레벨 (예: 8비트면 256)
        
    - 밝은 영역은 어둡게, 어두운 영역은 밝게 반전
        
- **감마 보정 (Gamma Correction)**
    
    $$
    g(x, y) = c \cdot f(x, y)^{\gamma}
    $$
	- $\gamma < 1$: 어두운 영역 강조
        
    - $\gamma > 1$: 밝은 영역 강조
### 프로그램 3-5: 감마 보정 실험하기
---
```python
import cv2 as cv
import numpy as np


img = cv.imread('silver.png')
img = cv.resize(img, dsize=(0, 0), fx=0.25, fy=0.25) 

def gamma(f, gamma=1.0):
f1 = f/255.0
return np.uint8(255*(f1**gamma))  
  
gc = np.hstack((gamma(img, 0.5), gamma(img, 0.75), gamma(
img, 1.0), gamma(img, 2.0), gamma(img, 3.0))) # type: ignore
cv.imshow('gamma', gc)
  
cv.waitKey()
cv.destroyAllWindows()
```
---

### 2. **이진화 (Thresholding)**

영상의 픽셀 값을 기준에 따라 0 또는 255로 이진화

$$
g(x, y) = \begin{cases} 255 & \text{if } f(x, y) \geq T \\ 0 & \text{otherwise} \end{cases}
$$
- $T$: 임계값
    
- 단일 임계값 외에 Otsu 방법 등 다양한 자동 임계값 설정 기법도 존재
    

---

### 3. **루킹 테이블(LUT, Look-Up Table) 기반 변환**

- 자주 쓰이는 TT 함수들을 미리 테이블화해 빠르게 적용
    
- LUT를 통해 실시간 처리가 가능함 (영상 장치에선 흔히 사용)
    

---

## 📊 실생활 예시

|예시|설명|
|---|---|
|의료영상에서 대비 향상|감마 보정 및 히스토그램 평활화|
|CCTV 야간영상 보정|명암 선형 조절 및 감마 보정|
|OCR을 위한 이진화 전처리|Thresholding|
|필터 적용 전 픽셀 정규화|선형 조정|

---

## ✅ 점 연산의 장점 vs 한계

|장점|한계|
|---|---|
|병렬 처리 가능 (빠름)|지역 특성 반영 불가|
|구현이 단순함|노이즈 제거에 효과적이지 않음|
|GPU에서 매우 효율적|객체 경계 검출 불가능|

---

좋아요, 히스토그램 평활화(Histogram Equalization)는 컴퓨터 비전/영상처리에서 **영상의 명암 대비를 향상시키는 대표적인 점 연산** 기법입니다. 특히 조명이 고르지 않거나 명암 분포가 한쪽에 치우쳐 있을 때 유용하게 사용됩니다.

---

## 🎯 1. 히스토그램 평활화란?

히스토그램 평활화는 영상의 **픽셀 분포를 고르게 만들어** 전체적으로 **더 넓은 범위의 밝기 값을 가지도록 변환하는 과정**입니다.

- 입력 영상의 히스토그램이 어두운 쪽에 몰려 있다면 → 밝은 영역도 살릴 수 있게 조정
    
- 결과적으로 더 넓은 대비(contrast)를 가지게 되어 **시각적으로 더 선명**하게 보입니다.
    

---

## 📊 2. 히스토그램이란?

- 영상의 각 **픽셀 값의 빈도수 분포**
    
- 예를 들어, 8비트 그레이스케일 영상은 픽셀 값이 0~255 사이의 정수이므로, 히스토그램은 256개의 막대로 표현 가능
    

예시:

|픽셀 값 (gray level)|0|1|...|255|
|---|---|---|---|---|
|빈도수 (frequency)|5|2|...|0|

---

## ⚙️ 3. 히스토그램 평활화의 수학적 원리

1. **정규화된 히스토그램** $p(r_k)$:
    
    $$
    p(r_k) = \frac{n_k}{MN}
    $$
    - $n_k$: 그레이레벨 $r_k$을 갖는 픽셀 수
        
    - $MN$: 전체 픽셀 수
        
2. **누적 분포 함수 (CDF)** $s_k$:
    
    $$
    s_k = \sum_{j=0}^{k} p(r_j)
    $$
    - 누적 분포는 항상 $[0, 1]$ 범위에 있음
        
3. **변환 함수**:
    
    $$
    T(r_k) = (L - 1) \cdot s_k
    $$
    - $L$: 사용할 수 있는 그레이레벨 수 (보통 256)
        
    - 이 함수는 $r_k$를 $T(r_k)$로 매핑하여 **픽셀 값을 재배치**
        

---

## 🧪 4. 예제 (OpenCV + Python)

```python
import cv2
import matplotlib.pyplot as plt

# 영상 불러오기 (흑백)
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 히스토그램 평활화
equalized = cv2.equalizeHist(img)

# 시각화
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')

plt.subplot(2, 2, 2)
plt.title("Equalized Image")
plt.imshow(equalized, cmap='gray')

plt.subplot(2, 2, 3)
plt.title("Original Histogram")
plt.hist(img.ravel(), 256, [0, 256])

plt.subplot(2, 2, 4)
plt.title("Equalized Histogram")
plt.hist(equalized.ravel(), 256, [0, 256])
plt.tight_layout()
plt.show()
```

---

## ✅ 5. 장점과 한계

|장점|한계|
|---|---|
|명암 대비 향상|노이즈도 함께 강조될 수 있음|
|단순하고 빠름|이미지 전체의 밝기 분포만 고려함 (지역 특성 무시)|
|실시간 처리 가능 (LUT로 구현 가능)|컬러 이미지에는 직접 적용 어려움 (색 왜곡)|

---

## 🌈 6. 컬러 영상에서의 처리

컬러 영상(RGB)에는 직접 적용하면 색상 왜곡 발생 → 일반적으로 **YUV / HSV 등으로 변환 후 밝기 채널(Y or V)에만 적용**:

```python
img = cv2.imread('color.jpg')
yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])  # Y 채널에만 적용
equalized = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
```

---

## 🔍 7. 응용 분야

- 의료 영상 (X-ray, CT) 명암 향상
    
- 저조도 환경의 보정
    
- 위성 영상 처리
    
- OCR 사전 처리
    
- 감시 카메라 영상 향상
    

---

$$
l' = \text{round}(\ddot{h}(l) \cdot (L - 1))
$$
은 **히스토그램 평활화(Histogram Equalization)** 과정 중 픽셀 값 매핑(변환)의 핵심 수식입니다. 이 식이 어떤 의미를 갖는지 단계별로 설명드릴게요.

---

## 🧩 수식 구성 요소 설명

- $l$: 입력 영상의 픽셀 값 (예: 0 ~ 255)
    
- $h(l)$: 누적 분포 함수 (CDF)에서 픽셀 값 $l$에 해당하는 누적 확률  
    즉, 전체 픽셀 중 값이 $l$ 이하인 비율
    $$
    \ddot{h}(l) = \sum_{i=0}^{l} \frac{n_i}{MN}
    $$
    (여기서 $n_i$는 $i$ 값의 픽셀 수, $MN$은 전체 픽셀 수)
    
- $L$: 영상의 밝기 수준 개수 (예: 8비트 영상이면 L=256L = 256)
    
- $l'$: 평활화된 결과 영상에서의 새 픽셀 값
    

---

## 📌 해석

$$
l' = \text{round}(\ddot{h}(l) \cdot (L - 1))
$$
이 식은 다음과 같은 의미를 가집니다:

> **입력 픽셀 값 $l$에 대해 누적 분포 함수 $h(l)$를 계산하고, 이를 밝기 값 범위 $[0, L-1]$ 에 선형적으로 확장하여 새로운 픽셀 값 $l'$로 변환한다.

### 직관적으로 이해하면:

- $\ddot{h}(l)$는 "이 픽셀보다 어두운 픽셀이 얼마나 많은가?"를 비율로 나타낸 값
    
- 이를 $L-1$과 곱해주면 "이 픽셀은 전체 밝기 범위에서 어디쯤에 있어야 하는가"를 알려줌
    
- 마지막에 `round`는 이 결과를 가장 가까운 정수 밝기값으로 반올림해줌
    

---

## 🔢 예시 (8비트 영상, L=256L = 256)

- 어떤 픽셀 값 $l = 50$
    
- 누적 분포 함수 $h(50) = 0.2$ (즉, 전체 픽셀 중 20%가 50 이하)
    
- 그럼:
    
    $$
    l' = \text{round}(0.2 \cdot 255) = \text{round}(51) = 51
    $$
    
    → 밝기 값 50이 51로 매핑됨
    
- 만약 $h(50) = 0.6$이었다면 $l' = 153$로 더 밝아졌겠죠.
    

---

## ✅ 핵심 요약

|항목|내용|
|---|---|
|목적|픽셀 값을 누적 분포 기반으로 재조정하여 명암 대비 향상|
|작동 원리|누적 히스토그램을 이용한 선형 스케일링|
|수식 의미|누적 비율 → 전체 밝기 범위로 확장 → 반올림해서 새 값 생성|

---

## 📚 참고로…

이 수식은 **히스토그램 평활화의 핵심 매핑 함수**입니다. 전체적으로는 다음과 같은 프로세스를 따릅니다:

1. 입력 영상의 히스토그램 계산
    
2. 누적 히스토그램(CDF) 계산
    
3. 위 수식으로 픽셀 값 매핑
    
4. 결과 영상 생성
    

---

## 프로그램 3-6: 히스토그램 평활화하기
---
```python
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('silver.png')

# 명암 영상으로 변환하고 출력
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 히스토그램을 구해 출력
h = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.plot(h, color='r', linewidth=1)
plt.show()

# 히스토그램을 평활화하고 출력
equal = cv.equalizeHist(gray)
plt.imshow(equal, cmap='gray')
plt.xticks()
plt.yticks()
plt.show()

# 히스토그램을 출력
h = cv.calcHist([equal], [0], None, [256], [0, 256])
plt.plot(h, color='r', linewidth=1)
plt.show()
```
