
**HOG (Histogram of Oriented Gradients)** 는 **객체 인식**, 특히 **사람 검출**에 자주 사용되는 특징 추출 기법입니다. 2005년 **Navneet Dalal**과 **Bill Triggs**가 논문 *"Histograms of Oriented Gradients for Human Detection"*에서 제안하였으며, 이후 OpenCV 등 다양한 라이브러리에서 지원하게 되었습니다.

---

## 🧠 핵심 개념 요약

> HOG는 "이미지의 국소 영역에서 방향성 있는 경계(edge) 분포를 히스토그램으로 요약"하는 방식으로 동작합니다.

---

## ✅ 주요 단계

### 1. 📦 입력 이미지 전처리

- 보통 흑백(grayscale) 이미지로 변환
    
- (선택) 히스토그램 평활화나 CLAHE 등으로 명암 대비 보정
    

---

### 2. 📏 그라디언트 계산 (Edge 방향 추출)

각 픽셀의 **수평(x)** 및 **수직(y)** 방향 변화량을 계산하여 **경계(edge)** 정보를 얻습니다.

- 일반적으로 [[Edge Operator#^ac73ae| Sobel 필터]] 사용:
    
    - $G_x = I(x+1, y) - I(x-1, y)$
        
    - $G_y = I(x, y+1) - I(x, y-1)$
        
- **크기 (magnitude)**:  
    $M = \sqrt{G_x^2 + G_y^2}$
    
- **방향 (angle)**:  
    $\theta = \arctan\left(\frac{G_y}{G_x}\right)$
    

---

### 3. 📊 셀(Cell)마다 방향 히스토그램 생성

- 이미지를 $8 \times 8$ 또는 $16 \times 16$ 픽셀 크기의 **셀**로 나눕니다.
    
- 각 셀에서 픽셀의 **그라디언트 방향**을 9개의 구간(0~180도 or 0~360도)으로 나눠 **히스토그램 생성**
    
- 각 방향 bin에 그라디언트 **크기(magnitude)** 로 가중치를 부여하여 누적
    

---

### 4. 🔄 블록(Block) 정규화

- 셀 단독 사용 시 조명 변화에 민감하므로, 여러 셀(보통 $2 \times 2$)을 하나의 블록으로 묶어 **L2-norm**으로 정규화
    
- 블록을 겹치게 슬라이딩하면서 전체 특징 벡터 추출 → **robustness 확보**
    

---

### 5. 🧮 특징 벡터 생성

- 전체 이미지 또는 ROI(region of interest)에 대해 위 과정을 반복
    
- 모든 블록의 히스토그램을 이어 붙인 하나의 **고차원 벡터** 생성
    

---

### 6. 🤖 분류기 학습 및 추론

- HOG 특징을 입력으로 사용하여 SVM 등 분류기 훈련
    
- 예: OpenCV의 `cv2.HOGDescriptor_getDefaultPeopleDetector()`는 사전 훈련된 SVM 사용
    

---

## 🔬 시각적 예시 (텍스트 버전)

```
[8x8 셀 내 edge 방향 예시]
↑ ↑ → → ↓ ↓ ← ←

→ 히스토그램
0~20°   : 2
20~40°  : 1
...     :
160~180°: 3
```

---

## 📐 파라미터 예시 (OpenCV 기본값 기준)

|파라미터|설명|
|---|---|
|`winSize`|검출 윈도우 크기 (기본: 64x128)|
|`blockSize`|블록 크기 (기본: 16x16)|
|`blockStride`|블록 이동 간격 (기본: 8x8)|
|`cellSize`|셀 크기 (기본: 8x8)|
|`nbins`|방향 히스토그램 bin 수 (기본: 9)|

---

## 📈 장점

- **사람 검출 성능 우수** (다양한 배경, 포즈에 견고)
    
- **구현 간단**, 실시간성 가능
    
- 학습 없이도 사전 모델(SVM) 사용 가능
    

## 📉 단점

- 딥러닝에 비해 **복잡한 객체 검출은 한계**
    
- **조명, 크기 변화**에 대해 완전한 불변성은 없음
    
- 계산량이 많을 수 있음 (특히 높은 해상도에서)
    

---

## 📚 참고 자료

- 논문: ["Histograms of Oriented Gradients for Human Detection"](https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf)
    
- OpenCV 문서:  
    [https://docs.opencv.org/4.x/d5/d33/structcv_1_1HOGDescriptor.html](https://docs.opencv.org/4.x/d5/d33/structcv_1_1HOGDescriptor.html)
    

---
