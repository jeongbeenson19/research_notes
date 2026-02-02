# Object Detection

## 한줄 요약
이미지에서 객체의 위치와 클래스를 동시에 예측하는 문제.

## 핵심 개념
- 바운딩 박스 회귀 + 분류를 함께 수행
- [[One-stage detectors]]와 [[Two-stage detectors]]로 구분
- 앵커 기반 접근에서 [[Anchor Boxes]]가 중요

## 대표 접근
- One-stage: YOLO, SSD
- Two-stage: [[R-CNN]], [[Faster R-CNN]]

## 대표 평가
- [[IoU]]
- [[Average Precision]]

## 실무 팁/주의점
- 데이터 라벨 품질이 성능에 크게 영향
- 작은 객체는 해상도와 앵커 설계가 중요

## 관련 노트
- [[One-stage detectors]]
- [[Two-stage detectors]]
- [[Anchor Boxes]]
- [[R-CNN]]
- [[Faster R-CNN]]
- [[YOLOv1]]
