
좋아요! VLAD(Vector of Locally Aggregated Descriptors)와 Fisher Vector는 둘 다 **이미지나 비디오 등의 지역(local) 특징 벡터들을 하나의 고정된 벡터로 요약하는 대표적인 방법**입니다. 주로 이미지 검색, 분류, 영상 분석 등에서 사용되며, **SIFT, SURF** 같은 지역 특징을 압축해 표현하는 데 사용됩니다.

---

## 🔹 공통 배경

- 이미지나 비디오는 많은 **local feature**(예: SIFT)로 표현됨.
    
- 그러나 머신러닝 모델에 넣기 위해선 **고정된 크기의 벡터**가 필요함.
    
- 이를 위해 local feature들을 하나의 벡터로 "pooling"하는 것이 필요.
    
- **VLAD**와 **Fisher Vector**는 그런 pooling 방법 중 고급 기법임.
    

---

## 🔸 VLAD (Vector of Locally Aggregated Descriptors)

^1a6a27

### 개념

- **K-means**로 학습한 **K개의 시각적 단어(centroid)** 를 기준으로, 각 local descriptor가 속한 centroid와의 **차이(잔차)** 를 누적해서 벡터화.
    

### 절차 요약

1. SIFT 같은 local descriptor 추출.
    
2. K-means로 시각적 단어 집합 $(codebook, {c1,...,cK}\{c_1, ..., c_K\})$ 생성.
    
3. 각 descriptor $x_i$가 가장 가까운 centroid $c_k$에 할당됨.
    
4. 각 $c_k$에 대해, 할당된 모든 $x_i$에 대해 $kx_i - c_k$를 누적.
    
5. 이렇게 만들어진 K개의 잔차 벡터들을 이어붙이면 최종 벡터 완성.
    

### 수식적으로:
$$
\text{VLAD}_k = \sum_{x_i \in C_k} (x_i - c_k)
$$
- $C_k$: $x_i$들이 할당된 클러스터 $k$
    
- 전체 VLAD 벡터 차원: $K \times D$ (K: 클러스터 수, D: descriptor 차원)
    

### 특징

- 상대적으로 단순하고 빠름.
    
- descriptor들의 **1차 통계**만 사용.
    

---

## 🔸 Fisher Vector

^0450ff

### 개념

- local descriptor들이 특정 **확률 모델(Gaussian Mixture Model, GMM)** 에 따라 생성되었다고 가정하고, 모델의 파라미터에 대해 **gradient**를 계산함.
    
- 즉, local descriptor가 GMM 파라미터(평균, 분산 등)를 얼마나 변경시킬 수 있는지를 이용해 고차원 벡터 생성.
    

### 절차 요약

1. SIFT 등 local descriptor 추출.
    
2. GMM을 학습해 K개의 가우시안 클러스터 생성.
    
3. 각 descriptor가 각 가우시안에 속할 확률(soft assignment) 계산.
    
4. GMM의 파라미터(평균, 분산 등)에 대한 **score function (gradient)** 을 계산하여 Fisher Vector 생성.
    

### 수식적으로:

- 각 가우시안 $k$에 대해, 평균 $\mu_k$, 분산 $\sigma_k$에 대한 gradient를 사용.
    
- Fisher Vector의 차원: $2 \times K \times D$
    

### 특징

- VLAD보다 복잡하고 계산량 많지만, 더 풍부한 표현 가능.
    
- **1차 + 2차 통계량** 사용 → 성능 더 좋을 수 있음.
    

---

## 🔸 비교 요약

| 항목    | VLAD                      | Fisher Vector                                 |
| ----- | ------------------------- | --------------------------------------------- |
| 기본 모델 | K-means (hard assignment) | GMM (soft assignment)                         |
| 정보량   | 1차 통계 (mean difference)   | 1차 + 2차 통계 (mean, variance)                   |
| 계산 비용 | 상대적으로 적음                  | 상대적으로 높음                                      |
| 차원 수  | $K \times D$              | $2 \times K \times D$                         |
| 성능    | 꽤 좋음                      | 더 좋을 수 있음 (especially for fine-grained tasks) |

---

## 🔹 실제 사용 예시

- **VLAD**: 이미지 검색, mobile vision (효율성 중시).
    
- **Fisher Vector**: 이미지 분류, fine-grained classification (성능 중시).
    

---
