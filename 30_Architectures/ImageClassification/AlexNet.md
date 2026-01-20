
## 🧠 1. AlexNet이란?

- **정식 명칭**: AlexNet
    
- **제안자**: Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton
    
- **발표 시기**: 2012년
    
- **논문 제목**: [[ImageNet classification with deep convolutional neural networks]]
    
- **대회 수상**: ILSVRC 2012 1위 (Top-5 error: 15.3%, 2등은 26.2%)
    

---

## 🎯 2. 주요 기여 및 혁신

|항목|설명|
|---|---|
|GPU 사용|당시 GPU 2개(NVIDIA GTX 580)로 병렬 학습을 수행하여 큰 모델을 훈련 가능하게 함|
|ReLU 도입|sigmoid/tanh 대신 **ReLU** 활성화 함수 도입 → 학습 속도 향상|
|Dropout|Fully Connected Layer에서 **과적합 방지**를 위해 Dropout 사용|
|Data Augmentation|훈련 데이터를 확대하기 위해 랜덤 크롭, 좌우 반전 등을 활용|
|Local Response Normalization (LRN)|ReLU 사용 후 local competition 효과를 위한 정규화 기법 도입 (지금은 거의 사용되지 않음)|

---

## 📐 3. AlexNet 구조

AlexNet은 총 **8개의 학습 계층**으로 구성되어 있습니다:

- **5개의 Convolution Layer**
    
- **3개의 Fully Connected Layer**
    
- 마지막 출력은 Softmax
    

### 📊 Input

- 이미지 크기: **224×224×3**  
    → 원래는 227×227×3이었으나, 구현 시 대부분 224×224로 통일
    
- RGB 이미지 (3채널)
    

---

### 🔢 각 계층 요약

|계층|타입|필터 크기|필터 수|Stride|Padding|출력 크기|
|---|---|---|---|---|---|---|
|Conv1|Convolution|11×11|96|4|0|55×55×96|
|LRN + MaxPool1|정규화 + 풀링|3×3|-|2|-|27×27×96|
|Conv2|Convolution|5×5|256|1|2|27×27×256|
|LRN + MaxPool2|정규화 + 풀링|3×3|-|2|-|13×13×256|
|Conv3|Convolution|3×3|384|1|1|13×13×384|
|Conv4|Convolution|3×3|384|1|1|13×13×384|
|Conv5|Convolution|3×3|256|1|1|13×13×256|
|MaxPool3|Max Pooling|3×3|-|2|-|6×6×256|
|FC6|Fully Connected|-|4096|-|-|4096|
|FC7|Fully Connected|-|4096|-|-|4096|
|FC8|Fully Connected|-|1000|-|-|1000 (softmax)|

---

## 🔍 4. 주요 레이어 설명

### 🟦 Conv1

- 필터 크기 11×11, stride 4 → 빠르게 공간 차원 축소
    
- GPU 2개를 사용해 48개씩 나눠 병렬 처리
    

---

### 🟩 LRN + Pooling

- LRN (Local Response Normalization): 인접 뉴런끼리 정규화 → ReLU 출력을 안정화시키려는 목적
    
- 지금은 LRN은 거의 사용되지 않음 (BatchNorm이 대체)
    

---

### 🟨 FC6, FC7

- 각 노드 수: 4096
    
- **Dropout 사용 (p=0.5)** → 과적합 방지
    

---

### 🎯 FC8 + Softmax

- 최종 출력: 1000 클래스 (ImageNet의 클래스 수)
    

---

## 📈 5. AlexNet 성능

|항목|수치|
|---|---|
|Top-1 Error|약 37.5%|
|Top-5 Error|약 15.3%|
|파라미터 수|약 **6천만 개**|
|연산량|약 7.2억 FLOPs|
|학습 시간|당시 GPU 2개로 **5~6일 소요**|

---

## 💡 6. AlexNet 이후 영향

- 딥러닝 연구의 **대중화 촉진**
    
- 이후 등장한 VGG, GoogLeNet, ResNet 등에 **구조적 토대 제공**
    
- ReLU, Dropout, Data Augmentation 등은 이후 모델에서도 표준처럼 사용됨
    

---

## 🔬 7. PyTorch 예시 구현

```python
import torch.nn as nn

class AlexNet(nn.Module):
    def __init__(self, num_classes=1000):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 96, kernel_size=11, stride=4, padding=0),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            # LRN은 보통 생략
            nn.Conv2d(96, 256, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(256, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2)
        )
        self.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), 256 * 6 * 6)
        x = self.classifier(x)
        return x
```

---

## 📚 참고 자료

- 논문: [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)
    
- GitHub 구현: PyTorch 공식 모델 `torchvision.models.alexnet`
    

---
