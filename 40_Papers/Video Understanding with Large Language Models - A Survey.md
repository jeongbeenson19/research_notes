---
type: paper
title: "Video Understanding with Large Language Models: A Survey"
venue: ""
year: 2023
authors: ["Yunlong Tang", "Jing Bi", "Siting Xu", "Luchuan Song", "Susan Liang", "Teng Wang", "Daoan Zhang", "Jie An", "Jingyang Lin", "Rongyi Zhu", "Ali Vosoughi", "Chao Huang", "Zeliang Zhang", "Pinxin Liu", "Mingqian Feng", "Feng Zheng", "Jianguo Zhang", "Ping Luo", "Jiebo Luo", "Chenliang Xu"]
url: "https://arxiv.org/html/2312.17432v5"
tasks: ["benchmark", "streaming"]
methods: ["retrieval"]
datasets: []
metrics: []
trends: []
status: to-read
date_read: ""
---

# Main Contribution (3 lines)
1) **What**: LLM을 활용한 비디오 이해(Vid-LLM) 연구를 체계적으로 정리한 서베이.
2) **Why**: 비디오 콘텐츠의 급증과 LLM의 멀티모달 역량 확대로, 분야 전반의 구조·역할·평가 체계를 통합 정리할 필요가 있음.
3) **Impact**: Vid-LLM 아키텍처 분류, LLM 역할, 과제·벤치마크·응용, 한계·미래 과제를 한눈에 파악할 수 있는 연구 지도를 제공.

## Method (<=5 bullets)
- Vid-LLM을 Video Analyzer×LLM, Video Embedder×LLM, (Analyzer+Embedder)×LLM로 분류.
- LLM의 기능을 Summarizer/Manager/Text Decoder/Regressor/Hidden Layer로 구분.
- 비디오 이해 과제, 데이터셋, 벤치마크 및 평가 방법을 체계적으로 정리.
- 다양한 응용 분야를 정리하고 확장 가능성을 논의.
- 기존 Vid-LLM의 한계와 향후 연구 방향을 정리.

## Evidence
- Benchmarks: 비디오 이해 벤치마크와 평가 프로토콜을 폭넓게 정리.
- Key numbers:
- Key ablations (2):
  -
  -

## Assumptions / Limitations (2 each)
- Assumptions:
  - Vid-LLM을 공통 구조/역할 기준으로 분류할 수 있다는 가정.
  - 공개 벤치마크가 실제 비디오 이해 성능을 대표한다는 전제.
- Limitations:
  - 서베이 시점 이후의 최신 연구/모델은 포함되지 않을 수 있음.
  - 정성적 분류 중심이라 동일 조건의 직접 비교에는 한계.

## Failure Modes (3)
- 긴 비디오에서 요약/선별 과정의 오류로 중요한 사건을 놓침.
- 시간적 일관성이나 인과 추론이 깨져 잘못된 설명을 생성.
- 시각적 환각으로 실제에 없는 객체/사건을 생성.

## One-liner takeaway
- Vid-LLM 연구를 구조·역할·평가·응용·한계까지 포괄적으로 조망하는 종합 서베이.

## Next experiment idea (1)
- 분류 체계를 실제 성능/비용 지표와 연결하는 정량 비교 프레임워크 제안.

## Contents

![[스크린샷 2026-01-16 오후 8.28.09.png]]![[스크린샷 2026-01-16 오후 8.31.13.png]]
