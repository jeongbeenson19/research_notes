---
title: "Meta Learning"
tags: [concept, learning, few-shot, generalization]
---
# Meta Learning

## 한줄 요약
다양한 태스크에 빠르게 적응하도록 학습하는 "학습하는 방법을 학습"하는 접근.

## 핵심 아이디어
- 여러 태스크 분포에서 학습하여 새로운 태스크에 소수의 샘플만으로 적응
- 에피소드 학습(N-way K-shot)으로 일반화 능력을 강화

## 대표 계열
- **MAML 계열:** 몇 번의 그래디언트 업데이트로 빠른 적응
- **Metric 기반:** Prototypical Networks, Matching Networks
- **Optimization 기반:** Reptile, FOMAML 등

## 장점
- 적은 데이터로 빠른 적응
- 분포 이동에 대한 초기 적응 속도 개선

## 한계
- 태스크 설계/샘플링에 성능이 민감
- 학습 비용이 높을 수 있음

## 관련 노트
- [[Zero-shot and Few-shot Learning]]
- [[Transfer Learning]]
