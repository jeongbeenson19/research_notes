
# **📌 핀홀 카메라 모델과 좌표계**

  

## **1. 개념**

  

핀홀 카메라 모델은 3차원 점이 2차원 영상 평면으로 투영되는 과정을 설명하는 이상적 모델이다.

이 과정은 **외부 파라미터**(세계→카메라 변환)와 **내부 파라미터**(카메라 평면→픽셀 변환)로 나뉜다.

---

## **2. 좌표계**

- **세계 좌표계 $\mathcal{W}$**: 점 $\mathbf{X}_w=[X,Y,Z]^T$
    
- **카메라 좌표계 $\mathcal{C}$**: 점 $\mathbf{X}_c=[X_c,Y_c,Z_c]^T$
    
- **정규화 영상 좌표계 $\mathcal{N}$**: $(x,y)=(X_c/Z_c, Y_c/Z_c)$
    
- **픽셀 좌표계 $\mathcal{I}$**: $\tilde{\mathbf{x}}=[u,v,1]^T$ (동차좌표)
    

---

## **3. 외부 파라미터**

  

$$

\mathbf{X}_c = R\mathbf{X}_w + \mathbf{t}, \quad

\mathbf{t}=-R\mathbf{C}

$$

- $R$: 세계→카메라 회전행렬
    
- $\mathbf{t}$: 이동 벡터
    
- $\mathbf{C}$: 카메라 중심 (월드 좌표계)
    

---

## **4. 내부 파라미터**

  

$$

K=\begin{bmatrix}

f_x & s & c_x \

0 & f_y & c_y \

0 & 0 & 1

\end{bmatrix},\quad

\tilde{\mathbf{x}} \sim K\begin{bmatrix}x \ y \ 1\end{bmatrix}

$$

- $f_x,f_y$: 축별 초점거리 (픽셀 단위)
    
- $c_x,c_y$: 주점(principal point)
    
- $s$: skew (일반적으로 0)
    

---

## **5. 전체 투영식**

  

$$

\tilde{\mathbf{x}} \sim K,[R|\mathbf{t}],\tilde{\mathbf{X}}_w = P\tilde{\mathbf{X}}_w

$$

  

비동차 형태:

  

$$

u=f_x \frac{X_c}{Z_c} + s\frac{Y_c}{Z_c}+c_x,\quad

v=f_y \frac{Y_c}{Z_c}+c_y

$$

  

단, $Z_c>0$일 때만 가시.

---

## **6. 역투영**

  

픽셀 좌표로부터 광선(ray)을 얻는다:

  

$$

\lambda \begin{bmatrix}x\y\1\end{bmatrix}=K^{-1}\tilde{\mathbf{x}}, \quad \lambda>0

$$

  

즉, 한 픽셀은 3차원 공간의 **무한 직선**에 대응하며, 깊이가 주어져야 점 위치를 특정할 수 있다.

---

## **7. 구현 포인트**

- OpenCV: cv2.projectPoints, cv2.undistortPoints
    
- 단위 혼동 주의 (mm ↔ m ↔ pixel)
    
- $\mathbf{t}$ 와 $\mathbf{C}$ 혼용 주의 ($\mathbf{t}=-R\mathbf{C}$)
    

---

## **📂 카테고리 제안**

- Computer Vision/Geometry
    
- 생성 권장:
    
    - Computer Vision/Geometry/Camera Model
        
    - Computer Vision/Geometry/Projection
        
    

---
