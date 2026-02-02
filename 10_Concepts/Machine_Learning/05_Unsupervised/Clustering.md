# Clustering

## 한줄 요약
라벨 없이 데이터의 유사성을 기준으로 군집을 찾는 비지도 학습 기법.

## 핵심 개념
- 거리/유사도 정의가 결과에 큰 영향
- K-means, 계층적 군집, DBSCAN 등 다양한 방법
- 평가 지표는 응용에 맞게 선택

## 대표 알고리즘
- K-means: 구형 클러스터에 강함, 초기값 민감
- Hierarchical: 덴드로그램으로 군집 구조 파악
- DBSCAN: 밀도 기반, 이상치 탐지에 유리

## 대표 수식/지표
- WCSS(Within-Cluster Sum of Squares)
- Silhouette Score

## 예시
- 고객 세그먼트 분리
- 이미지 색상 군집화

## 실무 팁/주의점
- 스케일링과 거리 메트릭 선택이 성능을 좌우
- K 선택은 엘보우/실루엣으로 보조 판단
- 고차원에서는 [[Dimensionality Reduction]]으로 선행 압축

## 관련 노트
- [[Unsupervised Learning]]
- [[Dimensionality Reduction]]
