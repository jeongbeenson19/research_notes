---
aliases: ["Lost and Found", "BUSCA"]
type: paper
tags:
  - DeepLearning
  - Paper
  - MultiObjectTracking
  - Transformer
status: 🟧 Reading
rating: 0
date: 2026-02-04
title: "Lost and Found: Overcoming Detector Failures in Online Multi-Object Tracking"
authors: ["Lorenzo Vaquero", "Yihong Xu", "Xavier Alameda-Pineda", "Victor M. Brea", "Manuel Mucientes"]
year: 2024
venue: "ECCV 2024"
paper_url: https://arxiv.org/abs/2407.10151
topics: ["Multi-Object Tracking", "Detector Failures", "Online Tracking", "Occlusion Handling", "Transformer"]
---

## **📄 Lost and Found: Overcoming Detector Failures in Online Multi-Object Tracking 개요**

- **발표 논문**: "Lost and Found: Overcoming Detector Failures in Online Multi-Object Tracking" by Lorenzo Vaquero et al., ECCV 2024.
- **핵심 아이디어**: Multi-object tracking (MOT)에서 [[tracking-by-detection]] (TbD) 방식의 문제점인 탐지기(detector) 실패(예: [[가려짐 (occlusion)]]으로 인한 객체 누락)를 극복하기 위한 프레임워크 [[BUSCA]]를 제안한다. BUSCA는 기존 TbD 시스템과 호환되며, 과거 추적 결과나 미래 프레임에 접근하지 않고도(fully online manner) 탐지기가 놓친 객체를 지속적으로 추적할 수 있도록 한다. [[BUSCA]]는 인접 트랙, 모션, 학습된 토큰을 기반으로 제안(proposal)을 생성하고, 멀티모달 시각 및 시공간 정보를 통합하는 [[Decision Transformer]]를 활용하여 객체-제안 연관(object-proposal association) 문제를 다지선다형 질문-답변 태스크로 해결한다.
- **주요 성과**:
    - 기존 온라인 TbD 시스템과 호환되는 범용 프레임워크를 제공한다.
    - 과거 추적 결과 수정이나 미래 프레임 접근 없이(fully online) 탐지기 실패를 극복한다.
    - 합성 데이터로만 독립적으로 학습되며, 기본 트래커의 미세 조정(fine-tuning)이 필요 없다.
    - 5가지 다른 트래커에서 일관된 성능 향상을 보였으며, 3가지 다른 벤치마크에서 새로운 SOTA(State-of-the-Art)를 달성했다.

---

## **🏗 아키텍처 개요**

[[BUSCA]]는 기존 TbD 시스템에 플러그인 방식으로 통합되어, 탐지기가 놓친 객체를 추적하는 역할을 한다. 이는 매칭되지 않은 트랙($T_u$)을 입력으로 받아, 제안 생성 프로세스(proposal generation process)를 통해 생성된 제안(proposals)과 비교한다. 이 비교는 혁신적인 [[Decision Transformer]]를 통해 수행되며, 이는 [[Spatiotemporal Encoding (STE)]]를 사용한다.

### **0. 기호/차원**
- $T_u$: 매칭되지 않은 트랙 (Unmatched tracks)
- $B$: 후보 (Candidates) (제안의 구성 요소)
- $C$: 문맥 정보 (Contextual information) (제안의 구성 요소)
- $L$: 학습된 토큰 (Learned tokens) (제안의 구성 요소)

### **1. Decision Transformer**
- **구성**: [[Decision Transformer]]는 멀티모달 시각 및 시공간 정보를 통합한다.
- 각 층:
    1. **[[Spatiotemporal Encoding (STE)]]**: 시공간 정보를 인코딩한다.
    2. **[[Decision Transformer]]**: 객체-제안 연관을 다지선다형 질문-답변 태스크로 처리한다.
- **특이 사항**: 탐지기가 놓친 객체를 "찾는" 핵심 메커니즘이다.

### **2. 제안 생성 프로세스 (Proposal Generation Process)**
- **구성**: 인접 트랙, 모션, 학습된 토큰을 기반으로 제안을 생성한다.

### **3. 주요 수식 요약**
- **객체-제안 연관**:
  - 객체-제안 연관 문제는 다지선다형 질문-답변 태스크로 공식화된다.

---

## **🎯 주요 구성 요소**

### **1. [[BUSCA]]**
- 입력/출력 및 작동 원리 설명: 탐지기가 놓친 객체를 "찾기(search)" 위해 설계된 프레임워크이다. 매칭되지 않은 트랙($T_u$)을 입력으로 받아, 인접 트랙(neighboring tracks), 모션(motion), 학습된 토큰(learned tokens)을 기반으로 제안(proposals)을 생성한다. 이 제안들은 후보(B), 문맥 정보(C), 학습된 토큰(L)으로 구성된다.
- $$ (논문에서 구체적인 수식 확인 필요) $$

### **2. [[Decision Transformer]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: 멀티모달 시각(multimodal visual) 및 시공간(spatiotemporal) 정보를 통합하여 객체-제안 연관(object-proposal association) 문제를 다지선다형 질문-답변 태스크(multi-choice question-answering task)로 해결한다. [[Spatiotemporal Encoding (STE)]]를 활용한다.
- 설정 값 (논문 기준): (논문에서 구체적인 설정 값 확인 필요)

### **3. [[Spatiotemporal Encoding (STE)]]**
- [[Decision Transformer]] 내에서 시공간 정보를 효과적으로 인코딩하는 역할을 한다.

---

## **⚖️ [제안 모델] vs [기존 모델]**

| **비교 항목** | **[제안 모델] (BUSCA)** | **[기존 TbD 트래커]** | **[오프라인 복구 기법]** |
| :--- | :--- | :--- | :--- |
| **탐지기 실패 처리** | 탐지기가 놓친 객체를 지속적으로 추적 | 탐지기 실패 시 추적 중단 | 사후 처리(post-processing)를 통해 객체 복구 |
| **온라인/오프라인** | 완전 온라인 (Fully Online) | 온라인 | 오프라인 |
| **과거/미래 프레임 접근** | 없음 | 없음 | 과거 예측 수정 또는 미래 프레임 접근 |
| **기존 시스템 호환성** | 모든 온라인 TbD 시스템과 호환 | - | - |
| **복잡도** | $O(\dots)$ (논문에서 구체적인 복잡도 확인 필요) | $O(\dots)$ (논문에서 구체적인 복잡도 확인 필요) | $O(\dots)$ (논문에서 구체적인 복잡도 확인 필요) |

- BUSCA는 트랙의 평균 수명(average lifespan)을 연장하여 궤적의 일관성(consistency)과 연속성(continuity)을 향상시킨다. 특히 가시성이 매우 낮은(extremely low visibility) 객체들을 식별하는 데 효과적이다.

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 완전 온라인(Fully online) 방식으로 작동하며, 과거 추적 결과 수정이나 미래 프레임 접근 없이 현재 프레임에서 결정을 내린다.
- **특징**: 매칭되지 않은 트랙($T_u$)과 제안(proposals)을 [[Decision Transformer]]를 통해 연관 짓는 방식으로 추론을 수행한다.

---

## **⚙️ 학습 설정**

- **데이터셋**: 합성 데이터(synthetic data)로만 학습되며, 기본 트래커의 미세 조정(fine-tuning)이 필요 없다.
- **하드웨어**: (논문에서 구체적인 하드웨어 사양 확인 필요)
- **학습 시간**: (논문에서 구체적인 학습 시간 확인 필요)
- **옵티마이저**: (논문에서 구체적인 옵티마이저 및 파라미터 확인 필요)
- **규제(Regularization)**: (논문에서 구체적인 규제 기법 확인 필요)

---

## **⚠️ 한계**
- (논문에서 명시적인 한계점 확인 필요. 일반적인 추론으로는 매우 복잡하거나 예측 불가능한 환경에서의 성능 저하, 합성 데이터 학습으로 인한 실제 환경에서의 일반화 문제 등이 있을 수 있음.)

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

|**모델**|**HOTA**|**IDF1**|
|---|---|---|
| [비교 모델 A] | 수치 | 수치 |
| [비교 모델 B] | 수치 | 수치 |
| **[제안 모델] (BUSCA)** | **향상된 수치** | **향상된 수치** |

- BUSCA는 5가지 다른 트래커에서 일관된 성능 향상을 보였으며, 3가지 다른 벤치마크에서 새로운 SOTA를 달성했다. 특히 HOTA 및 IDF1 지표에서 향상된 성능을 보였다.

---

## **🔮 향후 연구 방향**
- (논문에서 구체적인 향후 연구 방향 확인 필요)

---

## **🔗 관련 링크**
- [[Multi-Object Tracking]]
- [[Tracking-by-Detection]]
- [[Transformer]]
- [[Occlusion]]
- [[BUSCA]]
- [[Decision Transformer]]
- [[Spatiotemporal Encoding]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2407.10151
- **코드**: https://github.com/lorenzovaquero/BUSCA
