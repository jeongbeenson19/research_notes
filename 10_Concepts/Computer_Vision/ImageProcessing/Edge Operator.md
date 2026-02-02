
### 🔹 에지 연산자 (Edge Operator)

**에지 연산자**는 영상에서 경계(에지)를 검출하는 데 사용되는 수학적 연산자입니다.  
에지는 픽셀 값(밝기)이 급격히 변화하는 부분을 의미하며, 객체의 윤곽을 나타냅니다.

#### 대표적인 에지 연산자:

1. **Sobel 연산자**
    
    - 수직, 수평 방향의 에지를 강조함.
        
    - 주로 `3x3` 마스크를 사용.
        
    - 수식 예:  
        $$
        G = √(Gx² + Gy²)
        $$
2. **Prewitt 연산자**
    
    - Sobel과 비슷하지만 마스크 값이 조금 다름.
        
3. **Laplacian 연산자**
    
    - 2차 미분 기반, 방향에 관계없이 에지를 검출.
        
	    수식 예:  
    $$
        Δf = ∂²f/∂x² + ∂²f/∂y²
        $$
4. **Canny 연산자**
    
    - 노이즈에 강하고, 얇고 연결된 에지를 검출.
        
    - 복잡하지만 매우 정밀함.
        

---

### 🔹 램프 에지 (Ramp Edge)

**램프 에지**는 **밝기 값이 점진적으로 변화하는 에지**입니다.  
즉, 단번에 밝기값이 바뀌는 게 아니라 **몇 개의 픽셀에 걸쳐 서서히 변화**합니다.

#### 예시:

- 왼쪽에서 오른쪽으로 갈수록 점점 밝아지는 경우.
    

#### 시각적 예:

```
픽셀 밝기:  [10, 20, 30, 40, 50, 60]
              ↑ 점진적 변화 = Ramp Edge
```

#### 반대 개념:

- **Step Edge**: 한 픽셀에서 갑자기 밝기 값이 확 바뀌는 에지.  
    예: $[10, 10, 10, 100, 100, 100]$
    

---

### 정리

|구분|설명|
|---|---|
|에지 연산자|에지를 수학적으로 검출하는 도구|
|램프 에지|밝기 값이 서서히 변하는 경계(완만한 에지)|

---

## 🔹 공통 개요

**Sobel**과 **Prewitt** 연산자는 모두 **1차 미분 기반의 경계 검출 필터**입니다.  
이산 도함수를 근사하여 이미지에서 수평 및 수직 방향의 경계를 찾습니다.

에지란 밝기 $I(x, y)$의 변화율이 큰 곳이며, 수학적으로는 **그래디언트(Gradient)** 로 표현됩니다.

$$
\nabla I| = \sqrt{\left(\frac{\partial I}{\partial x}\right)^2 + \left(\frac{\partial I}{\partial y}\right)^2}
$$
---

## 🔹 Sobel 연산자

^ac73ae

### ✔ 핵심 특징:

- 미분 연산에 **가우시안 스무딩 효과**를 결합해 **노이즈에 덜 민감**합니다.
    
- 중앙에 더 큰 가중치를 둡니다.
    

### ✔ 커널:

**수평 방향 (Gx):**
$$
\begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}
$$
**수직 방향 (Gy):**

$$
\begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}
$$
### ✔ 특징:

- 중간 행/열에 가중치 2를 부여하여 더 부드러운 미분 근사.
    
- 공간적 스무딩이 내장되어 있음.
    

---

## 🔹 Prewitt 연산자

### ✔ 핵심 특징:

- 더 단순한 커널을 사용.
    
- **노이즈에 더 민감**하지만 계산량이 적음.
    

### ✔ 커널:

**수평 방향 (Gx):**

$$
\begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix}
$$
**수직 방향 (Gy):**

$$
\begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}
$$
### ✔ 특징:

- 각 방향에서 **단순한 미분 근사**.
    
- 가중치가 균등 → 연산적으로 가볍지만 노이즈에 약함.
    

---

## 🔸 Sobel vs Prewitt 요약 비교

|항목|Sobel|Prewitt|
|---|---|---|
|커널 가중치|중심에 더 큰 가중치 (2배)|균등 가중치|
|노이즈 민감도|상대적으로 낮음|상대적으로 높음|
|연산량|조금 더 큼|더 단순|
|정확도|경계 추정 정확도 더 높음|상대적으로 낮음|

---

## 🔹 실제 사용 팁

- 실무나 연구에서는 대부분 **Sobel**을 선호합니다.  
    이유는 약간의 스무딩이 포함되어 있어 잡음에 덜 민감하기 때문입니다.
    
- 하지만 간단한 실험이나 계산량이 중요한 임베디드 환경에서는 **Prewitt**이 쓰일 수도 있습니다.
    

---

### 에지 강도(Edge Strength)

$$
s(y, x) = \sqrt{f'_x(y, x)^2 + f'_y(y,x)^2}
$$
- 에지일 가능성을 나타냄

### 그레이디언트 방향(Gradient Direction)
$$
d(y, x)=\arctan \left( \frac{f'_y(y,x)}{f'_x(y,x)} \right)
$$
- 에지의 진행 방향을 나타냄
- 에지 방향은 그레이디언트 방향을 90도 회전한 방향으로 정의함

## 프로그램 4-1: 소벨 에지 검출(Sobel 함수 사용)하기
---
```python
import cv2 as cv


img = cv.imread('god.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3)
grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3)

sobel_x = cv.convertScaleAbs(grad_x)
sobel_y = cv.convertScaleAbs(grad_y)

edge_strength = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv.imshow('Original', gray)
cv.imshow('sobelx', sobel_x)
cv.imshow('sobely', sobel_y)
cv.imshow('edge_strength', edge_strength)

cv.waitKey()
cv.destroyAllWindows()
```

