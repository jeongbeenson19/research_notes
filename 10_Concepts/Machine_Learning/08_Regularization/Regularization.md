
## L2 Regularization

$$
C = C_0 + \frac{\lambda}{2n}\sum_w w^2
$$

- $C_0$ = cost function
- $n$ = 훈련 데이터의 개수
- $\lambda$ = regularization 변수
- $w$ = 가중치

위 식처럼 regularization 항목이 들어가면, 학습의 방향이 단순하게 $C_0$ 값이 작아지는 방향으로만 진행되는 것이 아니라,
$w$ 값들 역시 최소가 되는 방향으로 진행하게 된다
이렇게 정의된 cost function을 가중치 $w$에 대해서 편미분을 수행하면, 결과적으로는 새로운 가중치는 아래와 같이 결정된다.
$$
\begin{align}
w &\rightarrow w - \eta\frac{\partial C_0}{\partial w} - \frac{\eta \lambda}{n}w \\
  &= \left( 1 - \frac{\eta \lambda}{n} \right) w - \eta \frac{\partial C_0}{\partial w}
\end{align}
$$

## L1 Regularization

$$
C = C_0 + \frac{\lambda}{n}\sum_w |w|
$$
가중치 $w$에 대해서 편미분을 수행하여 결정되는 가중치
$$
w \rightarrow w' = w - \frac{\eta \lambda}{n}\text{sgn}(w) - \frac{\partial C_0}{\partial w}
$$

L1 regularization은 통상적으로 상숫값을 빼주게 되어 있으므로 작은 가중치들은 거의 0으로 수렴이  되어, 몇 개의 중요한 가중치들만 남게 된다. 그러므로 몇 개의 의미 있는 값을 끄집어내고 싶은 경우에는 L1 regularization이 효과적이기 때문에 “sparse model(희소한 모델)”에 적합하다. 
단, 기본 수식에서도 알 수 있듯이 미분할 수 없는 점이 있으므로 gradient-based learning에 적용할  때는 주의가 필요하다.
Regularization은 그 개념을 정확히 이해하는 것이 중요하기 때문에, 되도록 수식을 배제하고자 하였으나, L1과 L2 regularization의 차이를 설명하고, 개념 이해를 위해 일부 수식을 사용하였다.

| 항목    | L1 정규화 (Lasso)              | L2 정규화 (Ridge)            |
| ----- | --------------------------- | ------------------------- |
| 규제항   | $\sum^n_{j=1} \|\theta_j\|$ | $\sum^n_{j=1} \theta^2_j$ |
| 영향    | 일부 가중치를 0으로 만듦              | 모든 가중치를 작게 만듦             |
| 특성 선택 | 가능 (희소한 해)                  | 불가능                       |
| 최적화   | 절댓값으로 인해 미분 불가능한 지점 있음      | 매끄럽고 미분 가능                |
| 사용 상황 | 특성이 많은 경우, 해석이 중요할 때        | 다중공선성 문제 해결 등             |
