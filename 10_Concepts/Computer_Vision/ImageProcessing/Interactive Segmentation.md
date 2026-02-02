
**대화식 분할 (Interactive Segmentation)** 은 사용자의 **입력(예: 클릭, 마스크, 드로잉 등)** 을 바탕으로 컴퓨터가 이미지를 분할하는 기법입니다.  
즉, **사람의 직관과 기계의 연산력을 결합**하여 더 정밀한 분할 결과를 얻는 방식입니다.

---

## 🧠 1. 대화식 분할이란?

> 사용자가 **일부 정보(전경/배경 표시 등)** 를 주면,  
> 알고리즘이 이를 바탕으로 **전경 객체 전체를 자동 분할**합니다.

---

## 🔎 2. 대표적인 대화식 분할 방식

|방식|설명|대표 알고리즘|
|---|---|---|
|점 클릭 기반|전경/배경 일부를 클릭|GrabCut, Deep Extreme Cut (DEXTR)|
|드로잉 기반|사용자가 직접 전경/배경을 브러시로 칠함|GraphCut + Scribbles|
|박스 기반|사각형 영역을 지정하면 내부 객체 추정|GrabCut|
|마스크 기반|초기 마스크를 주면 정제|Interactive Segmentation Networks (e.g. RITM)|

---

## 📌 3. 대표 알고리즘

### 3.1 🔵 GrabCut (OpenCV에도 포함)

- 사용자가 사각형으로 전경을 둘러싸면, GMM 기반으로 전경/배경 분리
    
- 반복적인 최적화(그래프 컷)로 영역 정제
    

### 프로그램 4-7: GrabCut을 이용해 물체 분할하기

```python
import cv2 as cv
import numpy as np

# 이미지 불러오기
img = cv.imread('silver.png')
img_show = np.copy(img)  # 원본을 복사해서 표시용 이미지로 사용

# 초기 이미지 표시
cv.imshow('Painting', img_show)

# GrabCut 마스크 초기화: 모든 픽셀을 "아마도 배경(GC_PR_BGD)"으로 설정
mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
mask[:, :] = cv.GC_PR_BGD

# 브러시 크기 및 색상 설정
BrushSiz = 9
LColor, RColor = (255, 0, 0), (0, 0, 255)  # 왼쪽 클릭(파란색), 오른쪽 클릭(빨간색)

# 마우스 이벤트에 따라 사용자 입력을 반영
def painting(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:  # 왼쪽 버튼 클릭: 전경(FGD) 설정
        cv.circle(img_show, (x, y), BrushSiz, LColor, -1)  # 시각적 표시
        cv.circle(mask, (x, y), BrushSiz, cv.GC_FGD, -1)   # 마스크에 전경으로 마킹
    elif event == cv.EVENT_RBUTTONDOWN:  # 오른쪽 버튼 클릭: 배경(BGD) 설정
        cv.circle(img_show, (x, y), BrushSiz, RColor, -1)
        cv.circle(mask, (x, y), BrushSiz, cv.GC_BGD, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        # 마우스 이동 + 왼쪽 버튼 누른 상태: 전경 그리기 지속
        cv.circle(img_show, (x, y), BrushSiz, LColor, -1)
        cv.circle(mask, (x, y), BrushSiz, cv.GC_FGD, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        # 마우스 이동 + 오른쪽 버튼 누른 상태: 배경 그리기 지속
        cv.circle(img_show, (x, y), BrushSiz, RColor, -1)
        cv.circle(mask, (x, y), BrushSiz, cv.GC_BGD, -1)
    cv.imshow('Painting', img_show)  # 수정된 이미지 다시 표시

# 마우스 콜백 설정
cv.namedWindow('Painting')
cv.setMouseCallback('Painting', painting)

# 사용자 입력을 기다리는 루프 (q 키를 누르면 종료)
while True:
    if cv.waitKey(0) == ord('q'):
        break

# GrabCut 수행을 위한 임시 모델 배열 생성
background = np.zeros((1, 65), np.float64)  # 배경 모델
foreground = np.zeros((1, 65), np.float64)  # 전경 모델

# GrabCut 알고리즘 실행
# - img: 원본 이미지
# - mask: 사용자 지정 마스크
# - rect: 사각형 None (마스크 기반으로 수행)
# - bgdModel / fgdModel: 알고리즘 내부 계산용 모델
# - iterCount: 반복 횟수 (5회)
# - mode: 마스크를 이용한 초기화
cv.grabCut(img, mask, None, background, foreground, 5, cv.GC_INIT_WITH_MASK)

# 마스크 결과를 0 또는 1로 변환 (배경은 0, 나머지는 1)
mask2 = np.where(
    (mask == cv.GC_BGD) | (mask == cv.GC_PR_BGD), 0, 1).astype('uint8')

# 마스크를 원본 이미지에 적용하여 전경만 남기기
grab = img * mask2[:, :, np.newaxis]  # 각 채널에 마스크 적용

# 결과 이미지 표시
cv.imshow('Grab cut image', grab)

# 아무 키나 누르면 종료
cv.waitKey()
cv.destroyAllWindows()

```

---

### 3.2 🔴 Scribble-based Graph Cut

- 사용자가 전경/배경 일부에 선(Scribble)을 그리면
    
- 그래프 컷 알고리즘이 전체 영역을 분할
    

> Ex: Adobe Photoshop의 "선택 및 마스크" 기능

---

### 3.3 🟣 Deep Extreme Cut (DEXTR)

- **4개의 극점 (상/하/좌/우)**를 사용자가 클릭
    
- 이를 입력으로 CNN이 전체 객체의 마스크 예측
    

> CNN + 위치 마스크 → 객체 분할  
> 특히 **의료 영상**이나 복잡한 장면에서 효과적

---

### 3.4 🟢 RITM (Region-based Interactive Topological Modeling)

- 최근 딥러닝 기반 대화식 분할 SOTA 중 하나
    
- **사용자의 클릭**을 점차 추가하면서 마스크를 refinement함
    
- 클릭 history + 이미지 → CNN이 마스크 반복 개선
    

---

## 🎯 4. 특징 및 활용

|장점|단점|
|---|---|
|사용자 직관이 반영돼 정밀함|완전 자동이 아님|
|다양한 상황(복잡한 배경 등)에 적응 가능|사용자 개입 필요|
|클릭 몇 번으로 정확도 향상|실시간 처리엔 무거울 수 있음|

---

## 🖼️ 5. 주요 활용 예

- 의료 영상에서 병변, 장기 추출
    
- 동영상 편집에서 객체 분리 (예: 사람 배경 제거)
    
- 자율주행 데이터셋 라벨링
    
- 지리정보(GIS) 영상 라벨링
    
- 훈련용 데이터셋 제작 (manual labeling 보조)
    

---

## 📘 정리

|항목|설명|
|---|---|
|정의|사용자 입력에 기반하여 이미지를 분할|
|주요 입력|클릭, 선(Scribble), 사각형, 마스크 등|
|알고리즘|GrabCut, GraphCut, DEXTR, RITM 등|
|장점|정밀도 높고 직관적|
|단점|사용자 개입이 필요함|
|활용|의료, 동영상, 라벨링, 훈련 데이터 제작 등|

---

## 🧠 능동 외곽선 (Active Contour Model, Snake)란?

**능동 외곽선**은 영상에서 **객체의 윤곽(경계)을 찾아내기 위한 곡선 기반 분할 기법**입니다.  
초기 윤곽선을 설정한 뒤, 이미지 내부의 경계, 에지, 색상 정보 등에 따라  
윤곽선이 **자동으로 움직이며 객체의 실제 경계에 수렴**하도록 만들어진 알고리즘입니다.

---

## 🧩 핵심 아이디어

> 초기 곡선을 영상 위에 두고,  
> 곡선이 에너지 최솟값이 되도록 변형하면서  
> **객체의 윤곽을 찾아가는** 방식

---

## 📐 수학적 개념

능동 외곽선은 **에너지 최소화 문제**로 정의됩니다.

### 🎯 전체 에너지 함수

$$
E_{\text{snake}} = \int \left[ \alpha E_{\text{internal}} + \beta E_{\text{image}} + \gamma E_{\text{external}} \right] ds
$$

### 1. 내부 에너지 (Internal Energy)

- 곡선 자체의 형태 유지
    
- 매끄러움(smoothness)을 보장
    
- 두 가지 성분:
    
    - 탄성 에너지 (elasticity, 1차 미분)
        
    - 곡률 에너지 (rigidity, 2차 미분)
        

$$
E_{\text{internal}} = \alpha |\mathbf{v}'(s)|^2 + \beta |\mathbf{v}''(s)|^2
$$

### 2. 이미지 에너지 (Image-based Energy)

- 영상에서의 정보 (에지, 색상 등)
    
- 경계(edge)를 찾아가도록 유도
    

$$
E_{\text{image}} = -|\nabla I(x,y)|^2
$$

### 3. 외부 에너지 (External Constraint)

- 사용자의 입력(포인트, 선 등)에 따른 제약
    
- 예: 끌어당기는 힘, 고정된 점 등
    

---

## 🧪 시각적 예시

1. 초기 윤곽선을 대략적으로 그림
    
2. 에너지를 반복적으로 최소화 → 곡선이 객체 윤곽에 수렴
    
3. 객체 외곽이 정확히 추출됨
    

---

## 🛠️ OpenCV & Python 사용 예 (cv2.createContour)

OpenCV에는 기본적인 Snakes는 구현되어 있지 않지만,  
`scikit-image` 라이브러리를 통해 `active_contour()` 함수를 사용할 수 있어요.

```python
from skimage import data, color
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import matplotlib.pyplot as plt
import numpy as np

img = data.astronaut()
img_gray = color.rgb2gray(img)
img_smooth = gaussian(img_gray, 3)

s = np.linspace(0, 2*np.pi, 400)
r = 220 + 100*np.sin(s)
c = 220 + 100*np.cos(s)
init = np.array([r, c]).T

snake = active_contour(img_smooth, init, alpha=0.01, beta=0.1, gamma=0.01)

plt.figure()
plt.imshow(img_gray, cmap='gray')
plt.plot(init[:, 1], init[:, 0], '--r', label='Initial')
plt.plot(snake[:, 1], snake[:, 0], '-b', label='Final')
plt.legend()
plt.show()
```

---

## ✅ 장점 vs ❌ 단점

|장점|단점|
|---|---|
|직관적이고 수학적으로 명확|초기 윤곽선 설정이 민감|
|부드러운 경계 탐지 가능|노이즈에 약하고 에지가 약하면 실패 가능|
|사용자 개입 가능|로컬 최적해에 빠질 수 있음|

---

## 🎯 주요 응용 분야

- **의료 영상**: 장기, 종양, 혈관 경계 검출
    
- **문서 분석**: 문자 또는 셀 외곽선 추출
    
- **영상 분할 전처리**
    
- **객체 추적**: 능동 곡선을 프레임별로 추적
    

---

## 🔄 변형 모델

- **Gradient Vector Flow (GVF) Snake**:  
    에지 주변에서 더 멀리까지 힘을 전달할 수 있게 개선한 방식
    
- **Balloon Snake**:  
    윤곽선이 스스로 팽창하거나 수축하며 더 쉽게 수렴하게 함
    
- **Level Set Method**:  
    스네이크의 한계를 극복하고 자동 위상 변화(분리, 병합 등)를 처리 가능
    

---

## 🧾 요약표

|항목|설명|
|---|---|
|정식 명칭|Active Contour Model (Snake)|
|목표|객체의 외곽선 자동 추출|
|핵심 방식|에너지 최소화 기반 윤곽선 이동|
|입력|초기 윤곽선 (곡선 형태)|
|출력|객체 경계에 수렴한 최종 곡선|
|알고리즘 구성|내부 에너지 + 이미지 에너지 + 외부 에너지|
|확장|GVF, Balloon, Level Set 등|

---

### 📌 비교해볼 개념들

- **GrabCut** vs **능동 외곽선**:  
    GrabCut은 픽셀 기반 분할 (GMM), Snake는 곡선 기반 경계 추출
    
- **Edge Detection** vs **능동 외곽선**:  
    전자는 단순한 경계 검출, 후자는 경계 위 곡선을 자동 정렬함
    

---
