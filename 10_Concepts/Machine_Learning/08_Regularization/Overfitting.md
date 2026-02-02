# Overfitting

## 한줄 요약
훈련 데이터에 과도하게 맞춰져 일반화 성능이 떨어지는 현상.

## 핵심 개념
- 모델 복잡도가 높거나 데이터가 부족할 때 발생
- 검증 성능 하락이 대표 신호
- 정규화, 데이터 증강으로 완화

## 대표 진단
- Train 성능 상승, Val/Test 성능 하락

## 실무 팁/주의점
- 데이터 분리와 누수 점검이 우선
- [[Dropout]], [[Data Augmentation]], 조기 종료 활용

## 관련 노트
- [[Generalization]]
- [[Regularization]]
- [[Data Augmentation]]
- [[Dropout]]
