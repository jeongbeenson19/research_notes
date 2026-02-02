---
tags:
  - ML
  - learning_rule
  - neuroscience
aliases:
  - 헤비안 규칙
  - Hebb's Rule
---

# Hebbian Rule (헤비안 규칙)

Hebbian Rule(헤비안 학습 규칙)은 신경과학자 **Donald Hebb**가 1949년 저서 *"The Organization of Behavior"* 에서 제안한 신경망 학습의 기본 원리입니다. 이 규칙은 생물학적 [[Synaptic Plasticity|시냅스 가소성]]을 수학적으로 설명하며, 오늘날 인공신경망 학습의 이론적 기반 중 하나로 여겨집니다.

> **핵심 원리**: “**Cells that fire together, wire together.**”
> (함께 활성화되는 뉴런은 그 연결이 강화된다.)

즉, 어떤 뉴런 A가 뉴런 B의 발화를 지속적으로 또는 반복적으로 유발하면, 뉴런 A와 B 사이의 시냅스 연결이 강화된다는 원리입니다.

## ⚙️ 수학적 표현

가장 기본적인 형태의 Hebbian Rule은 다음과 같이 표현됩니다:

`Δw_ij = η * y_j * x_i`

-   `Δw_ij`: 입력 뉴런 `i`와 출력 뉴런 `j` 사이의 가중치 변화량
-   `η`: 학습률 (Learning Rate)
-   `x_i`: 입력 뉴런 `i`의 활성도(출력)
-   `y_j`: 출력 뉴런 `j`의 활성도(출력)

이 수식은 입력 뉴런과 출력 뉴런이 **동시에 활성화될수록** 그 연결 가중치가 증가함을 의미합니다.

## ✨ 주요 특징 및 한계

| 특징              | 설명                                                 |
| ----------------- | ---------------------------------------------------- |
| **[[Unsupervised Learning|비지도 학습]]** | 외부의 정답(label)이나 보상 신호 없이 학습이 가능합니다.   |
| **지역성 (Locality)**   | 가중치 업데이트에 필요한 정보가 해당 뉴런 주변에 한정됩니다. |
| **생물학적 타당성** | 실제 뇌의 시냅스 학습 과정(LTP)과 유사합니다.        |

**한계점**으로는 가중치가 양의 값으로 무한히 발산할 수 있다는 문제가 있어, 이를 보완하기 위해 가중치 정규화(normalization)를 추가한 **Oja's Rule** 같은 변형 규칙들이 제안되었습니다.

## 🔗 관련 개념

-   [[ANN]]
-   [[Synaptic Plasticity]]
-   [[Unsupervised Learning]]
-   [[Hopfield Network]]: 연상 메모리(associative memory)를 구현한 모델로, Hebbian 규칙을 기반으로 패턴을 저장합니다.
