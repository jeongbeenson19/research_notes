---
alias: ["공간 인지 기반 시점 비디오 객체 추적"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟧 Reading
rating: 0
date: 2026-02-04
title: "Spatial Cognition from Egocentric Video: Out of Sight, Not Out of Mind"
authors: ["Chiara Plizzari", "Shubham Goel", "Toby J Perrett", "Jacob I Chalk", "Angjoo Kanazawa", "Dima Damen"]
year: 2024
venue: "3DV 2025 (International Conference on 3D Vision)"
paper_url: "https://arxiv.org/abs/2404.05072"
topics: ["Egocentric Vision", "3D Object Tracking", "Spatial Cognition", "Computer Vision"]
---

## **📄 Spatial Cognition from Egocentric Video: Out of Sight, Not Out of Mind 개요**

- **발표 논문**: Spatial Cognition from Egocentric Video: Out of Sight, Not Out of Mind (Chiara Plizzari et al., 3DV 2025)[1][2]
- **핵심 아이디어**:
    인간이 시야에서 사라진 물체의 위치를 기억하는 [[공간 인지 (Spatial Cognition)]] 능력에서 영감을 받아, [[시점 비디오 (Egocentric Video)]]에서 활성 객체를 3D로 추적하는 "Out of Sight, Not out of Mind" 문제를 공식화한다. 기존 2D 또는 3D 추적 방법론의 한계를 극복하기 위해, 부분적인 2D 관측을 3D 월드 좌표로 변환하고, 시각적 외형, 3D 위치 및 상호작용을 사용하여 시간 경과에 따른 객체를 매칭하며, 시야에서 벗어난 객체도 추적을 유지하는 **Lift, Match, and Keep (LMK)**라는 간단하지만 효과적인 접근 방식을 제안한다.[1][3]
- **주요 성과**:
    - EPIC-KITCHENS 데이터셋의 장시간 시점 비디오 100개에 대한 벤치마크에서 LMK는 120초 후에도 객체의 57%를 정확하게 3D 위치를 파악한다.[1][3]
    - 이는 최신 시점 비디오용 3D 방법론의 33% 및 일반 2D 추적 방법론의 17%에 비해 크게 향상된 성능이다.[1][3]
    - 특히, 시야에서 벗어난 지 2분 후에도 객체의 60%를 3D 공간에서 정확하게 위치시킬 수 있음을 보여준다.[4]

---

## **🏗 아키텍처 개요**

LMK (Lift, Match, and Keep)는 시점 비디오에서 객체를 3D로 추적하기 위한 세 가지 주요 단계로 구성된다.[1][3]

### **0. 기호/차원**
- $O$: 객체 (Object)
- $P$: 2D 관측 (2D Observation)
- $W$: 3D 월드 좌표 (3D World Coordinates)
- $T$: 시간 (Time)

### **1. Lift (2D 관측을 3D 월드 좌표로 변환)**
- **구성**: 2D 이미지 평면에서 감지된 객체 관측 ($P$)을 3D 월드 좌표 ($W$)로 "들어 올리는" (lift) 과정.[1][3]
- **특이 사항**: 카메라 포즈(camera pose) 정보를 활용하여 2D 관측을 3D 공간으로 매핑한다.[5]

### **2. Match (시간 경과에 따른 객체 매칭)**
- **구성**: 3D 월드 좌표로 변환된 객체들을 시간 ($T$)에 걸쳐 매칭하여 객체 트랙(object tracks)을 형성한다.[1][3]
- **각 층**:
    1. **[[시각적 외형 (Visual Appearance)]]**: 객체의 시각적 특징을 기반으로 매칭.
    2. **[[3D 위치 (3D Location)]]**: 3D 공간에서의 근접성을 기반으로 매칭.
    3. **[[상호작용 (Interactions)]]**: 객체 간의 상호작용 정보를 활용하여 매칭.
- **특이 사항**: 3D 할로센트릭(allocentric, 세계 중심) 좌표 표현을 활용하여 추적 문제를 단순화한다.[5]

### **3. Keep (시야 밖 객체 트랙 유지)**
- **구성**: 카메라 시야(out-of-view)에서 벗어난 객체들의 트랙을 지속적으로 유지한다.[1][3]
- **특이 사항**: 인간의 공간 인지 능력처럼, 시야에 없더라도 객체의 3D 위치를 "기억"하는 메커니즘을 포함한다.[1][3]

---

## **🎯 주요 구성 요소**

### **1. [[Lift (2D to 3D)]]**
- 입력/출력 및 작동 원리 설명: 2D 이미지에서 감지된 객체 바운딩 박스 또는 마스크와 해당 시점의 카메라 포즈 정보를 입력으로 받아, 객체의 대략적인 3D 월드 좌표를 추정한다.
- $P_{2D} \xrightarrow{\text{Camera Pose}} W_{3D}$

### **2. [[Match (Tracking)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 시각적 특징 임베딩, 3D 공간 거리, 그리고 객체 간의 과거 상호작용 패턴 등을 종합적으로 고려하여 현재 프레임의 3D 객체와 기존 트랙을 연결한다.
- 설정 값 (논문 기준): (구체적인 설정 값은 논문 본문 참조 필요)

### **3. [[Keep (Object Permanence)]]**
- 시야 밖 객체에 대한 지속적인 3D 위치 추정 및 관리를 담당한다. 이는 객체가 일시적으로 가려지거나 카메라 시야를 벗어나더라도 그 존재와 위치를 추론하여 트랙을 유지하는 핵심 메커니즘이다.

---

## **⚖️ LMK vs 기존 모델**

| **비교 항목** | **LMK (제안 모델)** | **최신 3D 시점 비디오 방법** | **일반 2D 추적 방법** |
| :--- | :--- | :--- | :--- |
| **핵심 접근 방식** | 3D 공간 인지 기반 추적 | 3D 추적 (세부 미상) | 2D 이미지 평면 추적 |
| **시야 밖 객체 처리** | 트랙 유지 (공간 인지) | 제한적 또는 없음 | 없음 |
| **성능 (120초 후)** | 57% 정확도[1][3] | 33% 정확도[1][3] | 17% 정확도[1][3] |
| **복잡도** | $O(\dots)$ (논문 본문 참조 필요) | $O(\dots)$ | $O(\dots)$ |

- LMK는 인간의 [[공간 인지]] 능력을 모방하여 시야에서 벗어난 객체에 대한 추적 성능을 획기적으로 개선한다. 특히, 3D 월드 좌표계에서의 추적과 시각적 외형, 3D 위치, 상호작용을 결합한 매칭 전략이 강점이다.[1][3]

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: LMK는 2D 관측을 3D로 변환하고, 이를 시간적으로 매칭하여 객체 트랙을 생성하며, 시야 밖 객체에 대한 트랙을 유지하는 방식으로 추론을 수행한다.[1][3]
- **특징**: 3D 할로센트릭 표현을 사용하여 객체 추적의 견고성을 높인다.[5]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - [[EPIC-KITCHENS]] (100개의 장시간 시점 비디오)[1][3]
- **하드웨어**: (논문 본문 참조 필요)
- **학습 시간**: (논문 본문 참조 필요)
- **옵티마이저**: (논문 본문 참조 필요)
- **규제(Regularization)**:
    - (논문 본문 참조 필요)

---

## **⚠️ 한계**
- (논문 본문 참조 필요)

---

## **📊 주요 실험 결과**

### **[3D 객체 위치 파악 성능]**

|**모델**|**120초 후 3D 위치 정확도**|
|---|---|
| 최신 3D 시점 비디오 방법 | 33%[1][3] |
| 일반 2D 추적 방법 | 17%[1][3] |
| **LMK (제안 모델)** | **57%**[1][3] |

---

## **🔮 향후 연구 방향**
- (논문 본문 참조 필요)

---

## **🔗 관련 링크**
- [[Egocentric Vision]]
- [[3D Object Tracking]]
- [[Spatial Cognition]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2404.05072[3]
- **코드**: (논문 본문 또는 프로젝트 페이지 참조 필요)

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```

```