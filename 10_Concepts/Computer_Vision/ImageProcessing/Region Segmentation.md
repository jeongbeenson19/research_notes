
## 📌 영역 분할(Segmentation)이란?

**영역 분할**이란 이미지를 **픽셀 수준에서 의미 있는 영역들로 나누는 작업**입니다.

즉,

> “이 픽셀은 고양이, 저 픽셀은 배경”처럼  
> **픽셀 하나하나가 어떤 객체(또는 영역)에 속하는지를 구분**하는 과정입니다.

---

## 📚 주요 종류

|종류|설명|
|---|---|
|**Semantic Segmentation**|같은 클래스를 하나로 취급 (예: 모든 고양이 픽셀은 동일하게 "고양이")|
|**Instance Segmentation**|같은 클래스 내에서도 개별 객체를 구분 (고양이 1, 고양이 2)|
|**Panoptic Segmentation**|Semantic + Instance를 결합한 개념|

---

## 🎯 전통적 영역 분할 방법

### 1. Thresholding (임계값 분할)

- 회색조 이미지에서 **일정 임계값**을 기준으로 픽셀을 분할
    
- ex: 이진화(`cv2.threshold`)
    

```python
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
```

> ✅ 간단하지만 조명 변화에 민감

---

### 2. Edge-based Segmentation

- **에지(경계선)를 찾아서 분할**하는 방식
    
- Canny, Sobel 등의 필터 활용
    

> ✅ 경계가 뚜렷한 물체에 효과적  
> ❌ 에지 누락이나 잡음에 민감

---

### 3. Region-based Segmentation

#### 3-1. Region Growing

- **시드 픽셀(seed pixel)**에서 시작해 비슷한 이웃을 병합
    

#### 3-2. Watershed Algorithm

- 이미지를 **지형처럼 해석**하여, 물이 고이는 영역을 따라 분할
    
- **거리 변환(Distance Transform)** 과 함께 많이 사용
    

```python
cv2.watershed(image, markers)
```

> ✅ 분할 정확도 높음  
> ❌ 오버세그먼트(over-segmentation) 가능성 있음

---

### 4. Clustering 기반

#### 4-1. K-means Segmentation

- 픽셀을 **색상 또는 위치 기반으로 클러스터링**
    

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3).fit(image.reshape(-1, 3))
segmented = kmeans.labels_.reshape(image.shape[:2])
```

#### 4-2. Mean Shift

- 비모수(non-parametric) 기반 클러스터링
    

---

**SLIC (Simple Linear Iterative Clustering)** 은 **영역 분할(Segmentation)** 에서 **Superpixel 기반 Segmentation 기법**에 해당합니다.

---

## 🧩 SLIC은 어디에 속하나?

|분류|포함 여부|설명|
|---|---|---|
|✅ Region-based Segmentation|**Yes**|인접한 픽셀 간의 색상/거리 유사성을 기반으로 병합|
|✅ Clustering 기반|**Yes**|실제로는 K-means 알고리즘을 개선한 방식 사용|
|❌ 딥러닝 기반|No|전통적인 알고리즘이며 학습은 하지 않음|

즉, **"클러스터링 기반의 지역(region) 병합 방식"**이라  
Region-based와 Clustering 기반 둘 다의 특성을 가지고 있습니다.

---

## 🔍 SLIC (Simple Linear Iterative Clustering) 요약

### 📌 목적

이미지를 **수백~수천 개의 Superpixel**로 나누어,  
각 Superpixel이 유사한 색상 및 공간 정보를 갖도록 함

> 🔸 Superpixel: 비슷한 픽셀끼리 묶은 작은 덩어리  
> 🔸 이후 딥러닝, 객체 추적, 영상 이해 등에서 전처리로 많이 사용됨

---

## ⚙️ 핵심 원리

- **K-means 클러스터링**을 변형한 방식
    
- 색상 + 공간 정보 $(L, a, b, x, y)$를 함께 고려  
    (Lab 색공간 사용 → 인간의 시각적 유사성에 더 가깝게)
    

### 거리 함수:

$$
D = \sqrt{d_{lab}^2 + \left(\frac{d_{xy}}{S}\right)^2 \cdot m^2}
$$

- $d_{lab}$: 색상 거리
    
- $d_{xy}$: 픽셀 위치 거리
    
- $S$: Superpixel 간격 (초기 클러스터 중심 간 거리)
    
- $m$: Compactness 계수 → 클러스터의 뭉침 정도 제어
    

---

## 프로그램 4-5: SLIC 알고리즘으로 입력 영상을 슈퍼 화소 분할하기

```python
import skimage
import numpy as np
import cv2 as cv


img = skimage.data.coffee()
cv.imshow('Coffee image', cv.cvtColor(img, cv.COLOR_RGB2BGR))

slic1 = skimage.segmentation.slic(img, compactness=20, n_segments=600)
sp_img1 = skimage.segmentation.mark_boundaries(img, slic1)
img1 = np.uint8(sp_img1*255.0)
  
slic2 = skimage.segmentation.slic(img, compactness=40, n_segments=600)
sp_img2 = skimage.segmentation.mark_boundaries(img, slic2)
sp_img2 = np.uint8(sp_img2*255.0)

cv.imshow('Super pixes (compact 20)', cv.cvtColor(sp_img1, cv.COLOR_RGB2BGR))
cv.imshow('Super pixes (compact 40)', cv.cvtColor(sp_img1, cv.COLOR_RGB2BGR))

cv.waitKey()
cv.destroyAllWindows()

```

---
## 프로그램 4-6: 정규화 절단 알고리즘으로 영역 분할하기
```python
import skimage
import numpy as np
import cv2 as cv
import time


coffee = skimage.data.coffee()
start = time.time()

slic = skimage.segmentation.slic(
coffee, compactness=20, n_segments=600, start_label=1)


g = skimage.graph.rag_mean_color(coffee, slic, mode='similarity')
ncut = skimage. graph.cut_normalized(slic, g)
print(coffee.shape, 'Coffee 영상을 분할하는 데', time.time()-start, '초 소요')


marking = skimage.segmentation.mark_boundaries(coffee, ncut)
ncut_coffee = np.uint8(marking*255)


cv.imshow('Normalized cut', cv.cvtColor(ncut_coffee, cv.COLOR_RGB2BGR))


cv.waitKey()
cv.destroyAllWindows()
```

## ✅ 장점 vs ❌ 단점

|장점|단점|
|---|---|
|빠르고 메모리 효율적|완전한 객체 분할은 아님|
|경계 보존 가능|클러스터 수를 지정해야 함|
|다른 딥러닝/후처리와 잘 결합됨|물체 의미 이해는 불가|

---

## 🔗 활용 예

- 딥러닝 입력 축소 (Superpixel로 downsampling)
    
- 객체 추적 (영역 단위로 트래킹)
    
- 의료 영상 분할
    
- 영상 전처리 (ROI 추출 등)
    

---

## 🧾 요약

|항목|설명|
|---|---|
|분류|Clustering 기반, Region-based Segmentation|
|방식|Lab 색상 + 위치 정보 기반의 K-means 변형|
|결과|수백~수천 개의 Superpixel 영역|
|핵심 파라미터|`n_segments`, `compactness`|
|라이브러리|`skimage.segmentation.slic()`|

---

## 🤖 딥러닝 기반 영역 분할

최근에는 거의 **딥러닝 기반 세분화(Segmentation)** 가 표준입니다.

### 1. FCN (Fully Convolutional Network)

- CNN의 완전연결층을 제거하고 **픽셀 단위로 분류** 가능하게 함
    

### 2. [[U-Net Convolutional Networks for Biomedical  Image Segmentation|U-Net]]

- 의료 영상 등에서 많이 사용
    
- **인코더-디코더 구조 + 스킵 연결**로 정밀한 분할 가능
    

### 3. DeepLab (v3, v3+)

- **Atrous Convolution**과 **CRF**로 경계 정교화
    
- Semantic segmentation에서 강력한 성능
    

### 4. Mask R-CNN (Instance Segmentation)

- Faster R-CNN에 **segmentation 브랜치 추가**
    
- 각 객체 인스턴스별로 mask 예측
    

---

## 🧠 평가 지표 (Segmentation 평가)

|지표|설명|
|---|---|
|**IoU (Intersection over Union)**|예측 마스크와 실제 마스크 간의 겹침 비율|
|**Pixel Accuracy**|전체 픽셀 중 맞게 분류된 비율|
|**Dice Coefficient**|2 * TP / (2 * TP + FP + FN) — 의료 영상에서 자주 사용|

---

## 🧪 실전 예시 (U-Net with PyTorch)

```python
class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        self.encoder = ...
        self.decoder = ...
        self.final = nn.Conv2d(...)

    def forward(self, x):
        x1 = self.encoder(x)
        ...
        out = self.final(x_decoded)
        return torch.sigmoid(out)  # binary segmentation
```

---

## ✅ 요약 정리

|항목|설명|
|---|---|
|목적|픽셀 단위로 의미 있는 영역 구분|
|고전 기법|Thresholding, Edge, Region Growing, Watershed|
|딥러닝 기법|FCN, U-Net, DeepLab, Mask R-CNN|
|사용 분야|자율주행, 의료 영상, 인스턴스 구분 등|
|지표|IoU, Dice, Pixel Accuracy|

---

## 🔍 추천 논문 / 학습 자료

- **"U-Net: Convolutional Networks for Biomedical Image Segmentation"** (2015)
    
- **"Mask R-CNN" (He et al., 2017)**
    
- DeepLab v3+: Semantic Image Segmentation with DeepLab
    

---
