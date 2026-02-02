# Dimensionality Reduction

## 한줄 요약
고차원 데이터를 저차원으로 변환해 정보 밀도를 높이는 기법.

## 핵심 개념
- 시각화, 노이즈 제거, 계산 비용 감소 목적
- 선형: [[Principal Component Analysis]]
- 비선형: t-SNE, UMAP 등

## 예시
- 임베딩 시각화
- 차원 축소 후 클러스터링

## 실무 팁/주의점
- 비선형 기법은 재현성(랜덤 시드)에 민감
- 다운스트림 태스크 성능을 기준으로 평가

## 관련 노트
- [[Principal Component Analysis]]
- [[Autoencoder]]
- [[Clustering]]
