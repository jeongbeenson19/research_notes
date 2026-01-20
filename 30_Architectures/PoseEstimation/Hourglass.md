
## 🧠 1. Hourglass Network란?

### 📌 기본 아이디어

> 입력 이미지를 점차 downsampling하여 **전역 문맥(global context)** 을 추출한 후, 다시 upsampling하며 **고해상도 특징(local detail)** 을 복원하는 **대칭형 encoder-decoder 구조**.

### 📌 구조적 핵심

- CNN 다운샘플링 (maxpool, conv)
    
- CNN 업샘플링 (nearest upsample, conv)
    
- skip connection으로 down path의 feature를 up path에 전달
    
- 출력: 관절 히트맵 (heatmap)
    

### 예시 구조

```
Input
 ↓
[Downsampling Path]
 ↓
[Bottleneck Layer]
 ↑
[Upsampling Path]
 ↑
Output Heatmap
```

---

## 🔁 2. Stacked Hourglass Network란?

### 📌 개념

> 여러 개의 hourglass 모듈을 **연속(stacked)** 으로 연결하여, 반복적으로 피드백을 받아 **예측을 점점 정교화하는 구조**.

- 예측 결과를 intermediate로 출력하고,
    
- 다음 hourglass block에 다시 피처와 함께 입력
    
- 각 블록마다 loss를 걸어 학습
    

---

## 🔬 구조적 차이

|항목|Hourglass|Stacked Hourglass|
|---|---|---|
|정의|1개의 hourglass module|여러 개를 순차적으로 연결|
|학습 흐름|단일 feedforward|반복적인 refinement|
|출력 방식|최종 output 1회|각 stage마다 intermediate output|
|목적|단일 pass로 예측|반복 refinement로 점진적 개선|
|성능|기준 성능|더 높지만 복잡도 증가|

---

## 🧱 Stacked 구조 예시 (2-stack 기준)

```
Input
 ↓
[Hourglass 1]
 ↓
[Intermediate Heatmap 1]
 ↓ (Residual 연결)
[Hourglass 2]
 ↓
[Final Heatmap Output]
```

- 중간 히트맵은 supervision에 사용 (MSE loss)
    
- 이후 블록이 이전 블록의 예측을 다시 참조함 → **Refinement**
    

---

## 🎯 왜 stacking하는가?

|이유|설명|
|---|---|
|반복적 정제|coarse → fine 추정|
|더 깊은 학습|여러 loss로 gradient 흐름 분산|
|학습 안정성|deep supervision 적용 가능|
|성능 향상|COCO 기준 AP 상승|

---

## 📌 정리 문장

> **Hourglass**는 대칭적 encoder-decoder 구조를 통해 multi-scale feature를 추출하는 기본 모듈이며,  
> **Stacked Hourglass**는 이를 여러 번 반복하여, 중간 예측 결과를 기반으로 반복적으로 keypoint 위치를 정제하는 구조이다.

---

## 📁 옵시디언 분류 제안

- `Computer Vision > Networks > Hourglass`
    
- 또는 `Research > Theory > Multi-stage Refinement` (신규 생성 가능)
    
