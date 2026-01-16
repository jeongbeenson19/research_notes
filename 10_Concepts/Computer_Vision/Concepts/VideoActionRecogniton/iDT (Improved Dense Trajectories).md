---
title: "iDT (Improved Dense Trajectories)"
tags: [concept, feature, video, action-recognition]
---
# iDT (Improved Dense Trajectories)

## 한줄 요약
카메라 움직임을 보정한 dense trajectory 기반의 비디오 특징 추출 기법으로, 딥러닝 이전 VAR의 표준 베이스라인.

## 핵심 아이디어
- 영상 전역에 촘촘히 샘플링한 점들을 optical flow로 추적해 궤적을 생성
- 카메라 모션을 제거해 사람/객체의 실제 움직임을 강조

## 배경과 의의
- Dense Trajectories의 성능을 유지하면서 **카메라 모션 보정**으로 오검출을 줄임
- 딥러닝 이전 액션 인식의 강력한 표준 베이스라인으로 널리 사용됨

## 파이프라인 요약
1. **Dense sampling**: 프레임마다 일정 간격으로 포인트 샘플링
2. **Tracking**: optical flow로 짧은 궤적(trajectory) 생성
3. **Camera motion compensation**: 배경 추정 및 궤적 보정
4. **Local descriptors**: 궤적 주변에서 HOG/HOF/MBH 추출
5. **Encoding**: BoVW, Fisher Vector 등으로 집계

## 세부 단계
### 1) Dense sampling
- 여러 스케일에서 일정 격자로 포인트를 샘플링
- 매우 낮은 텍스처 영역은 제외해 노이즈를 줄임

### 2) Tracking
- 프레임 간 optical flow로 점을 추적해 짧은 궤적 생성
- 보통 15프레임 정도의 짧은 길이로 제한해 드리프트를 완화

### 3) Camera motion compensation
- 프레임 간 **전역 모션**을 추정(예: homography)해 카메라 움직임을 제거
- 매칭 실패나 큰 오클루전 구간에서는 보정이 어려움

### 4) Local descriptors
- 궤적 주변 3D 공간에서 특징을 추출
- HOG: 외형/경계
- HOF: 모션 크기와 방향
- MBH: flow의 gradient로 카메라 모션 영향 감소

### 5) Encoding
- 각 디스크립터를 BoVW 또는 Fisher Vector로 집계
- 클래스 분류는 선형 SVM이 일반적

## 주요 특징(디스크립터)
- **HOG**: 외형/에지 기반
- **HOF**: 흐름 기반 움직임
- **MBH**: flow의 gradient로 카메라 모션에 비교적 강함

## 장점
- 딥러닝 없이도 높은 성능을 제공
- 카메라 모션이 큰 영상에서 안정적
- 다양한 데이터셋에 강한 일반화

## 한계
- optical flow 계산 비용이 큼
- 긴 시퀀스/복잡한 상호작용에는 한계
- end-to-end 학습 대비 표현력 제약

## 실무 팁
- 흐름 계산을 미리 캐시하고 I/O 병목을 고려
- 궤적 길이와 샘플링 간격은 성능/속도 트레이드오프
- 카메라 모션 보정 실패 케이스(빠른 패닝, 줌)에 유의

## 딥러닝과의 관계
- Two-Stream, 3D-CNN 이후에도 강력한 비교 기준으로 사용됨
- iDT + CNN 특징을 결합한 하이브리드 접근이 성능을 높이기도 함

## 참고 키워드
- Dense Trajectories
- Fisher Vector
- HOG/HOF/MBH

## 관련 노트
- [[Optical Flow]]
- [[Video Action Recognition]]
- [[Two-Stream Network]]
