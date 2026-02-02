---
alias: ["Out of Sight, Still in Mind"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟩 Done
rating: 4 # 1~5점
date: 2026-02-02
title: "Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models"
authors: ["Yixuan Huang", "Jialin Yuan", "Chanho Kim", "Pupul Pradhan", "Bryan Chen", "Li Fuxin", "Tucker Hermans"]
year: 2024
venue: "IEEE International Conference on Robotics and Automation (ICRA)"
paper_url: "https://arxiv.org/abs/2309.15278"
topics: ["Robotics", "Artificial Intelligence", "Computer Vision", "Machine Learning"]
---

## **📄 Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models 개요**

- **발표 논문**: Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models, Yixuan Huang et al., IEEE International Conference on Robotics and Automation (ICRA) 2024.
- **핵심 아이디어**:
    로봇이 현실적인 환경에서 안정적으로 작동하기 위해서는 이전에 관찰되었지만 현재는 가려진(occluded) 객체에 대한 기억을 유지해야 합니다. 이 논문은 **[[UVOS (Unsupervised Video Object Segmentation)]]** 알고리즘을 활용하여 객체 지향 메모리(object-oriented memory)를 명시적으로 인코딩하는 새로운 접근 방식을 제안합니다. 이는 장기적인 이력 관리를 가능하게 하고, 기존의 암묵적인 자기회귀(autoregressive) 모델보다 더 견고하게 하위 계획(downstream planning)을 수행할 수 있도록 합니다. 제안하는 프레임워크는 **[[DOOM (Deep Object-Oriented Memory)]]** 과 **[[LOOM (Latent Object-Oriented Memory)]]** 이라는 두 가지 구현체를 포함합니다.
- **주요 성과**:
    - 부분적인 포인트 클라우드(partial-view point clouds)와 객체 발견 및 추적 엔진을 기반으로 **[[트랜스포머 관계형 역학 (transformer relational dynamics)]]** 을 활용하여 궤적 이력(history of trajectories)을 인코딩합니다.
    - 가려진 객체(occluded objects)에 대한 추론, 새로운 객체 출현(novel objects appearance), 객체 재출현(object reappearance)을 포함한 다양한 도전적인 작업을 성공적으로 수행합니다.
    - 광범위한 시뮬레이션 및 실제 환경 실험에서 다양한 수의 객체와 방해 행동(distractor actions)에 대해 암묵적 메모리 기준선(implicit memory baseline)보다 우수한 성능을 보였습니다.

---

## **🏗 아키텍처 개요**

[모델의 전체적인 구조 설명은 논문 본문에 상세히 기술되어 있을 것으로 예상되나, 초록 및 검색 결과만으로는 구체적인 아키텍처를 파악하기 어렵습니다. 핵심 아이디어에서 언급된 구성 요소를 바탕으로 개요를 작성합니다.]

### **0. 기호/차원**
- $Z_t$: 현재 관측값 (current observation)
- $(A_t, \theta_t)$: 현재 행동 (current action)
- $Z_{0:t-1}$: 이전 관측값의 압축된 메모리 (compressed memory of previous observations)
- $A_{0:t-1}$: 이전 행동 (previous actions)
- $r_{t+1}'$: 결과 관계 (resulting relations)
- $p_{t+1}'$: 결과 객체 포즈 (resulting object poses)
- $Q$: 메모리 표현 (memory representation)

### **1. 메모리 기반 신경망 프레임워크**
- **구성**: 전체 이력 대신 현재 관측값, 현재 행동, 그리고 이전 관측값의 압축된 메모리를 입력으로 받아 다음 관계 및 객체 포즈를 예측합니다.
- 각 층:
    1. **[[UVOS (Unsupervised Video Object Segmentation)]]**: 객체 지향 메모리를 명시적으로 관리하고, 이전에 알려지지 않은 객체를 발견하며, 시간 경과에 따라 객체를 추적합니다.
    2. **[[트랜스포머 관계형 역학 (transformer relational dynamics)]]**: 궤적 이력을 인코딩하는 데 사용됩니다.
- **특이 사항**: Huang et al.의 기존 프레임워크를 기반으로 하며, 이 프레임워크는 그래프 신경망(Graph Neural Net) 또는 트랜스포머 기반 인코더(Transformer-based encoder)를 사용하여 가변적인 수의 객체를 인코딩합니다.

### **2. DOOM 및 LOOM 구현**
- **구성**: 제안된 프레임워크의 두 가지 구현체입니다.
- 각 층:
    - **[[DOOM (Deep Object-Oriented Memory)]]**: 포인트 클라우드 기반 인코딩(point cloud-based encoding)을 사용하여 메모리를 표현합니다.
    - **[[LOOM (Latent Object-Oriented Memory)]]**: 잠재 공간 인코딩(latent space encoding)을 사용하여 메모리를 표현합니다.

### **3. 주요 수식 요약**
- **관계 및 포즈 예측**:
  - $Z_t, (A_t, \theta_t), Q \rightarrow r_{t+1}', p_{t+1}'$ (여기서 $Q$는 $Z_{0:t-1}$ 및 $A_{0:t-1}$의 압축된 메모리)

---

## **🎯 주요 구성 요소**

### **1. [[UVOS (Unsupervised Video Object Segmentation)]]**
- 입력/출력 및 작동 원리 설명: UVOS 알고리즘은 로봇 조작 작업에서 객체에 대한 세분화 레이블이 없을 때 유용합니다. 이 알고리즘은 이전에 알려지지 않은 객체를 동시에 발견하고 시간 경과에 따라 추적하며, 심지어 심하고 장기적인 완전한 가려짐(occlusions) 상황에서도 추적이 가능합니다.
- $$UVOS_{output} = \{O_t^i\}_{i=1}^N$$ (여기서 $O_t^i$는 시점 $t$에서의 $i$번째 객체 세그먼트)

### **2. [[DOOM (Deep Object-Oriented Memory)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: DOOM은 메모리를 표현하기 위해 포인트 클라우드 기반 인코딩을 사용합니다.

### **3. [[LOOM (Latent Object-Oriented Memory)]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: LOOM은 메모리를 표현하기 위해 잠재 공간 인코딩을 사용합니다.

---

## **⚖️ [제안 모델] vs [기존 모델]**

| **비교 항목** | **[제안 모델 (DOOM/LOOM)]** | **[암묵적 메모리 기준선 (Implicit Memory Baseline)]** | **[Huang et al. 프레임워크]** |
| :--- | :--- | :--- | :--- |
| **메모리 관리** | 명시적 객체 지향 메모리 (Explicit object-oriented memory) | 암묵적 자기회귀 모델 (Implicit autoregressive models) | 모든 관련 객체가 관찰 가능하다고 가정 |
| **장기 이력** | 장기 이력 관리에 더 견고함 | 장기 이력 관리에 어려움 | - |
| **가려진 객체** | 가려진 객체에 대한 추론 및 계획 가능 | 가려진 객체에 대한 장기 기억 유지 어려움 | 가려진 객체 시나리오에서 실패 |
| **성능** | 우수한 성능 (시뮬레이션 및 실제 환경) | 제안 모델보다 낮은 성능 | - |
| **복잡도** | $O(\dots)$ | $O(\dots)$ | $O(\dots)$ |

- 제안 모델(DOOM 및 LOOM)은 UVOS 알고리즘을 통해 객체 지향 메모리를 명시적으로 관리함으로써, 가려진 객체에 대한 장기적인 기억과 추론 능력을 크게 향상시켜 기존의 암묵적 메모리 모델 및 모든 객체가 관찰 가능하다고 가정하는 프레임워크의 한계를 극복합니다.

---

## **🧠 [추론/디코딩/생성] 과정**
- **방식**: 다단계 계획(multi-step planning)을 효과적으로 수행하기 위해 예측을 연결(chaining together predictions)합니다.
- **특징**: 사라진 객체의 포즈를 여러 행동 후에도 기억할 수 있도록 합니다.

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - UVOS 모델을 로봇에 익숙하게 하기 위해 YCB-Video 데이터셋 [55]의 로봇 팔 및 객체 주석을 사용하여 미세 조정(fine-tuned)됩니다.
- **하드웨어**: [정보 없음]
- **학습 시간**: [정보 없음]
- **옵티마이저**: [정보 없음]
- **규제(Regularization)**:
    - [정보 없음]

---

## **⚠️ 한계**
- 기존 프레임워크(Huang et al. [17, 18])는 모든 관련 객체가 관찰 가능하다고 가정하여, 가려진 객체가 있는 시나리오에서는 성공적으로 계획하고 실행하지 못합니다.
- 암묵적인 자기회귀 모델은 반복적인 메모리 업데이트를 통해 오랫동안 가려져 있는 객체의 장기 기억을 유지하는 데 어려움이 있습니다.
- 로봇 관측의 전체 이력을 입력으로 사용하는 것은 장기적인 작업에서 입력이 시간과 선형적으로 증가하여 효율적으로 관리하기에는 너무 커지므로 지속 불가능합니다.

---

## **📊 주요 실험 결과**

### **메인 태스크 성능**

| **모델**                  | **가려진 객체 추론** | **새로운 객체 출현** | **객체 재출현** | **암묵적 메모리 기준선 대비 성능** |
| ----------------------- | ------------- | ------------- | ---------- | --------------------- |
| [비교 모델 A]               | -             | -             | -          | -                     |
| [비교 모델 B]               | -             | -             | -          | -                     |
| **[제안 모델 (DOOM/LOOM)]** | **성공적 수행**    | **성공적 수행**    | **성공적 수행** | **우수**                |

---

## **🔮 향후 연구 방향**
- [논문의 Future Work 섹션은 직접적으로 언급되지 않았으나, 논문의 목표와 한계를 고려할 때 다음과 같은 방향을 추론할 수 있습니다.]
- UVOS 알고리즘을 로봇 조작 작업에 활용하여 세분화 레이블이 없는 객체에 대한 추적 및 기억 능력을 더욱 강화하는 연구.
- 다양한 객체 수와 방해 행동이 있는 환경에서 모델의 견고성을 더욱 향상시키는 연구.

---

## **🔗 관련 링크**
- [[객체 지향 메모리]]
- [[UVOS (Unsupervised Video Object Segmentation)]]
- [[트랜스포머 관계형 역학 (transformer relational dynamics)]]
- [[로봇 계획]]

## **📌 참고 링크**
- **논문 원문**: https://arxiv.org/abs/2309.15278
- **코드**: [정보 없음 - arXiv 페이지에서 확인 필요]

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics) AND file.name != this.file.name
SORT year desc
```