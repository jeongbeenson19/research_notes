---
title: 결정 로그 (MNSv2 / VI4S)
type: decision-log
status: 🟩 Active
tags:
  - decisions
  - design
  - ablation
topics:
  - VIS
  - SSM
  - VideoInstanceSegmentation
updated: 2026-07-24
---

# 사용 규칙
- [[MNS(Workflow)|MNS]]의 Decision Log 포맷을 이 프로젝트(MNSv2/VI4S, 실제 구현·실험 단계)용으로 차용.
- 결정 1개당: 후보 → 결정 → 근거(실측 수치+세션로그 날짜) → 반례(실패한 대안) → 구현 메모(파일 경로).
- 이 문서는 `docs/session_log_YYYY_MM_DD.md`(git repo, 코드와 같이 버전관리)와 Claude auto-memory(`MEMORY.md`)를
  압축한 것 — raw 기록은 그쪽에 있고, 여긴 "지금 결론이 뭔가"만 담는다. **`updated` 날짜보다 새 session_log가
  있으면 이 문서가 stale일 수 있음.**

---

## D1. Query propagation: 1-Linear vs Selective SSM
- **후보**: VideoMT(B0)의 1-Linear propagator / EoMT+Selective SSM(Mamba류, query-slot당 state) 주입
- **결정**: Selective SSM 채택(VI4S). 단 conv1d+residual 없는 초기형은 h-inert(무기여)로 나왔다가,
  conv+residual 추가 후 인과기여가 통계적으로 확정됨(wipe-h 짝비교, half-life +0.79, 71편 중 46편,
  sign-test p<1e-11).
- **근거**: 순수 구조수정만으로 mAP_L 41.34→**42.97**(B0/VideoMT 공식 42.6 첫 추월). conv1d 부재 시
  "선택 파라미터가 순간 x_t만 보고 국소 시간 텍스처를 못 씀"이라는 진단이 맞았음.
- **반례**: 1-Linear(B0)도 OVIS에서 online-SOTA급 — SSM이 무조건 이기는 게 아니라, association을
  raw state로 하려는 여러 시도(M3-B SyncedSamba 등)는 반복 KILL됨(D4 참고).
- **구현 메모**: `VI4S/models/ssm_cell.py`(SSMCell, conv+residual), `VI4S/models/query_ssm_fusion.py`.
  [[vi4s-conv-residual-h-revival|conv+residual 반전 결과]] · [[Mamba- Linear-Time Sequence Modeling with Selective State Spaces]]

---

## D2. Masked-attention: 유지 vs 제거
- **후보**: EoMT의 프레임별 hard masked-attn(예측 마스크 영역으로 쿼리 attention 제한) 유지 / 제거
- **결정**: 유지하되, **이중성(two-face)을 인지하고 다룬다**. 순net효과는 +4.22(ON 45.55 vs OFF 41.33)지만
  분해하면 **readout −5.94(lock-in이 마스크 품질 자체를 깎음) + continuity +10.16(파편화 방지)**. 이득의
  실체는 "연속성 접착제"지 identity 학습이 아님.
- **근거**: Identity Oracle을 ON/OFF 양쪽에 적용해 순수 association 제거한 천장 비교 —
  **O_ON=53.15 < O_OFF=59.09**(OFF 쪽 마스크 품질 천장이 더 높음, 슬롯 수 10/영상 동일이라 cherry-pick
  아님). idsw 정량분해로도 masked-attn 이득의 90%가 연속 binding, 10%만 permanence.
- **반례**: OFF 단독은 net −4.22(41.33)라 그냥 끄면 손해. "readout은 순수 이득"이 아니라 **hard 마스킹이
  lock-in을 유발해 마스크 품질 자체를 깎는다**는 게 핵심 — 그래서 D7(annealing)이 나옴.
- **구현 메모**: `MODEL.VI4S.MASKED_ATTN_ENABLED`. [[vi4s-masked-attention-confound-and-bugfix]]

---

## D3. 챔피언 레시피 사다리 (conv+residual → vis-gate → ordered+warmup)
- **후보**: visibility-only / +correspondence(xattn) / +ordered-sampling 단독 / +carry-warmup 병행
- **결정**: **conv+residual + vis-gate + ordered-sampling + carry-warmup(DAQ 4000iter 지연)** 조합이
  현재 40k champion(**mAP_L 45.55**, 공식 gt_long 71편).
- **근거(사다리, 전부 40k, 같은 harness)**:

  | 구성 | mAP_L | 비고 |
  |---|---|---|
  | B0(1-Linear) | 42.41 (official 42.6) | 출발선 |
  | VI4S inject + deep-sup 배선 | 41.34 | B0 −1.07, 아직 미달 |
  | + visibility-only | 43.14 | B0 첫 추월 (+0.73) |
  | + conv+residual(구조수정만) | 42.97 | h-inert 반전(D1) |
  | + vis-gate | 44.17 | 그 시점 최고 |
  | + correspondence(xattn) | 44.01 | **−0.16 순손해**, 이후 correspondence는 안 씀 |
  | + ordered-sampling **단독** | 43.70 | vis-gate-only 대비 **−0.47** |
  | + ordered **+ carry-warmup** | **45.55** | **신규 최고**(vis-gate-only 대비 +1.38) |

  ordered-sampling 단독은 손해(cross-clip state carry가 초반엔 나쁜 state를 물려줌), DAQ식 4000iter
  cold-start warmup을 병행해야 순이득으로 전환 — "구성요소 하나만 보면 오판" 사례.
- **반례**: correspondence(xattn) — vis-gate 위에 얹으면 −0.16으로 순손해, 사용 안 함.
- **구현 메모**: `configs/vi4s_v2_inject.yaml`(_BASE_) + `MODEL.VI4S.{USE_VISIBILITY_GATE,ORDERED_CARRY_WARMUP_ITERS}`,
  `INPUT.ORDERED_VIDEO_SAMPLING`. [[vi4s-ordered-sampling-cross-clip-carry]] · [[vi4s-daq-carry-warmup]]

---

## D4. Identity/association: explicit 모듈이 필요한가
- **후보**: contrastive slot embedding(S1) / relink head / M3-B(SyncedSamba, tracklet-indexed state) /
  아무것도 안 하고 masked-attn+SSM의 암묵적 continuity에 맡김
- **결정(궤적, 여러 번 뒤집힘)**:
  1. 최초: contrast/relink 등 explicit 모듈 전부 KILL(mAP_L 무변화~손해) → "identity는 mAP_L과 직교"로 결론.
  2. **07-23/24 재반전**: 챔피언 자신의 per-frame 마스크에 Identity Oracle(GT 기준 최적 재배정)을 적용하니
     mAP_L **45.55→53.15(+7.6)**, 순수 re-link 성분만 **+11.9**(FP-suppression 격리). → **explicit identity가
     무용했던 게 아니라, 그동안의 구현(contrast/relink/M3-B)이 전부 결함이 있었을 뿐 — headroom은 실재하고 크다.**
  3. 단 07-24 확인: 이 headroom은 **raw 신호(mask-IoU/appearance/SSM state 어느 것도) bolt-on 재연결로는
     안 열림** — mask-IoU 0% capture(챔피언 마스크 연속프레임 self-IoU 0.35, 공간이 불안정), SSM state는
     appearance와 redundant(둘 다 raw cosine으로 baseline 45.54를 못 넘음). **학습된 refine이 필요**하다는
     결론으로 수렴(D6/D8).
- **근거**: `tools/identity_oracle_apL.py`, `tools/rethread_feat.py`(state 37.7 / embed 40.6 / combo ~40.5,
  전부 baseline 45.54 미달).
- **반례**: OVIS에서는 Identity Oracle이 +121%(YTVIS +4%와 대비) — association이 데이터셋에 따라
  1차 레버가 되기도 함(occlusion 밀도 차이로 추정).
- **구현 메모**: [[vi4s-idsw-decomposition-s1-contrastive]] (전체 궤적), [[vi4s-memory-thesis-partial-falsification]]
  · [[Learning to Track with Object Permanence]] · [[XMem Long-Term Video Object Segmentation with an Atkinson-Shiffrin Memory Model]]

---

## D5. mAP_L 축 우선순위 확정: mask-readout vs identity
- **후보**: 남은 연구 노력을 (a) mask-readout/coverage 축(annealing, 예산, state capacity)에 쏟을지
  (b) explicit association/identity 축에 쏟을지
- **결정**: **mask-readout 축이 확인된 1순위**(annealing 커리큘럼으로 45.55→48.75 실측). association 축은
  D4/D8에서 보듯 시도한 노선(온라인 refiner·오프라인 refiner·GIA·bolt-on rethread)이 전부 무이득/KILL로
  귀결 — 이번 세션(position/motion 신호, D8)이 마지막 검증.
- **근거**: idsw 정량분해 — masked-attn 이득 90%가 continuity(=mask-readout 인접 개념), 10%만 permanence.
- **반례**: 없음(이 결정은 누적 증거 기반, 단일 반례 아님).
- **구현 메모**: [[vi4s-idsw-decomposition-s1-contrastive]] §mAP_L 1순위 확정.

---

## D6. Temporal refiner 전략: online-causal → decoupled mamba → offline bidirectional (3연속 KILL)
- **후보**: (1) frozen champion 위 online-causal residual refiner, (2) decoupled mamba refiner(M2/M3
  계열, SyncedSamba observe-mode), (3) frozen champion 위 양방향(offline) refiner + 자체 head(co-adapt)
- **결정**: **셋 다 KILL** — 이 방향(frozen base + refiner로 association/temporal 보정) 자체가 안 통함.
  1. online-causal refiner: 단조 붕괴(5k≈champion→10k noise peak→40k 39.2).
  2. SyncedSamba(observe-mode, MaskObs+obs-dropout+synced): 20k full training 후 g10+ reattach
     0.00(vs raw 0.44~0.50), 2번째 독립 실패.
  3. offline bidirectional refiner(양방향 attn+object self-attn+cross-attn to raw memory+자체 head):
     171에서 40k(T=24) 완주, **peak 44.8 < base champion 45.55** → 3번째 실패.
- **근거**: LOMM offline(54.0)은 co-adapt 전체학습이지 frozen 후처리가 아니라는 확인과 합치 — "frozen
  base 위 refiner"라는 구조 자체가 LOMM 격차(online 48.2/48.75 parity → offline +5.8)를 재현 못 함.
- **반례**: 없음 — 세 아키텍처(causal/synced-state/bidirectional-own-head)가 서로 다른 실패 요소를
  제거하며 시도됐는데도 전부 KILL이라, "frozen+refiner" 접근 자체의 구조적 한계로 본다.
- **구현 메모**: `VI4S/models/{temporal_refiner,offline_refiner}.py`. [[vi4s-offline-refiner-design]]
  (★★KILL 확정 갱신됨) · `docs/session_log_2026_07_20.md` §1 · `docs/session_log_2026_07_23.md` §2

---

## D7. mask-annealing: confound인가 레버인가 (진행중, 미확정)
- **후보**: hard→soft masked-attn 전환(annealing)이 (a) 예산 비교를 오염시키는 나쁜 confound인지
  (b) 의도적으로 쓸 만한 커리큘럼(레버)인지
- **결정(아직 확정 아님, 07-24 기준 최신 이해)**:
  1. 챔피언 40k(45.55)=hard 내내 / 160k(43.16)=iter~74k부터 soft — 이게 예산이 아니라 hard↔soft
     confound임을 ckpt buffer(`attn_mask_probs`)로 확정.
  2. 07-23 재해석: annealed-140k(mAP_L 48.75, 전 변종 최고)의 오라클 천장이 57.85로 hard-40k(53.15)보다
     높음 → "hard-first로 association 확립 + soft로 마스크 품질 회복 = best-of-both" 가설.
  3. **07-24 반증**: 이 가설이 맞다면 hard를 예산 비례로 더 오래 유지(×4 지연 스케줄)하면 더 좋아야
     하는데, 실측은 **정반대**(원본 조기전환 32ckpt평균 41.92 > 지연스케줄 38.68, peak 48.75 > 44.49).
     → "hard 지속기간"이 아니라 **"soft 전환 후 적응에 쓴 학습량(soft-dwell-time)"**이 진짜 변수일 가능성.
- **근거/반례**: 위 3번이 2번 가설의 직접 반례. **미확정 — hard-160k(전 구간 hard, soft-dwell=0) 대조
  실험이 168에서 진행 중**, 세 스케줄(조기전환/지연/무전환)이 갖춰져야 결론 가능.
- **구현 메모**: `configs/vi4s_champion_ytvis22_160k_{annealing,hard}.yaml`. [[vi4s-mask-annealing-confound]]

---

## D8. Association headroom(+7.6) 회수 경로 (association 축 최종 검증, 진행중)
- **후보**: (a) GT 없는 mask-IoU/appearance/state bolt-on re-thread, (b) TCOVIS식 clip-level GT 지도
  (GIA), (c) frozen base 위 학습 refiner(D6, 전부 KILL), (d) SSM 입력에 위치/동역학 신호 주입
- **결정(진행중)**:
  - (a) mask-IoU: **0% capture**(공간 불안정, self-IoU 0.35) → 폐기.
  - (a) SSM state(raw cosine): appearance와 **redundant**(둘 다 baseline 45.54 미달, combo도 무이득)
    → "SSM state가 same-category dynamics를 잡는다"는 명분 닫힘. 학습 re-linker는 appearance 기반이어야.
  - (b) GIA(clip-level Hungarian, VideoHungarianMatcher_Consistent): 40k 최종 38.82, 예산 내
    annealing confound와 겹쳐 순수효과 미측정, champion 못 넘음.
  - (c) refiner 3종: D6에서 전부 KILL.
  - (d) **position/motion 신호**(mask soft-centroid+area를 SSM in_proj에 학습형 projection으로 주입,
    conv1d가 국소차분/속도유사 신호를 유도할 능력이 있는지 검정): 구현+GPU smoke 통과, 171에서
    real-arm + shuffle-control(§6 필수 대조군) 40k 학습 착수(2026-07-24). **결과 미정.**
- **근거**: (a)(b)(c) 전부 무이득/KILL 확인됨 — association 축에서 유일하게 미시험이던 게 "동역학
  원재료(위치) 부재" 가설. 이걸로 association 축 전체를 열거나 최종 종결.
- **kill 기준**: gap-idsw 개선 + conv커널 유한차분패턴 + shuffle대조군 유의성, **셋 다** 필요. 하나라도
  실패 시 "SSM이 동역학을 배운다" 노선을 motion 부재 변명 없이 최종 종결 → association 축 전체 닫고
  D5(mask-readout 축)에 집중.
- **구현 메모**: `VI4S/models/query_ssm_fusion.py`(pos_proj), `VI4S/vi4s_model.py`(_soft_centroid_pos_feat),
  `scripts/smoke_position_signal_integration.py`. [[vi4s-position-motion-signal-impl]]
