
## 📊 Evaluation Metrics

딥러닝/머신러닝 모델의 성능을 평가하기 위한 주요 지표들을 정리한다. 각각의 지표는 문제 유형(이진 분류, 다중 클래스 분류, 객체 탐지 등)에 따라 해석이 다를 수 있다.

---

### ✅ 1. Accuracy (정확도)

- **정의**: 전체 샘플 중 올바르게 분류된 비율
    

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

- **사용처**: 클래스 간 **불균형이 크지 않은** 분류 문제
    
- **단점**: 불균형 데이터에서 **모든 샘플을 다수 클래스로 예측해도 높게 나올 수 있음**
    

---

### ✅ 2. Precision (정밀도)

^941fcf

- **정의**: 모델이 **Positive**로 예측한 것 중 실제로 **Positive**인 비율
    

$$\text{Precision} = \frac{TP}{TP + FP}$$

- **사용처**: False Positive를 **줄이는 게 중요한 상황**
    
    - 예: 스팸 메일 필터링 (정상 메일을 스팸으로 분류하면 큰 손해)
        

---

### ✅ 3. Recall (재현율, 민감도)

^1d4e7f

- **정의**: 실제 **Positive** 중에서 모델이 Positive로 잘 찾아낸 비율
    

$$\text{Recall} = \frac{TP}{TP + FN}$$

- **사용처**: False Negative를 **줄이는 게 중요한 상황**
    
    - 예: 암 진단 (환자를 놓치는 것은 치명적)
        

---

### ✅ 4. [[F1-Score]]

- **정의**: Precision과 Recall의 조화 평균 (Harmonic Mean)
    

$$\text{F1} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

- **사용처**: Precision과 Recall 간 균형이 중요할 때
    

---

### ✅ 5. [[Average Precision|Average Precision (AP)]]

- **정의**: Precision-Recall 곡선의 아래 면적
    

$$\text{AP} = \int_0^1 \text{Precision}(r) \, dr$$

- **객체 탐지 사용 예**:
    
    - `AP@0.5`: IoU ≥ 0.5 일 때 정답으로 간주
        
    - `AP@0.5:0.95`: IoU 0.5부터 0.95까지 0.05 간격으로 평균
        

---

### ✅ 6. mAP (mean Average Precision)

- **정의**: 클래스별 AP의 평균
    
- **사용처**: **다중 클래스 객체 탐지** 성능 비교
    

$$\text{mAP} = \frac{1}{N} \sum_{i=1}^{N} \text{AP}_i$$

---

### ✅ 7. Efficiency

- **정의**: 다양한 의미로 사용되나, 보통은 **정확도 대비 연산 자원 사용량**을 의미
    
- **예시 지표**:
    
    - **FLOPs**: 연산량
        
    - **FPS (Frame per Second)**: 1초에 처리 가능한 프레임 수
        
    - **Latency**: 응답 시간
        
- **사용처**: **실시간 처리, 경량화 모델 평가**, edge device 적용 시
    

---

### 📌 용어 정리 요약

| 지표         | 수식                                    | 중요 포인트               |
| ---------- | ------------------------------------- | -------------------- |
| Accuracy   | $$\frac{TP + TN}{TP + TN + FP + FN}$$ | 전체 정확도, 불균형 데이터에 민감함 |
| Precision  | $$\frac{TP}{TP + FP}$$                | 정답이라고 예측한 것의 정확성     |
| Recall     | $$\frac{TP}{TP + FN}$$                | 실제 정답을 얼마나 잘 찾았는가    |
| F1-Score   | $$2 \cdot \frac{P \cdot R}{P + R}$$   | P-R 균형 고려한 조화 평균     |
| AP         | PR 곡선 면적                              | 정밀도-재현율 관계의 종합적 요약   |
| mAP        | 클래스별 AP 평균                            | 다중 클래스에서 성능 요약       |
| Efficiency | (정의 다양)                               | 속도·연산량 관련 평가 지표      |

---
.