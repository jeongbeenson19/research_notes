
## 🧠 1. LeNet이란?

- **정식 명칭**: LeNet-5
    
- **제안자**: Yann LeCun 등 (1998년 논문)
    
- **목적**: 손글씨 숫자(MNIST) 인식
    
- **특징**:
    
    - CNN의 효시라 불림
        
    - 합성곱 계층과 풀링 계층의 반복
        
    - 마지막에 Fully Connected Layer로 분류 수행
        

> 📄 논문: _“Gradient-Based Learning Applied to Document Recognition”_, Proceedings of the IEEE, 1998.

---

## 📐 2. LeNet-5 구조 요약

|계층|타입|입력 크기|필터/유닛 수|필터 크기|출력 크기|
|---|---|---|---|---|---|
|Input|이미지|32×32×1|-|-|32×32×1|
|C1|Conv|32×32×1|6|5×5|28×28×6|
|S2|Avg Pool|28×28×6|-|2×2|14×14×6|
|C3|Conv|14×14×6|16|5×5|10×10×16|
|S4|Avg Pool|10×10×16|-|2×2|5×5×16|
|C5|Conv (FC처럼 동작)|5×5×16|120|5×5|1×1×120|
|F6|Fully Connected|-|84|-|84|
|Output|FC + Softmax|-|10|-|10|

---

## 🔍 3. 각 계층의 상세 설명

### 🟦 **C1: Convolution Layer**

- 입력: 32×32 흑백 이미지
    
- 6개의 5×5 필터 사용 → 6개의 feature map 생성
    
- 출력 크기: 28×28×6 (padding 없음, stride=1)
    
- Activation Function: **tanh** (당시에는 ReLU보다 tanh나 sigmoid가 일반적)
    

---

### 🟩 **S2: Subsampling (Average Pooling)**

- 2×2 영역에서 평균값을 취해 다운샘플링 (stride=2)
    
- 출력 크기: 14×14×6
    
- 학습 가능한 스케일링 파라미터와 바이어스 포함
    
- Activation: tanh
    

---

### 🟨 **C3: Convolution Layer**

- 16개의 feature map 생성, 5×5 필터 사용
    
- **이전의 6개 feature map 중 일부만 연결**됨 (Partial connection)
    
- 이유: 연산량 감소, 공간적 다양성 확보
    
- 출력: 10×10×16
    

> 📌 이 부분은 LeNet 논문의 독특한 설계. 일부 filter는 몇 개의 채널과만 연결되어 있음 (e.g., filter #1은 input map #0, #1만 사용)

---

### 🟧 **S4: Subsampling**

- 2×2 average pooling → 5×5×16
    

---

### 🟥 **C5: Convolution**

- 입력: 5×5×16 → 120개의 뉴런 생성
    
- 사실상 **Fully Connected Layer**처럼 작동함
    
- 이유: 입력 크기와 필터 크기가 동일해서 전체 연결됨
    

---

### 🟪 **F6: Fully Connected Layer**

- 120개의 뉴런을 84개의 뉴런으로 연결
    
- Activation: tanh
    

---

### 🎯 **Output Layer**

- 84개 → 10개의 클래스(score)로 연결
    
- Softmax 함수를 통해 확률 출력
    

---

## 📈 4. 학습 방식

- 손실 함수: Cross-Entropy
    
- 최적화: SGD 또는 Momentum 기반 Gradient Descent
    
- 역전파 (Backpropagation)로 모든 층의 가중치 학습
    

---

## 🧩 5. LeNet의 의의 및 한계

### ✅ 장점

- CNN 구조의 초석을 다짐
    
- 지역 수용 영역, weight sharing, pooling 등 **CNN의 기본 개념 정립**
    
- 오늘날 거의 모든 CNN 구조에 영향을 줌
    

### ❌ 한계

- 작은 모델 (당시 하드웨어 한계)
    
- 고해상도 이미지나 복잡한 데이터에는 부적합
    
- GPU 최적화가 미흡했던 시대의 설계
    

---

## 🔬 6. LeNet의 현대적 재현 (PyTorch 예시)

```python
import torch.nn as nn

class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        self.conv_block = nn.Sequential(
            nn.Conv2d(1, 6, kernel_size=5),  # C1
            nn.Tanh(),
            nn.AvgPool2d(kernel_size=2),    # S2
            nn.Conv2d(6, 16, kernel_size=5),# C3
            nn.Tanh(),
            nn.AvgPool2d(kernel_size=2),    # S4
            nn.Conv2d(16, 120, kernel_size=5), # C5
            nn.Tanh()
        )
        self.fc = nn.Sequential(
            nn.Linear(120, 84),             # F6
            nn.Tanh(),
            nn.Linear(84, 10)               # Output
        )

    def forward(self, x):
        x = self.conv_block(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)
```

---

## 📚 참고 문헌 및 자료

- 논문: [Gradient-Based Learning Applied to Document Recognition (1998)](http://yann.lecun.com/exdb/lenet/)
    
- Yann LeCun의 웹사이트: [http://yann.lecun.com/](http://yann.lecun.com/)
    
- PyTorch 구현: `torchvision.models` → `LeNet` 구조는 기본 제공 X, 직접 구현해야 함
    
