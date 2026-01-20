---
tags:
  - MILAB
  - ComputerVision
  - ObjectDetection
---

# Fast R-CNN

## 1. 개요 (Overview)

| 항목      | 설명                                                          |     |
| ------- | ----------------------------------------------------------- | --- |
| **이름**  | **Fast R-CNN**                                              |     |
| **발표**  | ICCV 2015                                                   |     |
| **제안자** | Ross Girshick (R-CNN 제안자)                                   |     |
| **논문**  | [[30_Architectures/ObjectDetection/Fast R-CNN|Fast R-CNN]] |     |
| **핵심**  | **RoI Pooling**과 **End-to-End 학습 가능한 통합 파이프라인**             |     |

---

## 2. 등장 배경: 이전 모델의 한계

### 2.1. R-CNN의 한계

| 문제점 | 설명 |
| --- | --- |
| **느린 속도** | 약 2,000개의 후보 영역(Region Proposal) 각각에 대해 **독립적인 CNN Forward Pass를 수행**하여 극심한 연산 중복 발생. |
| **복잡한 학습 과정** | **3단계 파이프라인** (CNN Fine-tuning, SVM 분류기 학습, BBox Regressor 학습)으로 분리되어 있어 학습이 복잡하고 비효율적. |
| **최적화의 어려움** | End-to-End 학습이 불가능하여 전체 파이프라인을 한 번에 최적화할 수 없음. |

### 2.2. SPPNet의 한계

- **CNN 연산 공유**: 이미지 전체에 대해 CNN을 한 번만 수행하여 속도를 개선.
- **남아있는 문제**: SPP(Spatial Pyramid Pooling) 레이어 이전의 컨볼루션 레이어들은 가중치가 업데이트되지 않아, **네트워크 전체를 End-to-End로 학습시키지 못하는 한계**가 여전히 존재.

---

## 3. 핵심 아이디어

Fast R-CNN은 **R-CNN의 정확도**와 **SPPNet의 속도**라는 장점들을 결합하고, 학습 과정을 통합하여 객체 탐지 모델의 패러다임을 바꿨습니다.

1.  **CNN 피쳐맵 공유**: SPPNet과 같이, 이미지 전체에 대해 CNN을 단 한 번만 수행하여 피쳐맵을 계산하고 이를 공유.
2.  **RoI Pooling Layer**: SPP 레이어를 간소화 및 개선하여, 전체 네트워크의 End-to-End 학습을 가능하게 함.
3.  **통합된 학습 파이프라인**: 분류기(Classifier)와 경계 상자 회귀(Bounding Box Regressor)를 하나의 네트워크 안에서 **Multi-task Loss**로 동시에 학습.

---

## 4. 네트워크 아키텍처

### 4.1. 전체 프로세스

1.  **입력**: 전체 이미지 1장과 해당 이미지에 대한 후보 영역(RoI)들의 리스트를 입력받습니다.
2.  **컨볼루션 피쳐맵 생성**: 이미지를 CNN에 통과시켜 전체 이미지에 대한 피쳐맵을 생성합니다. (예: VGG16의 마지막 컨볼루션 레이어까지)
3.  **RoI Pooling**: 각 RoI에 대해, **RoI Pooling 레이어**가 피쳐맵의 해당 영역에서 **고정된 크기(예: 7x7)의 특징 벡터**를 추출합니다.
4.  **분류 및 위치 보정**: 고정 크기 특징 벡터는 FC 레이어들을 거친 후, 최종적으로 두 개의 브랜치로 나뉩니다.
    -   **Softmax Classifier**: (K개의 객체 클래스 + 1개의 배경)에 대한 확률을 예측합니다.
    -   **Bounding Box Regressor**: 각 RoI의 위치를 정교하게 보정할 값을 예측합니다.

### 4.2. RoI Pooling 상세 설명

> **RoI Pooling**은 서로 다른 크기의 RoI들로부터 고정된 크기의 특징을 추출하여 FC 레이어에 연결할 수 있도록 하는 핵심적인 요소입니다. 동작 과정은 다음과 같습니다.
> 
> 1.  **RoI Projection**: 원본 이미지 좌표계의 RoI를 CNN 피쳐맵의 좌표계로 투영(projection)합니다.
> 2.  **Grid 분할**: 투영된 RoI 영역을 목표하는 출력 크기(예: 7x7)와 동일한 개수의 그리드(sub-window)로 나눕니다.
> 3.  **Max Pooling**: 각 그리드 셀 내부에서 가장 큰 값을 뽑는 Max Pooling을 수행합니다.
> 4.  **결과**: 이 과정을 거치면, 원본 RoI의 크기와 상관없이 항상 고정된 크기(예: 7x7)의 피쳐맵이 출력됩니다.

---

## 5. 손실 함수 (Multi-task Loss)

Fast R-CNN은 **분류(Classification)** 와 **위치 회귀(Localization)** 라는 두 가지 작업을 동시에 수행하기 위해 Multi-task Loss를 사용합니다.

$$ L(p, u, t^u, v) = L_{\text{cls}}(p, u) + \lambda [u \ge 1] L_{\text{loc}}(t^u, v) $$

> 각 항에 대한 상세 설명은 다음과 같습니다.
> 
> - $L_{\text{cls}}(p, u) = - \log p_u$
>   - **분류 손실 (Log Loss)** 입니다.
>   - $u$는 실제 정답 클래스이며, $p_u$는 모델이 예측한 클래스 $u$에 대한 Softmax 확률입니다.
> 
> - $\lambda [u \ge 1] L_{\text{loc}}(t^u, v)$
>   - **위치 회귀 손실 (Localization Loss)** 입니다.
>   - **Iverson bracket `[u ≥ 1]`**: 이 부분은 **RoI가 배경(background, u=0)이 아닐 경우에만 위치 손실을 계산**하라는 의미입니다. 배경에 대해서는 위치를 보정할 필요가 없기 때문입니다. $\lambda$는 두 손실 간의 가중치를 조절하는 하이퍼파라미터입니다. (논문에서는 1로 설정)
>   - $L_{\text{loc}}$는 예측된 경계 상자 $t^u$와 실제 정답 경계 상자 $v$ 간의 차이를 계산하며, 일반적으로 **Smooth L1 Loss**가 사용됩니다.

#### Smooth L1 Loss란?
> $$ \text{smooth}_{L_1}(x) = 
\begin{cases} 
0.5x^2 & \text{if } |x| < 1 \\|x| - 0.5 & \text{otherwise} 
\end{cases} $$
> L2 Loss보다 outlier에 덜 민감하고, L1 Loss보다 0 근처에서 미분이 부드러워 학습을 안정시키는 장점이 있습니다.

---

## 6. 성능 및 의의

- **속도와 정확도 동시 달성**: R-CNN 대비 **학습은 9배, 추론은 213배** 빨라졌으며, mAP 또한 약 66% (PASCAL VOC07 기준)로 향상되었습니다.
- **End-to-End 학습의 실현**: 복잡했던 학습 파이프라인을 **하나의 네트워크로 통합**하여 학습과 최적화를 간결하게 만들었습니다.
- **실용성의 증대**: 딥러닝 기반 객체 탐지 모델의 실용성을 크게 높여, 후속 연구들의 기반이 되었습니다.

---

## 7. 한계점

- **후보 영역 생성의 병목**: Fast R-CNN의 추론 과정 자체는 매우 빨라졌지만, 여전히 CPU에서 동작하는 **Selective Search** 알고리즘으로 후보 영역을 생성하는 부분이 전체 속도의 병목으로 남았습니다.
- 이 문제는 후속 모델인 **[[30_Architectures/ObjectDetection/Faster R-CNN|Faster R-CNN]]** 에서 **Region Proposal Network(RPN)** 를 도입하여 해결됩니다.