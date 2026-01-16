---
title: "Optical Flow"
tags: [concept, vision, motion, video]
---
# Optical Flow

## 한줄 요약
연속 프레임 간 픽셀 이동 벡터를 추정해 움직임을 표현하는 기법.

## 핵심 아이디어
- 움직임을 (u, v) 벡터장으로 표현
- 밝기 보존과 공간적 부드러움 가정을 활용

## 대표 알고리즘
- Farneback: 비교적 빠른 밀집(dense) 흐름
- TV-L1: 노이즈에 강하고 두-스트림에 자주 사용
- RAFT 등 딥러닝 기반 흐름 추정

## 비디오 인식에서의 활용
- Two-Stream의 temporal stream 입력으로 사용
- 모션 정보가 중요한 액션(달리기, 점프 등)에 효과적

## 실무 팁
- 흐름 계산 비용이 커서 오프라인 캐시가 일반적
- 프레임 간 간격/해상도에 따라 성능과 비용이 크게 변함
- 압축 비디오의 motion vector로 근사 가능

## 관련 노트
- [[Two-Stream Network]]
- [[Temporal Segment Networks]]
- [[Video Action Recognition]]
