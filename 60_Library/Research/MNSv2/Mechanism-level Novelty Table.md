아래는 리뷰어가 “그래서 기존이랑 뭐가 달라?”를 한 번에 판단하게 만드는 **novelty/related-work 대비표**야. 핵심은 **구현 디테일이 아니라 ‘동작(behavioral mechanism) 단위’** 로 비교하는 것.

---

# **(iii) Related Work 대비표 (Mechanism-level Novelty Table)**

## **비교 축(열) 정의**

- **Obj-Slot**: 객체별 persistent slot(상태)로 유지되는가
    
- **Episodic Bank**: per-object snapshot bank(에피소드)로 복수 기억을 유지하는가
    
- **Write Control**: 저품질 관측에서 업데이트를 **동결/감쇠(freeze/decay)**로 제어하는가
    
- **Explicit Reactivation**: 장기 단절 후 **재활성화 정책 + 명시적 assignment(게이팅/퓨전/헝가리안 등)**이 설계로 존재하는가
    
- **Event-centric Eval**: occlusion/view-shift/blur 같은 **사건 슬라이스 평가(reactivation window, gap bucket)**를 핵심으로 보고하는가
    
- **Long-context Efficient Temporal**: 긴 시퀀스를 **효율적으로** 처리하는 시간 백본(예: VideoMamba/SSM)을 시스템 핵심으로 사용하는가
    

---

## **1) 메인 대비표**

| **Method / Lineage**                 | **Domain**          | **Obj-Slot**                  | **Episodic Bank**      | **Write Control (Freeze/Decay)** | **Event-centric Eval** | **Explicit Reactivation + Assignment** | **Long-context Efficient Temporal** |
| ------------------------------------ | ------------------- | ----------------------------- | ---------------------- | -------------------------------- | ---------------------- | -------------------------------------- | ----------------------------------- |
| **MinVIS**                           | VIS                 | △ (query=instance proxy)      | ✗                      | ✗                                | ✗                      | △ (query bipartite matching)           | ✗                                   |
| **EfficientVIS**                     | VIS                 | △ (tracklet query)            | ✗                      | ✗/△                              | ✗                      | △ (query/tracklet linking)             | ✗                                   |
| **SeqFormer**                        | VIS                 | △ (video-level instance repr) | ✗                      | ✗                                | ✗                      | △ (implicit linking)                   | ✗                                   |
| **XMem**                             | VOS                 | △ (target memory)             | ✓ (multi-store memory) | △ (memory management 중심)         | ✗                      | ✗/△ (VOS propagation, assignment는 다름)  | ✗                                   |
| **PermaTrack (Obj Permanence)**      | MOT/Tracking        | ✓                             | ✗                      | ✗/△ (learned recurrence)         | △ (occlusion 관점은 있음)   | △ (tracking continuity)                | ✗                                   |
| **MeMOT**                            | MOT                 | ✓                             | ✓ (buffer/FIFO)        | △ (buffer 관리)                    | ✗                      | ✓ (association 중심)                     | ✗                                   |
| **VideoMamba**                       | Video Understanding | ✗                             | ✗                      | ✗                                | ✗                      | ✗                                      | ✓                                   |
| **VMS (Video Mamba Suite)**          | Bench/Suite         | ✗                             | ✗                      | ✗                                | ✗                      | ✗                                      | ✓(역할/평가 틀)                          |
| **Long-form STVG w/ Memory Banks**   | STVG                | △                             | △                      | ✗/△                              | ✗/△                    | △                                      | △                                   |
| Ours (Maintenance Core + VideoMamba) | VIS(+STVG optional) | ✓                             | ✓(EKVM) / ✗(DSM)       | ✓                                | ✓                      | ✓                                      | ✓                                   |

---

## **2) 리뷰어가 “조합 아니냐?”고 공격할 때의 방어 포인트(표에서 바로 읽히게)**

리뷰어가 흔히 하는 공격은 “각 요소는 다 있잖아”인데, 그때 방어는 **‘단일 요소’가 아니라 ‘결합 위치 + 평가 언어’** 로 가야 함.
### **핵심 차별 1:** 

### **Write Control이 ‘설계 중심’으로 들어감**

- 기존 VIS 계열은 “전파/링킹”은 있어도, **저품질 관측에서 업데이트 오염을 막는 freeze/decay를 코어 동작으로 고정**한 사례가 상대적으로 약함.
    
- 네 방법은 write-control이 **성능 개선의 원인**임을 ablation으로 증명하도록 설계됨(−Freeze, −Decay).
    
### **핵심 차별 2:** 

#### **Explicit Reactivation(장기 단절) + Assignment를 ‘태스크 불변 코어’로 정의**

- VIS는 보통 “쿼리/링킹”이 암묵적일 수 있는데, 너는 **재활성화 정책(조건) + 후보 게이팅 + 스코어 퓨전 + 1:1 할당**을 명시한다.
    
- 즉, “추적 문제를 푸는 로직”을 VIS/grounding에 **그대로 이식 가능한 코어**로 고정.
    
### **핵심 차별 3:** 

#### **Event-centric Eval을 메인 기여로 가져감**

- 기존 논문들은 평균 AP/J&F/IoU 보고가 중심이라 “단절에서 뭐가 좋아졌는지”가 흐려짐.
    
- 너는 gap bucket / reactivation window를 **주지표급으로 끌어올려** “object maintenance가 좋아졌다”를 보이게 함.
    
### **핵심 차별 4:** 

#### **VideoMamba는 ‘주장’이 아니라 ‘곡선(긴 T)’로 정당화**

- 단순 백본 교체가 아니라, **긴 컨텍스트/장기 단절에서의 효율-성능 곡선**으로 “왜 SSM 계열이 maintenance에 유리한가”를 정량화하는 설계를 포함.
    

---

## **3) 논문에 그대로 넣기 좋은 “Related Work 대비문” (짧은 문장 3개)**

1. _VIS methods based on instance queries or tracklet queries provide implicit linking, but typically lack explicit write-control mechanisms that prevent memory corruption under low-quality observations._
    
2. _Memory-based segmentation models maintain appearance cues over time, yet their memory operations are often task-specific and do not explicitly implement long-gap reactivation as a unified assignment problem._
    
3. _Our work unifies explicit reactivation (gating + score fusion + assignment) with quality-controlled memory updates and evaluates them with event-centric protocols, while using VideoMamba to scale temporal context efficiently._
    

---
