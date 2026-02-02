---
type: paper
title: "Video-XL: Extra-Long Vision Language Model for Hour-Scale Video Understanding"
venue: "CVPR"
year: 2025
authors:
  - Yan Shu
  - Zheng Liu
  - Peitian Zhang
  - Minghao Qin
  - Junjie Zhou
  - Zhengyang Liang
  - Tiejun Huang
  - Bo Zhao
url: "https://openaccess.thecvf.com/content/CVPR2025/papers/Shu_Video-XL_Extra-Long_Vision_Language_Model_for_Hour-Scale_Video_Understanding_CVPR_2025_paper.pdf"
tasks:
  - benchmark
  - long-video
methods:
  - compression
  - retrieval
datasets: []
metrics: []
trends: []
status: to-read
date_read: ""



---

# Main Contribution (3 lines)
1) **What**: 비디오 이해를 위한 새로운 모델/학습/프롬프트 방법을 제안.
2) **Why**: 긴 비디오 이해를 위해 메모리/토큰/검색 효율을 높이는 방법을 제안.
3) **Impact**: 장시간, 효율 측면에서 비디오 이해/평가를 확장.

## Method (<=5 bullets)
- 문제 설정에 맞춘 비디오 이해 파이프라인/모델 구성을 제안.

## Evidence
- Benchmarks: MLVU, Video-MME, VNBench, LongVideoBench, Video-Vista, VideoChatGPT Benchmark, MVBench, Needle-in-a-Haystack.
- Key numbers: 16x 압축에서도 손실 최소; 단일 A100 GPU에서 2048 프레임 처리; Needle-in-a-Haystack 95% 정확도.
- Key ablations (2):
  - 16x 고정 비율에서 압축 기법 비교(Table 2).
  - 압축 비율(2x/4x/8x/16x)별 성능 변화로 견고성 평가.

## Assumptions / Limitations (2 each)
- Assumptions:
  - 구간별 정보 밀도 추정이 실제 시각 복잡도를 잘 반영한다.
  - VST 요약이 긴 시간 범위에서도 과제 관련 단서를 보존한다.
- Limitations:
  - 구간 간 압축 오류 누적으로 세밀한 검색/추론이 악화될 수 있다.
  - 장시간 비디오 지시 데이터에 의존하며 합성 데이터 편향 가능성.

## Failure Modes (3)
- 정보가 희박한 구간에서 과도한 압축으로 드문/미세 이벤트를 놓침.
- VST 요약이 모호하면 시간적으로 먼 사건을 혼동.
- 프레임 단위 정밀 위치 추정이 필요한 과제에서 성능 저하.

## One-liner takeaway
- Video-XL: Extra-Long Vision Language Model for Hour-Scale Video Understanding은/는 긴 비디오 이해를 위해 메모리/토큰/검색 효율을 높이는 방법을 목표로 한다.

## Next experiment idea (1)
-
