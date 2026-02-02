---
title: 평가 프로토콜 초안
tags: [evaluation, protocol, reactivation, ids]
---

# 핵심: 사건 중심(event-based) 평가
평균 지표만 보지 않고 “관측 단절 → 재등장” 사건을 추출하여 평가한다.

## 1) Unobserved interval 정의
- tracklet A 종료 t_end
- tracklet B 시작 t_start
- gap = t_start - t_end - 1
- (GT 가능하면) 동일 ID인 경우를 re-activation 사건으로 취급

## 2) Gap-length bucket (초안)
- S: 0–15 frames
- M: 16–60 frames
- L: 61–180 frames
- XL: 181+ frames

## 3) Reactivation window 평가
- 재등장 시점 기준 ±K frames에서
  - IDS 발생 빈도
  - false merge
  - re-activation 성공률
  - IDF1/HOTA의 국소 변화(가능하면)

## 4) View-shift(선택: PTZ 강조)
- 카메라 운동이 큰 구간을 이벤트로 태깅(로그가 있으면 로그, 없으면 영상 기반)
- 이벤트 전후 구간에서만 성능을 별도로 보고