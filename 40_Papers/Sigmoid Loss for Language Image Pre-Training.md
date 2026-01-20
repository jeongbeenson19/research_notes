---
title: Sigmoid Loss for Language Image Pre-Training
aliases:
  - SigLIP
  - SigLiT
tags:
  - paper
  - vision-language
  - contrastive-learning
  - loss
  - pretraining
  - retrieval
  - multilingual
year: 2023
venue: arXiv
arxiv: https://arxiv.org/abs/2303.15343
project: https://github.com/google-research/big_vision
---
# Sigmoid Loss for Language Image Pre-Training

## 한줄 요약
- **소프트맥스 대조 손실 대신 pairwise sigmoid loss를 사용해 배치 크기 의존을 줄이고, 작은 배치에서도 성능을 높이면서 대규모 배치 학습을 더 효율적으로 만든다.**

## 개요
- SigLIP는 [[Softmax]] 기반 대조 학습의 전역 정규화 요구를 없애, 대규모 배치에서의 메모리/통신 병목을 완화한다.
- SigLiT는 LiT 설정(locked image tower)과 결합해 적은 TPUv4로도 경쟁력 있는 zero-shot 성능을 달성한다.
- 이 손실 설계는 [[CLIP and Vision-Language Alignment]]의 기본 구조를 유지하면서 학습 효율을 개선하는 쪽에 초점을 둔다.

## 핵심 기여
- **Sigmoid loss 제안**: 모든 이미지-텍스트 쌍을 독립적으로 이진 분류로 처리해 전역 정규화가 필요 없다.
- **메모리 효율 구현**: all-gather 없이 chunked 방식으로 |B|^2 메모리를 b^2로 축소.
- **배치 스케일링 관찰**: 16k 이하에서 sigmoid가 유의하게 우수, 32k에서 성능 포화.
- **자원 효율**: 적은 TPUv4에서도 경쟁력 있는 zero-shot 성능 (SigLiT/SigLIP).
- **멀티링구얼 확장**: mSigLIP로 XM3600에서 SOTA 달성, 대규모 vocab도 bottleneck으로 효율화.
- **안정화/어블레이션**: beta2 조정, bias term, negative 비율, 라벨 노이즈 강건성 분석.

핵심 기여를 바탕으로, 아래에서 모델 구성과 학습 흐름을 더 구체적으로 정리한다.

## 문제 설정 및 배경
- 목표는 이미지-텍스트 쌍을 같은 임베딩 공간에 정렬해 zero-shot 분류와 검색을 수행하는 것.
- 기존 [[Cross-Entropy Loss]] 기반의 softmax 대조 손실은 배치 전체 유사도 행렬이 필요해 통신/메모리 비용이 크다.
- Sigmoid 손실은 쌍 단위 이진 분류로 재정의하여 전역 정규화 없이도 학습이 가능하도록 설계된다.

## 모델 아키텍처
- **이미지 인코더**: ViT 계열 [[Vision Transformer]] 사용.
- **텍스트 인코더**: Transformer 기반 [[Transformer]] 사용.
- **공유 임베딩 공간**: 이미지/텍스트 임베딩을 정규화 후 내적 유사도로 정렬.
- **학습 파라미터**: temperature `t`와 bias `b`를 학습하며 초기값은 `t=10`, `b=-10`.

아키텍처는 [[CLIP and Vision-Language Alignment]]의 기본 구조를 유지하므로, 차이는 손실과 학습 효율에 집중된다.

## 데이터 흐름
1. 이미지 입력 → 이미지 인코더 → 임베딩 `x_i` 산출.
2. 텍스트 입력 → [[Tokenization]] → 텍스트 인코더 → 임베딩 `y_j` 산출.
3. 모든 쌍 `(i, j)`에 대해 유사도 `x_i · y_j` 계산.
4. 양성(정합)과 음성(비정합) 라벨로 sigmoid 손실을 합산.
5. 장치 간 임베딩을 순환 교환해 chunked 방식으로 전체 쌍을 커버.

이 흐름은 전역 정규화 없이도 학습을 진행할 수 있어, 대규모 배치에서 특히 유리하다.

## Sigmoid loss 설계
- 모든 쌍을 이진 분류로 보고, `z_ij`를 양성(+1)/음성(-1)로 정의한다.
- 손실은 다음과 같이 합산된다.

$$
\mathcal{L} = -\frac{1}{|B|}\sum_{i=1}^{|B|}\sum_{j=1}^{|B|} \log \sigma\big(z_{ij} (t \cdot x_i^\top y_j - b)\big)
$$

- `b=-10` 초기화는 극심한 클래스 불균형에서 초기 과보정을 줄이는 역할을 한다.
- 이 관점은 [[Class Imbalance]]와 [[Hard Negative Mining]] 논의와도 연결된다.

## 효율적 구현(Chunked)
- 전통적 softmax는 |B|x|B| 유사도 행렬을 요구한다.
- Sigmoid는 장치 간 텍스트 임베딩을 순환 교환하며 부분 블록만 계산.
- 이로 인해 메모리는 `|B|^2 → b^2`로 감소하고, all-gather 없이도 전체 쌍 손실을 누적할 수 있다.

효율화 덕분에 배치 크기를 키워도 시스템 병목이 완만해지며, 이후의 실험 결과와 연결된다.

## 실험 설정(요지)
- 이미지 인코더: ViT-B/L/g/So-400m 등 다양한 크기.
- 텍스트 인코더: 동일 규모의 Transformer.
- SigLiT: LiT 설정(locked image tower + precomputed embeddings).
- SigLIP: WebLI 영어 페어(32k vocab, 최대 16 토큰)로 CLIP 스타일 학습.
- mSigLIP: WebLI 100개 언어, 큰 vocab은 bottleneck(예: K=96)로 메모리 절감.
- 옵티마이저: AdaFactor/Adam, 안정화를 위해 `beta2=0.95` 설정.

## 주요 결과
- **SigLiT(4 TPUv4, 2일)**: ImageNet zero-shot **84.5%**.
- **SigLiT(4 TPUv4, 1일)**: ImageNet zero-shot **79.7%**.
- **SigLIP(WebLI, B/16)**: 16 TPUv4, 3일 학습으로 **71.0%** zero-shot.
- **SigLIP(자원 효율)**: pretrained image tower에 weight decay 제외 시 16 TPUv4, 3일에 **71%** 달성.
- **From-scratch SigLIP**: 32 TPUv4, 2일에 **72.1%** zero-shot.
- **배치 스케일링**: 32k에서 성능 포화, 1M 배치는 이득이 작음.
- **mSigLIP**: XM3600 text→image 평균 **34.9%**, 기존 28.5% 대비 +6%p 이상.
- **Scaled mSigLIP**: XM3600 image R@1 **42.6%**, text R@1 **54.1%**.

이 결과는 [[Zero-shot and Few-shot Learning]] 맥락에서 대규모 이미지-텍스트 사전학습의 효율 개선을 보여준다.

## 분석/어블레이션
- **Negative 비율**: 쉬운 음성만 남기면 급격히 악화, hardest negatives 유지 시 성능 보존.
- **Bias term**: `b=-10` 초기화가 초기 과도 보정(over-correction)을 막아 일관된 개선.
- **라벨 노이즈**: 이미지/텍스트/배치 교란에서 sigmoid 학습이 softmax 대비 더 강건.
- **대배치 안정화**: gradient spike를 줄이기 위해 `beta2=0.95` 설정이 유효.

## 학습/추론 엔트리포인트 (확인 필요)
- 논문은 공개 코드(google-research/big_vision)를 언급하지만, 구체 엔트리포인트 파일/함수는 확인이 필요하다.
- 확인 위치: `https://github.com/google-research/big_vision` (repo 구조 및 트레이닝 스크립트 확인 필요).

## 설정 파일 (확인 필요)
- SigLIP/SigLiT의 실험 설정은 공개 코드 내 config로 제공될 가능성이 높다.
- 확인 위치: `https://github.com/google-research/big_vision` 내 실험 설정 파일.

## 의존성 (확인 필요)
- 논문은 TPUv4 기반 학습을 보고하지만, 구체 라이브러리(JAX/Flax 등)는 코드 확인이 필요하다.
- 확인 위치: `https://github.com/google-research/big_vision`의 `requirements`/환경 설정.

## 확장 포인트
- **음성 샘플링**: [[Hard Negative Mining]]과 결합해 효율적인 음성 선택 전략 탐색.
- **멀티링구얼 확장**: vocab bottleneck 설계를 다른 다국어 데이터셋으로 확장.
- **노이즈 강건성**: 약지도 데이터셋에서 sigmoid 손실의 강건성을 활용한 데이터 정제.
- **대배치 최적화**: [[Optimization]] 관점에서 스케줄/옵티마이저 안정화 연구.

## 의의와 한계
- 전역 정규화가 필요한 [[Softmax]] 대비 구현 단순성과 효율을 확보했다는 점이 핵심.
- 다만 32k 이상에서 성능 포화가 관찰되며, 초대형 배치가 항상 이득은 아니다.
- 또한 음성 쌍이 방대해지는 구조적 특성상, 효율적 음성 선택이 향후 과제로 남는다.

## 참고
- arXiv: https://arxiv.org/abs/2303.15343
- alphaXiv: https://www.alphaxiv.org/abs/2303.15343
- 코드: https://github.com/google-research/big_vision
