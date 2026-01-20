
## 🧠 개요: ResNet이란?

| 항목      | 내용                                                                                      |
| ------- | --------------------------------------------------------------------------------------- |
| 이름      | ResNet (Residual Network)                                                               |
| 제안자     | Kaiming He et al. (Microsoft Research)                                                  |
| 발표      | 2015, CVPR / ILSVRC 2015 우승                                                             |
| 논문      | [[Deep Residual Learning for Image Recognition]]                                        |
| 핵심 아이디어 | **Residual connection** (skip connection) 도입으로 gradient vanishing 문제 해결 및 깊은 네트워크 학습 가능 |

---

## ❓ 왜 ResNet이 필요한가?

### 문제점: 더 깊은 네트워크 = 더 좋은 성능? → ❌

- 일반적으로 CNN depth가 깊을수록 성능 향상이 기대됨
    
- 하지만 실제로는:
    
    - 깊은 네트워크가 **훈련 오류(training error)**조차 증가
        
    - 이는 **vanishing/exploding gradient**와 **표현력의 축소** 때문
        

> 깊게 쌓았는데 오히려 성능 하락  
> → 단순한 네트워크가 오히려 더 잘 학습됨

---

## 🧩 핵심 아이디어: **Residual Learning**

ResNet은 **입력 x와 출력 H(x)** 사이의 관계를 직접 학습하는 대신, **잔차(residual) F(x) = H(x) – x** 를 학습합니다.

### Residual Block 구조:

$$
\textbf{Output: } y = F(x) + x
$$

- 여기서:
    
    - $F(x)$: convolution, batch norm, ReLU 등을 포함한 일반적인 CNN 연산
        
    - $x$: shortcut (identity) connection을 통해 그대로 더해짐
        

### 장점:

- $F(x) = 0$일 경우 → **identity mapping**이 기본값이 됨
    
- 깊은 네트워크에서 학습이 **더 쉬워지고**, **성능이 안정화**
    

---

## 🧱 구조: ResNet의 구성 (예: ResNet-50)

|이름|구조|Block 수|
|---|---|---|
|ResNet-18/34|기본 residual block (2-layer)|18, 34 층|
|ResNet-50/101/152|**Bottleneck block (3-layer)** 사용|50, 101, 152 층|

### Bottleneck Block 구조 (ResNet-50~)

$$x \rightarrow 1\times1 \rightarrow 3\times3 \rightarrow 1\times1 \rightarrow +x
$$

- **1×1 convolution**을 통해 차원 축소 및 확장
    
- 계산량 줄이고 효율성 증가
    

---

## 📈 성능

|Model|Top-5 Error (ILSVRC)|
|---|---|
|ResNet-34|5.71%|
|ResNet-50|5.25%|
|ResNet-152|**4.49%** (당시 최고)|

---

## 🧪 수학적 직관

### Identity shortcut이 안정화를 돕는 이유:

- 역전파 시 gradient가 **직접 shortcut 경로로 흘러감**
    
- 즉, 블록 내부에서 gradient가 사라지더라도 $\frac{\partial L}{\partial x} = \frac{\partial L}{\partial y}$경로가 존재
    
- 이로 인해 **정보 흐름이 막히지 않음**
    

---

## 🔍 ResNet의 학문적 의의

|측면|설명|
|---|---|
|Optimization 관점|Gradient vanishing 문제 해결, 깊은 네트워크 학습 가능|
|구조적 단순성|기존 CNN 위에 residual block만 더해도 됨 (모듈화 용이)|
|Generalization|다양한 task (detection, segmentation 등)에 쉽게 확장 가능|
|후속 발전|ResNeXt, DenseNet, HRNet, Swin Transformer 등 여러 아키텍처에 영향을 줌|

---

## 📘 키워드 요약

|키워드|설명|
|---|---|
|Residual Block|입력을 그대로 더해 학습 안정성 확보|
|Skip Connection|정보 손실 없이 전달, gradient 흐름 강화|
|Bottleneck|1×1 conv로 연산 최적화|
|Ultra-deep|100+ 층의 네트워크를 실용적으로 만듦|

---

## ✅ 한 문장 요약

> **ResNet은 identity skip connection을 도입하여 gradient 소실 문제를 해결하고, 초깊은 신경망의 학습 가능성과 성능을 획기적으로 개선한 딥러닝 아키텍처의 전환점입니다.**

---
