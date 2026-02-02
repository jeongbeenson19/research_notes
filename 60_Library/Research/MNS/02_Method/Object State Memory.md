---
title: Object State Memory 정의
tags: [memory, belief, state, tracking]
---

# Object State Memory (per-object slot)
각 객체 i에 대해 상태를 유지한다.

## State 구성(후보)
- Location state: (bbox, velocity) + **belief distribution p(x,t)**
- Appearance state: prototype set / snapshot bank
- Semantic state: (category, attribute, action, group relation 중 1~2개만)
- Uncertainty: location/appearance/semantic 신뢰도 + decay schedule

## Update / Freeze / Decay 규칙(초안)
- Update: 관측 품질이 좋을 때만 업데이트 (low occlusion, high conf)
- Freeze: occlusion/blur/high crowd에서 appearance 업데이트 억제
- Decay: unobserved interval 길이에 따라 uncertainty 증가, prior 영향 감소

## Reactivation(재활성화) 개념
- Memory slot을 검색하여 새 관측을 기존 객체에 연결(assignment)
- 강주입(injection)보다 **candidate gating / score fusion** 중심으로 설계