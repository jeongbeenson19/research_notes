
## 📌 1. 기초 수학: 선형대수와 좌표계

### 1.1. 벡터와 행렬

- **벡터**는 방향과 크기를 가지며, 점이나 방향을 표현.
    
- **행렬**은 벡터를 선형 변환(linear transformation)하는 도구.
    

### 1.2. 동차 좌표(Homogeneous Coordinates)

- 2D 점 $(x, y)$ → $(x, y, 1)$로 표현.
    
- 이로써 **이동(translation)** 을 행렬 곱으로 표현 가능.
    

---

## 📌 2. 2D 기하 변환 (Image Plane 상의 변환)

### 2.1. 기본 변환 (Affine Transformations)

2D 변환 행렬 (3x3):

$$
\begin{bmatrix} a & b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{bmatrix}
$$

- **이동 (Translation)**  
    이동 벡터 $(t_x, t_y)$
    
- **회전 (Rotation)**  
    각도 $\theta$일 때:
    
    $$
    \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}
    $$
    
- **스케일 (Scaling)**  
    $(s_x, s_y)$
    
- **기울이기 (Shearing)**  
    평행 사변형 모양으로 변형
    

> 이 네 가지는 **Affine Transform**으로 통합적으로 표현 가능

### 2.2. 원근 변환 (Perspective or Projective Transform)

- Homography matrix $H \in \mathbb{R}^{3 \times 3}$
    
- 두 평면 간의 대응을 정의
    

$$
x' \sim Hx \quad \text{(x, x': homogeneous coordinates)}
$$

- 카메라 이동, 시점 변화, planar object alignment 등에 사용됨.
    

---

## 📌 3. 3D 기하와 카메라 모델

### 3.1. 핀홀 카메라 모델 (Pinhole Camera Model)

3D 점 $X = [X, Y, Z, 1]^T$ → 2D 이미지 점 $x = [u, v, 1]^T$

$$
x \sim K[R|t]X
$$

- $K$: **내부 파라미터(intrinsic matrix)**  
    (초점 거리, 중심점 등 포함)
    
- $R, t$: **외부 파라미터(extrinsic parameters)**  
    (카메라의 회전, 위치)
    

### 3.2. 삼각측량 (Triangulation)

- 여러 시점에서의 이미지 점들로부터 3D 점 복원
    

### 3.3. 에피폴라 기하 (Epipolar Geometry)

- 두 카메라 간의 대응점 관계를 수학적으로 모델링
    
- 핵심 요소:
    
    - **기본 행렬 (Fundamental Matrix) F**
        
    - **필수 행렬 (Essential Matrix) E**
        

---

## 📌 4. 실전 응용 예시

### 4.1. 카메라 캘리브레이션

- 내부/외부 파라미터 추정
    
- OpenCV의 `cv2.calibrateCamera()` 사용
    

### 4.2. Homography를 이용한 이미지 정합

- 한 평면 위에 있는 두 이미지 매칭
    
- 예: 증강현실에서 마커 인식, 문서 스캔 자동 정렬
    

### 4.3. 스테레오 비전

- 왼쪽/오른쪽 이미지로부터 깊이 정보 추출 (Disparity map → Depth map)
    

### 4.4. Visual SLAM

- 카메라 움직임과 지도 동시 추정 (기하 추정 핵심)
    

---

## 🧠 보충 학습 리소스

- 📘 _Multiple View Geometry in Computer Vision_ by Hartley & Zisserman (고전 교재)
    
- 📘 _Computer Vision: Algorithms and Applications_ by Richard Szeliski (무료 PDF 공개)
    
- 📘 OpenCV-Python Tutorials: [https://docs.opencv.org](https://docs.opencv.org/)
    

---

## 🔁 요약

|개념|설명|핵심 수학 도구|
|---|---|---|
|2D 변환|이미지 회전/이동/변형|Affine, Homography|
|3D→2D 투영|카메라 모델|Intrinsic/Extrinsic matrix|
|점 대응|Epipolar geometry|Fundamental/Essential Matrix|
|깊이 추정|스테레오, Triangulation|Triangulation, disparity|
|실전 응용|AR, SLAM, 재구성|모든 기하 연산|

---

영상 보간(Video Interpolation)은 **연속된 두 영상 프레임 사이에 새로운 중간 프레임을 생성**하는 기술입니다. 이는 시간 해상도(temporal resolution)를 높이기 위해 사용되며, 영상의 **슬로우 모션 생성, 프레임 레이트 향상(FPS 증가), 안정화, 보정** 등에 활용됩니다.

---

## 📌 1. 영상 보간의 기본 개념

### ✅ 정의

- 두 프레임 $I_t$, $I_{t+1}$가 주어졌을 때, 시간적으로 중간에 해당하는 $I_{t+\alpha}$ $(0 < \alpha < 1)$를 생성하는 것.
    

---

## 📌 2. 보간 방법 분류

### 1. **단순 보간 (Basic Interpolation)**

- 각 픽셀 위치에서 선형적으로 보간:
    

$$
I_{t+\alpha}(x, y) = (1 - \alpha) \cdot I_t(x, y) + \alpha \cdot I_{t+1}(x, y)
$$
- 📌 **한계**: 객체의 움직임을 고려하지 않으므로 **블러링(ghosting)**이나 **왜곡** 발생
    

---

### 2. **옵티컬 플로우 기반 보간 (Optical Flow-based Interpolation)**

#### ✅ 옵티컬 플로우란?

- 두 프레임 간의 **픽셀 단위 움직임 벡터(Flow Field)**를 추정하는 것
    

$$
F_{t \rightarrow t+1}(x, y) = \text{픽셀이 이동한 벡터}
$$

#### ✅ 사용 방식

1. $I_t$에서 $I_{t+1}$까지의 Flow 계산
    
2. Flow를 이용해 중간 시점의 픽셀 위치를 역방향으로 추정 (backward warping)
    
3. 두 프레임의 역방향 warping 결과를 가중합으로 보간
    

#### ✅ 장점

- 객체의 움직임을 반영
    
- 부드러운 중간 프레임 생성 가능
    

#### ✅ 단점

- Flow 추정이 어려움 (특히 경계, 투명, 빠른 움직임)
    

---

### 3. **딥러닝 기반 보간 (Deep Learning-based Interpolation)**

#### ✅ 대표 모델

- **Super SloMo (CVPR 2018)**  
    : 옵티컬 플로우 + 프레임 보간을 딥러닝으로 공동 학습
    
- **DAIN (Depth-Aware Interpolation Network)**  
    : 깊이 정보까지 고려하여 occlusion 처리 개선
    
- **FILM (Frame Interpolation for Large Motion)**  
    : 플로우 없이 CNN이 직접 보간
    

#### ✅ 특징

- 학습 기반으로 움직임과 경계 정보 등을 더 잘 처리
    
- occlusion, 불확실성 영역도 개선
    

---

## 📌 3. 영상 보간의 주요 과제

|문제|설명|
|---|---|
|**Occlusion**|두 프레임 중 하나에만 존재하는 픽셀 (가려짐) 처리|
|**Large Motion**|빠른 움직임 → 정확한 보간 어려움|
|**Blur / Ghosting**|단순 보간 시 경계 모호함|
|**Flow Error**|옵티컬 플로우가 틀리면 보간도 오류 발생|

---

## 📌 4. 실전 활용 예시

|응용 분야|설명|
|---|---|
|🎥 슬로우 모션 영상 생성|일반 영상 → 슬로우 모션 변환|
|🎮 게임 리플레이 향상|프레임 증가로 부드럽게 재생|
|🧠 신경망 훈련 데이터 증강|중간 프레임 생성으로 데이터 다양성 증가|
|📺 비디오 품질 향상|저프레임 영상을 고프레임처럼 보이게|

---

## 📌 5. 코드 예시 (Python + OpenCV)

### 선형 보간 예시 (단순)

```python
import cv2
import numpy as np

# 두 프레임 불러오기
frame1 = cv2.imread('frame1.png').astype(np.float32)
frame2 = cv2.imread('frame2.png').astype(np.float32)

# 알파값으로 중간 프레임 생성
alpha = 0.5
interpolated = (1 - alpha) * frame1 + alpha * frame2
interpolated = interpolated.astype(np.uint8)

cv2.imwrite('interpolated.png', interpolated)
```

### 딥러닝 기반 영상 보간 (예: RIFE 사용)

- [RIFE (Real-Time Intermediate Flow Estimation)](https://github.com/megvii-research/ECCV2022-RIFE)
    
- 명령어: `python inference_video.py --video input.mp4 --output output.mp4`
    

---

## 📌 6. 정리

|방식|설명|장점|단점|
|---|---|---|---|
|선형 보간|픽셀값만 단순 계산|빠름|움직임 반영 안 됨|
|옵티컬 플로우 기반|움직임 반영|상대적으로 정밀|Flow 추정 오류 민감|
|딥러닝 기반|움직임+깊이+경계 보정|매우 부드럽고 고화질|학습 필요, 느릴 수 있음|

---

# 🧠 전제

입력 이미지 $I(x, y)$에서 실수 위치 $(x', y')$의 픽셀 값을 구하고자 한다고 가정합니다.

예)  
이미지를 2배 확대할 때, 출력 좌표 $(i, j)$는 원래 이미지 좌표 $(x', y') = (i/2, j/2)$로 매핑됩니다.  
이때 $(x', y')$는 **소수점 좌표**이므로, 그 위치의 값을 예측하기 위해 **보간법**을 사용합니다.

---

## ✅ 1. 최근접 이웃 보간 (Nearest Neighbor Interpolation)

### 🎯 핵심 아이디어:

**가장 가까운 정수 좌표**의 픽셀 값을 그대로 복사

### 🧮 수식:

$$
I'(x', y') = I(\text{round}(x'), \text{round}(y'))
$$

### 🧑‍🏫 예시:

- $x' = 2.7,\ y' = 3.3$ 이면  
    $$
    \text{round}(x') = 3,\ \text{round}(y') = 3  
    $$
    → 출력 픽셀 = 입력의 (3,3)
    

### ✅ 장점

- 매우 빠름
    
- 연산량 거의 없음
    

### ❌ 단점

- 경계가 **거칠고 블록 형태**로 나타남 (계단 현상)
    

---

## ✅ 2. 양선형 보간 (Bilinear Interpolation)

### 🎯 핵심 아이디어:

**수직/수평 방향으로 선형 보간 2회 수행**

### 🧮 연산 과정:

1. 실수 좌표 $(x', y')$에서, 바닥 정수 좌표를 찾음:
    
    $$
    \begin{align}
    x_1 &= \lfloor x' \rfloor,\quad x_2 = x_1 + 1 \\
    y_1 &= \lfloor y' \rfloor,\quad y_2 = y_1 + 1
    \end{align}
    $$
2. 픽셀 값들:
    
$$
\begin{aligned} Q_{11} &= I(x_1, y_1) \\ Q_{21} &= I(x_2, y_1) \\ Q_{12} &= I(x_1, y_2) \\ Q_{22} &= I(x_2, y_2) \end{aligned}
$$
3. 비율 계산:
    

$$
dx = x' - x_1,\quad dy = y' - y_1
$$
4. 보간 수행:
    

$$
\begin{aligned} I'(x', y') &= (1 - dx)(1 - dy) \cdot Q_{11} \\ &\quad + dx(1 - dy) \cdot Q_{21} \\ &\quad + (1 - dx)dy \cdot Q_{12} \\ &\quad + dx dy \cdot Q_{22} \end{aligned}
$$

### ✅ 장점

- 경계가 부드럽고 시각적으로 자연스러움
    

### ❌ 단점

- 객체 경계가 **약간 흐릿**해짐
    

---

## ✅ 3. 양3차 보간 (Bicubic Interpolation)

### 🎯 핵심 아이디어:

**16개(4×4) 주변 픽셀 값을 이용해 2차원 cubic 함수로 보간**

### 🧮 과정 요약:

#### 1. 입력 위치 주변의 4×4 픽셀 추출

$$
(x', y') \text{에 대해 } \lfloor x' \rfloor - 1 \leq x \leq \lfloor x' \rfloor + 2
$$

총 16개의 픽셀을 사용합니다.

#### 2. 1차원 Cubic 보간 함수 사용

- 보통 **Catmull-Rom spline** 또는 **Keys cubic convolution**을 사용함
    
- 1차원에서:
    

$$
f(u) = a_0 + a_1 u + a_2 u^2 + a_3 u^3
$$

또는,

$$
f(x) = \sum_{i=-1}^{2} w(i, x) \cdot P_i
$$

여기서 $w(i, x)$는 가중치, $P_i$는 주변 픽셀

#### 3. 수행 방식

1. **4행** 각각에 대해 **x 방향으로 1차원 cubic 보간** 수행
    
2. 그 결과에 대해 **y 방향으로 다시 cubic 보간** 수행
    

### ✅ 장점

- 매우 부드러운 결과
    
- 가장 자연스러운 고해상도 이미지 생성
    

### ❌ 단점

- 연산량이 많고 느림
    
- 경계 Overshoot(고리현상, ringing artifact) 가능성
    

---

## 📊 성능 비교

|방법|연산량|경계 부드러움|속도|품질|
|---|---|---|---|---|
|최근접|최소|매우 낮음|★★★★★|★☆☆☆☆|
|양선형|적당함|중간|★★★★☆|★★☆☆☆|
|양3차|높음|매우 좋음|★★☆☆☆|★★★★☆|

---

## 프로그램 3-8: 보간을 이용해 영상의 기하 변환하기
---
```python
import cv2 as cv 


img = cv.imread('silver.png')
patch = img[250:350, 170:270, :]

img = cv.rectangle(img, (170, 250), (270, 350), (255, 0, 0), 3)
patch1 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5,
interpolation=cv.INTER_NEAREST)
patch2 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5,
interpolation=cv.INTER_LINEAR)
patch3 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5,
interpolation=cv.INTER_CUBIC)

cv.imshow('Original', img)
cv.imshow('Resize nearest', patch1)
cv.imshow('Resize bilinear', patch2)
cv.imshow('Resize bicubic', patch3)

cv.waitKey()
cv.destroyAllWindows()
```

---

## 🎓 요약 정리

|보간법|픽셀 수|수학적 특징|사용처|
|---|---|---|---|
|최근접|1|rounding|라벨 이미지, 빠른 디스플레이|
|양선형|2×2 = 4|선형 보간|일반 리사이징|
|양3차|4×4 = 16|Cubic 보간|고화질 확대, 디테일 보존|

---
