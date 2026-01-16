
Object tracking은 **비디오 프레임 시퀀스 내에서 특정 객체의 위치를 시간에 따라 추적**하는 컴퓨터 비전 기술입니다. 다음과 같이 핵심 구성 요소, 분류, 대표 알고리즘, 평가 지표 등의 구조로 상세히 설명하겠습니다.

---

## 📌 1. 정의

Object Tracking은 비디오의 **연속적인 프레임에서 객체의 경로(trajectory)를 추정**하는 문제입니다.  
보통 **객체 감지(Object Detection)** 와 함께 수행되며, 첫 프레임에서 객체가 감지된 후 그 위치를 지속적으로 추적합니다.

---

## 📌 2. 주요 과제

1. **Occlusion** (가림): 객체가 다른 객체에 의해 가려지는 경우
    
2. **Appearance Change**: 조명, 각도, 자세 변화 등
    
3. **Scale Variation**: 객체 크기가 시간에 따라 변함
    
4. **Fast Motion / Blur**: 빠르게 움직일 때 추적 어려움
    
5. **Multiple Object Tracking (MOT)**: 여러 객체 추적 시 ID 관리 문제 발생
    

---

## 📌 3. Tracking 분류

### 🔹 1) Tracking-by-Detection (TBD)

- 프레임마다 object detection 수행 후, 각 detection을 연결
    
- 대부분의 **현대 MOT 시스템**에서 사용
    
- 예시: [SORT](https://arxiv.org/abs/1602.00763), [DeepSORT](https://arxiv.org/abs/1703.07402), [ByteTrack](https://arxiv.org/abs/2110.06864)
    

### 🔹 2) Online vs Offline

|구분|설명|
|---|---|
|Online|현재 프레임과 이전 정보만 사용|
|Offline|전체 비디오를 활용해 후처리 가능 (더 정확하지만 지연 존재)|

### 🔹 3) Single Object vs Multi Object

- 단일 객체(SOT) 추적 vs 여러 객체(MOT) 동시 추적
    

---

## 📌 4. Tracking-by-Detection 방식 구조

```text
[영상 프레임 입력]  
     ↓  
[Object Detector (YOLO, Faster R-CNN 등)]  
     ↓  
[Detection 결과 (bounding box + score)]  
     ↓  
[Tracking 알고리즘 (Kalman Filter + Hungarian 등)]  
     ↓  
[Object ID 할당 및 프레임 간 연결]
```

---

## 📌 5. 대표 알고리즘

|이름|설명|
|---|---|
|**SORT**|Kalman Filter + Hungarian algorithm으로 bounding box association|
|**DeepSORT**|SORT에 appearance feature embedding 추가 → 유사도 기반 매칭 강화|
|**ByteTrack**|낮은 confidence detection도 고려해 recall 상승|
|**FairMOT**|detection과 re-ID를 한 네트워크에서 수행 (joint learning)|
|**TrackFormer, TransTrack**|Transformer 기반 tracker → attention으로 association 수행|

---

## 📌 6. 핵심 구성 요소

### 🔸 1) Motion Model

- Kalman Filter, Particle Filter 등으로 객체 이동 예측
    

### 🔸 2) Appearance Model

- CNN 기반 특징 추출로 유사도 비교
    
- re-identification (re-ID) 모델이 여기에 해당
    

### 🔸 3) Data Association

- 이전 프레임의 track과 현재 프레임의 detection을 연결
    
- IoU, cosine similarity, Hungarian algorithm 등 사용
    

---

## 📌 7. 평가 지표 (주로 MOT benchmark 사용)

|지표|설명|
|---|---|
|**MOTA** (Multiple Object Tracking Accuracy)|FP, FN, IDSW 고려한 전체 정확도|
|**IDF1**|ID가 일치하는 프레임 비율 (정확한 ID 유지 여부)|
|**MT / ML**|Mostly Tracked / Mostly Lost 트랙 비율|
|**FP / FN / IDSW**|False Positive / False Negative / ID Switch 수|

---

## 📌 8. 적용 분야

- 자율주행 자동차 (보행자/차량 추적)
    
- 스포츠 분석 (선수 추적)
    
- 영상 감시 (사람/행동 감지)
    
- 증강현실 (AR 객체 추적)
    
- 로봇 내비게이션 등
    

---

## 📌 9. 관련 기술과 연계

- **Detection** (YOLO, [[Faster R-CNN]] 등)
    
- **Re-ID** (특징 임베딩 기반 식별)
    
- **Optical Flow** (Dense Tracking 방식)
    
- **Multi-camera tracking** (다중 시점 통합)
    

---

## 🗂️ 옵시디언 분류 제안

`/MILAB/Computer Vision/Networks/Object Tracking`  
또는  
`/MILAB/Computer Vision/Feature Engineering/Tracking`

---

원하는 항목이 있다면 (예: DeepSORT 구조도, ByteTrack 수식 등) 더 자세히 설명해드릴 수 있습니다.