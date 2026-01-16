
## 📘 FlowNet2s란?

> **FlowNet2s**는 **FlowNet2 (Ilg et al., 2017, CVPR)** 논문에서 제안된 optical flow 추정 네트워크 중 하나로,  
> **“FlowNet2-Simple”** 의 줄임말입니다.

- FlowNet2 계열은 전체적으로 **FlowNet(Simple, Corr)** 들을 쌓아서 구성되며,
    
- FlowNet2s는 그 중에서도 **가장 단순한 구조**를 갖는 variant입니다.
    

---

## ✅ 기본 정보 요약

|항목|내용|
|---|---|
|논문|**FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks**|
|([https://arxiv.org/abs/1612.01925](https://arxiv.org/abs/1612.01925))||
|구조|단일 FlowNet-S 네트워크 기반|
|특징|가장 단순하고 연산량이 적음 (Single-pass architecture)|
|목적|빠르고 경량화된 optical flow 추정|

---

## 🔍 구조 설명: FlowNet2s = FlowNet-S

### 🔧 입력

- 두 연속 프레임 $I_1, I_2$ (크기 $H \times W \times 3$)
    
- 입력은 두 프레임을 **concat하여 6채널 입력**으로 처리
    

$$x_{\text{input}} = \text{concat}(I_1, I_2) \in \mathbb{R}^{H \times W \times 6}$$

---

### 🧱 네트워크 아키텍처

- **Encoder-Decoder 구조**
    
- 주요 구성 요소:
    

|블록|설명|
|---|---|
|**Encoder**|여러 convolution 층을 거쳐 공간 해상도를 줄이고 추상적 feature 추출|
|**Decoder**|up-convolution (deconv) 계층을 통해 flow field 복원|
|**Skip connections**|중간 feature들을 decoder에 연결하여 세부 정보 보존|
|**Multi-scale prediction**|여러 해상도에서 flow를 예측하고, coarse-to-fine 방식으로 정제|

---

### 🎯 출력

- 최종 출력: **optical flow field**
    
    $$F_{1 \rightarrow 2} \in \mathbb{R}^{H \times W \times 2}$$
    
    각 픽셀의 $(u, v)$ 변위 벡터
    

---

## 🆚 FlowNet2 vs FlowNet2s

| 항목     | FlowNet2                                    | **FlowNet2s**       |
| ------ | ------------------------------------------- | ------------------- |
| 구조     | 여러 FlowNet-S + Warping + Refinement 네트워크 스택 | 단일 FlowNet-S        |
| 정확도    | 높음 (Sintel 기준 상위권)                          | 낮음 (Baseline 수준)    |
| 추론 속도  | 느림 (중간~고)                                   | **빠름 (실시간 가능)**     |
| 파라미터 수 | 크고 복잡함                                      | **작고 단순함**          |
| 사용 목적  | 정확도 우선                                      | **경량 모델, 추론 속도 우선** |

---

## 🧠 학습 정보

- 학습 데이터:
    
    - FlyingChairs (synthetic)
        
    - FlyingThings3D, Sintel, KITTI
        
- 손실 함수:
    
    - Endpoint Error (EPE):
        
        $$\text{EPE} = \frac{1}{N} \sum_{i=1}^{N} \| \hat{F}_i - F_i \|_2$$
- fine-tuning: 일반적으로 coarse → fine으로 transfer learning 적용
    

---

## 🛠️ 적용 예시

|응용 분야|사용 목적|
|---|---|
|Pose Tracking|이전 관절 위치 warp|
|Video Object Tracking|dense motion field 기반 ROI 이동|
|Motion Segmentation|배경과 객체의 motion 분리|
|Visual Odometry|프레임 간 카메라 이동량 추정|

---

## 📎 발표용 설명 문장 예시

> FlowNet2s는 FlowNet2 시리즈 중 가장 단순한 구조를 갖는 optical flow 추정 모델로,  
> 단일 FlowNet-S 아키텍처 기반이며, 두 프레임을 concat한 후 CNN을 통해 dense motion field를 예측합니다.  
> 정확도는 높지 않지만, 연산량이 적어 **실시간 pose propagation**이 필요한 작업에 적합합니다.

---

## 📁 옵시디언 카테고리 제안

```
/MILAB/Computer Vision/Networks/Foundational/FlowNet2s.md
```

또는 좀 더 응용 관점으로:

```
/MILAB/Computer Vision/Feature Engineering/Feature Extraction/Optical Flow/FlowNet2s.md
```

---

필요하시면 FlowNet2s의 논문 요약, 구조 다이어그램, PyTorch 코드 예시도 제공해 드릴 수 있습니다.