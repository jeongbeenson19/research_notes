---
aliases: ["Snakes and Ladders: Two Steps Up for VideoMamba", "VideoMambaPro"]
type: paper
tags:
  - DeepLearning
  - Paper
  - VideoUnderstanding
  - StateSpaceModel
  - Mamba
status: 🟩 Done
rating: 5
date: 2026-03-17
title: "Snakes and Ladders: Two Steps Up for VideoMamba"
authors: ["Yu Zhou", "Boyu Yang", "Jingyang Peng", "Yizhe Zhu", "Yinan He", "Liqiang Nie", "Limin Wang"]
year: 2025
venue: "ICCV 2025"
paper_url: "https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_Snakes_and_Ladders_Two_Steps_Up_for_VideoMamba_ICCV_2025_paper.html"
code_url: "https://github.com/hotfinda/VideoMambaPro"
topics: ["Video Understanding", "Mamba", "VideoMamba", "Bidirectional SSM", "Action Recognition"]
---

## Paper
- Title: Snakes and Ladders: Two Steps Up for VideoMamba
- Venue/Year: ICCV 2025
- Link: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_Snakes_and_Ladders_Two_Steps_Up_for_VideoMamba_ICCV_2025_paper.html
- 역할(문제정의/방법/평가/반박): 방법 개선 + VideoMamba 반박/보완 + 분석 논문

## Extract
- Task: 비디오 액션 인식 및 비디오 백본 개선. 기존 VideoMamba의 구조적 약점을 분석하고 더 강한 SSM 비디오 모델을 제안한다.
- Unobserved interval: occlusion보다는 긴 temporal dependency와 sparse key-frame reliance 문제를 다룬다.
- Memory unit: bidirectional SSM hidden state. 다만 저자들은 단순 bidirectional scan 자체가 정보 전달을 왜곡할 수 있다고 본다.
- State: VideoMamba의 recurrent state에 더해, residual SSM 경로가 추가되어 pairwise dependency를 더 안정적으로 전달한다.
- Update rule: 기존 forward/backward scan 위에 `Masked Backward Computation`과 `Residual SSM`을 넣어 historical decay와 element contradiction을 완화한다.
- Reactivation: 별도 track reactivation은 없지만, backward 경로의 자기참조 중복을 막고 residual 경로를 추가해 먼 과거 토큰 신호가 다시 활용되기 쉬운 구조를 만든다.
- Fusion: forward residual SSM + masked backward residual SSM을 결합한 bidirectional block.
- Assumptions: VideoMamba 성능 저하는 단순 capacity 부족이 아니라 구조적 정보 전달 문제에서 온다는 가정.
- Evaluation: Kinetics-400, Something-Something V2, UCF101, HMDB51, AVA v2.2.
- Failure modes: 주로 action recognition에서 검증되었고, localization-heavy task나 video-language 확장성은 본문에서 충분히 다루지 않는다.

## Takeaway
- 내 설계에 적용(1줄): SSM 백본을 그대로 쓰는 것보다 "어떤 정보가 뒤로 갈수록 약해지는가"와 "양방향 경로가 무엇을 중복/왜곡하는가"를 먼저 분석해야 한다.
- D1/D2/D3에 미치는 영향: `D1`은 단순 bidirectional fusion보다 residual memory path가 더 중요할 수 있다는 신호를 준다. `D2`는 state를 하나의 통로로만 보내지 말고 보정 경로를 두는 쪽이 안정적임을 시사한다. `D3`는 semantic 증가보다 memory transport quality 개선이 선행 과제임을 보여준다.

## 개요

이 논문은 단순히 "VideoMamba 성능을 조금 올린 후속작"이 아니다. 저자들은 VideoMamba를 self-attention의 관점에서 다시 읽고, 왜 비디오에서 성능이 기대보다 낮았는지를 두 가지 구조적 문제로 해석한다.

- historical decay
- element contradiction

즉, 문제의 핵심은 capacity 부족이나 학습 레시피 부족이 아니라, bidirectional SSM이 비디오 토큰 간 관계를 전달하는 방식 그 자체에 있다는 주장이다. 이 분석 위에서 저자들은 `VideoMambaPro`를 제안한다.

## VideoMamba에 대한 진단

### 1. Historical Decay
- self-attention 관점으로 보면, VideoMamba의 유효 유사도 행렬은 lower-triangular한 성격을 가지며 시간이 멀어질수록 영향력이 약해진다.
- 그 결과 멀리 떨어진 key frame의 정보가 뒷부분 토큰에 충분히 전달되지 않는다.
- action recognition처럼 sparse but critical frame가 중요한 문제에서 이 현상은 치명적이다.

### 2. Element Contradiction
- bidirectional SSM은 앞뒤 정보를 모두 흘리지만, 동일한 element가 여러 토큰 관계를 동시에 떠맡으면서 충돌이 생길 수 있다.
- 저자들의 표현을 빌리면, 하나의 state element가 상충하는 dependency를 동시에 표현해야 하는 "contradiction" 문제가 발생한다.
- 이 때문에 장거리 정보 전달이 균질하게 되지 않고, 일부 중요한 연결이 약화된다.

## 제안 방법: VideoMambaPro

### 1. Masked Backward Computation
- backward branch에서 자기참조나 중복되는 diagonal 정보를 그대로 누적하면 유효성이 떨어진다.
- 이를 막기 위해 backward computation에 mask를 적용해 불필요한 중복 의존성을 제거한다.
- 결과적으로 과거-현재 관계를 더 날카롭게 전달할 수 있다.

### 2. Residual SSM
- 저자들은 단일 SSM 경로만으로는 다양한 dependency를 동시에 표현하기 어렵다고 본다.
- 그래서 residual connection을 state transport 경로 수준에 도입한다.
- 논문 본문 기준 블록은 `forward residual SSM`과 `masked backward residual SSM`을 함께 사용한다.

### 3. Block-Level 해석
- patch embedding 뒤에 여러 개의 bidirectional Mamba block이 쌓이는 큰 틀은 VideoMamba와 유사하다.
- 하지만 실제 정보 전달은 "원래 SSM 경로 + residual 보정 경로 + backward mask"의 조합으로 바뀐다.
- 즉, 겉보기에는 비슷한 backbone이지만 dependency transport 품질은 꽤 다르다.

## 실험 설정

### 데이터셋
- Kinetics-400
- Something-Something V2
- UCF101
- HMDB51
- AVA v2.2

### 학습 자원
- 본문 기준 K400/SSv2는 16개의 A100 GPU를 사용한다.
- UCF101/HMDB51은 8개 A100, AVA는 32개 A100 설정이 보고된다.

### 비교 대상
- VideoMamba
- VideoMAE
- MViT
- InternVideo2
- 기타 transformer 기반 비디오 모델

## 실험과 결과

### 1. Kinetics-400
- 공식 ICCV 2025 PDF Table 5 기준 `VideoMambaPro-M`은 `90.3` top-1을 기록한다.
- 같은 표에서 `VideoMamba-M`은 `82.4` top-1, `VideoMAE-M`은 `85.2` top-1이다.
- 즉, published final table 기준으로도 VideoMamba 대비 큰 폭의 향상이 확인된다.

### 2. Something-Something V2
- 공식 PDF Table 5 기준 `VideoMambaPro-M`은 `69.4` top-1이다.
- 동일 표의 `VideoMamba-M`은 `68.3`이므로 published setting에서도 개선이 유지된다.
- motion order에 민감한 데이터셋에서 구조 수정 효과가 분명하다는 의미다.

### 3. UCF101 / HMDB51
- Table 5 기준 `VideoMambaPro-M`은 `UCF101 91.6`, `HMDB51 63.2`를 기록한다.
- 이는 transfer setting에서도 backbone 수정이 일회성 과적합이 아니라는 근거다.

### 4. AVA v2.2
- Table 5 기준 `VideoMambaPro-M`의 action detection 성능은 `31.9 mAP`다.
- 같은 표의 `VideoMamba-M`은 `30.1 mAP`이므로 localization 계열에서도 개선이 이어진다.

### 5. Ablation
- Table 7 기준 K400에서 각 구성의 효과는 다음과 같다.
  - baseline VideoMamba: `82.4`
  - `w/o residual`: `83.6`
  - `w/o masking`: `83.0`
  - full VideoMambaPro: `84.0`
- 즉, 두 구성요소 모두 유효하고, 둘을 함께 넣을 때 가장 좋다.

### 6. 통계적 검증
- 논문은 McNemar test도 보고한다.
- `VideoMambaPro-M`이 `VideoMAE-M`과 다른 예측을 낸 샘플은 2,577개이며, 그중 `2,075`개를 올바르게 맞추고 `502`개만 틀렸다고 적고 있다.
- 단순 평균 정확도뿐 아니라 예측 차이 자체가 통계적으로 유의하다는 점을 강조한다.

## 왜 중요한가

### 1. "SSM을 비디오에 쓰면 왜 약한가"를 설명한다
- VideoMamba는 강한 기준선이지만, 왜 transformer 대비 완전히 우세하지 못한지 설명은 약했다.
- 이 논문은 그 약점을 행렬/의존성 관점에서 분석해 후속 설계의 언어를 제공한다.

### 2. 개선 포인트가 구조적으로 명확하다
- 더 큰 모델
- 더 긴 학습
- 더 많은 데이터

위와 같은 스케일링이 아니라, backward masking과 residual transport라는 구체적 수정을 제안한다는 점이 좋다.

### 3. MNS류 메모리 모델에 직접적인 힌트
- occlusion memory도 결국 시간이 지날수록 감쇠되고, 양방향/재활성화 경로에서 중복 신호가 생긴다.
- 즉, historical decay와 element contradiction은 비디오 분류 문제에만 국한되지 않는다.

## 한계

- action recognition 중심 검증이라 object-level memory, tracking, grounding으로 그대로 일반화된다고 보긴 어렵다.
- published abstract와 preprint 버전 사이에서 개선 폭 표현이 달라 보일 수 있으므로, 세부 수치는 final PDF table 기준으로 보는 것이 안전하다.
- 여전히 pure SSM 계열이라, explicit object interaction이나 sparse retrieval가 꼭 필요한 문제는 별도 모듈이 필요하다.

## MNS 관점 연결

- MNS가 겪는 장기 occlusion 문제도 본질적으로 "중요한 과거 상태가 시간이 지나며 약해지는 문제"다. historical decay 분석은 그대로 옮겨올 수 있다.
- object state memory에 backward reactivation을 넣을 때 중복 자기참조를 제거하는 masking 설계가 필요할 수 있다.
- residual memory path를 넣어 주기억과 보정 기억을 분리하는 아이디어는 MNS의 belief state 설계에 직접 적용 가능하다.

## 참고 링크
- 논문: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_Snakes_and_Ladders_Two_Steps_Up_for_VideoMamba_ICCV_2025_paper.html
- PDF: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhou_Snakes_and_Ladders_Two_Steps_Up_for_VideoMamba_ICCV_2025_paper.pdf
- 코드: https://github.com/hotfinda/VideoMambaPro
