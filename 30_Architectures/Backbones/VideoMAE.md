---
title: VideoMAE
aliases:
  - Video Masked Autoencoder
  - 비디오 MAE
  - 비디오 마스크드 오토인코더
tags:
  - computer-vision
  - video
  - self-supervised
  - transformer
  - backbone
topics:
  - masked-autoencoder
  - pretraining
  - reconstruction
---
# VideoMAE

## 1. 한줄 요약
- **VideoMAE는 비디오 토큰을 대량 마스킹하고 복원하도록 학습하는 자기지도 Transformer로, 효율적인 사전학습을 제공한다.**

## 2. 배경과 문제의식
- 비디오는 연속 프레임 때문에 중복 정보가 많고 계산 비용이 큼.
- 대규모 라벨 데이터를 확보하기 어려움.
- MAE 아이디어를 비디오로 확장해 **고마스킹 비율에서도 효율적인 자기지도 학습**을 목표.

## 3. 핵심 아이디어
### 3.1 High Masking Ratio
- 일반적으로 75%~90% 이상의 토큰을 마스킹.
- 마스킹된 토큰은 디코더가 복원하도록 학습.

### 3.2 Asymmetric Encoder-Decoder
- **인코더는 가볍게**: 보이는 토큰만 처리.
- **디코더는 얕게**: 마스크 복원을 담당.
- 학습 효율 향상.

### 3.3 비디오용 토큰
- 시간+공간을 포함하는 3D 패치 기반 토큰화.
- 마스킹은 시간/공간 차원 모두에서 적용 가능.

## 4. 구성 요소
### 4.1 Encoder
- 입력: 마스킹 후 남은 토큰만 사용.
- Transformer encoder로 글로벌 표현 학습.

### 4.2 Decoder
- 마스크 토큰을 포함해 원래 길이 복원.
- 픽셀/패치 재구성 손실로 학습.

### 4.3 손실
- 재구성 손실(MSE 등)을 사용.
- 특정 토큰/프레임에만 계산.

## 5. 수식(요약)
- 입력 토큰 $X \in \mathbb{R}^{n \times d}$.
- 마스킹 연산 $\mathcal{M}$:
  - $X_{vis} = \mathcal{M}(X)$, $X_{mask}$는 제거.
- 인코더 출력 $Z = f_{enc}(X_{vis})$.
- 디코더 입력 $[Z; \text{mask tokens}]$ → 복원 $\hat{X}$.
- 손실:
  - $\mathcal{L} = \|X_{mask} - \hat{X}_{mask}\|^2$.

## 6. 장점과 한계
### 장점
- 비디오 라벨 없이도 강력한 표현 학습.
- 높은 마스킹 비율로 **효율적인 사전학습**.
- 다양한 비디오 다운스트림 작업에 전이 가능.

### 한계
- 재구성 목표가 항상 다운스트림 성능과 일치하지 않을 수 있음.
- 긴 비디오에서 토큰 수가 많아 여전히 비용 부담.

## 7. 적용 분야
- 비디오 분류
- 행동 인식
- 비디오 이해 전반

## 8. 관련 개념
- [[Transformer]]
- [[Vision Transformer]]
- [[Self-Attention]]
- [[Masked Autoencoders (MAE)]]

## 9. 참고 문헌
- Tong, Z. et al. (2022). *VideoMAE: Masked Autoencoders Are Data-Efficient Learners for Self-Supervised Video Pre-Training*. https://arxiv.org/abs/2203.12602
