---
alias:
  - BroadTrack
type: paper
tags:
  - DeepLearning
  - Paper
  - ComputerVision
  - CameraTracking
  - Soccer
  - ViewShift
status: 🟧 Reading
rating: 0
date: 2026-02-03
title: "BroadTrack: Broadcast Camera Tracking for Soccer"
authors:
  - Floriane Magera
  - Thomas Hoyoux
  - Olivier Barnich
  - Marc Van Droogenbroeck
year: 2024
venue: arXiv
paper_url: https://arxiv.org/abs/2412.01721
topics:
  - Camera Tracking
  - Soccer Analytics
  - Broadcast Systems
  - Computer Vision
---

## **📄 BroadTrack: Broadcast Camera Tracking for Soccer 개요**

- **발표 논문**: BroadTrack: Broadcast Camera Tracking for Soccer, Floriane Magera et al., arXiv 2024[1][2][3]
- **핵심 아이디어**: 기존 축구 중계 카메라 트래킹 시스템의 성능 및 상용화 부족 문제를 해결하기 위해, 오픈소스 [[축구장 검출기]](soccer field detectors)와 정교하게 설계된 [[카메라 모델]](camera model) 및 [[삼각대 모델]](tripod model)을 결합한 효율적이고 견고하며 정확한 [[카메라 트래킹]](camera tracking) 시스템인 BroadTrack을 제안한다.[1][3][4]
- **주요 성과**:
    - SoccerNet 데이터셋에서 평균 재투영 오차(mean reprojection error)를 절반으로 감소시켰다.[1][3]
    - SoccerNet 데이터셋에서 카메라 캘리브레이션(camera calibration)의 [[Jaccard 지수]](Jaccard index)를 15% 이상 향상시켰다.[1][3]
    - 최첨단(state-of-the-art) 방법론들을 능가하는 성능을 보여주었다.[1][3]
    - 20분 길이의 실제 중계 영상 클립에서 시스템의 견고함과 타당성을 입증했다.[1][3]

---

## **🏗 아키텍처 개요**

BroadTrack은 축구장 마킹 검출을 통해 2D-3D 대응점(correspondences)을 설정하고, 이를 기반으로 특수 설계된 카메라 및 삼각대 모델을 활용하여 카메라의 움직임을 효율적이고 정확하게 추적한다.[1][3][4]

### **0. 기호/차원**
- **주요 기호 및 차원 정의**:
    - 카메라 초점 거리: $f$ (focal length)[4]
    - 주점: principal point[4]
    - 카메라 위치: $C$ (camera position)[4]
    - 회전 행렬: $R$ (rotation matrix)[4]
    - 오일러 각: pan ($\phi$), tilt ($\theta$), roll ($\gamma$)[4]
- **입력 데이터 차원 등**: (논문 본문 확인 필요)

### **1. 카메라 모델**
- **구성**: [[핀홀 카메라 모델]](pinhole camera model)을 기반으로 하며, 초점 거리($f$)와 주점을 주요 내재 파라미터(intrinsic parameters)로 사용한다. 픽셀이 정사각형이므로 스큐(skew)는 무시한다.[4]
- 각 층:
    1. **[[방사 왜곡]](Radial Distortion)**: 렌즈의 물리적 특성으로 인한 왜곡을 고려하며, 단순화된 [[Brown-Conrady 모델]](Brown-Conrady model)을 사용하여 이미지 포인트의 원점으로부터의 거리에 따라 조정한다.[4]
    2. **[[카메라 포즈]](Camera Pose)**: 3D 공간에서의 카메라 위치($C$)와 회전 행렬($R$)로 특징지어지며, 오일러 각(pan ($\phi$), tilt ($\theta$), roll ($\gamma$))을 사용하여 파라미터화된다.[4]
- **특이 사항**: 비선형 최적화(non-linear optimization)를 통해 왜곡 모델을 정제한다.[4]

### **2. 삼각대 모델**
- **구성**: 카메라가 팬(pan) 및 틸트(tilt)될 수 있지만, 광축(optical axis)은 삼각대 베이스에 대해 고정된 관계를 유지하도록 정의된다.[4]
- 각 층: (논문 본문 확인 필요)

### **3. 주요 수식 요약**
- **방사 왜곡 모델**: (논문 본문 확인 필요)
- **카메라 포즈**: (논문 본문 확인 필요)

---

## **🎯 주요 구성 요소**

### **1. [[축구장 검출기]](Soccer Field Detectors)**
- **입력/출력 및 작동 원리 설명**: 기존의 오픈소스 축구장 검출기를 활용하여 축구장 마킹을 감지하고, 이를 통해 카메라 캘리브레이션에 필수적인 2D-3D 대응점(correspondences)을 설정한다.[1][3][4]
- $$ (논문 본문 확인 필요) $$

### **2. [[카메라 및 삼각대 모델]](Camera and Tripod Models)**
- **병렬 처리, 분할, 혹은 특수 기능 설명**: 축구 중계 카메라의 고유한 특성을 통합하여 설계된 모델로, 카메라의 팬, 틸트 움직임과 광축의 고정 관계를 반영한다.[1][3][4]
- **설정 값 (논문 기준)**: (논문 본문 확인 필요)

### **3. [기타 구성 요소]**
- [Embedding, Position Encoding 등 설명]: (논문 본문 확인 필요)

---

## **⚖️ BroadTrack vs 기존 모델**

| **비교 항목** | **BroadTrack** | **기존 SOTA** |
| :--- | :--- | :--- |
| **평균 재투영 오차** | 절반 감소[1][3] | 높음 |
| **Jaccard 지수 (캘리브레이션)** | 15% 이상 향상[1][3] | 낮음 |
| **견고성** | 20분 클립에서 입증[1][3] | (정보 부족) |
| **복잡도** | $O(\dots)$ (논문 본문 확인 필요) | $O(\dots)$ (논문 본문 확인 필요) |

- BroadTrack은 기존 최첨단 방법론에 비해 평균 재투영 오차를 크게 줄이고 Jaccard 지수를 향상시켜, 축구 중계 카메라 캘리브레이션 및 트래킹에서 월등한 정확도와 효율성을 제공한다.[1][3]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: (논문 본문 확인 필요)
- **특징**: (논문 본문 확인 필요)

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - [[SoccerNet 데이터셋]](SoccerNet dataset) (비디오 길이가 비교적 짧음, 30초)[1][3]
    - 테스트 세트는 광각 카메라 및 어안 카메라를 포함한 다양한 중계 카메라의 3,141개 이미지로 구성된다.[1]
- **하드웨어**: (논문 본문 확인 필요)
- **학습 시간**: (논문 본문 확인 필요)
- **옵티마이저**: (논문 본문 확인 필요)
- **규제(Regularization)**: (논문 본문 확인 필요)

---

## **⚠️ 한계**
- (논문에서 명시된 한계점은 검색 결과에서 직접적으로 찾기 어려움)

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**평균 재투영 오차 (Mean Reprojection Error)**|**Jaccard 지수 (Camera Calibration)**|
|---|---|---|
| 기존 SOTA | 높음 | 낮음 |
| **BroadTrack** | **절반 감소**[1][3] | **15% 이상 향상**[1][3] |

---

## **🔮 향후 연구 방향**
- (논문 본문 확인 필요)

---

## **🔗 관련 링크**
- [[카메라 트래킹]]
- [[축구 분석]]
- [[컴퓨터 비전]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2412.01721[2]
- **코드**: https://github.com/evs-broadcast/BroadTrack[2][5][3]

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```

```