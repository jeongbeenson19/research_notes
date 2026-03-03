
# Key Reference

## **1) Mamba를 비디오 시간 모델로 쓰는 근거**

- **VideoMamba: State Space Model for Efficient Video Understanding (2024)** — 비디오에서 Mamba/SSM로 장기 시간 의존성을 효율적으로 모델링하는 대표 레퍼런스. 
    
- **Video Mamba Suite (VMS) (2024)** — Mamba가 비디오에서 맡을 수 있는 역할을 분류(“roles”)하고, 여러 태스크에서 평가한 “범용 실험 스위트”. 
    
- **MambaVision (2024, hybrid Mamba-Transformer backbone)** — 순수 SSM만으로 공간 전역 상호작용이 약해질 수 있어 하이브리드가 실용적이라는 근거로 자주 인용됨. 


---

## **2) VIS에서 MOT식 association/ID 일관성(=query/tracklet 기반 연결) 근거**

- **MinVIS (2022)** — 프레임별 인스턴스(seg) 결과를 **query bipartite matching**으로 연결하는 “최소” VIS 파이프라인. (너의 “게이팅/할당” 철학과 가장 가까운 축) 
    
- **EfficientVIS (CVPR 2022)** — **tracklet query/proposal**로 공간-시간 RoI를 연결하고, 클립 간 linking까지 end-to-end로 다루는 VIS 레퍼런스. 
    
- **SeqFormer (2021/2022)** — instance query 기반으로 비디오 레벨 인스턴스 표현을 만들어 tracking/association이 “자연스럽게” 되도록 하는 VIS 계열. 
    

---

## **3) “메모리(working/long-term)로 장기 세그 유지” 근거 (VOS/RVOS 포함)**

- **XMem (2022)** — 장기 VOS에서 multi-store memory(working/long-term 등)로 성능 유지 + 메모리 폭발 방지. (너의 “slot memory + decay/갱신 제어”에 직접 대응) 
    
- **Referring Video Object Segmentation via Language-aligned Track Selection (SOLA) (2024)** — RVOS를 **track generation + track selection**으로 분해(= “후보 트랙 생성 → 선택/연결”). 네가 말한 “후보 생성→게이팅/선택” 구조의 좋은 근거. 
    

---

## **4) “object permanence / persistent tracking” 근거 (단절/가림 중에도 유지)**

- **Learning to Track with Object Permanence (ICCV 2021; PermaTrack)**
    
    — occlusion 등에서 “보이지 않아도 존재”를 다루는 MOT 방향의 대표 레퍼런스(메모리/재귀 모듈). 
    

---

## **5) “장기 ST grounding에서 memory bank(공간/시간) 쓰는 흐름” 근거**

- **Towards Long-Form Spatio-Temporal Video Grounding (2026)** — streaming STVG로 처리하면서 **spatial & temporal memory banks**를 decoder에 두는 접근. 너의 “장기/스트리밍 + 메모리 + 연결” 근거로 적합. 
    

---

## **6) (보너스) MOT에서 “메모리로 장기 재연결” 근거**

- **MeMOT: Multi-Object Tracking with Memory (CVPR 2022)** — 장기 구간에서 ID 임베딩을 메모리에 저장하고 필요 시 참조/집계하는 방식. (너의 persistent memory+reactivation 철학과 직접 닿음) 
    

---

### **너의 아이디어를 레퍼런스 맵으로 한 줄 요약하면**

- **시간 통합 엔진(Mamba)**: VideoMamba / VMS / (하이브리드) MambaVision 
    
- **세그/인스턴스 연결(association)**: MinVIS / EfficientVIS / SeqFormer 
    
- **장기 메모리(working/long-term)**: XMem 
    
- **단절 중 지속성(object permanence)**: PermaTrack(ICCV’21) 
    
- **그라운딩의 장기 스트리밍 메모리**: Long-form STVG(2026) 
    
- **MOT 장기 메모리/재연결**: MeMOT 
    


# Architecture Draft
## **1) 공간 연산을 어떻게 할지: 3가지 선택지**

시간 모델(Mamba)은 “시간축 상태 업데이트”에 강하고, **공간에서 객체를 집어내는 연산은 별도 메커니즘**이 필요하다. 가장 깔끔한 옵션은 아래 3개 중 하나로 고정하면 된다.

### **A. Proposal/ROI 기반(가장 MOT식, 구현 안정)**

- 프레임별로 box/mask proposal(또는 blob)을 만들고
    
- 각 proposal에서 **ROIAlign / mask pooling**으로 feature를 뽑아
    
- 그 feature를 슬롯 업데이트(Mamba)로 넣는다.
    
- 장점: association(헝가리안/게이팅)이 직관적, 실패 분석 쉬움
    
- 단점: proposal 품질이 상한을 만든다
    

### **B. Query/Attention 기반(세그·그라운딩에 자연)**

- K개의 object slot(query)이 프레임 feature map에서 **cross-attention(또는 deformable attention)** 으로 자기 영역을 읽어온다.
    
- slot이 곧 “트랙 상태”가 된다.
    
- 장점: proposal 없이도 돌아감, VIS/VOS/grounding이 자연
    
- 단점: 학습/안정화가 A보다 어려움
    

### **C. Dense-map → Soft assignment(살리언시/heatmap에 강함)**

- dense logits/embedding map을 만들고
    
- slot마다 **soft mask(가중치 맵)** 으로 pooling해서 slot feature를 만든다.
    
- 장점: 이산화 없이 매끈하게 연결
    
- 단점: 서로 가까운 객체 분리(competition)가 필요(정규화/entropy/repulsion 등)


**권장 고정(MVP~논문화)**: B(쿼리/어텐션) + 필요하면 A(ROI) 백업.

즉, “slot이 공간에서 읽어오고 → 시간축으로 유지”가 가장 범용이다.

---

## **2) 전체 모듈 구성(공통 백본/시간 + 공통 슬롯 메모리)**

### **(0) Video backbone (공간 feature)**

- 입력: 프레임 I_t
    
- 출력: 다중 해상도 feature map F_t \in \mathbb{R}^{H\times W\times C} (또는 토큰)
    
- 역할: **공간 표현(경계/형상/텍스처/객체 단서)** 담당
    

### **(1) Spatial Reader (slot이 공간에서 읽기)**

아래 중 하나로 구현(위 1번의 A/B/C 중 선택).

- 입력: F_t, slot 상태 S_{t-1} (또는 query)
    
- 출력: 슬롯 관측치 o_t^k (k번째 슬롯의 현재 프레임 관측 feature), 그리고 선택적으로 **soft mask/box** 같은 공간적 어텐션 맵
    
### **(2) Slot Memory + Reliability Controller (freeze/decay 포함)**

- 상태: 각 슬롯 k에 대해
    
    - appearance/semantic prototype p^k
        
    - spatial belief(간단히 box/center+cov, 또는 mask prior)
        
    - reliability r^k, last_seen, quality 통계
        
    
- 관측 품질 q_t^k 가 낮으면: **write gate 닫기(freeze)**
    
- 미관측/저품질 지속 시: **decay(불확실성 증가, prototype 신뢰도 감소)**
    
### **(3) Temporal Integrator: Mamba(SSM)로 slot 업데이트**

- 입력: 슬롯 관측 시퀀스 \{o_t^k\} 와 게이트(quality/reliability)
    
- 출력: 업데이트된 슬롯 상태 \tilde{S}_t^k
    
- 구현 포인트: “프레임 토큰 전체”를 Mamba에 넣기보다,
    
    - **슬롯 단위(feature 길이 K)** 또는
        
    - **ROI/slot pooled feature**만 넣어서 시간 통합을 수행하는 게 안정적이다.
        
### **(4) Reactivation / Association (태스크 불변 모듈)**

- 현재 프레임의 후보(슬롯 관측 또는 proposal)와 기존 슬롯을
    
    - visibility/quality/시간 gap prior로 **candidate gating**
        
    - appearance + spatial + (선택)semantic 점수로 **score fusion**
        
    - 필요 시 **global assignment(헝가리안)** 또는 query 유지로 연결
        
    
- 결과: “이 관측은 어느 슬롯(인스턴스)에 속하는가”가 결정됨

> 이 (1)~(4)가 **태스크 불변 core**이고, head만 바꿔서 task를 갈아끼운다.

---

## **3) Head 교체로 수행 가능한 task 정리**

아래는 “slot이 유지되는 공통 코어” 위에 **출력 형식만 바꿔서** 가능한 것들이다.

### **A) VIS(Video Instance Segmentation)**

- Head: **mask head + (선택) box head + class head**
    
- 입력: 각 슬롯 상태 \tilde{S}_t^k + 현재 feature F_t
    
- 출력: 인스턴스별 마스크(및 클래스), 시간 ID는 슬롯이 담당
    
- 병목 대응: ID switch/drift는 association + freeze/decay가 직접 타격
    
### **B) VOS / RVOS(Referring VOS)**

- VOS: 클래스 없이 target mask 유지
    
    - Head: mask head
        
    
- RVOS: 텍스트 조건이 추가
    
    - Head: mask head + text-slot alignment head(간단히 슬롯 점수 스칼라)
        
    
- 핵심: “어느 슬롯이 지시된 대상인가”를 한 번 고르고(또는 매 프레임 점수),
    
    그 슬롯의 마스크를 출력
    
### **C) Spatiotemporal Grounding(STVG) / Tube grounding**

- Head: (1) moment(시간 구간) head + (2) tube/box/mask head
    
- 출력 형태 2가지
    
    1. **온라인**: 매 프레임 slot의 box/mask + 텍스트-슬롯 점수 → 상위 슬롯의 궤적이 곧 tube
        
    2. **오프라인**: 슬롯 시퀀스 점수를 모아 시작/끝(t_start,t_end) 추정 + 해당 구간 tube 출력
        
    
- MOT 철학이 특히 잘 먹는 이유: “텍스트가 가리키는 대상”을 **시간축으로 일관되게 선택**해야 함
    
### **D) Video Object Localization / Tracking-by-seg/box(추적 계열)**

- Head: box head(또는 center+size head)
    
- 출력: 슬롯별 box trajectory
    
- 사실상 MOT/Tracking의 일반화
    
### **E) Video Classification / Action recognition(객체-중심 버전)**

- Head: cls head(비디오 레벨 또는 segment 레벨)
    
- 방식:
    
    - 슬롯들을 aggregate(가중합/attention pooling)해서 비디오 표현을 만들거나
        
    - 특정 slot(예: 사람/핵심 객체)만 선택해서 분류
        
    
- 장점: “배경 평균”이 아니라 “객체 기반”으로 시간 통합이 가능
    
### **F) Referring Expression Comprehension (프레임/클립 단위 객체 선택)**

- Head: 슬롯 선택(score) head + (선택) mask/box head
    
- 출력: “이 텍스트는 이 슬롯이다” + 해당 슬롯의 box/mask
    

---

## **4) 어떤 조합이 “범용”에 가장 가까운가(추천 고정안)**

- **공간**: Query/Deformable reader(B)
    
- **시간**: Slot-level Mamba 업데이트
    
- **연결**: gating + fusion + (필요시) assignment
    
- **head**: {mask, box, cls, moment} 4종만 두면
    
    - VIS/VOS/RVOS/ST grounding/box tracking/action 분류까지 커버 가능
        
    

---

원하면, 위 설계를 **“최소 공통 I/O 스펙”** 으로 더 딱 고정해줄 수 있다(각 텐서 shape, K 슬롯 수, 어떤 신뢰도 지표로 gate할지, association 비용항 구성). 이렇게 고정하면 바로 구현 체크리스트로 바뀐다.