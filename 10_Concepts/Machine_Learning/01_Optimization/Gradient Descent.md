# Gradient Descent

## 한줄 요약
손실 함수를 줄이는 방향(음의 기울기)으로 파라미터를 반복 업데이트하는 최적화 방법.

## 핵심 개념
- 학습률이 수렴/발산을 좌우
- 배치/미니배치/확률적 경사하강법 변형 존재
- [[Backpropagation]]과 함께 사용되어 신경망을 학습

## 대표 수식
- theta <- theta - eta * grad_theta L

## 예시
- 선형 회귀의 MSE 최소화
- 로지스틱 회귀의 교차 엔트로피 최소화

## 실무 팁/주의점
- 학습률 스케줄링과 초기화가 중요
- [[Condition Number]]가 큰 문제는 수렴이 느림
- Adam 등 적응적 옵티마이저는 초기 학습에 유리

## 관련 노트
- [[Optimization]]
- [[Backpropagation]]
- [[Condition Number]]
