# Optimization

## 한줄 요약
목적 함수를 최소화 또는 최대화하는 파라미터 탐색 과정.

## 핵심 개념
- 비선형/비볼록 문제에서 지역 최적 존재
- 학습률, 초기값, [[Condition Number]]가 수렴에 영향
- [[Gradient Descent]]가 대표적 방법

## 대표 방법
- GD/SGD/Adam
- 2차 방법: 뉴턴, L-BFGS

## 실무 팁/주의점
- 스케줄러와 초기화가 수렴을 크게 좌우
- 대규모 모델은 혼합정밀도와 분산학습 고려

## 관련 노트
- [[Gradient Descent]]
- [[Condition Number]]
