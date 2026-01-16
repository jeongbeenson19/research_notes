
#ComputerVision #FeatureEngineering #FeatureRepresentation

---

# **Part Affinity Fields (PAFs)**

  

## **정의**

- PAFs는 **관절 쌍(limb)을 연결하는 벡터 필드**
    
- 각 픽셀마다 “특정 limb 위에 있는가, 그리고 연결 방향은 무엇인가”를 나타냄
    
- 관절이 **어떤 사람에 속하는지 구분**할 수 있게 하는 핵심 요소
    

---

## **필요성**

- Bottom-up 방식: 모든 keypoint를 검출한 뒤, 사람별 skeleton으로 묶어야 함
    
- Heatmap만으로는 **사람 구분 불가능** (옆에 서 있는 사람의 keypoints가 섞일 수 있음)
    
- PAFs는 관절 간의 **방향·위치 일관성**을 제공하여 사람별 grouping 문제 해결
    

---

## **수학적 정의**

- limb $c$ (예: 어깨–팔꿈치)에 대해, 두 관절 좌표 $x_a, x_b$ 존재
    
- 단위 벡터:
    
    $$
    
    v = \frac{x_b - x_a}{\lVert x_b - x_a \rVert}
    
    $$
    
- limb 구간 위 픽셀 $p$:
    
    $$
    
    PAF_c(p) = v
    
    $$
    
- limb와 무관한 픽셀:
    
    $$
    
    PAF_c(p) = 0
    
    $$
    

---

## **네트워크 출력**

- OpenPose는 두 가지 맵을 예측
    
    1. **Part Confidence Map**: 관절 위치 heatmap
        
    2. **Part Affinity Field**: limb 방향 벡터장
        
    

---

## **직관적 예시**

- 두 사람이 동시에 존재할 때
    
    - “머리 → 목” PAF는 각 사람의 머리와 목을 연결하는 방향 벡터장을 형성
        
    - 여러 “머리” keypoint가 있을 때, PAF 방향·크기 일관성으로 올바른 “목”과 연결
        
    

---

## **장점**

- 복잡한 다인 장면에서도 사람별 skeleton 추출 가능
    
- Top-down 방식 대비 **강건성**과 **실시간성** 확보
    
- Multi-person pose estimation을 실시간(20fps 이상)으로 수행 가능
    

---

## **요약**

  

**PAFs = 관절을 올바르게 연결하기 위한 방향 정보 벡터장**

→ OpenPose가 Bottom-up 방식에서 여러 사람을 구분할 수 있게 만든 핵심 기술