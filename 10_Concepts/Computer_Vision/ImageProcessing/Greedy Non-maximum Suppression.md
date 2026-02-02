
**Greedy Non-Maximum Suppression (NMS)**  는 **객체 탐지(Object Detection)** 에서 **중복된 바운딩 박스(Bounding Box)를 제거**하는 후처리 알고리즘입니다.

주요 목적은 **같은 객체를 여러 박스가 검출하는 것을 하나로 정리**하는 것입니다.

---

## ✅ **핵심 아이디어**

1. **탐지된 모든 바운딩 박스**를 **Confidence Score(신뢰도 점수)** 기준으로 정렬
    
2. 가장 높은 점수를 가진 박스를 선택(이 박스는 최종 결과로 채택)
    
3. 선택된 박스와 **[[IoU|IoU(Intersection over Union)]]** 가 일정 임계값($\text{threshold}$) 이상 겹치는 나머지 박스들은 **중복된 것으로 간주하고 제거**
    
4. 남은 박스에 대해 2~3 과정을 반복
    

"Greedy"라는 이름은 이 알고리즘이 **항상 현재 가장 높은 점수의 박스를 먼저 선택하는 탐욕적(Greedy) 전략**을 사용하기 때문입니다.

---

## ✅ **구체적인 연산 과정**

### 1. **입력**

- 바운딩 박스 집합: $[B_1, B_2, ..., B_n]$
    
- 각 박스의 **Confidence Score**: $[S_1, S_2, ..., S_n]$
    
- **IoU 임계값:** $t$ (예: 0.3 ~ 0.5)
    

### 2. **알고리즘 단계**

```
1) 박스들을 Confidence Score 기준으로 내림차순 정렬
2) 최종 선택 박스 집합 selected = []

3) while 박스가 남아있을 때:
    a) 가장 높은 점수를 가진 박스 M 선택 → selected에 추가
    b) 남은 박스 중에서 M과 IoU > t 인 박스 제거
4) selected 반환
```

---

## ✅ **수식 (IoU 계산)**

두 박스 $A$와 $B$의 $IoU$:

$\text{IoU}(A, B) = \frac{\text{Area}(A \cap B)}{\text{Area}(A \cup B)}$

---

## ✅ **특징**

### ✔ 장점

- 구현이 간단하고 빠름 (O(n log n))
    
- YOLO, Faster R-CNN 등 대부분의 객체 탐지 모델에서 표준적으로 사용
    

### ✘ 단점

- **Greedy**하게 동작 → **높은 점수를 가진 박스가 잘못 선택되면, 이후 박스들도 제거될 위험**
    
- 객체가 겹쳐 있는 경우(특히 군집된 객체) → 여러 객체를 하나로 잘못 묶을 수 있음  
    → 이런 한계를 개선하기 위해 **Soft-NMS** 등이 제안됨
    

---

### ✅ **Selective Search 이후 NMS의 역할**

Selective Search가 **후보 영역(Region Proposals)** 을 수천 개 생성하면, CNN이 각 후보를 분류 후, 겹치는 박스를 NMS로 정리합니다.

---
