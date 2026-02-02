
## 🧠 개요: GoogLeNet이란?

|항목|내용|
|---|---|
|이름|GoogLeNet (Inception v1)|
|제안자|Szegedy et al., Google|
|발표|2014 ILSVRC (1위, Top-5 error: 6.67%)|
|논문|["Going deeper with convolutions"](https://arxiv.org/abs/1409.4842)|
|핵심 개념|**Inception module**을 활용한 효율적이고 깊은 네트워크 구조|

---

## 🔍 배경: 왜 Inception 구조가 필요한가?

- 깊은 CNN은 일반적으로 성능이 좋지만, 다음과 같은 문제가 존재:
    
    - 파라미터 수가 폭발적으로 증가
        
    - Overfitting 위험
        
    - 연산량 증가 (특히 Fully Connected Layer)
        

→ GoogLeNet은 **“같은 성능을 더 적은 연산량과 파라미터로 구현”** 하는 것을 목표로 등장

---

## 🧱 Inception Module: 핵심 구성 요소

### ✅ 아이디어:

- 하나의 convolution layer 대신, **여러 크기의 필터 (1×1, 3×3, 5×5)** 를 병렬적으로 적용
    
- Max Pooling도 병렬적으로 처리
    
- 결과 feature map들을 **depth 방향(concatenation)** 으로 합침
    

### ✅ 구성:

- 1×1 Conv → 채널 축소 및 연산량 감소
    
- 3×3 Conv (with 1×1 conv before it)
    
- 5×5 Conv (with 1×1 conv before it)
    
- 3×3 Max Pooling (with 1×1 conv after it)
    

### 🎯 핵심: 다양한 **receptive field**를 동시에 고려

---

## 🔢 GoogLeNet 전체 구조 요약

- 전체 네트워크는 총 **22개 계층 (conv/FC 기준)** 으로 구성
    
- 총 **9개의 Inception module**
    
- **Auxiliary Classifier**: 학습을 돕기 위한 보조 분류기 두 개 삽입
    

```
입력 (224×224×3)
↓
Conv + MaxPool
↓
Conv + MaxPool
↓
Inception (3a, 3b)
↓
MaxPool
↓
Inception (4a ~ 4e) ← Auxiliary Classifier 1, 2
↓
MaxPool
↓
Inception (5a, 5b)
↓
Average Pooling
↓
Dropout (40%)
↓
Fully Connected (1000 classes)
↓
Softmax
```

---

## 🧮 연산량 감소의 비결: 1×1 Convolution

- $1 \times 1$ convolution은 단순한 연산이 아니라:
    
    - 채널 차원 축소 역할 (Dimensionality Reduction)
        
    - 비선형성 추가 (ReLU 사용)
        
    - 계산량을 대폭 줄이는 핵심 요소
        

> 예시: 256채널 → $1\times1$ conv → 64채널 → 3×3 conv  
> → 연산량: $64 \times 3 \times 3$ vs $256 \times 3 \times 3$ → **약 75% 절감**

---

## 🧪 Auxiliary Classifier (보조 분류기)

- 깊은 네트워크에서 **gradient vanishing 문제** 방지
    
- Inception 4a, 4d 뒤에 붙여서 **보조 손실(loss)** 을 계산
    
- 학습 중에만 사용, 추론 시에는 제거 가능
    

---

## ✅ GoogLeNet의 성능과 영향

|항목|설명|
|---|---|
|파라미터 수|약 6.8M (AlexNet보다 훨씬 적음, ~60M)|
|연산량|효율적 구조로 연산량도 절감|
|성능|ILSVRC 2014 우승 (Top-5 error 6.67%)|
|영향력|이후 Inception v2, v3, v4, Inception-ResNet 등 발전으로 이어짐|

---

## 📘 학문적 의의

- CNN 구조 설계에 있어 단순히 “layer를 깊게” 쌓는 것보다, **병렬 구조, receptive field 다변화, 파라미터 효율성** 등을 고려한 아키텍처 설계의 필요성을 강조
    
- Inception 구조는 **ResNet, EfficientNet, NASNet** 등의 발전에 영향을 줌
    

---

## 🧩 요약 정리 (1문장)

> GoogLeNet은 **Inception module**을 통해 다양한 스케일의 특징을 동시에 추출하고, **1×1 convolution과 auxiliary classifier**를 활용해 **효율적이고 깊은 CNN을 구현한 대표적인 구조**입니다.

---

필요하시면 GoogLeNet의 PyTorch 구현 예제나 Inception module만 따로 설명드릴 수도 있습니다.