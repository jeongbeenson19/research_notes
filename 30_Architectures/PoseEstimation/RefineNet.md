
# 🔁 2. RefineNet: Hard Keypoint Refinement

### ✅ 목적

> GlobalNet에서 coarse하게 예측한 히트맵을 기반으로, **정확한 위치 예측이 어려운 keypoints**를 **선택적으로 정교화**하는 모듈

---

## 🧱 구조

### 📌 입력 구성

- GlobalNet의 output feature map + intermediate features
    

### 📌 구성 요소

- **Residual Block** × 4 (shallow CNN)
    
- 각 residual block은 256 채널을 유지
    
- 마지막에는 **deconv + conv** 조합으로 heatmap 출력
    

```text
[GlobalNet output] 
    ↓
[Residual Block × 4]
    ↓
[Upsample + 1x1 Conv]
    ↓
[Refined heatmap output]
```

- 이 결과는 GlobalNet보다 더 정교한 keypoint 위치를 제공함
    

---

### 📌 학습 전략: **OHKM (Online Hard Keypoints Mining)**

- GlobalNet은 모든 keypoints에 대해 일반적인 MSE Loss 적용
    
- RefineNet은:
    
    1. keypoint별 loss 계산
        
    2. loss가 큰 top-K (ex: 8개) keypoints만 선택
        
    3. 이 keypoint에 대해서만 loss backpropagation
        

```text
예: 17개의 keypoint 중
→ 손목, 발목, 코 등 MSE가 큰 8개 선택
→ 선택된 keypoint만 gradient 계산
```

---

### 📌 장점 및 효과

|항목|설명|
|---|---|
|selective learning|쉬운 keypoint는 학습 제외 → 효과적 학습|
|성능 향상|어려운 부위(손목, 발끝 등) 정확도 크게 개선|
|연산량|비교적 적음 (shallow block 구조)|

---
