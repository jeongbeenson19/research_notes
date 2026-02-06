---
alias: ["LSTR", "온라인 행동 감지 롱 숏텀 트랜스포머"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟧 Reading
rating: 0
date: 2026-02-02
title: "Long Short-Term Transformer for Online Action Detection"
authors: ["Mingze Xu", "Yuanjun Xiong", "Hao Chen", "Xinyu Li", "Wei Xia", "Zhuowen Tu", "Stefano Soatto"]
year: 2021
venue: "NeurIPS"
paper_url: "https://arxiv.org/abs/2107.03377"
topics: ["Online Action Detection", "Transformer", "Temporal Modeling", "Video Analysis"]
---

## **📄 Long Short-Term Transformer for Online Action Detection 개요**

- **발표 논문**: Long Short-Term Transformer for Online Action Detection, Mingze Xu et al., NeurIPS 2021
- **핵심 아이디어**:
    실시간 비디오 스트림에서 행동을 감지하는 **[[Online Action Detection]]** 태스크를 위해 장단기 컨텍스트를 모두 활용하는 **[[Transformer]]** 기반의 새로운 아키텍처 **LSTR (Long Short-Term Transformer)** 을 제안합니다. LSTR은 **인코더**를 통해 최대 8분 길이의 긴 과거 정보(Long-Term Context)를 거시적으로 압축하여 맥락을 파악하고, **디코더**를 통해 현재 시점의 짧은 클립(Short-Term Context)에 집중하여 행동의 세부 사항을 모델링합니다. 이 이중적인 접근을 통해, 긴 시간의 의존성을 효율적으로 학습하면서도 실시간 예측에 필요한 세밀한 정보를 놓치지 않습니다.
- **주요 성과**:
    - THUMOS'14, TVSeries, HACS Segment 등 주요 온라인 행동 감지 벤치마크에서 SOTA(State-of-the-Art) 성능을 달성했습니다.
    - 기존의 순환(recurrent) 모델들이 겪는 긴 시퀀스 학습의 어려움과, 일반적인 트랜스포머가 긴 시퀀스에 적용될 때 발생하는 계산 복잡도 문제를 효과적으로 해결했습니다.

---

## **🏗 아키텍처 개요**

LSTR은 인코더-디코더 구조를 채택하여, 긴 과거 정보와 짧은 현재 정보를 분리하여 처리하고 이를 결합하여 최종 예측을 수행합니다.

### **0. 기호/차원**
- $T_L$: 인코더가 처리하는 긴 시퀀스 길이 (Long-term window, e.g., 2048 frames)
- $T_S$: 디코더가 처리하는 짧은 시퀀스 길이 (Short-term window, e.g., 32 frames)
- $H_L$: 인코더에 의해 압축된 장기 컨텍스트 메모리 (Long-term memory)
- $H_S$: 디코더가 처리하는 단기 컨텍스트 (Short-term context)

### **1. LSTR 인코더 (Long-Term Encoder)**
- **구성**: 긴 시간(e.g., $T_L$)에 걸친 비디오 특징(feature) 시퀀스를 입력받아, 이를 고정된 크기의 장기 메모리($H_L$)로 압축합니다.
- 각 층:
    1. **Temporal-Only Transformer Encoder**: 공간 정보 없이 시간 축에 대해서만 셀프 어텐션을 수행하여 계산 효율성을 높입니다.
    2. **Memory Compression**: 어텐션 풀링(attention pooling)과 유사한 방식으로, 시퀀스의 정보를 몇 개의 대표 벡터로 압축합니다.
- **특이 사항**: 전체 과거를 저장하는 대신, 고정된 크기의 메모리를 점진적으로 업데이트하며 사용하므로 매우 긴 비디오도 효율적으로 처리할 수 있습니다.

### **2. LSTR 디코더 (Short-Term Decoder)**
- **구성**: 현재 시점의 짧은 비디오 클립 특징(e.g., $T_S$)을 입력받습니다.
- 각 층:
    1. **Cross-Attention**: 디코더는 현재 클립 특징($H_S$)을 쿼리(Query)로 사용하고, 인코더로부터 받은 장기 메모리($H_L$)를 키(Key)와 값(Value)으로 사용하여 두 컨텍스트를 융합합니다.
    2. **Temporal-Only Transformer Decoder**: 융합된 정보를 바탕으로 현재 프레임의 행동을 분류(classification)합니다.

### **3. 주요 수식 요약**
- **장기 메모리 압축 (Conceptual)**:
  - $H_L = \text{Encoder}(\text{Past Features}[-T_L:])$
- **디코더의 Cross-Attention**:
  - $\text{Fused Features} = \text{CrossAttention}(\text{Query}=H_S, \text{Key}=H_L, \text{Value}=H_L)$

---

## **🎯 주요 구성 요소**

### **1. 장단기 메모리 메커니즘 (Long and Short-term Memory)**
- LSTR의 핵심으로, 과거의 중요한 맥락(Long-term)과 현재의 세부적인 정보(Short-term)를 분리하여 모델링합니다.
- **Long-term**: "현재 드라마 에피소드가 결혼식 장면이다"와 같은 전반적인 컨텍스트를 제공합니다.
- **Short-term**: "주인공이 방금 반지를 꺼냈다"와 같은 현재 행동의 결정적인 단서를 포착합니다.
- 이 두 정보를 Cross-Attention으로 결합함으로써, 모델은 맥락에 맞는 정확한 행동 예측을 수행할 수 있습니다.

### **2. 시간 전용 트랜스포머 (Temporal-Only Transformer)**
- 비디오의 각 프레임에서 추출된 1D 특징 벡터 시퀀스에 대해 어텐션을 적용합니다.
- 2D/3D 연산이 필요한 Spatio-temporal 어텐션에 비해 계산량이 훨씬 적어, 온라인(실시간) 처리에 적합하고 매우 긴 시퀀스를 다룰 수 있게 합니다.

---

## **⚖️ LSTR vs 기존 모델**

| **비교 항목** | **LSTR** | **RNN 기반 모델 (e.g., LSTM)** | **일반 Transformer 모델** |
| :--- | :--- | :--- | :--- |
| **장기 의존성** | 명시적인 장기 메모리로 효과적으로 포착 | Gradient Vanishing 문제로 학습이 불안정 | 가능하지만, 시퀀스가 길어지면 $O(T^2)$ 복잡도 |
| **계산 효율성** | Temporal-Only 어텐션과 메모리 압축으로 높음 | 순차 처리로 인해 병렬화에 한계 | 매우 긴 시퀀스에 적용 시 계산 비용이 큼 |
| **정보 흐름** | 인코더-디코더 구조로 장/단기 정보 명시적 분리 | 정보를 단일 Hidden State에 모두 압축하려 함 | 모든 시간 단계가 동등하게 상호작용 |

- LSTR은 RNN의 장기 의존성 문제와 일반 트랜스포머의 계산 복잡도 문제를 절충한 영리한 구조로, 온라인 행동 감지 태스크에 매우 적합한 특성을 가집니다.

---

## **🧠 추론/디코딩/생성 과정**
- **방식**: 인과적(Causal) 추론. 즉, 현재 예측은 오직 과거와 현재의 정보만을 사용합니다.
- **과정**:
    1. 비디오 스트림이 들어오면, 인코더는 과거 $T_L$ 길이의 특징을 지속적으로 업데이트하며 장기 메모리 $H_L$을 갱신합니다.
    2. 매 예측 시점마다, 디코더는 최근 $T_S$ 길이의 클립 특징 $H_S$와 인코더의 $H_L$을 입력받습니다.
    3. Cross-Attention을 통해 $H_L$에서 $H_S$와 관련된 정보를 가져와 결합합니다.
    4. 디코더의 최종 출력을 통해 현재 프레임의 행동 클래스를 예측합니다.

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - THUMOS'14, TVSeries, HACS Segment
    - **사전 학습**: 행동 분류 데이터셋(Kinetics, ActivityNet)으로 사전 학습된 I3D 또는 SlowFast 같은 모델을 특징 추출기(feature extractor)로 사용합니다.
- **하드웨어**: [논문 원문 참조]
- **학습 시간**: [논문 원문 참조]
- **옵티마이저**: [논문 원문 참조]
- **규제(Regularization)**: [논문 원문 참조]

---

## **⚠️ 한계**
- 사전 학습된 강력한 특징 추출기에 성능이 크게 의존할 수 있습니다.
- 인코더와 디코더의 윈도우 크기($T_L$, $T_S$)와 같은 하이퍼파라미터에 민감할 수 있습니다.

---

## **📊 주요 실험 결과**

### **THUMOS'14 성능 (mAP)**

|**모델**|**mAP@0.3**|**mAP@0.5**|
|---|---|---|
| OadTR (이전 SOTA) | 60.9 | 55.4 |
| **LSTR (Ours)** | **63.4** | **59.1** |

- LSTR은 기존의 트랜스포머 기반 모델(OadTR) 및 다른 모든 비교 모델들보다 높은 성능을 기록하며, 특히 mAP@0.5에서 큰 폭의 성능 향상을 보였습니다.

---

## **🔮 향후 연구 방향**
- 특징 추출 과정까지 End-to-End로 학습하여 성능을 극대화하는 연구.
- 더 효율적인 메모리 업데이트 및 압축 방식을 탐구하여 더 긴 컨텍스트를 처리하는 연구.

---

## 🔁 내 연구와의 매핑
- 파이프라인 위치: pre / in-loop / post
- State 대응
  - location: (표현/업데이트/사용 위치)
  - appearance: (사용 여부, 사용 위치)
  - semantic: (종류, 사용 위치)
  - uncertainty: (표현, miss/occlusion 시 동작)
- 키워드 연결
  - 주축:
  - 부축:
- 판정
  - 유사:
  - 차용:
  - 충돌:

## **🔗 관련 링크**
- [[Online Action Detection]]
- [[Temporal Modeling]]
- [[Transformer]]

## **📌 참고 링크**
- **논문 원문**: [https://arxiv.org/abs/2107.03377](https://arxiv.org/abs/2107.03377)
- **코드**: [https://github.com/xumingze0308/LSTR](https://github.com/xumingze0308/LSTR)

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, "Online Action Detection") AND file.name != this.file.name
SORT year desc
```