---
title: "Temporal Segment Networks"
tags: [architecture, video, action-recognition]
---
# Temporal Segment Networks

## 한줄 요약
긴 비디오를 여러 구간으로 나눠 대표 클립을 샘플링하고, 각 구간의 예측을 합의(consensus)로 결합하는 구조.

## 핵심 아이디어
- 긴 비디오의 전체 동작을 포괄하도록 균등 구간 샘플링
- 각 구간의 클립을 동일 백본으로 처리하고 결과를 합산/평균

## 구성 요소
- Segment sampling: N개 구간으로 분할 후 랜덤/고정 샘플링
- Backbone: 2D-CNN 또는 Two-Stream
- Consensus: 평균, 가중 합, 또는 간단한 투표 방식

## 장점
- 긴 비디오에서도 시간적 커버리지를 확보
- 계산량을 제어하면서 성능을 유지 가능

## 한계
- 구간 내 세밀한 시간 정보는 손실될 수 있음
- 구간 수와 샘플링 전략 튜닝이 필요

## 관련 노트
- [[Two-Stream Network]]
- [[Video Action Recognition]]
- [[3D-CNN]]
