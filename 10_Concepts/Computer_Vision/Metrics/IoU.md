
**Intersection over Union (IoU)** 는 **두 개의 바운딩 박스가 얼마나 겹치는지를 수치적으로 표현한 지표**입니다. 객체 탐지에서 **정답 박스(Ground Truth)** 와 **예측 박스(Predicted Box)** 의 일치 정도를 측정하거나, **Non-Maximum Suppression(NMS)** 에서 **중복 제거 기준**으로 사용됩니다.

---

## ✅ 정의

두 바운딩 박스 $A$와 $B$에 대해, IoU는 다음과 같이 정의됩니다:

$$
\text{IoU}(A, B) = \frac{\text{면적}(A \cap B)}{\text{면적}(A \cup B)}
$$
- $A \cap B$: 두 박스의 **교집합 영역**
    
- $A \cup B$: 두 박스의 **합집합 영역**  
    → **겹친 정도 / 전체 차지한 면적**
    

---

## ✅ 수치적 해석

|IoU 값|의미|
|---|---|
|1.0|두 박스가 완전히 일치|
|0.5|절반 정도 겹침|
|0.0|전혀 겹치지 않음|
|≥ 0.5|보통 객체 탐지에서 "정탐(True Positive)"으로 간주하는 기준|

---

## ✅ 예시 (직관적 설명)

- 예측 박스가 정답 박스와 **완전히 겹치면** → IoU = 1.0
    
- 예측 박스가 **정답을 살짝 벗어나면** → IoU < 1
    
- 예측 박스가 **완전히 빗나가면** → IoU ≈ 0
    

---

## ✅ 시각적 예시 (ASCII)

```
[정답 박스]  
+---------+  
|         |  
|         |  
|         |  
+---------+

[예측 박스]  
    +---------+  
    |         |  
    |         |  
    |         |  
    +---------+

[교집합] = 겹친 영역  
[합집합] = 두 박스가 차지하는 전체 영역  
```

---

## ✅ 활용 예시

1. **객체 탐지 평가 지표**
    
    - mAP(mean Average Precision) 계산 시 IoU ≥ 0.5를 기준으로 TP/FP 판단
        
2. **NMS(Non-Maximum Suppression)**
    
    - IoU가 0.5 이상 겹치는 예측들은 **중복으로 간주하고 제거**
        

---

## ✅ 간단한 코드 예시 (PyTorch 스타일)

```python
def iou(box1, box2):
    # box = [x1, y1, x2, y2]
    xA = max(box1[0], box2[0])
    yA = max(box1[1], box2[1])
    xB = min(box1[2], box2[2])
    yB = min(box1[3], box2[3])

    inter_area = max(0, xB - xA) * max(0, yB - yA)
    
    box1_area = (box1[2]-box1[0]) * (box1[3]-box1[1])
    box2_area = (box2[2]-box2[0]) * (box2[3]-box2[1])

    union_area = box1_area + box2_area - inter_area

    return inter_area / union_area
```

---

### ✅ 정리

- **IoU = 겹친 영역 / 전체 영역**
    
- **0~1 사이의 값**으로, 높을수록 두 박스가 더 유사함
    
- **객체 탐지에서 성능 평가 및 NMS에 핵심적으로 사용**
    

---
