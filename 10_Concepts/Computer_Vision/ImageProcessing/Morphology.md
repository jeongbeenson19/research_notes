
## 🧩 1. 기본 개념

- **모폴로지**는 수학적 형태학(Mathematical Morphology)에서 유래
    
- 이미지를 구성하는 픽셀 집합에 대해 **구조 요소(structuring element)**를 사용해 연산
    
- 주로 **노이즈 제거, 객체 경계 보정, 구멍 채우기** 등에 사용됨
    

---

## 🧱 2. 구조 요소 (Structuring Element)

- 모폴로지 연산에서 핵심 역할을 함
    
- 작은 형태(예: 3×3 정사각형, 십자 모양 등)
    
- 중심 화소를 기준으로 주위 픽셀의 값을 보고 판단
    

OpenCV에서는 보통 아래처럼 생성:

```python
cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
```

---

## 🔨 3. 기본 모폴로지 연산

### 1) **침식 (Erosion)**

- 객체를 **수축**시킴 (흰 영역이 줄어듦)
    
- 구조 요소가 **완전히 들어맞는** 경우만 중심 픽셀을 1로 유지
    
- 효과: **노이즈 제거**, **얇은 선 제거**
    

```python
eroded = cv2.erode(img, kernel)
```

---

### 2) **팽창 (Dilation)**

- 객체를 **확장**시킴 (흰 영역이 커짐)
    
- 구조 요소가 **하나라도 겹치면** 중심 픽셀을 1로 설정
    
- 효과: **끊긴 선 연결**, **구멍 메움**
    

```python
dilated = cv2.dilate(img, kernel)
```

---

## 🧪 4. 응용 연산 (조합)

### 3) **열림 (Opening)** = 침식 후 팽창

- 작은 노이즈 제거, 큰 객체 보존
    
- 효과: **배경의 작은 잡음 제거**
    

```python
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
```

### 4) **닫힘 (Closing)** = 팽창 후 침식

- 객체의 작은 구멍 메우기
    
- 효과: **전경 내의 작은 블랙홀 제거**
    

```python
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
```

---

### 5) **모폴로지 그라디언트** = 팽창 - 침식

- 객체의 경계만 추출
    

```python
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
```

---

### 6) **Top Hat & Black Hat**

- **Top Hat** = 원본 - 열림 → 밝은 작은 객체 추출
    
- **Black Hat** = 닫힘 - 원본 → 어두운 작은 객체 추출
    

---

## 📌 요약표

|연산|설명|용도|
|---|---|---|
|**침식**|객체 축소|잡음 제거, 구멍 생성|
|**팽창**|객체 확장|선 연결, 구멍 메움|
|**열림**|침식 후 팽창|작은 객체 제거|
|**닫힘**|팽창 후 침식|구멍 메우기|
|**그라디언트**|경계 추출|윤곽선 검출|
|**Top Hat**|밝은 작은 요소 추출|배경보다 밝은 잡음 검출|
|**Black Hat**|어두운 작은 요소 추출|배경보다 어두운 잡음 검출|

---

## ✅ 예시 코드 (OpenCV)

```python
import cv2
import numpy as np

img = cv2.imread('binary_image.png', 0)  # 이진 이미지 로드
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

eroded = cv2.erode(img, kernel)
dilated = cv2.dilate(img, kernel)
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
```

---
## 프로그램 3-4: 모폴로지 연산 적용하기
```python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('silver.png', cv.IMREAD_UNCHANGED)

# 오츄 이진화 적용
t, bin_img = cv.threshold(img[:, :, 2], 0, 255,
cv.THRESH_BINARY+cv.THRESH_OTSU)
plt.imshow(bin_img, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 이미지 크롭
b = bin_img[bin_img.shape[0]//2:bin_img.shape[0], 0:bin_img.shape[0]//2+1]
plt.imshow(b, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 구조 요소
se = np.uint8([[0, 0, 1, 0, 0],
[0, 1, 1, 1, 0],
[1, 1, 1, 1, 1],
[0, 1, 1, 1, 0],
[0, 0, 1, 0, 0]]) # type: ignore

# 팽창
b_dilation = cv.dilate(b, se, iterations=1) # type: ignore
plt.imshow(b_dilation, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 침식
b_erosion = cv.erode(b, se, iterations=1) # type: ignore
plt.imshow(b_erosion, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()

# 닫기
b_closing = cv.erode(cv.dilate(b, se, iterations=1), # type: ignore
se, iterations=1) # type: ignore
plt.imshow(b_closing, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.show()
```
