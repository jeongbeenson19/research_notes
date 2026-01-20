# Mean Squared Error

## 한줄 요약
예측값과 실제값의 차이를 제곱해 평균한 회귀 손실 함수.

## 핵심 개념
- 큰 오차에 더 큰 패널티 부여
- 이상치에 민감
- 회귀 및 [[Autoencoder]] 학습에 자주 사용

## 대표 수식
- MSE = (1/n) * sum((y - y_hat)^2)

## 예시
- 선형 회귀, 이미지 복원

## 실무 팁/주의점
- 이상치가 많으면 MAE나 Huber 손실 고려

## 관련 노트
- [[Autoencoder]]
- [[Regularization]]
