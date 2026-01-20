---
title: "3D-CNN"
tags: [architecture, video, cnn, spatiotemporal]
---
# 3D-CNN

## 한줄 요약
공간과 시간 축을 함께 컨볼루션하는 비디오 전용 CNN 구조.

## 핵심 아이디어
- 2D-CNN은 프레임 단위 특징, 3D-CNN은 클립 단위 시공간 특징을 학습
- 커널이 (T, H, W)로 움직임 패턴을 직접 포착

## 대표 계열
- C3D: 초기 표준 구조
- I3D: 2D 가중치를 3D로 인플레이트해 성능 향상
- SlowFast: 느린/빠른 스트림 병렬로 시간 정보 보강

## 장점
- 모션을 직접 학습해 광학 흐름 없이도 성능 확보
- 시공간 특징이 강해 복잡한 행동 인식에 유리

## 한계
- 연산량과 메모리 부담이 큼
- 긴 시퀀스 모델링은 여전히 어려움

## 실무 팁
- 클립 길이와 샘플링 전략이 성능/비용에 큰 영향
- 사전학습(예: Kinetics) 활용이 중요

## 관련 노트
- [[20_Tasks/VideoUnderstanding/Abstract/Video Action Recognition]]
- [[Two-Stream Network]]
- [[Temporal Segment Networks]]
- [[C3D]]
