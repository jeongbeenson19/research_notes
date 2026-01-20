
## 🔹 Canny Edge Detection이란?

**Canny Edge Detection**은 1986년 John F. Canny가 제안한 경계 검출 알고리즘으로,  
**노이즈에 강하고, 얇고, 연결된 에지를 검출**하기 위해 설계되었습니다.

Canny는 에지 검출 문제를 **최적화 문제**로 수식화하였고, 다음 세 가지 조건을 만족하는 알고리즘을 도출했습니다.

### ✔ 최적화 기준

1. **검출 최적성 (Good Detection)**: 실제 에지와 가까운 위치의 에지를 잘 찾아야 함.
    
2. **정밀한 위치 (Good Localization)**: 에지의 실제 위치와 검출된 위치의 차이가 작아야 함.
    
3. **단일 응답 (Minimal Response)**: 한 에지에 대해 하나의 응답만 있어야 함.
    

---

## 🔹 Canny 알고리즘의 단계

### 1. **Gaussian 필터로 노이즈 제거**

$$
G(x, y) = \frac{1}{2\pi\sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}}
$$

- 작은 에지(고주파 노이즈)를 제거하기 위한 **스무딩** 단계.
    
- $σ$(시그마)는 스무딩 정도를 조절.
    

### 2. **Gradient 계산 (Sobel 필터 활용)**

- x, y 방향의 그래디언트 계산:
    

$$
G_x = \frac{\partial I}{\partial x}, \quad G_y = \frac{\partial I}{\partial y}
$$
- 크기와 방향 계산:
    

$$
M(x, y) = \sqrt{G_x^2 + G_y^2}, \quad \theta(x, y) = \arctan2(G_y, G_x)
$$

### 3. **Non-maximum Suppression (NMS, 비최대 억제)**

- 가장자리의 **폭을 줄여 얇은 에지를 만들기 위한 단계**.
    
- 그래디언트 방향을 따라 인접 픽셀들과 비교하여, 최대값이 아닌 경우 제거.
    

### 4. **이중 임계값 (Double Thresholding)**

- 두 개의 임계값 $T_{\text{low}}, T_{\text{high}}$를 사용:
    
    - $M(x, y) \geq T_{\text{high}}$: Strong Edge
        
    - $T_{\text{low}} \leq M(x, y) < T_{\text{high}}$: Weak Edge
        
    - $M(x, y) < T_{\text{low}}$: 제거
        

### 5. **Edge Tracking by Hysteresis (이력적 연결)**

- Weak edge가 **strong edge와 연결되어 있을 때만 유지**.
    
- Edge 연결성을 기반으로 false positive를 억제.
    

---

## 🔸 수학적 요약 흐름

$$
\text{Input Image} \xrightarrow{\text{Gaussian Smoothing}} \xrightarrow{\nabla I} \xrightarrow{\text{NMS}} \xrightarrow{\text{Double Threshold}} \xrightarrow{\text{Hysteresis}} \text{→ Final Edges}
$$
---

## 🔹 OpenCV 예시 코드

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, threshold1=50, threshold2=150)

plt.imshow(edges, cmap='gray')
plt.title('Canny Edges')
plt.axis('off')
plt.show()
```

---

## 🔹 장점과 단점

|장점|단점|
|---|---|
|정밀하고 얇은 에지 검출 가능|속도가 느릴 수 있음|
|노이즈에 강함 (Gaussian smoothing + 이중 임계값)|임계값 및 σ 선택에 민감|
|연결된 에지만 유지 → 해석 용이|작은 에지는 제거될 수 있음|

---

## 🔹 Canny 알고리즘의 활용 분야

- 객체 검출 전처리
    
- 윤곽선 추출 (Contour Detection)
    
- Optical Flow, Motion Tracking
    
- OCR, 문서 스캐닝 등 구조적 정보 추출
    

---
## 프로그램 4-2: 케니 에지 실험하기
---
```python
import cv2 as cv


img = cv.imread('god.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny1 = cv.Canny(gray, 50, 150)
canny2 = cv.Canny(gray, 100, 200)

cv.imshow('Original', gray)
cv.imshow('Canny1', canny1)
cv.imshow('Canny2', canny2)

cv.waitKey()
cv.destroyAllWindows()
```
