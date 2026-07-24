---
title: Experiments (MNSv2 / VI4S)
type: experiment-log
status: 🟩 Active
tags:
  - experiments
  - VIS
  - ablation
topics:
  - VIS
  - SSM
  - YTVIS22
updated: 2026-07-24
---

> ⚠️ **이 문서는 실제 구현/실험 결과로 재작성됨(2026-07-24)**. 이전 버전은 구현 착수 전 실험 설계
> 초안(DSM/EKVM/VideoMamba 백본 가정)이었고, 실제로 지어진 시스템·수치와 맞지 않아 전면 교체함.
> 원래 구상/문헌근거는 [[Idea]] · [[Draft]] · [[Mechanism-level Novelty Table]]에 역사적 기록으로 보존.
> 결정의 근거/반례는 [[Decision Log]] 참고 — 이 문서는 **수치와 결과**에 집중.

---

# 실제로 지어진 것: VI4S

**EoMT(ViT-L, DINOv2) 세그멘터 + query-slot당 Selective SSM(Mamba류, conv1d+residual) 시간 전파**,
`external/videomt`의 online meta-architecture 위에 detectron2 플러그인으로 얹음(`VI4S/` 디렉토리).
"DSM"/"EKVM"이라는 이름의 별도 메모리 모듈은 짓지 않았고, SSM의 hidden state 자체가 그 역할을 겸함.

## 평가 방법론 (★반드시 주의)
- **공식 지표 = mAP_L**(`external/videomt/utils/yt2022_evaluate.py`) — d2 표준 COCO-style AP가 아니다.
- 평가 split = **gt_long.json**(YTVIS-2022 valid 중 71편, 논문 비교 대상 AP^L=42.6 재현 기준).
- **분산 큼(±6)** — 단일 ckpt 비교는 노이즈일 수 있음. 마지막 3-4 ckpt 평균 또는 여러 ckpt 궤적으로 판단.
- in-training eval은 최종 standalone eval보다 ~2점 낮게 나오는 경향 있음 → 최종 숫자는 `scores.txt` 기준.

---

## 1. 아키텍처 사다리 (40k, 1/4 예산, 모두 같은 harness)

| 구성 | mAP_L | Δ | 비고 |
|---|---|---|---|
| B0 (VideoMT 1-Linear propagator) | 42.41 | — | official 42.6, 출발선 |
| VI4S inject + deep-sup 배선 | 41.34 | −1.07 | 배선 버그 있었음 |
| + visibility head (aux, only) | 43.14 | +0.73 | B0 첫 추월 |
| + conv1d+residual (구조수정만) | 42.97 | — | h-inert→인과기여 반전([[Decision Log#D1]]) |
| + vis-gate (MaskObs, obs_mask) | 44.17 | — | |
| + correspondence(xattn) | 44.01 | **−0.16** | vis-gate 위에 얹으면 순손해, 폐기 |
| + ordered-sampling 단독 | 43.70 | −0.47 | cross-clip state carry 초반 악영향 |
| **+ ordered + carry-warmup(DAQ 4000iter)** | **45.55** | **+1.38** | **현재 champion(40k)** |

세부: [[Decision Log#D3]], [[vi4s-conv-residual-h-revival]], [[vi4s-ordered-sampling-cross-clip-carry]],
[[vi4s-daq-carry-warmup]]

## 2. 예산(160k) — 아직 definitive 아님, 진행중

| 실험 | mAP_L | 비고 |
|---|---|---|
| champion 40k (hard masked-attn 내내) | **45.55** | 기준 |
| champion 160k (원본, annealing 조기전환) | 43.16 (final) / **48.75 (140k peak)** | hard↔soft confound 발견([[Decision Log#D7]]) |
| 160k, annealing 스케줄 ×4 지연 | 38.68 (32ckpt 평균) / 44.49 (peak) | 원본보다 전지표 열세 — "hard 오래 유지" 가설 반증 |
| **160k, hard 전 구간(annealing OFF)** | 진행중(168, iter~7k/160k) | 세 스케줄 비교의 마지막 축 |

**아직 결론 안 남**: annealing이 예산과 독립인 진짜 레버인지, soft-dwell-time이 핵심 변수인지는
hard-160k 완료 후 판단.

## 3. Masked-attention 이중성 (readout vs continuity)

| | net ΔmAP_L | oracle 천장(re-link 제거) |
|---|---|---|
| masked-attn ON (champion) | 45.55 (기준) | 53.15 |
| masked-attn OFF | 41.33 (**−4.22**) | **59.09** |

**분해**: 이득 +4.22 = readout **−5.94**(lock-in이 마스크 품질을 깎음) + continuity **+10.16**(파편화 방지).
즉 masked-attn의 실질 가치는 identity 학습이 아니라 **연속 프레임 재국소화(공간 접착제)** — 그리고 이게
마스크 품질 상한 자체는 깎는다. 상세: [[Decision Log#D2]], [[vi4s-masked-attention-confound-and-bugfix]]

## 4. State/depth/mamba 변형 (OFF-baseline 기준 ablation)

| 변형 | ΔmAP_L (OFF 기준) | 비고 |
|---|---|---|
| state_dim 64→128 | +1.03 | |
| block2(SSM 2-layer stack) | **+3.04** | OFF 전용 레버 — ON(masked-attn)과 길항(champion+block2=41.84) |
| mamba cell (readout-norm 없음) | −? (KILL 초기판정) | |
| mamba + readout-norm | 42.35 | 조건부 회복(층분업 L0-slow/L1-fast) |

세부: [[vi4s-state-capacity-ablation]]

## 5. Identity/association 축 — 전체가 재역전된 궤적

1. **1차**: contrastive slot embedding(S1)/relink head/M3-B(SyncedSamba) — 전부 KILL, "identity는
   mAP_L과 직교"로 결론.
2. **2차 반전(07-23/24)**: 챔피언 자신의 마스크에 **Identity Oracle**(GT 최적 재배정)을 적용 →
   mAP_L **45.55→53.15(+7.6)**, 순수 re-link 성분 **+11.9**. → headroom은 실재, 과거 KILL은 **구현
   결함**(contrast/relink/M3-B) 때문이었음.
3. **3차(07-24)**: 이 headroom이 **raw 신호로는 안 열림** — mask-IoU 0% capture, SSM state는
   appearance와 redundant(둘 다 baseline 45.54 미달, combo도 무이득). **학습된 refine이 필요.**

| 시도 | 결과 | 판정 |
|---|---|---|
| Identity Oracle (상한 측정) | 45.55→53.15 (+7.6), 순수 re-link +11.9 | 헤드룸 확인 |
| best_slot 대조(FP-suppression만) | 41.28 (−4.27) | re-link 성분과 분리 |
| GT-없는 mask-IoU 재연결 | mAP_L 0.06~0.12 | **0% capture**, 폐기 |
| SSM state (raw cosine) | 37.7 | appearance(40.6)보다 낮고 redundant |
| appearance embedding (raw cosine) | 40.6 | baseline(45.54) 미달 |
| state+embedding combo | ~40.5 | 무이득, redundant 확인 |

세부: [[Decision Log#D4]], [[vi4s-idsw-decomposition-s1-contrastive]]

## 6. Temporal refiner — 3연속 KILL

| Refiner 종류 | 결과 | 판정 |
|---|---|---|
| online-causal residual refiner | 5k≈champion→40k 39.2 | 단조붕괴 KILL |
| decoupled mamba refiner (SyncedSamba, observe-mode) | g10+ reattach 0.00 vs raw 0.44~0.50 | KILL |
| offline bidirectional refiner (자체 head, co-adapt) | peak 44.8 < base 45.55 | KILL (3번째) |

**함의**: "frozen champion 위 refiner로 association/lookahead 보정" 노선 자체가 안 통함. LOMM
offline(54.0)은 co-adapt 전체학습이지 frozen 후처리가 아니라는 확인과 합치. 세부: [[Decision Log#D6]]

## 7. GIA (TCOVIS식 clip-level supervision)

VideoHungarianMatcher_Consistent로 clip 전체 가시 프레임에 대해 한 번의 Hungarian(첫 등장 프레임
대신). 40k 최종 mAP_L **38.82**(궤적 평균 39.2, peak 41.79) — champion(45.55) 못 넘음, annealing
confound와 겹쳐 순수효과는 미측정. 스케일업 보류.

## 8. 현재 진행중인 실험 (2026-07-24 기준)

| 머신 | 실험 | 목적 |
|---|---|---|
| 168 | `vi4s_champion_ytvis22_160k_hard`(annealing OFF, 160k 전구간 hard) | §2 세 스케줄 비교 완성 |
| 171 | `vi4s_position_signal_ytvis22_40k` + shuffle 대조군 | association 축 최종 검증([[Decision Log#D8]]) |

---

## 참고
- 원본 실험 설계(구현 전, DSM/EKVM 가정): [[Idea]], [[Draft]], [[Mechanism-level Novelty Table]]
- 결정 근거/반례: [[Decision Log]]
- raw 세션 기록: `docs/session_log_2026_06_*.md` ~ `docs/session_log_2026_07_24.md` (MNSv2 git repo)
