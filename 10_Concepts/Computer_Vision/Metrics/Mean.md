
# **1) 정의 (표본:** $x_1,\dots,x_n>0$)

- **산술평균 (Arithmetic mean, AM)**
    
    $$\mathrm{AM}=\frac{1}{n}\sum_{i=1}^n x_i$$
    
- **기하평균 (Geometric mean, GM)**
    
    $$\mathrm{GM}=\Big(\prod_{i=1}^n x_i\Big)^{1/n} =\exp\!\Big(\frac{1}{n}\sum_{i=1}^n \ln x_i\Big)$$
    
- **조화평균 (Harmonic mean, HM)**
    
    $$\mathrm{HM}=\frac{n}{\sum_{i=1}^n \frac{1}{x_i}}$$
     ^6518f6
- **가중 평균(가중치** $w_i>0$**, 합** $\sum w_i$**)**
    
    $$\mathrm{AM}_w=\frac{\sum w_i x_i}{\sum w_i},\quad \mathrm{GM}_w=\exp\!\Big(\frac{\sum w_i\ln x_i}{\sum w_i}\Big),\quad \mathrm{HM}_w=\frac{\sum w_i}{\sum \frac{w_i}{x_i}}$$
    

  

# **2) 기본 관계(AM–GM–HM 부등식)**

  

$$\mathrm{AM}\;\ge\;\mathrm{GM}\;\ge\;\mathrm{HM}$$

- **동치 조건**: 세 평균이 모두 같아지는 **필요충분조건**은 $x_1=\dots=x_n$ (모두 동일).
    
- **역수 관계**:$$ \mathrm{HM}(x)=\frac{1}{\mathrm{AM}(1/x)}, \mathrm{GM}(1/x)=\frac{1}{\mathrm{GM}(x)}.$$
    
- **멱평균(Generalized mean)**: $$M_p=\Big(\frac1n\sum x_i^p\Big)^{1/p}.$$
    
    **순서성:** $$p>q\Rightarrow M_p\ge M_q.$$ 여기서 $M_1=\mathrm{AM},\; M_0=\mathrm{GM},\; M_{-1}=\mathrm{HM}.$
    

  

# **3) 해석과 쓰임**

- **AM**: _가산적 합산_ 에 자연스럽다. 독립 기여들의 평균, 선형 모델의 기대값, 오차의 평균 등.
    
- **GM**: _곱셈적 과정/비율_의 평균. 성장률(연복리), 비율들의 중앙 경향(로그 스케일 평균), 로그정규 분포 데이터에 적합.
    
    예) 연 수익률 $r_i → \mathrm{GM} of (1+r_i) − 1$이 “평균 수익률”.
    
- **HM**: _율/속도_ 평균(공통 분모가 고정) 또는 조화적 결합.
    
    예) **고정거리** 두 구간의 평균속도, **F1-score**($2PR/(P+R)$), 병렬 저항.
    

  

# **4) 예시 계산**

- 데이터 [2,8]
    
    - $\mathrm{AM}=\frac{2+8}{2}=5$
        
    - $\mathrm{GM}=\sqrt{2\cdot8}=\sqrt{16}=4$
        
    - $\mathrm{HM}=\frac{2}{\frac12+\frac18}=\frac{2}{0.625}=3.2$
        
        → 분산이 있을수록 $\mathrm{AM}\ge\mathrm{GM}\ge\mathrm{HM}$ 간격이 벌어진다.
        
    
- 데이터 [1,1,9]
    
    - $\mathrm{AM}=\frac{11}{3}\approx 3.6667$
        
    - $\mathrm{GM}=\sqrt[3]{9}\approx 2.0801$
        
    - $\mathrm{HM}=\frac{3}{1+1+\frac19}=\frac{3}{\frac{19}{9}}=\frac{27}{19}\approx 1.4211$
        
    

  

# **5) 성질 및 주의점**

- **스케일 변환**: c>0일 때
    
    $\mathrm{AM}(cx)=c\,\mathrm{AM}(x), \mathrm{GM}(cx)=c\,\mathrm{GM}(x), \mathrm{HM}(cx)=c\,\mathrm{HM}(x).$
    
    (AM은 **이동 불변**: $\mathrm{AM}(x+a)=\mathrm{AM}(x)+a$. GM/HM은 이동 불변이 아님.)
    
- **영(0)/음수 포함 시**:
    
    - AM: 제약 없음.
        
    - GM: 어떤 $x_i=0$이면 $GM=0$. 음수 섞이면 일반적으로 실수영역에서 정의 불가(로그/루트 문제).
        
    - HM: $x_i=0$이면 정의 불가(분모 0), 음수도 보통 배제.
        
    
- **변동성 민감도**: 같은 평균이라도 분산이 클수록 $\mathrm{AM}-\mathrm{GM}, \mathrm{GM}-\mathrm{HM}$ 차이가 커진다(불균형에 HM이 가장 민감).
    

  

# **6) 부등식 간단 증명 스케치**

- **AM**  $\ge$ **GM (n=2)**: $$(\sqrt{x}-\sqrt{y})^2\ge 0 \Rightarrow x+y \ge 2\sqrt{xy}\Rightarrow \frac{x+y}{2}\ge\sqrt{xy}$$
    
    n>2는 **Jensen(볼록성)** 또는 **귀납**으로 일반화.
    
- **GM** $\ge$ **HM**: 역수에 대해 $AM\ge GM$을 적용하면
    
    $$\frac{1}{\mathrm{HM}}=\mathrm{AM}(1/x)\ge \mathrm{GM}(1/x)=\frac{1}{\mathrm{GM}}\Rightarrow \mathrm{GM}\ge \mathrm{HM}.$$
    

  

# **7) 언제 무엇을 써야 하나 (실전 규칙)**

- **합을 나누는 평균**(점수 평균, 지출 평균 등): **AM**.
    
- **곱셈적 효과/성장률**(연복리 수익률, 배수형 개선율, 스케일 비율): **GM**.
    
    예) +10\% 후 -10\% →$\mathrm{GM}(1.1,0.9)=\sqrt{0.99}\approx 0.99499$ ⇒ **평균 수익률 약** -0.501\%.
    
- **고정 분모의 율/속도**(동일 거리의 구간 속도 평균, 비율의 조화): **HM**.
    
    예) 100km씩 두 구간, $60\text{ km/h}와 120\text{ km/h}$ → 평균속도
    
    $\mathrm{HM}= \frac{2}{\frac{1}{60}+\frac{1}{120}}=80\text{ km/h}.$
    
- **정밀도–재현율 통합**: $F_1=\frac{2PR}{P+R}$ (P와 R의 HM).
    
    예) $P=0.9, R=0.6\Rightarrow F_1=\frac{2\cdot0.9\cdot0.6}{0.9+0.6}=0.72.$
    

  

# **8) 요약 표**

| **평균** | **수식**                 | **해석/용도**      | **정의역(일반적)** |
| ------ | ---------------------- | -------------- | ------------ |
| AM     | $\frac{1}{n}\sum x_i$  | 가산적 평균, 기대값    | 실수 전체        |
| GM     | $(\prod x_i)^{1/n}$    | 곱셈/비율 평균, 로그평균 | $x_i>0$      |
| HM     | $\frac{n}{\sum 1/x_i}$ | 율/속도 평균, 공통분모  | $x_i>0$      |

필요하면, 특정 데이터셋으로 세 평균을 계산해 비교(분산·왜도와의 관계 포함)까지 보여드리겠습니다.