---
title: "Zero-shot and Few-shot Learning"
tags: [concept, learning, generalization, transfer]
---
# Zero-shot and Few-shot Learning

## 한줄 요약
학습 데이터가 없거나 매우 적은 클래스에 대해 일반화하도록 학습하는 패러다임.

## 정의
- **Zero-shot (ZSL):** 타깃 클래스의 학습 예시가 전혀 없는 상태에서 분류/인식을 수행
- **Few-shot (FSL):** 타깃 클래스당 소수의 예시(예: 1~5개)만으로 학습/적응

## 왜 중요한가
- 라벨링 비용 절감
- 롱테일/희귀 클래스 대응
- 새로운 클래스 등장 시 빠른 확장

## 전형적 설정
- **Seen/Unseen 분리:** 학습(Seen)과 평가(Unseen) 클래스가 분리됨
- **에피소드 학습(FSL):** N-way K-shot 형태로 반복 학습
- **Generalized ZSL:** Seen과 Unseen을 동시에 예측해야 하는 현실적 설정

## 대표 접근
- **전이 학습/메타러닝:** MAML, Prototypical Networks 등
- **사전학습 + 경량 적응:** 대규모 사전학습 후 선형 헤드/LoRA 등으로 적응
- **멀티모달 정렬:** 텍스트-비전 정렬(예: CLIP)로 ZSL 수행
- **생성 기반 접근:** 클래스 설명으로 특징을 합성해 분류기 학습

## 평가 지표
- Accuracy, Top-1/Top-5
- F1, mAP(멀티라벨/검출)
- Generalized ZSL에서 Seen/Unseen 균형 지표

## 장점과 한계
- **장점:** 데이터 효율적, 빠른 확장, 롱테일 대응
- **한계:** 클래스 설명 품질 의존, 도메인 시프트에 민감

## 관련 노트
- [[Transfer Learning]]
- [[Meta Learning]]
- [[20_Tasks/VideoUnderstanding/Abstract/Video Action Recognition]]
