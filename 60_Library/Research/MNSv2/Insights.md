---
title: Insights (MNSv2 / VI4S)
type: insights
status: 🟩 Active
updated: 2026-07-24
---

## 지금 결론 (2026-07-24 기준, 상세는 [[Decision Log]] · [[Experiments]])
- champion: EoMT+Selective SSM(conv+residual) + vis-gate + ordered-sampling + carry-warmup, YTVIS22
  gt_long mAP_L **45.55**(40k), 160k는 아직 확정 안 됨(annealing 스케줄 실험 진행중).
- masked-attention은 identity 학습이 아니라 **연속 프레임 재국소화(공간 접착제)**로 이득을 낸다 —
  단 그 lock-in이 마스크 품질 상한 자체는 깎는다(이중성, [[Decision Log#D2]]).
- **explicit identity/association headroom은 실재하고 크다(+7.6, Identity Oracle)** — 과거 "identity는
  mAP_L과 무관"이라는 결론은 구현 결함(contrast/relink/M3-B) 때문이었지 진짜 무관해서가 아니었음.
- 단 이 headroom은 **raw 신호(mask-IoU/appearance/SSM state) bolt-on으로는 안 열림** — SSM state는
  appearance와 redundant. Refiner 3종(online/mamba/offline)도 전부 KILL. 회수하려면 학습된 refine 필요.
- 현재 1순위 레버는 **mask-readout 축**(annealing 커리큘럼, 예산) — association 축은 마지막 검증
  (position/motion 신호 주입)이 진행중, 실패하면 최종 종결.

## State Space Model - Update Eq.
https://chatgpt.com/share/69b8b5b8-23bc-8007-a808-0722b1b7b24a