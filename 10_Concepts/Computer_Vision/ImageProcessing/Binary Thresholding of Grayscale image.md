
 ## 명암 영상의 이진화

명암 영상(Grayscale image)에서 이진화(Binary Thresholding)는 픽셀 값을 흑(0) 또는 백(255)으로 바꾸는 과정입니다. 이 과정은 영상처리에서 물체와 배경을 구분할 때 자주 사용됩니다. 아래에 이진화의 개념과 대표적인 방법들을 설명드릴게요.

---

## ✅ 이진화란?

- **입력**: 명암 영상 (0~255 범위의 픽셀 값)
    
- **출력**: 흑백 영상 (0 또는 255만 존재)
    
- **기본 아이디어**: 픽셀 값이 특정 임계값(threshold)보다 크면 흰색(255), 작으면 검정(0)으로 변환
    

---

## ✅ 1. 단순 임계값 이진화 (Global Thresholding)

### ✔️ 방법:

```python
if pixel_value > T:
    result = 255
else:
    result = 0
```

- `T`는 임계값(threshold), 사용자가 직접 설정
    
- 예: T = 128 → 픽셀 값이 128보다 크면 흰색, 작거나 같으면 검정
    
## 프로그램 3-2: 실제 영상에서 히스토그램 구하기
```python
import cv2 as cv

import matplotlib.pyplot as plt

  

img = cv.imread('silver.png')

h = cv.calcHist([img], [2], None, [256], [0, 256])
# (영상, 영상 채널 번호, 히스토그램을 구할 영역을 지정하는 마스크, 히스토그램의 칸 수, 명암값의 범위)

plt.plot(h, color='r', linewidth=1)

plt.show()
```
### ✔️ 장점

- 간단하고 빠름
    

### ✔️ 단점

- 조명에 따라 전체 이미지에 하나의 임계값만 적용하기 때문에 정확도가 낮을 수 있음
    

---

## ✅ 2. Otsu 이진화 (Otsu's Method)

- **설명**: 픽셀 값의 히스토그램을 분석해서 **클래스 간 분산(분리도)을 최대로 만드는 임계값**을 자동으로 선택
    
- **사용 예**: 배경과 객체가 뚜렷이 구분되는 경우
    
### 📈 1. 핵심 개념

- **이미지의 히스토그램(밝기 분포)을 기반으로**
    
- **두 개의 클래스** (예: 배경과 객체)로 나눌 수 있는 임계값 ttt를 선택
    
- 그 임계값은 다음 중 하나의 기준으로 선택할 수 있음:
    
    1. **클래스 간 분산을 최대화** (Between-class variance)
        
    2. **클래스 내 분산을 최소화** (Within-class variance)
        

> 두 접근은 **수학적으로 동일한 결과**를 제공함 (최적의 ttt는 같음)

---

### 🧮 2. 수식 설명 (클래스 간 분산)

### 전체 픽셀의 총 수

 $$ N = \sum_{i=0}^{255} h(i)  
$$
    (여기서 $h(i)$는 $i$ 밝기의 픽셀 개수)

### 확률 분포 (정규화된 히스토그램)

$$
p(i) = \frac{h(i)}{N}
$$
    

### 그룹 나누기

- 임계값 $t$를 기준으로 두 그룹 생성:
    
    - **배경 클래스 $C_0$**: 밝기 0~t
        
    - **전경 클래스 $C_1$**: 밝기 t+1~255
        

### 각 그룹의 확률

$$
\omega_0(t) = \sum_{i=0}^t p(i)
$$

$$
\omega_1(t) = \sum_{i=t+1}^{255} p(i)
$$


### 각 그룹의 평균 밝기

$$
\mu_0(t) = \frac{ \sum_{i=0}^t i \cdot p(i) }{ \omega_0(t) }
$$

$$
\mu_1(t) = \frac{ \sum_{i=t+1}^{255} i \cdot p(i) }{ \omega_1(t) }
$$


### 전체 평균 밝기

$$
\mu_T = \sum_{i=0}^{255} i \cdot p(i)
$$


### **클래스 간 분산** (Between-class variance)

$$
\sigma_b^2(t) = \omega_0(t) \cdot \omega_1(t) \cdot [\mu_0(t) - \mu_1(t)]^2
$$
### 🧮 2-1. 수식 설명 (클래스 내 분산)
$$
\hat{t} = \underset{t \in \{ 0, 1, 2, \dots, L-1 \}}{\text{argmin}} \; J(t)
$$

모든 명암값에 대해 목적 함수 $J$를 계산하고 $J$가 최소인 명암값을 $\hat{t}$으로 정한다. 이렇게 결정한 $\hat{t}$을 임곗값 $T$로 사용해 이진화한다.

$$
J(t) = n_0(t)v_0(t) + n_1(t)v_1(t)
$$
$n_0(t), n_1(t)$: 각 클래스의 비율 (또는 확률)
$v_0(t), v_1(t)$: 각 클래스의 분산
$t$: 임계값


1. **밝기값 $t$를 기준으로 두 클래스로 나눕니다:
    
    - 클래스 0: 밝기값 $i \leq t$
        
    - 클래스 1: 밝기값 $t > i$
        
2. **각 클래스의 확률(비율) $\omega_0(t), \omega_1(t)$** 계산  
    (히스토그램에서 비율을 누적해서 구함)
$$
\omega_0(t) = \sum_{i=0}^{t} p(i), \quad \omega_1(t) = \sum_{i=t+1}^{L-1} p(i)
$$
3. **각 클래스의 평균 밝기값 $\mu_0(t), \mu_1(t)$ 계산  
    (이진화 전의 원래 값 기준으로)
    
$$
\mu_0(t) = \frac{1}{\omega_0} \sum_{i=0}^{t} i \cdot p(i), \quad \mu_1(t) = \frac{1}{\omega_1} \sum_{i=t+1}^{L-1} i \cdot p(i)
$$
4. **각 클래스의 분산 $\sigma_0^2(t), \sigma_1^2(t)$** 계산  
    (각 클래스 내부의 픽셀 값에서 평균을 빼고 제곱한 후 평균냄)
    
$$
\begin{align}
\sigma_0^2(t) &= \frac{1}{\omega_0} \sum_{i=0}^{t} (i - \mu_0)^2 \cdot p(i) \\
\sigma_1^2(t) &= \frac{1}{\omega_1} \sum_{i=t+1}^{L-1} (i - \mu_1)^2 \cdot p(i)
\end{align}
$$

5. 마지막으로, 클래스 내 분산을 가중합으로 계산:
$$
\sigma_w^2(t) = \omega_0 \cdot \sigma_0^2 + \omega_1 \cdot \sigma_1^2
$$

---

## 🎯 3. 최적 임계값 선택

$\sigma_b^2(t)$를 계산하면서 **모든 $t$ (0~255)에 대해 비교**
    
- **가장 큰 $\sigma_b^2(t)$ 값을 만드는 $t$를 최적의 임계값으로 선택
    

---

## 프로그램 3-3: 오츄 알고리즘으로 이진화하기

```python
import cv2 as cv
import sys
  
img = cv.imread('silver.png')

t, bin_img = cv.threshold(img[:, :, 2], 0, 255,
cv.THRESH_BINARY+cv.THRESH_OTSU)
print('오츄 알고리즘이 찾은 최적 임곗값=', t)

cv.imshow('R channel', img[:, :, 2])
cv.imshow('R channel binarization', bin_img)

cv.waitKey()
cv.destroyAllWindows()
```
---
## 🔧 4. 파이썬 코드 예제 (OpenCV 사용)

```python
import cv2
import matplotlib.pyplot as plt

# 흑백 이미지 불러오기
img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Otsu 이진화 적용
_, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 결과 시각화
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(1, 2, 2), plt.imshow(binary, cmap='gray'), plt.title('Otsu Binarized')
plt.show()
```

---

## 📌 오츠 알고리즘의 장점과 한계

|장점|단점|
|---|---|
|임계값을 자동으로 정해줌|배경과 객체의 히스토그램이 뚜렷이 나뉘지 않으면 정확도 저하|
|간단하면서도 성능이 우수함|조명이 고르지 않은 경우 부적절할 수 있음|
|실시간 처리에 적합 (속도 빠름)|멀티 객체 분할에는 한계 있음|

---

## 📚 활용 예시

- 문서 이미지에서 글자/배경 분리
    
- 의료 영상에서 종양 검출 전처리
    
- 물체 감지의 사전 단계 이진화 등
    

---

## ✅ 3. 적응형 이진화 (Adaptive Thresholding)

- **설명**: 이미지의 **지역적 특성**을 반영하여 각 영역마다 임계값을 따로 설정
    
- 조명이 고르지 않은 이미지에서 효과적
    

### ✔️ 방식

- 주변 픽셀의 평균값 또는 가우시안 가중 평균값을 기준으로 임계값 결정
    

### ✔️ 예시 (OpenCV):

```python
binary = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,  # 또는 cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    cv2.THRESH_BINARY,
    blockSize=11,  # 주변 픽셀 범위
    C=2  # 평균에서 뺄 값 (편향 조절)
)
```

---

## ✅ 요약 비교표

|방법|특징|장점|단점|
|---|---|---|---|
|단순 임계값|고정된 T 사용|빠르고 간단|조명 변화에 취약|
|Otsu 이진화|히스토그램 기반 T 자동 결정|자동화 가능, 비교적 정확|배경-객체 구분이 어려우면 부정확|
|적응형 이진화|각 지역마다 다른 T 사용|조명 변화에 강함|상대적으로 느림|
