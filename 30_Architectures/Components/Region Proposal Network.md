# Region Proposal Network

## 한줄 요약
특징 맵 위에서 객체 후보 영역을 빠르게 제안하는 네트워크.

## 핵심 개념
- 슬라이딩 윈도우로 앵커를 평가
- 객체성 점수와 바운딩 박스 오프셋을 예측
- [[Faster R-CNN]]의 핵심 구성 요소

## 대표 구성
- Conv feature map + 작은 conv
- 분류(객체/배경) + 회귀(박스 오프셋)

## 실무 팁/주의점
- 앵커 스케일/비율 선택이 recall에 큰 영향
- NMS 임계값을 조정해 후보 수를 제어

## 관련 노트
- [[Faster R-CNN]]
- [[Two-stage detectors]]
- [[Anchor Boxes]]
