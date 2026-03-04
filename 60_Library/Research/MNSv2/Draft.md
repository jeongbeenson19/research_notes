
# Contribution
---

1. **Task-agnostic Object Maintenance Core (Memory + Reactivation-as-Association)**
    
    We introduce a task-agnostic _object maintenance core_ that maintains per-object slot states (appearance/semantic prototypes, spatial belief, and reliability) and performs explicit reactivation via candidate gating, score fusion, and one-to-one assignment, enabling stable identity/instance continuity across occlusion, out-of-view, and detector failures in spatiotemporal video tasks (VIS as the primary target).
    
2. **Quality-controlled Write Mechanism to Prevent Memory Corruption (Freeze/Decay)**
    
    We propose a quality-controlled write mechanism that selectively freezes or decays slot updates under blur/occlusion/view-shift-induced uncertainty, preventing prototype drift and reducing ID/instance switching; this turns “association” from a purely matching heuristic into a controlled memory update process that better aligns with the functional requirements of human object maintenance.
    
3. **Event-centric Evaluation for Human-like Maintenance Behaviors + Efficient Temporal Backbone (VideoMamba)**
    
    We provide an event-centric evaluation protocol (gap-length buckets, reactivation windows, and view-shift slices) that directly measures maintenance behaviors—reactivation latency, long-gap recovery, and capacity–performance trade-offs—beyond aggregate task metrics, and we show that VideoMamba-based temporal features improve both efficiency and long-context robustness when paired with the proposed maintenance core.

---

# Idea Eval.
---

## **1) 주제 매력의 핵심: ‘MOT 철학’을 MOT 밖으로 확장하는 지점**

VIS/grounding 같은 task는 대체로

- per-frame 예측이 흔들리고(flicker),
    
- occlusion/view-shift에서 대상이 바뀌거나 끊기고,
    
- 장기 컨텍스트에서 drift가 누적되는 문제가 많아.
      

여기에 “association = 지속성 유지(maintenance) 메커니즘”이라는 관점으로

- **상태 유지(메모리)**
    
- **오염 방지(write-control)**
    
- **재활성화(reactivation)**
    
    를 명시적으로 얹는 건 “단순히 모델 크기 키우기”랑 다른 **설계 중심 해결**이라 주제 매력이 있다.
    

---

## **2) 리뷰어가 좋아할 매력 포인트 2개**

### **A) “문제 자체가 분명함”: occlusion/view-shift/blur에서의 실패는 모두가 공감**


이건 실제로 정성 결과에서 눈에 띄고, 데이터셋 편향을 떠나 일반적인 고질병이야.

→ 즉, **문제 공감대가 넓다**는 점이 강점.

### **B) “평가를 바꿔서 기여를 보이게 할 수 있음”**

VIS나 grounding은 평균 mAP/IoU만 보면 “왜 좋아졌는지”가 흐려지는데,
네가 말한 **event-centric 평가(occlusion length, reactivation window)**를 넣으면
“우리는 장기 단절에서 좋아졌다”를 설득력 있게 보여줄 수 있어.

→ 주제 매력은 **성능 자체**보다 “현상을 계량화하는 관점”에서도 나온다.

---

## **3) 동시에 위험한 지점(매력 떨어질 수 있는 이유)**

### **A) “이미 다들 memory를 쓰는데?”라는 피로감**

메모리, 쿼리, 프로파게이션은 이미 흔해서,
너의 스토리가 “메모리 하나 더”처럼 보이면 매력이 급격히 떨어져.

**그래서 매력 포인트는 메모리 자체가 아니라**

- **write-control(오염 방지) + reactivation을 명시적으로 설계**
    
- **현상(가림/시프트/블러)의 발생 기전을 제약 신호로 사용**
    
- **이벤트 기반 평가로 행동 서명까지 제시**
    
    여기서 나와야 해.

### **B) “인지 주장”이 과하면 역효과**

“human object maintenance를 재현”을 강하게 말하면
리뷰어가 바로 인지과학 근거를 요구하거나 과장으로 본다.

매력을 살리려면 톤을:

- “동일하다”가 아니라 **“기능적으로 근사/유사한 계산 패턴”**
    
- “뇌를 설명”이 아니라 **“설계 원리로부터 영감”**
    
    쪽으로 잡는 게 안전.

---

## **4) 한 문장 평가(주제 매력 총평)**

- **매력 있음**: “spatiotemporal video task에서 ‘지속성’을 설계적으로 다루고, 그걸 이벤트 중심으로 계량화한다”는 메시지가 분명하고 수요가 큼.
    
- **성패는 포지셔닝**: “메모리 추가”가 아니라 “오염 방지형 유지+재활성화라는 ‘유지 시스템’”으로 보이게 해야 매력이 살아남음.
    
---

# Threats
---

## **A. 치명(Reject 트리거가 될 수 있는 포인트)**

### **A1) “MOT 철학 차용”이 너무 포괄적이고 새로움이 불명확**

- **공격:** VIS/VOS/RVOS/STVG는 원래 메모리/프로파게이션/쿼리 기반 추적이 흔하다. “association 철학”이라고 해도 이미 **MinVIS/EfficientVIS/SeqFormer/XMem/각종 grounding 메모리**가 유사한 일을 한다. 너의 기여가 _정확히 무엇_인지 불분명하다.
    
- **왜 약함:** 지금 draft는 “우리는 object-slot memory + reactivation 한다” 수준이라, 기존의 query propagation 또는 memory bank와 구분이 흐림.
    
- **방어/수정:**
    
    1. **명시적 사건 중심(occlusion/view-shift/blur) 제약 + write-control(Freeze/Decay) + reactivation window 평가**를 “핵심 기여”로 고정
        
    2. 기존과 비교표를 “동작 수준”으로: _업데이트 제어(오염 방지) 유무_, _재활성화 정책의 명시성_, _이벤트 슬라이스 평가 유무_를 열로 만들어 차별을 못 박아야 함.
        
    
### **A2) 범용 프레임워크 주장 vs 실험 설계의 현실성(스코프 과대)**

- **공격:** VIS/VOS/RVOS/STVG를 모두 포괄한다고 했는데, 각 태스크는 데이터/지표/출력(마스크·튜브·모먼트)이 다르다. 한 논문에서 모두 “제대로” 보여주기 어렵다. 결과적으로 어느 태스크에서도 SOTA급 설득력을 못 낼 가능성이 크다.
    
- **왜 약함:** WACV에서는 “범용” 주장에 비해 실험이 빈약하면 바로 깎인다.
    
- **방어/수정:**
    
    - **메인 태스크 1개 + 서브 1개**로 축소(예: VIS 메인, STVG 서브)
        
    - “모듈은 범용”은 주장하되, 실험은 **2개 태스크**에서만 깊게(특히 이벤트 평가) 파라야 함.
        
    
### **A3) “VideoMamba가 왜 필요한가?”가 약함(백본 교체 수준)**

- **공격:** VideoMamba는 그냥 백본이다. 네 성능은 사실 association/memory에서 나오는데, VideoMamba를 쓰는 이유가 “효율” 외에 명확하지 않다. 평범한 ViT/VideoSwIN/TimeSformer로도 되지 않나?
    
- **왜 약함:** 백본 기여가 없으면 “조합 논문”으로 보임.
    
- **방어/수정:**
    
    - “VideoMamba는 긴 컨텍스트에서 **이벤트 주변 히스토리 요약**을 싸게 제공해서 reactivation에 유리” 같은 **정량 가설** 필요
        
    - **백본 ablation(비디오 Transformer vs VideoMamba)** + **긴 T에서 효율/성능 곡선**을 반드시 제시.
        
    
### **A4) “인간 object maintenance 근사” 주장에 대한 증거 부족**

- **공격:** 인간 object permanence를 얘기하지만, 모델이 인간 행동과 닮았다는 실증이 없다. 단지 occlusion 성능이 좋아졌다고 “인간 근사”라고 말하는 건 과장이다.
    
- **왜 약함:** 인지 주장(approximation)을 하려면 최소한 “행동적 서명(behavioral signature)”이 있어야 함.
    
- **방어/수정:**
    
    - **행동 서명 2~3개를 명시**: (i) occlusion length에 따른 성능 저하 곡선 형태, (ii) capacity(K_total) 증가에 따른 포화, (iii) reactivation latency 분포
        
    - 이 곡선을 “인간과 동일”이라고 말하지 말고, **인간 연구 패러다임을 모사한 테스트**를 만들고 그 결과가 “유사한 현상(예: 장기 가림에서 점진적 붕괴, 용량 포화)”을 보인다고 주장해야 함.
        
    

---

## **B. 중간(Weak Accept ↔ Borderline을 가르는 포인트)**
### **B1) “Spatial Reader”가 애매함(설계가 2개라서 책임 회피로 보임)**

- **공격:** Query 기반/ROI 기반 둘 다 가능하다고 하면, 실제 구현이 무엇인지 불명확하고 공헌이 흐려진다.
    
- **방어:** 메인 구현을 **하나로 고정**하고, 다른 하나는 부록/추가 ablation으로.
    
### **B2) “품질/가시성/뷰시프트 점수” 산출이 불명확(휴리스틱 의심)**

- **공격:** blur/occlusion/view-shift를 어떻게 추정하나? 라벨이 없는데 학습한다고 하면 또 데이터 요구가 커진다. 결국 휴리스틱이면 일반화가 약하다.
    
- **방어:**
    
    - 최소 버전: **self-supervised synthetic augmentation**으로 학습(블러 강도 회귀 등)
        
    - 또는 논문에서 “proxy”로 고정: det score, feature sharpness, optical flow magnitude 같은 재현 가능한 정의.
        
### **B3) Hungarian + large K/N에서 속도/안정성 문제**

- **공격:** VIS에서 마스크/쿼리가 많고 K_total도 크다. 매 프레임 Hungarian은 느리고, gating이 강하면 recall이 떨어진다.
    
- **방어:**
    
    - “Active-only matching + top-k candidate pruning”으로 실제 Hungarian 크기를 줄인다는 것을 **명시**
        
    - 시간 복잡도/실측 FPS 보고
        
    
### **B4) “메모리 2안”이 논문에서 산만해질 위험**

- **공격:** EKVM/DSM 둘 다 내면 기여가 분산된다.
    
- **방어:** 하나를 **메인**으로, 다른 하나는 **Ablation/Appendix**.
    
---

## **C. 경미(메시지/서술/재현성)**
### **C1) 텐서 shape/하이퍼파라미터가 “예시”처럼 보이고 근거가 약함**

- **공격:** D=256, K=150, M_max=30 같은 숫자의 근거가 약하다.
    
- **방어:**
    
    - K_total sweep 실험(25~150)으로 “근거를 실험으로 대체”
        
    - 메모리 크기/에피소드 길이도 ablation으로 정당화
        
    
### **C2) 평가 지표가 태스크별로 정합이 약함**

- **공격:** VIS는 mAP인데 “ID switch”를 어떻게 정량화할지 애매하다.
    
- **방어:**
    
    - “이벤트 기반 IDS 유사 지표”를 **정의**해야 함(예: occlusion window에서 GT instance ID와 예측 slot의 매핑 변화 횟수)
        
    - 또는 YouTube-VIS에서 제공되는 tracking 성격의 평가(사용 가능한지 확인) 기반으로 명확히.
        
    

---

## **리뷰어가 가장 좋아할 “수정 방향” 요약(핵심만)**

1. **메인 태스크 고정(예: VIS)** + 서브 1개(STVG)
    
2. 차별점은 **write-control(freeze/decay) + reactivation 정책 + 이벤트 평가**로 못 박기
    
3. VideoMamba의 필요성을 **긴 T 효율/성능 곡선**으로 증명
    
4. “인간 근사”는 **행동 서명(occlusion length/latency/capacity)**로 최소 실증
    
5. Spatial Reader는 **하나로 고정**, 품질 신호는 **정의/학습 방법을 재현 가능하게**
    

---
