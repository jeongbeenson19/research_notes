
딥러닝에서 **Dropout**은 **과적합(overfitting)을 방지하기 위한 정규화 기법**입니다. 2014년 Hinton 등이 제안한 방법으로, 훈련 과정에서 **신경망의 일부 뉴런을 랜덤하게 비활성화(drop)** 하여 모델이 특정 뉴런에 과도하게 의존하지 않도록 합니다.

---

### 🔍 핵심 개념

- 훈련 시 매 미니배치마다 **무작위로 뉴런을 제거(0으로 설정)** 합니다.
    
- 제거 비율은 보통 0.2~0.5 정도로 설정하며, 이는 `dropout rate`라고 합니다.
    
- 테스트(추론) 시에는 **모든 뉴런을 사용**하지만, 훈련 시 드롭한 비율만큼 **출력값을 스케일링(scale)** 합니다 (예: `keep_prob = 0.5`이면 출력값에 0.5를 곱해 평균값을 맞춤).
    

---

### 💡 왜 효과적인가?

- Dropout은 **앙상블 학습처럼 작용**합니다. 훈련 과정에서 매번 다른 작은 신경망(sub-network)을 학습시키는 효과가 생기기 때문에, 다양한 모델이 학습되는 것과 비슷한 결과를 얻습니다.
    
- 따라서 특정 뉴런이나 경로에 의존하는 것을 방지하여 **일반화 성능이 향상**됩니다.
    

---

### 📘 예시 (TensorFlow/Keras 코드)

```python
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential

model = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(10, activation='softmax')
])
```

---

### 🧠 시각적 이해

훈련 시

```
Layer: [O O O O O]  →  Dropout(0.4) →  [O X O X O]
```

테스트 시

```
Layer: [O O O O O] (모두 사용)  
→ 출력에 dropout 비율을 곱하여 보정
```

---

### 📌 주의할 점

- Dropout은 **훈련 시에만 적용**해야 합니다.
    
- RNN이나 LSTM 같은 구조에서는 Dropout을 신중하게 적용해야 하며, 보통 **입력과 은닉 상태에 각각 별도로 적용**합니다.
    
- 최근에는 Batch Normalization과 함께 사용하거나, 다른 정규화 기법과 비교하여 선택적으로 사용됩니다.
    

---

### 참고 논문
[[Dropout; A Simple Way to Prevent Neural Networks from Overfitting]]
