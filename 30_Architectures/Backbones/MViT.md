---
title: MViT (Multiscale Vision Transformer)
aliases:
  - Multiscale Vision Transformer
  - MViT
  - 멀티스케일 비전 트랜스포머
tags:
  - computer-vision
  - transformer
  - video
  - backbone
  - multiscale
topics:
  - hierarchical
  - pooling
  - attention
---
# MViT (Multiscale Vision Transformer)

## 1. 한줄 요약
- **MViT는 토큰을 단계적으로 풀링해 해상도를 줄이고 채널을 늘리는 멀티스케일 계층형 Transformer로, 비디오/이미지에서 CNN처럼 피라미드 표현을 학습한다.**

## 2. 배경과 문제의식
- 기존 ViT는 **고정 해상도 토큰**을 전층에서 유지 → 계산량 $O(n^2)$가 커짐.
- CNN은 **공간 해상도를 줄이고 채널을 늘리는 피라미드 구조**로 효율적 표현 학습.
- MViT는 **Transformer에 멀티스케일 계층 구조**를 도입해 효율성과 성능을 동시에 노림.

## 3. 핵심 아이디어
### 3.1 멀티스케일 토큰 피라미드
- 토큰 수는 단계적으로 줄이고 채널 수는 늘림.
- 각 스테이지는 서로 다른 해상도를 담당 → **로컬/글로벌 정보가 자연스럽게 분리**.

### 3.2 Pooling Attention
- **Q, K, V 중 일부를 풀링**해 토큰 수를 줄임.
- 풀링은 보통 공간/시간 축에서 stride를 사용.
- 결과적으로 attention의 복잡도는 감소하면서도 **전역 문맥 추론 유지**.

### 3.3 계층형 설계
- CNN의 stage 개념처럼 **여러 stage로 쌓아 피라미드 표현**을 형성.
- 각 stage에서 해상도 감소와 채널 증가가 동시 진행.

## 4. 구성 요소
### 4.1 입력 토크나이징
- 이미지/비디오를 패치로 분할 후 선형 임베딩.
- 비디오의 경우 시간축까지 고려한 3D 패치 사용.

### 4.2 MViT 블록(요지)
- 기본은 Transformer 블록과 유사:
  - LayerNorm → Multi-Head Attention → MLP
  - Residual 연결 포함
- 차이점: **Pooling Attention**을 통해 Q/K/V 중 일부를 다운샘플링.

### 4.3 해상도/채널 스케줄
- 예: stage마다 spatial stride 2로 토큰 수 감소.
- 채널은 stage가 올라갈수록 증가.

## 5. 수식(요약)
- 입력 토큰 $X \in \mathbb{R}^{n \times d}$.
- 풀링된 쿼리: $\tilde{Q} = \mathrm{Pool}(XW_Q)$.
- 풀링된 키/밸류: $\tilde{K} = \mathrm{Pool}(XW_K),\; \tilde{V} = \mathrm{Pool}(XW_V)$.
- Attention:
  - $\mathrm{Attn}(\tilde{Q},\tilde{K},\tilde{V}) = \mathrm{softmax}(\tilde{Q}\tilde{K}^T/\sqrt{d_k})\tilde{V}$.
- 이때 $\tilde{Q},\tilde{K},\tilde{V}$는 **공간/시간 해상도 축에서 감소된 길이**.

## 6. 장점과 한계
### 장점
- 토큰 수를 줄여 **계산 효율 개선**.
- CNN과 유사한 **멀티스케일 표현 학습**.
- 비디오 태스크(행동 인식 등)에 특히 효과적.

### 한계
- 구조가 복잡해 하이퍼파라미터 설계가 어려움.
- 풀링 스케줄에 따라 성능 민감.
- ViT 대비 구현 난이도 상승.

## 7. 적용 분야
- 비디오 분류/행동 인식
- 비디오 이해(추적, 이벤트 인식)
- 고해상도 이미지 인식에도 활용 가능

## 8. 관련 개념
- [[Vision Transformer]]
- [[Transformer]]
- [[Multi-Head Attention]]
- [[Self-Attention]]
- [[CNN]]

## 9. 참고 문헌
- Fan, H. et al. (2021). *Multiscale Vision Transformers*. https://arxiv.org/abs/2104.11227
