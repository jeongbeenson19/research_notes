
## 🧠 개요: VGGNet이란?

|항목|내용|
|---|---|
|이름|VGGNet (Visual Geometry Group Net)|
|제안자|Karen Simonyan & Andrew Zisserman (Oxford VGG 팀)|
|발표|2014 ILSVRC (2위)|
|논문|["Very Deep Convolutional Networks for Large-Scale Image Recognition"](https://arxiv.org/abs/1409.1556)|
|핵심 아이디어|**작은 필터 (3×3)**를 반복해서 깊은 네트워크 구성|

---

## 🧱 VGGNet의 핵심 설계 철학

### ✅ 작은 필터 반복 (3×3 conv)

- 기존의 AlexNet은 11×11, 5×5 등 큰 커널 사용
    
- VGG는 **모든 convolution을 3×3**으로 통일
    
- 두 개의 3×3 conv는 하나의 5×5과 동일한 receptive field를 가지면서 **비선형성과 학습 가능성 증가**
    

> 예시:
> 
> 3×3 Conv+3×3 Conv→5×5 receptive field\text{3×3 Conv} + \text{3×3 Conv} → \text{5×5 receptive field} 3×3 Conv×3→7×7 receptive field\text{3×3 Conv} \times 3 → \text{7×7 receptive field}

### ✅ 깊은 구조 (16~19층)

- 네트워크 깊이를 16 (VGG16), 19 (VGG19)까지 확장
    
- 단순히 layer 수를 늘렸을 뿐인데도 **성능 대폭 향상**
    
- Fully connected layer는 3개로 고정 (4096 → 4096 → 1000)
    

---

## 🔢 VGG16 구조 요약

|Stage|구성|출력 크기|
|---|---|---|
|Input|RGB 이미지|224×224×3|
|Conv1|3×3 conv ×2 + maxpool|112×112×64|
|Conv2|3×3 conv ×2 + maxpool|56×56×128|
|Conv3|3×3 conv ×3 + maxpool|28×28×256|
|Conv4|3×3 conv ×3 + maxpool|14×14×512|
|Conv5|3×3 conv ×3 + maxpool|7×7×512|
|FC|FC 4096 → FC 4096 → FC 1000|-|
|Output|Softmax|1000|

---

## 📐 구조적 특징과 수학적 관점

### 1. 동일 패딩 (same padding):

- 모든 conv는 padding=1, stride=1로 설정
    
- 출력 크기를 입력과 동일하게 유지
    

### 2. 파라미터 수 폭발:

- Conv layer는 비교적 파라미터가 적지만,
    
- FC layer에서는 매우 많은 파라미터 사용
    
    - e.g., FC1의 입력은 7×7×512 = 25088 → 4096 → 약 1억 개 이상
        

---

## 🧪 성능 및 한계

|항목|내용|
|---|---|
|ILSVRC 2014|2위 (GoogLeNet 1위), Top-5 error 약 7.3%|
|장점|구조 단순함, 모듈화 쉬움, 강력한 feature extractor|
|단점|파라미터 수 많고 메모리/속도 비효율적, FC layer 부담 큼|
|활용|Transfer Learning, Feature Extraction, Fine-tuning에서 광범위하게 사용|

---

## 🎯 학문적 의의

- **구조의 단순화가 학습과 활용에 유리**하다는 실증
    
- 이후 **ResNet, DenseNet** 등으로 이어지는 **"더 깊은 네트워크는 더 나은 표현력을 가진다"**는 철학의 출발점
    
- **모듈화된 CNN 설계**의 대표 예시 (Conv block의 반복 구성)
    

---

## 📘 키워드 요약

|키워드|설명|
|---|---|
|3×3 convolution|CNN depth 증가와 파라미터 효율성의 핵심|
|Depth 증가|8층 → 16층 → 성능 향상|
|FC layer|전체 파라미터의 대부분을 차지|
|Transfer learning|사전학습 모델로써 가장 많이 활용됨 (특히 VGG16)|

---

## 🔍 요약 한 문장

> **VGGNet은 구조적 단순성(3×3 conv 반복)을 통해 깊은 네트워크의 강력한 표현력을 증명한 모델로, CNN의 표준적인 설계 패턴을 제시한 고전적인 아키텍처입니다.**

---

필요하다면 VGGNet의 PyTorch 코드 예시, VGG vs ResNet 비교표, 또는 transfer learning 응용도 도와드릴 수 있습니다.