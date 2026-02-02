
**Bag-of-Visual-Words (BoVW 또는 BoW)** encoding은 전통적인 이미지 표현 기법으로, 이미지를 **고정된 길이의 벡터**로 변환하는 데 사용됩니다. 이는 자연어 처리에서의 **Bag-of-Words** 개념을 이미지에 확장한 방식입니다.

---

## 🔹 개요

|항목|설명|
|---|---|
|목적|다양한 크기와 복잡도를 가진 이미지들을 벡터로 정규화해 분류기나 회귀모델에 입력하기 위함|
|핵심 아이디어|이미지를 **시각적 단어(visual words)**의 집합으로 보고, 등장 빈도를 벡터화|
|적용 분야|이미지 분류, 검색, 지역 특징 기반 분석 등|

---

## 🔹 처리 흐름

BoVW는 다음의 파이프라인을 따릅니다:

1. **로컬 특징 추출**
    
    - SIFT, SURF, ORB 등의 keypoint descriptor를 이미지에서 추출
        
    - 각 이미지에서 수백~수천 개의 로컬 벡터(예: 128-D SIFT) 생성
        
2. **시각적 단어 사전 생성 (Vocabulary)**
    
    - 모든 이미지의 특징 벡터를 수집
        
    - **K-means clustering** 등을 통해 K개의 클러스터 중심(= visual words) 생성
        
    - 이 과정을 **codebook learning** 또는 **dictionary learning**이라고 부름
        
3. **Encoding (벡터화)**
    
    - 각 이미지에서 추출한 로컬 특징들을 가장 가까운 visual word에 할당
        
    - 각 visual word의 등장 횟수를 히스토그램으로 구성
        
    - 결과: 크기 K짜리 벡터 (K = 클러스터 수)
        
4. **(선택) 정규화 및 차원 축소**
    
    - L2-normalization, TF-IDF, PCA 등을 적용
        

---

## 🔹 예시

- K = 4인 경우, vocabulary는 4개의 클러스터 중심을 갖고 있음
    
- 이미지 A에서 추출된 descriptor 100개 중
    
    - word 1: 30개, word 2: 10개, word 3: 50개, word 4: 10개 →
        
    
    $\text{BoVW encoding} = [30, 10, 50, 10]$

→ 정규화하면 `[0.3, 0.1, 0.5, 0.1]`

---

## 🔹 장점

- 입력 이미지의 크기나 구조와 무관하게 고정된 벡터 표현 가능
    
- SIFT 같은 강력한 특징을 이용하여 견고한 표현 가능
    

---

## 🔹 단점

- **위치 정보 손실** (어디에서 나온 특징인지 모름)
    
- clustering 단계에서의 **정보 손실**
    
- deep learning의 등장 이후 표현력에서 밀림
    

---

## 🔹 보완 기법

|기법|설명|
|---|---|
|**Spatial Pyramid Matching (SPM)**|위치 정보를 coarse-to-fine 수준에서 보존|
|**VLAD (Vector of Locally Aggregated Descriptors)**|residual vector를 기반으로 보다 풍부한 통계 표현|
|**Fisher Vector**|GMM 기반으로 확률적 soft assignment 및 고차 통계량 반영|

---

## 🔹 옵시디언 분류 추천

이 내용은 전형적인 **로컬 피처의 벡터화 기법**이므로 다음이 적절:

- MILAB/Computer Vision/Feature Engineering/Feature Encoding
    

---

## ✅ 요약

|항목|내용|
|---|---|
|핵심 개념|로컬 피처를 클러스터링하고 각 단어의 등장 빈도를 벡터화|
|입력|이미지에서 추출한 로컬 descriptor (e.g., SIFT)|
|출력|고정 길이 벡터 (visual word histogram)|
|주요 용도|이미지 분류, 검색, 전통적인 파이프라인에서 입력 벡터 생성|

---
