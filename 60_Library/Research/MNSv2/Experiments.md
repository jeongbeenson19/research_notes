
아래는 “**VIS 메인 기준으로 실험 섹션을 압축**”한 실행 결과야. 그대로 WACV Experiments/Methods에 붙여넣을 수 있게 **구조/조건/지표/어블레이션/통계/테이블**까지 고정했다. (서브 태스크는 _선택_으로만 짧게 넣음)

---

# **II) Experiments (VIS-centered, reviewer-proof)**

## **E1. Task, Baselines, and Scope**

### **E1.1 Main task**

- **Main:** Video Instance Segmentation (**VIS**)
    
- **Goal:** reduce **instance drift / identity inconsistency** under occlusion, view-shift, motion blur, and detector-like missing evidence, using MOT-style **association/reactivation** as an object maintenance mechanism.
    
### **E1.2 What we do not claim**

- We do **not** claim a full neuroscience model. We test **behavioral signatures** aligned with object maintenance: persistence across occlusion, reactivation upon reappearance, interference/capacity effects.
    
### **E1.3 Method variants to compare (core)**

- **Baseline-VIS:** standard VIS model without explicit maintenance (frame/clip-level prediction + conventional linking if any).
    
- **Ours-DSM:** Dynamic Slot Memory (fixed slots + gated write + decay + reactivation/assignment).
    
- **Ours-EKVM:** Episodic Key-Value Memory (episodic bank + retrieval-based reactivation).
    

Backbone setting (fixed unless in ablation):

- VideoMamba temporal backbone used to extract temporally integrated features; heads/readers are controlled across comparisons.
    

---

## **E2. Datasets and Splits**
### **E2.1 Primary dataset (VIS)**

- **YouTube-VIS 2019** (or 2021/2022 if your codebase targets it)
    
    - Use **official train/val split**.
        
    - Report metrics on **val**; optionally provide test submission if available.
        
### **E2.2 Stress-test dataset (optional but strong)**

Choose **one** (don’t over-scope):

- **OVIS** (occlusion-heavy VIS), if you want “occlusion regime” emphasis; OR
    
- a second VIS benchmark aligned to your implementation.
    
> Reviewer defense: one main dataset + one stress-test dataset is sufficient.

---

## **E3. Evaluation Metrics**
### **E3.1 Standard VIS metrics (report as usual)**

- **Video mAP** (overall AP) + AP50/AP75 if standard in that benchmark.
    
### **E3.2 Maintenance-specific metrics (your novelty “shows” here)**

  Define event-centric metrics on top of VIS GT (no new dataset needed).
#### **(M1) Occlusion-aware reactivation latency**
- For each GT instance i, detect a **reappearance time** t_reappear after an occlusion/miss gap (defined below).
    
- Let t_match be the first frame after t_reappear where the prediction assigned to that instance is **consistent** (same slot/track ID mapping) and IoU≥θ.
    
- **Latency(i) = t_match − t_reappear**, with θ=0.5 (mask IoU) or θ=0.3 if masks are noisy.
    
- Report: mean ± std, and histogram (optional).
    
#### **(M2) Recovery@L (long-gap recovery rate)**

- Bucket gaps by length L ∈ {5, 15, 30, 60, 120} frames (or dataset-dependent max).
    
- **Recovery@L** = fraction of occlusion events of length in bucket L for which the model reattaches the same instance within W frames (reactivation window), e.g. W=10.
    
#### **(M3) Event-window AP (occlusion slice)**

- Compute AP but **only on windows** around occlusion events:
    
    - window [t_reappear − w_pre, t_reappear + w_post], e.g. w_pre=5, w_post=15.
        
    
- This isolates “where maintenance matters” instead of letting easy frames dominate.
    
#### **(M4) Capacity–performance curve**

- Sweep K_total ∈ {25, 50, 75, 100, 150} (slots).
    
- Plot/report AP and Recovery@60 vs K_total (table + line plot in paper optional).
    
- Key signature: performance saturates with capacity (human-like constraint analogy, without claiming equivalence).
    

---

## **E4. Event Mining: How we define occlusion/view-shift/blur events (reproducible)**
### **E4.1 Occlusion / miss gap events (no extra labels required)**
For each GT instance i:
- Determine frames where GT mask exists (visible) vs not (absent/out-of-view).
- Define a **gap event** when:
    - visible at t0, absent for L frames, visible again at t1=t0+L+1.    
- Use only gaps with L≥5 for maintenance evaluation.
    
### **E4.2 View-shift proxy (no PTZ logs required)**
Define a view-shift score per frame:
- s_view(t) = mean_{pixels} ||Flow_t|| (optical flow magnitude) OR global homography residual.
    
- View-shift event occurs when s_view(t) exceeds a percentile threshold (e.g., top 5% frames).
    
- Evaluate event-window AP around these frames (similar window slicing).
    
### **E4.3 Motion blur proxy**

- Use a simple blur estimator (e.g., variance of Laplacian) on the frame or ROI.
    
- Define blur events as bottom 10% sharpness.
    
- Again, slice evaluation windows.

> Reviewer defense: all event definitions are **algorithmic proxies** and reproducible; not claiming ground-truth blur labels.

---

## **E5. Experimental Conditions (Main comparisons)**
### **E5.1 Models compared (fixed)**

- **Baseline-VIS (no maintenance):** same backbone + same mask head, but:
    
    - no slot memory, no decay/freeze, no reactivation assignment.
        
    
- **Ours-DSM:** full system with slot memory + write-control + reactivation assignment.
    
- **Ours-EKVM:** full system with episodic bank + retrieval + reactivation assignment.
    
### **E5.2 Fairness controls**

- Same detector/proposal source (if used), same training schedule, same augmentations.
    
- Same VideoMamba variant unless testing “backbone ablation”.
    
---

## **E6. Ablations and Controlled Tests (≥ 6, VIS-focused)**

(이 섹션이 리뷰어 설득의 핵심이야. “왜 좋아졌는지”를 분해해서 보여줘야 함.)
### **A1) Memory type**

- DSM vs EKVM vs None.
    
### **A2) Write-control ablation (freeze)**

- **−Freeze:** always update prototype/slot state (no quality gate).
### **A3) Decay ablation**

- **−Decay:** reliability fixed; no uncertainty growth.
    
### **A4) Reactivation/assignment ablation**

- **−Reactivation:** drop dormant slots after short timeout; no long-gap reattachment.
    
### **A5) Score fusion ablation**

- Only appearance / only spatial / only context
    
- Demonstrates that “association philosophy” is not just one cue.
    
### **A6) VideoMamba necessity ablation (critical)**

- Replace VideoMamba with:
    
    - per-frame backbone (no temporal integration), OR
        
    - a standard video transformer (if feasible).
        
    
- Report AP and maintenance metrics under long gaps / view-shifts.
    
### **A7) Capacity sweep (behavioral signature)**

- K_total sweep table.
    
### **A8) Synthetic perturbation test (psychophysics-style, optional but strong)**

Apply controlled corruptions on validation videos:

- (i) Cutout occluders on target instances for L frames
    
- (ii) Blur kernels during intervals
    
- (iii) Homography bursts
    
    Report Recovery@L and latency shifts.
    

---

## **E7. Training Protocol (kept minimal, reproducible)**

- Clip length: **T=8** (train), inference can be streaming.
    
- Optimizer: AdamW
    
    - head lr: 3e-4, backbone lr: 3e-5 (fine-tune stage)
        
    - weight decay: 1e-4
        
    
- Epochs: 30 (heads) + 20 (fine-tune) or a single 50-epoch schedule
    
- Augmentations:
    
    - cutout occlusion (p=0.3)
        
    - motion blur (p=0.3)
        
    - mild homography jitter (p=0.2)
        
    - frame drop (p=0.1) to simulate missing evidence
        
    

---

## **E8. Statistical Reporting**

- Run **3 seeds** for key variants: Baseline, DSM, DSM−Freeze, DSM−Decay, DSM−Reactivation.
    
- Report **mean ± std** for:
    
    - AP, Event-window AP, Recovery@60, Latency.
        
    
- Significance:
    
    - paired test over videos or over events (Wilcoxon recommended for latency distributions).
        
    

---

## **E9. Results Table Templates (VIS-only, ready to fill)**

### **Table 1 — Main VIS metrics**

|**Method**|**Backbone**|**Memory**|**AP ↑**|**AP50 ↑**|**AP75 ↑**|**FPS ↑**|
|---|---|---|---|---|---|---|
|Baseline-VIS|VideoMamba|None|||||
|Ours-EKVM|VideoMamba|EKVM|||||
|Ours-DSM|VideoMamba|DSM|||||
### **Table 2 — Maintenance metrics (occlusion-focused)**

|**Method**|**Event-AP(occ) ↑**|**Latency ↓**|**Recovery@15 ↑**|**Recovery@30 ↑**|**Recovery@60 ↑**|**Recovery@120 ↑**|
|---|---|---|---|---|---|---|
|Baseline-VIS|||||||
|Ours-EKVM|||||||
|Ours-DSM|||||||

### **Table 3 — Ablations (mechanism isolation)**

|**Variant**|**AP ↑**|**Event-AP(occ) ↑**|**Latency ↓**|**Recovery@60 ↑**|**Notes**|
|---|---|---|---|---|---|
|Full (DSM)||||||
|−Freeze||||||
|−Decay||||||
|−Reactivation||||||
|Appearance-only||||||
|Spatial-only||||||

### **Table 4 — Capacity sweep (behavioral signature)**

|**K_total**|**AP ↑**|**Event-AP(occ) ↑**|**Recovery@60 ↑**|**Latency ↓**|
|---|---|---|---|---|
|25|||||
|50|||||
|75|||||
|100|||||
|150|||||

### **Table 5 — Backbone ablation (VideoMamba justification)**

|**Backbone**|**AP ↑**|**Event-AP(occ) ↑**|**Recovery@60 ↑**|**FPS ↑**|
|---|---|---|---|---|
|VideoMamba|||||
|Per-frame backbone|||||
|Video Transformer (optional)|||||

---

## **E10. Minimal “Sub-task” extension (optional, keep it short)**


**Only if you want a second task** without scope explosion:

- Pick **STVG** (or RVOS) and reuse the same maintenance core.
    
- Report only:
    
    - main metric (tube IoU / grounding acc)
        
    - Maintenance metrics: latency + Recovery@L on reappearance events (defined via GT tube continuity)
        
    
- Keep experiments to **1 table + 2 ablations** (Full vs −Freeze vs −Reactivation).
    

---

원하면, 다음 단계로 (iii)인 **관련연구 대비표(novelty table)**를 “동작 단위”로 작성해줄게. (열: slot 유지/episodic bank/write-control/explicit reactivation/event-centric eval/VideoMamba-long-context)