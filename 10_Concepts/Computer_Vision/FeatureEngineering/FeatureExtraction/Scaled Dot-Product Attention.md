좋습니다. **Attention의 실제 연산과정**을 **숫자를 넣어 구체적으로** 보여드릴게요.  
(간단한 **Self-Attention** 예제, 토큰 2개, 차원 2로 가정)

---

## ✅ **1. 준비: 입력 토큰 & 가중치 행렬**

- 입력 문장: **["I", "play"]**
    
- 각 단어의 임베딩 벡터 (예제용 단순 값):
    

$$
X = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$
- 가중치 행렬 (학습으로 얻어지는 파라미터):
    
$$
W_Q = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix},\ W_K = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix},\ W_V = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$
---

## ✅ **2. Query, Key, Value 계산**

$$Q = X W_Q,\quad K = X W_K,\quad V = X W_V
$$
대입하면:

$$
\begin{align}
Q &= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} 
\\
K &= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} 
\\
V &= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
\end{align}
$$
---

## ✅ **3. Attention Score (유사도 계산)**

$$
\begin{align}
\text{Scores} = Q K^T
\\
Q K^T = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}
\end{align}
$$
즉:

- 첫 번째 토큰("I")이 스스로에게 1, 두 번째 토큰("play")에게 0 점수
    
- 두 번째 토큰("play")이 "I"에게 1, 자기 자신에게 1 점수
    

---

## ✅ **4. 정규화 (Softmax)**

각 행(토큰별)으로 Softmax 적용:

- 1행: $\text{softmax}([1,0]) = [0.73,\ 0.27]$
    
- 2행: $\text{softmax}([1,1]) = [0.5,\ 0.5]$
    

$$
\text{Attention Weights} = \begin{bmatrix} 0.73 & 0.27 \\ 0.5 & 0.5 \end{bmatrix}
$$
---

## ✅ **5. 최종 출력 (Value 가중합)**

$$
\begin{align}
\text{Output} = \text{Attention Weights} \times V 
\\
\begin{bmatrix} 0.73 & 0.27 \\ 0.5 & 0.5 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0.73 & 0.27 \\ 0.5 & 0.5 \end{bmatrix}
\end{align}
$$
즉,

- 첫 번째 토큰의 최종 표현 = **자신(0.73) + "play"(0.27)** 정보가 섞임
    
- 두 번째 토큰의 최종 표현 = **자신(0.5) + "I"(0.5)** 정보가 섞임
    

---

## ✅ **직관 정리**

1. **Q, K** → "누구한테 얼마나 집중할지" 계산
    
2. **V** → 실제 내용을 가중합으로 가져와 새로운 표현 생성
    
3. 결과적으로, 토큰 간 정보가 상호 섞여 문맥이 반영됨
    

---

