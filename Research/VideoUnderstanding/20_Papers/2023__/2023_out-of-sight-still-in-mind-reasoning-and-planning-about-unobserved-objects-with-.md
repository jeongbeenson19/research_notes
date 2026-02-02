---
type: paper
title: "Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models"
venue: ""
year: 2023
authors: ["Yixuan Huang", "Jialin Yuan", "Chanho Kim", "Pupul Pradhan", "Bryan Chen", "Li Fuxin", "Tucker Hermans"]
url: "https://arxiv.org/abs/2309.15278v3"
tasks: []
methods: ["memory", "retrieval"]
datasets: []
metrics: []
trends: []
status: to-read
date_read: ""
---

# Main Contribution (3 lines)
1) **What**: Propose DOOM and LOOM memory models that encode object-centric trajectory history using transformer relational dynamics from partial-view point clouds with an object discovery/tracking engine.
2) **Why**: Robots need memory of occluded objects to reason and plan reliably in realistic environments.
3) **Impact**: Improves reasoning about occluded/novel/reappearing objects and outperforms an implicit memory baseline in simulation and real-world experiments.

## Method (<=5 bullets)
- Object discovery and tracking engine provides object-centric tracks from partial-view point clouds.
- Transformer relational dynamics encode trajectory history into a memory for planning.
- Memory is integrated into a multi-object manipulation reasoning/planning framework.

## Evidence
- Benchmarks: simulation and real-world multi-object manipulation experiments (per abstract).
- Key numbers: not specified in abstract.
- Key ablations (2):
  - Not specified in abstract.
  - Not specified in abstract.

## Assumptions / Limitations (2 each)
- Assumptions:
  - Partial-view point clouds and an object discovery/tracking engine are available.
- Limitations:
  - Not specified in abstract.

## Failure Modes (3)
- Not specified in abstract.
- Not specified in abstract.
- Not specified in abstract.

## One-liner takeaway
- DOOM/LOOM add object-centric memory that helps robots plan despite occlusions.

## Next experiment idea (1)
- Stress-test with longer occlusions and heavier clutter in real-world scenes.
