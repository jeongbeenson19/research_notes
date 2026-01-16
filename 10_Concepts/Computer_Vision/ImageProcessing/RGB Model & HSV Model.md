
## RGB와 HSV의 차이
---
### ✅ 1. RGB (Red, Green, Blue)

- **정의**: 색을 빨강(R), 초록(G), 파랑(B) 세 가지 빛의 강도로 표현하는 모델
    
- **형태**: (R, G, B) → 각 값은 0~255 범위 (8비트 기준)
    
- **사용 예시**: 모니터, TV, 카메라 등 디지털 디스플레이에서 사용
    
- **특징**
    
    - 색을 빛의 삼원색으로 혼합해서 표현
        
    - 기계 친화적 (컴퓨터가 이해하기 쉬움)
        
    - 인간이 색상(Hue)이나 명도(Value)를 직관적으로 파악하기 어려움
        

---

### ✅ 2. HSV (Hue, Saturation, Value)

- **정의**: 색상(H), 채도(S), 명도(V)로 색을 표현하는 모델
    
- **형태**: (H, S, V)
    
    - **Hue (색상)**: 0~360도 (색상환의 각도, 예: 빨강=0°, 초록=120°, 파랑=240°)
        
    - **Saturation (채도)**: 0~100% (회색~선명한 색)
        
    - **Value (명도)**: 0~100% (어두운~밝은)
        
- **사용 예시**: 이미지 처리, 그래픽 디자인, 색 보정
    
- **특징**
    
    - 인간의 인식에 더 가까운 색 표현 방식
        
    - 색상 조절, 필터 적용 등에 직관적
        
    - 예: "노란색을 조금 더 진하게"라는 요구를 S 값 조절로 쉽게 구현 가능
        

---

### ✅ 주요 차이점 요약

|항목|RGB|HSV|
|---|---|---|
|구성 요소|Red, Green, Blue|Hue, Saturation, Value|
|표현 방식|빛의 조합으로 색 표현|색상/채도/명도 분리|
|직관성|낮음 (기계 중심)|높음 (사람 중심)|
|용도|디지털 기기 출력 등|색 조정, 필터링, 이미지 분석 등에 활용|

---

### ✅ 예시

- RGB (255, 0, 0) → 완전한 빨강
    
- HSV (0°, 100%, 100%) → 역시 완전한 빨강
    
- RGB (128, 128, 128) → 회색
    
- HSV (0°, 0%, 50%) → 채도가 없고, 명도 50%의 회색
    

---

### 프로그램 3-1: RGB 컬러 영상을 채널별로 구분해 디스플레이하기
---
```python
import cv2 as cv

import sys

  

img = cv.imread('silver.png')

  

if img is None:

sys.exit('파일을 찾을 수 없습니다.')

  

cv.imshow('original_RGB', img)

cv.imshow('Upper left half', img[0:img.shape[0]//2, 0:img.shape[1]//2])

cv.imshow('Center half', img[img.shape[0]//4:3 *

img.shape[0]//4, img.shape[1]//4:3*img.shape[1]//4, :])

  

cv.imshow('R channel', img[:, :, 2])

cv.imshow('G channel', img[:, :, 1])

cv.imshow('B channel', img[:, :, 0])

  

cv.waitKey()

cv.destroyAllWindows()
```
