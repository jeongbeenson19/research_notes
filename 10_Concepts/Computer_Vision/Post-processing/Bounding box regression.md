
RCNN 논문의 **부록 C (Appendix C)** 에서는 **Bounding Box Regression** 기법에 대해 설명합니다. 이 기법은 객체 탐지에서 **보다 정확한 바운딩 박스 위치를 예측**하기 위해 사용되며, RCNN의 성능을 높이는 데 중요한 역할을 합니다. 아래에 부록 C의 내용을 바탕으로 기계적이고 분석적으로 설명하겠습니다.

---

## **📌 Bounding Box Regression이 필요한 이유**

  

R-CNN은 처음에 Selective Search와 같은 Region Proposal 기법을 이용해 후보 바운딩 박스를 생성합니다. 하지만 이 바운딩 박스들은 **객체의 위치를 정확히 감싸지 못하는 경우가 많고**, **IoU가 낮은 경계 상자**도 포함됩니다.

  

이를 보완하기 위해 RCNN은 **CNN 특징 벡터를 기반으로 바운딩 박스 위치를 조정하는 회귀 모델**을 학습합니다. 이게 바로 **Bounding Box Regression**입니다.

---

## **🔢 수식 정리**


RCNN에서는 바운딩 박스의 위치를 조정하기 위해 다음과 같은 **좌표 변환 함수**를 정의합니다.

### **입력:**

- 바운딩 박스 proposal:
    
    $$P = (P_x, P_y, P_w, P_h)$$
    
    - 중심 좌표 $(P_x, P_y)$, 너비 $P_w$, 높이 $P_h$
        
    
- Ground-truth 박스:
    
    $$G = (G_x, G_y, G_w, G_h)$$
    

---

### **회귀 대상(정답 타겟) 정의:**

  

$$\begin{aligned} t_x &= \frac{G_x - P_x}{P_w}, \\ t_y &= \frac{G_y - P_y}{P_h}, \\ t_w &= \log \left(\frac{G_w}{P_w} \right), \\ t_h &= \log \left(\frac{G_h}{P_h} \right) \end{aligned}$$

  

이러한 방식으로 변환하면 **bounding box regression이 scale invariant**하도록 만들어줍니다.

- $P$: 원래 proposal (예측하려는 초기 박스)
    
- $G$: ground truth (정답 박스)
    
#### **🔍 각 회귀 타겟의 의미**

| **기호** | **의미**                                                    | **직관적 해석**                         |
| ------ | --------------------------------------------------------- | ---------------------------------- |
| $t_x$  | 정답 중심 x좌표가 proposal 중심 x보다 얼마나 **좌우로 이동**해야 하는가 (너비로 정규화) | “박스 중심이 얼마나 좌우로 치우쳐 있는가?”          |
| $t_y$  | 정답 중심 y좌표가 proposal 중심 y보다 얼마나 **상하로 이동**해야 하는가 (높이로 정규화) | “박스 중심이 얼마나 위아래로 어긋나 있는가?”         |
| $t_w$  | 정답 박스의 너비가 proposal보다 **얼마나 더 크거나 작은가** (로그 스케일)          | “박스의 너비가 얼마나 **늘어나거나 줄어들어야** 하는가?” |
| $t_h$  | 정답 박스의 높이가 proposal보다 얼마나 더 크거나 작은가 (로그 스케일)              | “박스의 높이가 얼마나 **늘어나거나 줄어들어야** 하는가?” |

---

## **🧠 왜 이런 방식으로 정의했는가?**

1. $t_x, t_y:$
    
    - 절대 위치 차이를 쓰지 않고, **proposal 박스의 크기로 정규화**해서 scale-invariant 하게 학습하도록 유도.
        
    - 작은 객체든 큰 객체든 학습이 일관되게 진행됨.
        
    
2. $t_w, t_h:$
    
    - 너비나 높이 차이를 단순히 빼는 게 아니라 **비율의 로그값**을 사용.
        
    - 이는 크기의 차이를 비율로 표현하여, **곱셈적인 변화(확대/축소)** 를 **덧셈적인 회귀 문제로 변환**하기 위함.
        
    

---

### **학습 대상 함수:**

  

이제 CNN 특징 벡터 $\phi(P)$를 입력으로 받고, 각각의 클래스 c에 대해 회귀기를 학습합니다.

  

$$f_c(\phi(P)) = (\hat{t}_x, \hat{t}_y, \hat{t}_w, \hat{t}_h)$$

  

회귀 손실 함수는 간단한 **L2 loss (squared error loss)** 를 사용합니다:

  

$$L = \sum_{i=1}^{N} \| t^{(i)} - f_c(\phi(P^{(i)})) \|^2$$

  

여기서:

- $t^{(i)}$는 정답 회귀 타겟
    
- $f_c(\phi(P^{(i)}))$는 예측값
    
- N은 학습 샘플 수
    

---

### **테스트 시 박스 보정:**

  

테스트 단계에서는 예측된 회귀값 $(\hat{t}_x, \hat{t}_y, \hat{t}_w, \hat{t}_h)$을 사용해 원래 proposal 박스 P를 보정하여 최종 박스 $\hat{G}$를 만듭니다.

  

$$\begin{aligned} \hat{G}_x &= \hat{t}_x \cdot P_w + P_x \\ \hat{G}_y &= \hat{t}_y \cdot P_h + P_y \\ \hat{G}_w &= \exp(\hat{t}_w) \cdot P_w \\ \hat{G}_h &= \exp(\hat{t}_h) \cdot P_h \end{aligned}$$

  

이렇게 변환된 $\hat{G}$가 최종 bounding box입니다.

---

## **📌 정리: Bounding Box Regression의 특징**

| **항목** | **설명**                                             |
| ------ | -------------------------------------------------- |
| 목적     | Proposal box의 위치 및 크기 보정                           |
| 회귀 대상  | 중심 좌표 차이 (정규화됨) + 로그 스케일 크기 차이                     |
| 입력     | CNN feature vector                                 |
| 출력     | 보정값 $(\hat{t}_x, \hat{t}_y, \hat{t}_w, \hat{t}_h)$ |
| 손실 함수  | L2 loss                                            |
| 장점     | 바운딩 박스 정밀도 개선, mAP 향상                              |

---

## **🧠 옵시디언 카테고리 제안**

  

이 개념은 다음 카테고리에 적합합니다:

```
MILAB
└── Computer Vision
    └── Object Detection
        └── Feature Engineering
            └── Bounding Box Regression.md
```

또는 좀 더 분석적으로 분리하려면 다음과 같은 신규 폴더 제안도 가능합니다:

```
MILAB
└── Computer Vision
    └── Object Detection
        └── Post-processing
            └── Bounding Box Regression.md
```

---

필요하면 LaTeX 수식 기반 문서 형태나 슬라이드용 요약도 만들어줄 수 있습니다.