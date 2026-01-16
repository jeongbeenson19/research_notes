
# **Stereo Rectification과 Q 행렬**

  

## **정의**

  

두 시점의 영상을 정사영 변환으로 재배치하여 에피폴라 선을 수평이도록 만드는 절차이다. 정렬 후 대응점 검색은 수평선상 1차원 문제로 축소되며, 시차 $d$를 통해 깊이 $Z$를 복원한다.

  

## **구성 요소**

  

입력: 내부 파라미터 $K_1,K_2$, 왜곡 계수, 상대 자세 $(R,\mathbf{t})$, 영상 크기

출력: 회전 $R_1,R_2$, 투영행렬 $P_1,P_2$, 재투영행렬 $Q$, 유효 영역 ROI

  

정렬 후 이상적 형태는

$$

P_1 = K_1,[R_1\mid \mathbf{0}],\quad

P_2 = K_2,[R_2\mid \mathbf{T}],\ \ \mathbf{T}=[T_x,0,0]^{\top}

$$

로, $T_x!=!-fB$가 되도록 선택하면 주Baseline이 $x$축 정렬이 되고 수평 시차 모델이 성립한다.

  

## **호모그래피 기반 정렬**

  

각 영상에 정사영 변환 $H_1,H_2$를 적용하여

$$

\tilde{\mathbf{x}}_1’ \sim H_1,\tilde{\mathbf{x}}_1,\quad

\tilde{\mathbf{x}}_2’ \sim H_2,\tilde{\mathbf{x}}_2

$$

정렬 후 에피폴라 선은 수평이 되며 시차는 $d=u_L’-u_R’$로 정의된다. 구현에서는 왜곡 보정과 정렬을 합성한 맵을 전계산한다(initUndistortRectifyMap).

  

## **Q 행렬(재투영 행렬)**

  

정렬된 투영행렬이

$$

P_1=

\begin{bmatrix}
f & 0 & c_x & 0\\
0 & f & c_y & 0\\
0 & 0 & 1 & 0
\end{bmatrix},
\quad
P_2=

\begin{bmatrix}

f & 0 & c_x’ & T_x\\

0 & f & c_y & 0\\

0 & 0 & 1 & 0

\end{bmatrix}

$$

일 때 OpenCV가 반환하는 $Q$는

$$

Q=

\begin{bmatrix}

1 & 0 & 0 & -c_x\\

0 & 1 & 0 & -c_y\\

0 & 0 & 0 & f\\

0 & 0 & -\tfrac{1}{T_x} & \tfrac{c_x-c_x’}{T_x}

\end{bmatrix}

$$

이다. 이를 통해 $(u,v,d)$로부터 $,[X\ Y\ Z\ W]^{\top}=Q,[u\ v\ d\ 1]^{\top}$ 를 얻고 $(X,Y,Z)=(X/W,Y/W,Z/W)$ 로 복원한다.

  

## **깊이/좌표 복원식**

  

$T_x=-fB$라면

$$

Z=\dfrac{fB}{d},\quad X=\dfrac{(u-c_x)Z}{f},\quad Y=\dfrac{(v-c_y)Z}{f}

$$

이 된다. 시차가 작을수록 깊이 추정은 잡음에 민감하며, $d\le 0$ 또는 미정합 영역은 무효로 처리한다.

  

## **파라미터 선택**

- CALIB_ZERO_DISPARITY: $c_x\approx c_x’$가 되도록 선택 → 좌영상 중심 기준 정렬
    
- alpha: 유효 시야 보존(>0) vs 크롭(0) 절충
    
- numDisparities, blockSize: 장면 스케일/텍스처에 맞게 조정
    

  

## **주의 사항**

- 베이스라인 $B$가 너무 짧으면 깊이 해상도 저하
    
- 순수 회전·평면 장면에서는 정렬 불안정
    
- 내부 보정 오차 및 왜곡 미보정은 $Q$와 깊이에 편향 유발
    

  

#MILAB #ComputerVision #Geometry #Rectification