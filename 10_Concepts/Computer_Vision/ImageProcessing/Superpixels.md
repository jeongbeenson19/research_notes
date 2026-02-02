
**Superpixels(슈퍼픽셀)** 은 **비슷한 속성을 가진 픽셀들을 묶어 놓은 작은 영역(Region)** 을 의미합니다. 즉, 이미지를 수많은 개별 픽셀 단위로 다루지 않고, **시각적으로 의미 있는 작은 조각**으로 표현하는 방법입니다.

---

## ✅ **왜 필요한가?**

1. **연산량 감소**
    
    - 원본 이미지가 100만 픽셀이라면 모든 픽셀을 직접 처리하는 건 비효율적입니다.
        
    - Superpixels로 묶으면 수천 개의 영역만 처리하면 되므로 연산량이 크게 줄어듭니다.
        
2. **객체 경계 보존**
    
    - 픽셀 단위보다 경계가 더 자연스럽게 유지됩니다.
        
    - 예: 머리카락, 물체 윤곽 등
        
3. **후처리 및 전처리에 활용**
    
    - **객체 탐지(Selective Search)**, **세그멘테이션**, **Saliency Detection**, **Optical Flow** 등에서 전처리 단계로 사용됩니다.
        

---

## ✅ **생성 방식**

대표적인 Superpixels 생성 알고리즘은 다음과 같습니다.

1. **[[Felzenszwalb & Huttenlocher’s graph-based segmentation|Felzenszwalb & Huttenlocher (Graph-based segmentation)]]**
    
    - Selective Search 초기 단계에서 사용됨.
        
    - 그래프 기반 병합으로 Superpixels 생성.
        
2. **SLIC (Simple Linear Iterative Clustering)**
    
    - K-means 유사한 클러스터링 방식.
        
    - 공간 좌표 + 색상 정보를 이용해 일정 크기의 Superpixels을 만듦.
        
    - 현재 가장 널리 쓰이는 방식.
        
3. **SEEDS, Quickshift, TurboPixels 등**
    
    - 다양한 방법 존재하지만 공통적으로 **색상 + 공간적 연속성**을 고려.
        

---

## ✅ **특징**

- 각 Superpixel은 **색상, 질감, 밝기 등이 비교적 균일**합니다.
    
- 크기와 개수는 알고리즘의 파라미터(예: SLIC의 `n_segments`)에 따라 조절 가능합니다.
    

---

## ✅ **시각적 예시 (설명)**

원본 이미지 → Superpixels 변환:

```
원본:   [개별 픽셀]
결과:   [각 Superpixel이 비슷한 색으로 채워짐, 경계가 선명함]
```

예를 들어 사람의 얼굴을 Superpixels으로 나누면, **눈/코/입/피부 영역별로 비슷한 색상끼리 묶여 하나의 조각**처럼 표현됩니다.

---

### 📌 **정리**

- **Superpixels = 픽셀 그룹화 단위**
    
- **[[Selective Search]]**: 이 Superpixels을 **기본 단위**로 사용하여 큰 영역으로 점진적 병합 진행.
    
- **Feature Extraction** 이전 단계에서 **연산 효율화 + 경계 보존** 역할.
    

---
