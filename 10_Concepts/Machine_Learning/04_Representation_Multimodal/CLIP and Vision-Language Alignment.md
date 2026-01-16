---
title: "CLIP and Vision-Language Alignment"
tags: [concept, multimodal, zero-shot, alignment]
---
# CLIP and Vision-Language Alignment

## 한줄 요약
이미지/비디오와 텍스트를 같은 임베딩 공간에 정렬해 zero-shot 분류를 가능하게 하는 접근.

## 핵심 아이디어
- 텍스트 인코더와 비전 인코더를 대규모 쌍 데이터로 공동 학습
- 텍스트 프롬프트를 클래스 설명으로 사용해 zero-shot 분류 수행

## 일반 절차
- 이미지/비디오 임베딩과 텍스트 임베딩을 유사도 비교
- 가장 유사한 텍스트 클래스가 예측 결과

## 응용
- Zero-shot 분류/검색
- Few-shot에서 텍스트-가이드 적응
- 비디오 행동 인식에서 텍스트 라벨을 활용한 일반화

## 한계
- 프롬프트 설계에 민감
- 도메인 시프트에 취약
- 비디오의 장기 시간 정보를 직접 다루기 어렵고 후속 모듈이 필요

## 관련 노트
- [[Zero-shot and Few-shot Learning]]
- [[Video Action Recognition]]
