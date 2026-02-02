---
title: "Video Action Recognition"
tags: [concept, video, action-recognition, deep-learning]
---
# Video Action Recognition

## 한줄 요약
비디오에서 사람의 행동/동작을 분류하거나 탐지하는 컴퓨터 비전 문제.

## 문제 정의
- 입력: 시간 순서의 프레임(혹은 클립) 시퀀스
- 출력: 행동 클래스(분류), 행동 구간(탐지), 다중 행동(멀티라벨) 등

## 핵심 난점
- 시간적 의존성: 동작은 여러 프레임의 순서와 맥락에 의존
- 시공간 결합: 외형(공간)과 움직임(시간)을 함께 모델링해야 함
- 데이터 규모: 라벨링 비용이 크고, 장기 시퀀스 학습이 어려움

## 대표 접근
- Two-Stream: RGB + Optical Flow 분리 학습 후 결합
- 3D-CNN: 시공간 컨볼루션으로 모션을 직접 학습
- RNN/LSTM: 프레임 특징을 시계열로 모델링
- Attention/Transformer: 중요한 시간/공간 영역에 집중
- Skeleton/GCN: 포즈 기반 그래프 모델링

## 평가 지표
- Accuracy(Top-1/Top-5)
- mAP(특히 멀티라벨/탐지 과제)
- Precision/Recall/F1

## 데이터셋 예시
- UCF101, HMDB51, Kinetics, ActivityNet
- Something-Something, Charades, AVA
- NTU RGB+D 60/120(스켈레톤)

## 관련 노트
- [[Two-Stream Network]]
- [[3D-CNN]]
- [[Temporal Segment Networks]]
- [[Optical Flow]]
- [[Transformer]]
