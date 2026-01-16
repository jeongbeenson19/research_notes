# Backpropagation

## 한줄 요약
오차를 출력층에서 입력층 방향으로 전달하며 각 층의 기울기를 계산해 가중치를 업데이트하는 알고리즘.

## 핵심 개념
- 연쇄 법칙을 이용해 손실 함수의 기울기를 효율적으로 계산
- 순전파로 예측과 손실을 계산하고, 역전파로 각 파라미터의 gradient를 산출
- 실제 업데이트는 보통 [[Gradient Descent]] 계열 최적화로 수행
- 활성화 함수와 깊이에 따라 [[Vanishing Gradient Problem]] 발생 가능

## 기본 절차
1. 순전파로 예측과 손실 계산
2. 출력층에서 오차(gradient) 계산
3. 은닉층으로 gradient 전파
4. 각 파라미터 업데이트

## 대표 수식
- 손실 함수 L에 대해 
  - 출력층: dL/dz = dL/dy * dy/dz
  - 가중치: dL/dW = dL/dz * dz/dW
- 일반적으로 체인 룰을 반복 적용해 각 층의 gradient를 구함

## 예시
- MLP 분류: [[Cross-Entropy Loss]] + [[Softmax]]를 사용해 출력층 gradient 계산
- 회귀: [[Mean Squared Error]]로 오차 계산

## 실무 팁/주의점
- 학습이 느리면 학습률, 초기화, [[Condition Number]]를 점검
- 깊은 네트워크에서는 ReLU 계열 활성화가 안정적
- 그래디언트 폭주/소실 시 클리핑, 정규화, 스킵 연결 고려

## 관련 노트
- [[Gradient Descent]]
- [[ANN]]
- [[Deep Learning]]
- [[Delta Rule]]
- [[Vanishing Gradient Problem]]
- [[Optimization]]
