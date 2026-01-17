---
title: "Video Understanding"
tags: [task, video, understanding, roadmap]
---
# Video Understanding

## 한줄 요약
비디오 이해는 프레임 기반 인식에서 시작해 시공간 모델, 멀티모달, 기초 모델, 그리고 추론/정렬 문제로 확장되어 왔다.

## 발전 흐름 (연대기 개요)
### 1) 핸드크래프트 특징 + 전통적 분류기 (2000s 초~2014)
- **Dense Trajectories / iDT**: optical flow 기반 궤적 + HOG/HOF/MBH
- **BoVW/Fisher Vector** 집계 + SVM 분류가 표준 파이프라인
- 장점: 데이터 적은 환경에서도 강건함
- 한계: end-to-end 학습 부재, 표현력 제한

### 2) 2D-CNN 기반 프레임 모델 (2014~)
- 이미지 분류 CNN을 프레임에 적용 후 평균 풀링
- 공간 정보는 잘 캡처하지만 시간 정보 손실
- **Two-Stream**으로 motion을 보완하며 성능 급상승

### 3) Two-Stream 및 시간 샘플링 전략 (2014~2017)
- RGB(Spatial) + Optical Flow(Temporal) 스트림 분리 학습
- **TSN** 등으로 긴 영상의 구간 샘플링과 합의 기반 예측
- 정확도는 크게 향상, 하지만 flow 계산 비용 증가

### 4) 3D-CNN과 시공간 컨볼루션 (2015~)
- **C3D, I3D, SlowFast** 등으로 시공간 특징 직접 학습
- 대규모 데이터셋(Kinetics) 사전학습이 성능을 좌우
- 연산 비용과 긴 시퀀스 모델링이 과제로 남음

### 5) 시계열 모델 결합 (2015~2020)
- CNN 특징을 RNN/LSTM/GRU로 모델링
- 클립 단위 특징의 장기 의존성을 보완
- 하지만 학습 안정성과 비용 문제가 지속

### 6) Attention/Transformer 시대 (2019~)
- Spatiotemporal Attention과 **Video Transformer** 등장
- 긴 의존성 모델링과 표현력 향상
- 데이터 규모와 계산 자원 의존성 증가
- 대표 논문
  - Non-local Neural Networks (2018): 시공간 전역 상호작용 도입
  - [[TimeSformer]] (2021): 순수 Transformer 기반 비디오 분류
  - ViViT (2021): 비디오 토큰화와 계층적 어텐션 설계
  - Video Swin Transformer (2021/2022): 윈도우 기반 효율적 어텐션

### 7) 멀티모달/멀티스트림 확장 (2020~)
- RGB + Flow + Skeleton + Audio + Text 결합
- 비디오-언어 정렬(CLIP 계열)로 **zero-shot** 가능성 확대
- 모달 정합과 효율적 융합이 핵심 과제
- 대표 논문
  - VideoBERT (2019): 비디오-텍스트 공동 사전학습
  - MIL-NCE (2020): 비디오-텍스트 대조학습
  - [[CLIP and Vision-Language Alignment|VideoClip]] (2021): 대규모 비디오-텍스트 정렬
  - CLIP4Clip (2021): CLIP 기반 비디오 검색/정렬

### 8) 비디오 기초 모델과 대규모 사전학습 (2021~)
- 대규모 비디오-텍스트/비디오-오디오 사전학습
- 일반화 성능 향상, 다운스트림 적응 용이
- 데이터 편향, 해석가능성 문제가 대두
- 대표 논문
  - [[VideoMAE]] (2022): 마스크드 오토인코딩 기반 비디오 사전학습
  - VATT (2021): 비디오-오디오-텍스트 트라이모달 사전학습
  - InternVideo (2022/2023): 대규모 비디오 기초 모델
  - BEVT (2022): 비디오-텍스트 공동 사전학습

## 현재의 핵심 이슈
- **장기 시간 모델링**: 긴 이벤트 이해와 계층적 구조 추론
- **효율성**: 연산/메모리/실시간 요구
- **일반화**: 도메인 이동과 롱테일 대응
- **멀티모달 정합**: 텍스트/오디오/포즈와의 정렬
- **평가**: 단순 분류에서 장면/이벤트 이해까지 확장

## Main Task
![[스크린샷 2026-01-16 오후 8.28.09.png]]
### **Abstract Understanding Tasks**
---
#### [[Video Action Recognition|Video Classification & Action Recognition]]
#### [[Text-Video Retrieval]]
#### [[Video-to-Text Summarization]]
#### [[Video Captioning]]
#### [[Video QA]]
---

### **Temporal Understanding Tasks**
---
#### [[Video Summarization]]
#### [[Video Highlight Detection]]
#### [[Temporal Action/Event Localization]]
#### [[Temporal Action Proposal Generation]]
#### [[Video Temporal Grounding]]
#### [[Moment Retrieval]]
#### [[Generic Event Boundary Detection]]
#### [[Generic Event Boundary Captioning & Grounding]]
#### [[Dense Video Captioning]]
---

### **Spatiotemporal Understanding Tasks**
----
#### [[Object Tracking]]
#### [[Re-Identification]]
#### [[Video Saliency Detection]]
#### [[Video Object Segmentation]]
#### [[Video Instance Segmentation]]
#### [[Video Object Referring Segmentation]]
#### [[Spatiotemporal Grounding]]

---

## 데이터셋 흐름 (요약)
- 초기: KTH, UCF101, HMDB51
- 중기: Sports-1M, ActivityNet, Kinetics
- 최근: Something-Something, AVA, Charades, Ego4D 등

## 관련 노트
- [[Two-Stream Network]]
- [[3D-CNN]]
- [[I3D]]
- [[Temporal Segment Networks]]
- [[Video Action Recognition]]
- [[Zero-shot and Few-shot Learning]]
