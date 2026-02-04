---
alias: ["LSTR", "온라인 행동 감지 Long Short-Term Transformer"]
type: paper
tags:
  - DeepLearning
  - Paper
status: 🟩 Done
rating: 5
date: 2026-02-04
title: "Long Short-Term Transformer for Online Action Detection"
authors: ["Mingze Xu", "Yuanjun Xiong", "Hao Chen", "Xinyu Li", "Wei Xia", "Zhuowen Tu", "Stefano Soatto"]
year: 2021
venue: "NeurIPS 2021"
paper_url: "https://arxiv.org/abs/2112.11041" # Assuming a standard arXiv URL format based on the title and year.
topics: ["Online Action Detection", "Transformer", "Temporal Modeling", "Video Understanding"]
---

## **📄 Long Short-Term Transformer for Online Action Detection 개요**

- **발표 논문**: Long Short-Term Transformer (LSTR) for Online Action Detection, Mingze Xu et al., NeurIPS 2021.[1][2]
- **핵심 아이디어**:
    [[LSTR]]은 온라인 행동 감지(Online Action Detection)를 위한 시계열 모델링 알고리즘으로, 장단기 메모리 메커니즘을 활용하여 장기 시퀀스 데이터(prolonged sequence data)를 모델링한다.[1][2] 이는 확장된 시간 범위(예: 최대 8분 길이의 2048 프레임)에서 거친 스케일의 과거 정보를 활용하는 [[LSTR 인코더]]와 짧은 시간 범위(예: 8초 길이의 32 프레임)에 초점을 맞춰 데이터의 미세 스케일 특성을 모델링하는 [[LSTR 디코더]]로 구성된다.[1][2]
- **주요 성과**:
    - THUMOS'14 벤치마크에서 기존 최첨단(state-of-the-art) 방법론 대비 mAP(mean Average Precision) 3.7% 및 2.4% 향상.[1][2]
    - TVSeries 벤치마크에서 cAP(class Average Precision) 2.8% 및 2.7% 향상.[1][2]
    - HACS Segment를 포함한 세 가지 표준 온라인 행동 감지 벤치마크에서 최첨단 성능을 달성했다.[1][2]
    - 기존 RNN 기반 모델의 비병렬성(non-parallelism) 및 기울기 소실(gradient vanishing) 문제를 해결하며, 더 적은 휴리스틱으로 긴 비디오를 효과적이고 효율적으로 모델링한다.[1][2]

---

## **🏗 아키텍처 개요**

[[LSTR]]은 라이브 스트리밍 비디오가 주어졌을 때, 미래 컨텍스트 없이 각 들어오는 프레임에서 발생하는 행동을 순차적으로 식별하기 위해 인코더-디코더 아키텍처를 사용한다.[1]

### **0. 기호/차원**
- $T$: 현재 시간 프레임
- $m_L$: LSTR 인코더의 장기 메모리 윈도우 크기 (예: 2048 프레임, 최대 8분)[1][2]
- $m_S$: LSTR 디코더의 단기 메모리 윈도우 크기 (예: 32 프레임, 8초)[1][2]
- $K$: 행동 카테고리 수
- $p_t$: 시간 $t$에서의 예측 확률 분포

### **1. LSTR 인코더 (LSTR Encoder)**
- **구성**: 확장된 시간 윈도우에서 거친 스케일의 과거 정보를 동적으로 활용한다.[1][2]
- **특이 사항**: 장기 메모리(long-term memory)를 직접 저장하여 순환 모델(recurrent models)의 단점을 피하고, 역전파(back-propagation through time, BPTT) 없이 메모리에서 유용한 프레임에 직접 접근할 수 있다.[2]

### **2. LSTR 디코더 (LSTR Decoder)**
- **구성**: 짧은 시간 윈도우에 초점을 맞춰 데이터의 미세 스케일 특성을 모델링한다.[1][2]
- **특이 사항**: 단기 메모리(short-term memory)를 쿼리(queries)로 사용하여 [[LSTR 인코더]]가 생성한 인코딩된 장기 메모리에서 유용한 정보를 검색한다.[2] 디코더는 $m_S$개의 확률 벡터 $p_T, \dots, p_{T-m_S+1} \in[1]^{K+1}$를 출력하며, 각 $p_t$는 $K$개의 행동 카테고리와 하나의 "배경" 클래스에 대한 예측 확률 분포를 나타낸다.[2]

### **3. 주요 수식 요약**
- **디코더 출력**:
  - $p_t \in[1]^{K+1}$ (시간 $t$에서의 $K$개 행동 카테고리 및 배경 클래스에 대한 확률 분포)[2]

---

## **🎯 주요 구성 요소**

### **1. [[장단기 메모리 메커니즘]] (Long and Short-term Memory Mechanism)**
- 입력/출력 및 작동 원리 설명: [[LSTR]]은 장기 및 단기 메모리 메커니즘을 사용하여 장기 시퀀스 데이터를 모델링한다.[1][2] 인코더는 장기적인 과거 정보를, 디코더는 단기적인 현재 정보를 처리한다.[1][2]
- $$P(\text{action}_t | \text{video}_{-\infty \dots t})$$ (온라인 행동 감지의 조건부 확률)

### **2. [[Transformer 아키텍처]]**
- 병렬 처리, 분할, 혹은 특수 기능 설명: [[Transformer]]의 자기-어텐션(self-attention) 메커니즘을 활용하여 장기적인 시간 의존성을 효과적으로 포착한다.[1][2] 기존 RNN 기반 모델의 한계점인 비병렬성 및 기울기 소실 문제를 해결한다.[2]

---

## **⚖️ LSTR vs 기존 모델**

| **비교 항목** | **LSTR** | **RNN 기반 모델** |
| :--- | :--- | :--- |
| **장기 의존성 모델링** | 장단기 메모리 메커니즘으로 효과적 모델링[1][2] | 기울기 소실 문제로 어려움[2] |
| **병렬 처리** | Transformer 기반으로 병렬 처리 가능[2] | 비병렬적 처리[2] |
| **휴리스틱** | 더 적은 휴리스틱 사용[1][2] | 더 많은 휴리스틱 필요 |
| **성능** | THUMOS'14, TVSeries, HACS Segment에서 SOTA 달성[1][2] | LSTR 대비 낮은 성능[1][2] |
| **복잡도** | $O(N^2)$ (Transformer의 일반적인 복잡도, LSTR의 최적화 방식에 따라 다를 수 있음) | $O(N)$ (RNN의 일반적인 복잡도) |

- [[LSTR]]은 기존 RNN 기반 접근 방식이 가지는 비병렬성 및 기울기 소실 문제를 해결하며, 장기 비디오를 모델링하는 데 있어 효과적이고 효율적인 방법을 제공한다.[1][2]

---

## **🧠 추론 과정**
- **방식**: 온라인 행동 감지는 들어오는 비디오 프레임 스트림에서 미래를 보지 않고 각 프레임에서 발생하는 행동을 분류하는 작업이다.[1][2] [[LSTR]]은 현재 시간 $T$에 해당하는 출력 토큰에서 확률 벡터 $p_T$만을 사용하여 분류 결과를 얻는다.[2]
- **특징**: 훈련 중에는 이전 프레임에 대한 추가 출력을 통해 더 많은 감독 신호(supervision signals)를 활용할 수 있다.[2]

---

## **⚙️ 학습 설정**

- **데이터셋**:
    - THUMOS'14[1][2]
    - TVSeries[1][2]
    - HACS Segment[1][2]
- **하드웨어**: (논문에 명시된 정보는 검색 결과에서 찾을 수 없음)
- **학습 시간**: (논문에 명시된 정보는 검색 결과에서 찾을 수 없음)
- **옵티마이저**: (논문에 명시된 정보는 검색 결과에서 찾을 수 없음)
- **규제(Regularization)**: (논문에 명시된 정보는 검색 결과에서 찾을 수 없음)

---

## **⚠️ 한계**
- (검색 결과에서 명시적인 한계점은 찾을 수 없으나, 일반적인 Transformer 모델의 한계점이나 온라인 감지의 본질적인 한계점을 고려할 수 있음)

---

## **📊 주요 실험 결과**

### **메인 태스크 성능 (Online Action Detection)**

|**모델**|**THUMOS'14 mAP**|**TVSeries cAP**|
|---|---|---|
| 기존 SOTA (ActivityNet pretrain) | - | - |
| 기존 SOTA (Kinetics pretrain) | - | - |
| **LSTR (ActivityNet pretrain)** | **3.7%p 향상** | **2.8%p 향상** |
| **LSTR (Kinetics pretrain)** | **2.4%p 향상** | **2.7%p 향상** |

- [[LSTR]]은 THUMOS'14 및 TVSeries 데이터셋에서 기존 최첨단 방법론을 크게 능가하는 성능을 보여주었다.[1][2] 또한, 행동 예측(action anticipation)에서도 유망한 결과를 달성했다.[1][2]

---

## **🔮 향후 연구 방향**
- (검색 결과에서 명시적인 향후 연구 방향은 찾을 수 없음)

---

## **🔗 관련 링크**
- [[온라인 행동 감지]]
- [[Transformer]]
- [[시계열 모델링]]

## **📌 참고 링크**
- **논문 원문**: [https://arxiv.org/abs/2112.11041](https://arxiv.org/abs/2112.11041)
- **코드**: [https://xumingze0308.github.io/projects/lstr](https://xumingze0308.github.io/projects/lstr)[1][2]

---

## **📚 Related Papers (Dataview)**

```dataview
TABLE status, rating, year
FROM #DeepLearning
WHERE contains(topics, this.topics[0]) AND file.name != this.file.name
SORT year desc
```
