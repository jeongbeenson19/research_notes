
# **Epipolar Geometry**

  

## **정의**

  

두 시점(카메라) 사이의 기하학적 제약으로, 한 영상의 점이 다른 영상에서 위치할 수 있는 후보가 **에피폴라 선(epipolar line)** 으로 제한되는 현상을 말한다. 두 카메라 중심을 잇는 선분을 **베이스라인**이라 하고, 한 카메라 중심이 다른 카메라 영상 평면에 투영된 점을 **에피폴(epipole)** 이라 한다.

  

## **핵심 구조**

- 에피폴라 평면: 한 3D 점과 두 카메라 중심이 이루는 평면.
    
- 에피폴라 선: 에피폴라 평면이 영상 평면과 만나는 직선.
    
- 에피폴: 모든 에피폴라 선이 지나는 교점.
    
- 제약: 한 영상의 점 $\tilde{\mathbf{x}}_1$ 에 대응하는 다른 영상의 점 $\tilde{\mathbf{x}}_2$ 는 반드시 에피폴라 선 위에 있다.
    

  

## **에피폴라 제약식**

  

$$

\tilde{\mathbf{x}}_2^{\top},\mathbf{F},\tilde{\mathbf{x}}_1=0

$$

여기서 $\mathbf{F}$ 는 **기본행렬(Fundamental matrix)**, $\tilde{\mathbf{x}}=[u,v,1]^{\top}$ 는 동차 픽셀 좌표이다. 에피폴라 선은

$$

\boldsymbol{\ell}_2=\mathbf{F},\tilde{\mathbf{x}}_1,\qquad

\boldsymbol{\ell}_1=\mathbf{F}^{\top},\tilde{\mathbf{x}}_2

$$

로 주어진다.

  

## **기본행렬 $\mathbf{F}$ 의 성질**

- 크기: $3\times 3$, 스케일까지 정의(동차).
    
- 랭크 제약: $\mathrm{rank}(\mathbf{F})=2$ 이며 $\det(\mathbf{F})=0$.
    
- 에피폴: $\mathbf{F},\tilde{\mathbf{e}}_1=\mathbf{0}$, $\mathbf{F}^{\top},\tilde{\mathbf{e}}_2=\mathbf{0}$.
    
- 정규화 좌표(내부 보정 후)가 아니어도 정의되며, 카메라 내부 파라미터를 포함한다.
    

  

## **본질행렬 $\mathbf{E}$ 와 정규화 좌표**

  

내부 보정으로 정규화 좌표 $\mathbf{x}_i=K_i^{-1}\tilde{\mathbf{x}}_i$ 를 사용하면

$$

\mathbf{x}_2^{\top},\mathbf{E},\mathbf{x}1=0,\qquad_
\mathbf{E}=[\mathbf{t}]{\times}\mathbf{R}

$$_

_여기서 $\mathbf{R},\mathbf{t}$ 는 두 시점 사이의 회전과 병진, $[\mathbf{t}]_{\times}$ 는 $\mathbf{t}$ 의 외적 행렬이다. $\mathbf{F}$ 와 $\mathbf{E}$ 의 관계는

$$

\mathbf{F}=K_2^{-\top},\mathbf{E},K_1^{-1}

$$

이다. $\mathbf{E}$ 는 특이값 두 개가 같고 하나는 0 이어야 하며(스케일 정규화 시 $\mathrm{diag}(1,1,0)$), $\mathrm{rank}(\mathbf{E})=2$ 이다.

  

## **추정(8점/7점)과 정규화**

- 8점 알고리즘: 최소 8쌍 대응점으로 선형 추정 후 $\mathrm{rank}=2$ 제약 투영, 필요 시 비선형 미세조정.
    
- 7점 알고리즘: 7쌍으로 다항 방정식 해.
    
- 수치 안정성: 좌표를 평균 원점, 평균 거리 $\sqrt{2}$ 로 **하틀리 정규화** 후 추정.
    
- 외란 제거: RANSAC 으로 오정합(outlier) 억제.
    

  

## **오차 척도(샘프슨 거리)**

  

알gebraic 잔차의 일차 근사로 **Sampson distance** 를 사용한다.

$$

d_S(\tilde{\mathbf{x}}_1,\tilde{\mathbf{x}}_2)=

\frac{\big(\tilde{\mathbf{x}}_2^{\top}\mathbf{F}\tilde{\mathbf{x}}_1\big)^2}

{(\mathbf{F}\tilde{\mathbf{x}}_1)_1^2+(\mathbf{F}\tilde{\mathbf{x}}_1)_2^2+(\mathbf{F}^{\top}\tilde{\mathbf{x}}_2)_1^2+(\mathbf{F}^{\top}\tilde{\mathbf{x}}_2)_2^2}

$$

  

## **$\mathbf{E}$ 분해와 포즈 복원**

  

$\mathbf{E}=U,\mathrm{diag}(1,1,0),V^{\top}$ (SVD, 특이값 보정 후) 라 하면

$$

\mathbf{W}=

\begin{bmatrix}

0&-1&0\

1&\ \ 0&0\

0&\ \ 0&1

\end{bmatrix}

$$

두 후보 회전과 병진(방향)은

$$

\mathbf{R}_1=U\mathbf{W}V^{\top},\quad \mathbf{R}_2=U\mathbf{W}^{\top}V^{\top},\quad
\mathbf{t}_{\pm}=\pm,U[:,3]

$$

으로 네 가지 조합이 나온다. **체리얼리티(cheirality) 검사**로 삼각측량한 점들의 깊이 $Z>0$ 개수가 최대인 조합을 선택한다. $|\mathbf{t}|$ 은 스케일 모호성으로 결정되지 않는다.

  

## **삼각측량 및 검증**

  

정규화 좌표로 $P_1=[I\mid\mathbf{0}]$, $P_2=[\mathbf{R}\mid\mathbf{t}]$ 를 구성하고

$$

\mathbf{X}=\arg\min_{\mathbf{X}}\sum_{i=1}^{2}\big|\mathbf{x}_i-\pi(P_i,\mathbf{X})\big|^2

$$

을 최소화(선형 DLT 초기화, 비선형 재투영 최소화)하여 3D 점을 추정한다. 선택된 $(\mathbf{R},\mathbf{t})$ 에 대해 양의 깊이 조건을 확인한다.

  

## **퇴화 상황과 주의점**

- 순수 회전($\mathbf{t}\approx \mathbf{0}$): 시차가 없으므로 $\mathbf{E}$ 미정.
    
- 거의 평면 장면: 호모그래피가 우세하여 $\mathbf{F}/\mathbf{E}$ 추정 불안정.
    
- 베이스라인이 너무 짧음: 수치적 조건수 악화, 깊이 분해능 저하.
    
- 내부 보정 오차: $\mathbf{E}$ 품질 저하 → 반드시 왜곡 보정 및 정확한 $K$ 사용.
    

  

## **정렬(rectification)과의 연결**

  

$(K_1,K_2,\mathbf{R},\mathbf{t})$ 가 주어지면 스테레오 정렬로 에피폴라 선을 수평으로 만들 수 있고, 이후 **시차 $d$** 만으로 깊이 $Z$ 를 계산한다.

  

#ComputerVision #Geometry