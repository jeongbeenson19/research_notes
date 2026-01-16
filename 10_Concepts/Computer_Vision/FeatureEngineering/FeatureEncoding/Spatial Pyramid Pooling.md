
# **개념 정의**

- **SPP**는 마지막 합성곱(Conv) 특성맵 위에서 **다중 해상도 격자(예: 1×1, 2×2, 4×4 …)** 로 공간을 분할해 **각 격자별 풀링(보통 max-pooling)** 을 수행하고, 모든 수준의 풀링 결과를 **연결(concatenate)** 하여 **입력 크기와 무관한 고정 길이 벡터**를 출력하는 모듈입니다. SPP는 **가변 크기 입력**을 처리하면서 **FC 층에 고정 길이 입력을 공급**할 수 있게 만들어줍니다. 
    

  

# **동기(왜 필요한가)**

1. 고전 CNN은 FC층 때문에 **고정 입력 크기(예: 224×224)** 를 요구 → 강제 리사이즈/워핑으로 **왜곡** 및 정확도 저하 가능.
    
2. 물체 탐지에서 **많은 RoI/윈도우**에 대해 매번 Conv를 반복 계산하면 비효율적.
    
    → SPP는 **입력 크기 제약 해제** + **Conv를 한 번만 계산**하고 다양한 영역에서 **고정 길이 기술자**를 추출할 수 있게 합니다. 
    

  

# **동작 원리(정의역·치역, 차원)**

- 입력: 마지막 Conv 특성맵 $\mathbf{F} \in \mathbb{R}^{C \times H \times W}$
    
- 수준(level) 집합: $\mathcal{L}=\{n_1, n_2, \dots\}$ (예: $\{1,2,4\}$)
    
- 각 수준 $n$에 대해 특성맵을 $n \times n$ **균등 격자**로 나누고, 각 격자 셀에서 채널별 풀링을 수행:
    
    $$\text{pool}{n,i,j}(c)=\text{pool}\big(\mathbf{F}{c}[\,\text{cell}(n,i,j)\,]\big)$$
    
- 출력: 모든 수준·셀의 결과를 **연결**
    
    $$\mathbf{z}=\bigoplus_{n\in\mathcal{L}}\;\bigoplus_{i=1}^{n}\;\bigoplus_{j=1}^{n}\;\text{pool}{n,i,j} \in \mathbb{R}^{C\cdot \sum{n\in\mathcal{L}} n^2}$$
    
    즉, 출력 차원 = $C \times \left(\sum_{n\in\mathcal{L}} n^2\right)$. 예를 들어 $C=256$, $\mathcal{L}=\{1,2,4\}$면 길이는 $256 \times (1+4+16)=256 \times 21$. (논문은 **max-pooling**을 기본 사용) 
    

  

> 구현 시 **격자 경계**는 (H,W)가 n으로 나누어떨어지지 않아도 되며, **적응형(adaptive) 풀링**처럼 **floor/ceil로 경계 보정**하여 전체 영역을 빈틈없이 분할합니다. (PyTorch `Adaptive{Avg,Max}Pool2d`와 동일 개념) 

  

# **표준 풀링과의 차이**

- **일반 풀링**: 고정 커널/스트라이드로 전체 공간을 균일 축소 → 출력 크기는 입력 크기에 종속.
    
- **SPP**: “**출력 격자 수**(각 수준의 $n \times n$)를 먼저 고정” → **입력 크기가 달라도** 항상 동일 길이의 벡터가 생성. **다중 수준**을 통해 전역(1×1)~지역(4×4, 7×7 …) 공간 정보를 동시에 보존. 
    

  

# **RoI Pooling/Align과의 관계**

- **SPP(전역/영역 일반화)**: 전체 특성맵(또는 임의의 서브영역)에 대해 n\times n 격자 풀링으로 **고정 길이**를 만듦.
    
- **RoI Pooling(Fast R-CNN)**: 주어진 **RoI**를 $H_{\text{out}}\times W_{\text{out}}$ 그리드로 나눠 풀링 → **RoI별 고정 크기 특징**. SPP의 **영역 한정 버전**으로 볼 수 있음. (후속인 RoI Align은 양자화 오차 제거) 
    

  

# **탐지 파이프라인에서의 이점(SPP-net)**

- **Conv를 전체 이미지에 한 번만 계산** 후, 많은 후보 영역에 대해 **SPP만 수행** → R-CNN 대비 **수십 배 속도 향상(24–102×)** 보고.
    
- 입력을 고정 크기로 워핑하지 않아 **정확도** 개선. 
    

  

# **구현 팁(PyTorch 관점)**

- 실제 코드는 보통 **AdaptiveMaxPool2d**(또는 Avg)로 각 수준을 구현하고 torch.cat으로 이어 붙입니다. (간단·미분 가능)
    
- 의사코드:
    
    1. levels = $[1, 2, 4]$
        
    2. pooled = `[AdaptiveMaxPool2d((n,n))(F) for n in levels]`  # (N,C,n,n)
        
    3. feat = `torch.cat([p.flatten(2) for p in pooled], dim=2)`  # (N,C, Σ n^2)
        
    4. feat = `feat.transpose(1,2).flatten(1)` 또는 $(N, C*Σ n^2)$로 정렬
        
    
- **메모리/속도**: 수준 수와 최대 n이 커질수록 $C\cdot \sum n^2$가 커져 FC 파라미터가 증가. 필요한 수준만 선택. 
    

  

# **장점·제약**

  

**장점**

- 가변 크기 입력 처리, 공간적 맥락의 다중 규모 보존, 탐지에서의 효율성 개선. 
    
    **제약**
    
- 출력 차원 증가(FC 부담↑), 격자 분할이 **하드 파티셔닝**이라 경계 근처 정보가 덜 매끄럽게 통합될 수 있음(후속 연구에서 RoI Align 등으로 보완). 
    

  

# **관련/혼동 주의**

- **GAP(Global Avg Pooling)**: 1×1 한 수준만 사용하는 SPP의 특수한 경우로 볼 수 있으나, 다중 수준의 **피라미드 맥락**은 제공하지 않음.
    
- **ASPP(Atrous SPP, DeepLab 계열)**: **팽창(공차) 합성곱**의 다중 수용영역을 병렬 적용하는 **다른 기법**으로, SPP의 “격자 풀링”과는 **연산적 성질이 다름**(이름만 유사).
    
    (참고: SPP는 풀링 기반, ASPP는 dilated conv 기반)
    

---

## **옵시디언 문서 카테고리 제안**

  

가장 적합:

- **Computer Vision / Feature Engineering / Feature Encoding / Spatial Pyramid Pooling**
    

  

교차 링크 권장:

- Computer Vision / Networks / Object Detection / Fast R-CNN (RoI Pooling 맥락)
    
- Computer Vision / Networks / Foundational (Pooling 계열 요약)
    

---

### **참고 문헌**

- He et al., _Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition_, ECCV 2014 / arXiv:1406.4729. 
    
- Girshick, _Fast R-CNN_, ICCV 2015 / arXiv:1504.08083. (RoI Pooling) 
    
- PyTorch Docs: Adaptive{Avg,Max}Pool2d (SPP 구현에 활용되는 적응형 풀링 메커니즘) 
    

  

필요하시다면 **간단한 PyTorch SPP 모듈 코드**도 바로 작성해드리겠습니다.