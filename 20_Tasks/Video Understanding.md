---
title: Video Understanding
aliases: Video Comprehension, 비디오 이해
tags:
  - computer-vision
  - video
  - multimodal
  - task
  - survey
topics: Computer Vision, Artificial Intelligence, Deep Learning, Video Analysis
---
# Video Understanding

## 한줄 요약
비디오 이해는 프레임 기반 인식에서 시작해 시공간 모델, 멀티모달, 기초 모델, 그리고 추론/정렬 문제로 확장되어 왔다.

## 발전 흐름 (연대기 개요)
### 1) 핸드크래프트 특징 + 전통적 분류기 (2000s 초~2014)
- **Dense Trajectories / iDT**: optical flow 기반 궤적 + HOG/HOF/MBH
- **BoVW/Fisher Vector** 집계 + SVM 분류가 표준 파이프라인
- 장점: 데이터 적은 환경에서도 강건함
- 한계: end-to-end 학습 부재, 표현력 제한

### 2) 2D-CNN 기반 프레임 모델 (2014~)
- 이미지 분류 CNN을 프레임에 적용 후 평균 풀링
- 공간 정보는 잘 캡처하지만 시간 정보 손실
- **Two-Stream**으로 motion을 보완하며 성능 급상승

### 3) Two-Stream 및 시간 샘플링 전략 (2014~2017)
- RGB(Spatial) + Optical Flow(Temporal) 스트림 분리 학습
- **TSN** 등으로 긴 영상의 구간 샘플링과 합의 기반 예측
- 정확도는 크게 향상, 하지만 flow 계산 비용 증가

### 4) 3D-CNN과 시공간 컨볼루션 (2015~)
- **C3D, I3D, SlowFast** 등으로 시공간 특징 직접 학습
- 대규모 데이터셋(Kinetics) 사전학습이 성능을 좌우
- 연산 비용과 긴 시퀀스 모델링이 과제로 남음

### 5) 시계열 모델 결합 (2015~2020)
- CNN 특징을 RNN/LSTM/GRU로 모델링
- 클립 단위 특징의 장기 의존성을 보완
- 하지만 학습 안정성과 비용 문제가 지속

### 6) Attention/Transformer 시대 (2019~)
- Spatiotemporal Attention과 **Video Transformer** 등장
- 긴 의존성 모델링과 표현력 향상
- 데이터 규모와 계산 자원 의존성 증가
- 대표 논문
  - Non-local Neural Networks (2018): 시공간 전역 상호작용 도입
  - [[TimeSformer]] (2021): 순수 Transformer 기반 비디오 분류
  - ViViT (2021): 비디오 토큰화와 계층적 어텐션 설계
  - Video Swin Transformer (2021/2022): 윈도우 기반 효율적 어텐션

### 7) 멀티모달/멀티스트림 확장 (2020~)
- RGB + Flow + Skeleton + Audio + Text 결합
- 비디오-언어 정렬(CLIP 계열)로 **zero-shot** 가능성 확대
- 모달 정합과 효율적 융합이 핵심 과제
- 대표 논문
  - VideoBERT (2019): 비디오-텍스트 공동 사전학습
  - MIL-NCE (2020): 비디오-텍스트 대조학습
  - [[CLIP and Vision-Language Alignment|VideoClip]] (2021): 대규모 비디오-텍스트 정렬
  - CLIP4Clip (2021): CLIP 기반 비디오 검색/정렬

### 8) 비디오 기초 모델과 대규모 사전학습 (2021~)
- 대규모 비디오-텍스트/비디오-오디오 사전학습
- 일반화 성능 향상, 다운스트림 적응 용이
- 데이터 편향, 해석가능성 문제가 대두
- 대표 논문
  - [[VideoMAE]] (2022): 마스크드 오토인코딩 기반 비디오 사전학습
  - VATT (2021): 비디오-오디오-텍스트 트라이모달 사전학습
  - InternVideo (2022/2023): 대규모 비디오 기초 모델
  - BEVT (2022): 비디오-텍스트 공동 사전학습

## 현재의 핵심 이슈
- **장기 시간 모델링**: 긴 이벤트 이해와 계층적 구조 추론
- **효율성**: 연산/메모리/실시간 요구
- **일반화**: 도메인 이동과 롱테일 대응
- **멀티모달 정합**: 텍스트/오디오/포즈와의 정렬
- **평가**: 단순 분류에서 장면/이벤트 이해까지 확장

## Main Task
![[스크린샷 2026-01-16 오후 8.28.09.png]]
### **추상적 이해 작업 (Abstract Understanding Tasks)**
---
#### [[20_Tasks/VideoUnderstanding/Abstract/Video Action Recognition|비디오 분류 및 행동 인식 (Video Classification & Action Recognition)]]
비디오 분류 및 행동 인식은 비디오 시퀀스 내의 클래스 레이블이나 활동, 이벤트 카테고리를 기반으로 비디오를 분류합니다.
#### [[Text-Video Retrieval|텍스트-비디오 검색 (Text-Video Retrieval)]]
텍스트-비디오 검색 작업은 비디오 클립과 입력된 텍스트 설명 간의 유사성을 기반으로 관련 비디오 클립을 찾아 검색합니다.
#### [[Video-to-Text Summarization|비디오-텍스트 요약 (Video-to-Text Summarization)]]
비디오-텍스트 요약은 비디오의 간결한 텍스트 요약을 생성하는 작업입니다. 비디오 요약 접근 방식은 핵심 시각 및 오디오 콘텐츠를 추출하고 해석하여 일관성 있고 유익한 요약을 생성하도록 학습됩니다.
#### [[Video Captioning|비디오 캡셔닝 (Video Captioning)]]
비디오 캡셔닝은 주어진 비디오에 대한 설명적이고 일관된 텍스트 캡션을 생성합니다. 비디오 캡션 모델은 일반적으로 비디오의 시각 및 청각 정보를 사용하여 정확하고 문맥적으로 관련된 설명을 생성합니다.
#### [[Video QA|비디오 질의응답 (Video QA)]]
비디오 질의응답(VQA)은 주어진 비디오를 기반으로 텍스트 질문에 답변하는 것을 목표로 하며, 모델은 시각 및 청각 정보를 분석하고, 맥락을 이해하며, 최종적으로 정확한 응답을 생성합니다.

---

### **시간적 이해 작업 (Temporal Understanding Tasks)**
---
#### [[Video Summarization|비디오 요약 (Video Summarization)]]
비디오 요약은 긴 비디오를 필수 콘텐츠를 보존하면서 더 짧은 버전으로 압축하는 것을 목표로 합니다. F1-점수, 스피어만, 켄달 계수 등이 이 작업의 평가 지표로 사용됩니다.
#### [[Video Highlight Detection|비디오 하이라이트 감지 (Video Highlight Detection)]]
비디오 하이라이트 감지는 비디오에서 가장 중요하고 흥미로운 부분을 식별하고 추출하는 것을 목표로 합니다.
#### [[Temporal Action_Event Localization|시간적 행동/이벤트 지역화 (Temporal Action/Event Localization)]]
이 작업은 비디오 내에서 행동이나 이벤트의 정확한 시간적 구간을 식별하는 것을 목표로 합니다. 순차적 프레임을 분석하여 이 작업에 맞게 학습된 모델은 특정 활동이 언제 시작되고 끝나는지 표시해야 합니다. 
#### [[Temporal Action Proposal Generation|시간적 행동 제안 생성 (Temporal Action Proposal Generation)]]
시간적 행동 제안 생성은 비디오 내에서 행동이나 이벤트를 포함할 가능성이 있는 후보 구간을 생성하는 작업입니다.
#### [[20_Tasks/VideoUnderstanding/Temporal/Video Temporal Grounding|비디오 시간적 그라운딩 (Video Temporal Grounding)]]
비디오 시간적 그라운딩은 주어진 텍스트 쿼리에 해당하는 비디오 내의 특정 순간이나 간격을 찾는 작업입니다. 이 과정은 언어적 설명과 시각적 콘텐츠를 정렬하여 비디오 검색 및 콘텐츠 분석과 같은 응용 프로그램에서 관련 부분을 정확하게 식별할 수 있도록 합니다.
#### [[Moment Retrieval|순간 검색 (Moment Retrieval)]]
순간 검색은 주어진 텍스트 또는 시각적 쿼리에 해당하는 정확한 비디오 부분을 식별하고 추출하는 작업으로, 쿼리와 비디오 프레임 간의 의미적 내용을 정렬합니다.
#### [[Generic Event Boundary Detection|일반 이벤트 경계 감지 (Generic Event Boundary Detection)]]
일반 이벤트 경계 감지는 비디오에서 중요한 변화가 발생하는 특정 프레임을 식별하고, 다른 이벤트나 활동을 기준으로 비디오를 분할하는 작업입니다.
#### [[Generic Event Boundary Captioning & Grounding|일반 이벤트 경계 캡셔닝 및 그라운딩 (Generic Event Boundary Captioning & Grounding)]]
일반 이벤트 경계 캡셔닝 및 그라운딩은 비디오에서 중요한 이벤트 간의 전환점을 식별하고 설명하는 작업입니다.
#### [[Dense Video Captioning|밀집 비디오 캡셔닝 (Dense Video Captioning)]]
밀집 비디오 캡셔닝[122]–[126]은 비디오 전체에 걸쳐 발생하는 여러 이벤트와 행동에 대한 상세하고 연속적인 텍스트 설명을 생성하는 것을 목표로 합니다.

---

### **시공간적 이해 작업 (Spatiotemporal Understanding Tasks)**
----
#### [[20_Tasks/Object Tracking|객체 추적 (Object Tracking)]]
객체 추적은 비디오 내에서 특정 객체의 위치를 시간에 따라 지속적으로 식별하고 추적하는 것을 목표로 합니다. 좋은 추적 모델은 가려짐, 외형 변화, 움직임이 있는 비디오에서도 객체의 정확하고 일관된 궤적을 유지해야 합니다.
#### [[Re-Identification|재식별 (Re-Identification)]]
재식별(Re-ID)은 다른 비디오 프레임이나 카메라 뷰에 걸쳐 개인이나 객체를 인식하고 일치시키는 작업입니다.
#### [[Video Saliency Detection|비디오 현저성 감지 (Video Saliency Detection)]]
비디오 현저성 감지는 비디오에서 시각적으로 가장 중요하고 주의를 끄는 영역을 식별하는 것을 목표로 합니다[136]. 이 작업은 움직임, 대비, 독특한 특징과 같은 요인으로 인해 두드러지는 영역을 강조합니다. 
#### [[Video Object Segmentation|비디오 객체 분할 (Video Object Segmentation)]]
비디오 객체 분할은 비디오를 개별 객체에 해당하는 세그먼트로 분할하고 시간에 따라 경계를 정확하게 묘사하는 것을 목표로 합니다.
#### [[Video Instance Segmentation|비디오 인스턴스 분할 (Video Instance Segmentation)]]
비디오 인스턴스 분할은 비디오 내의 각 고유 객체 인스턴스를 식별, 분할 및 추적하는 작업입니다. 
#### [[Video Object Referring Segmentation|비디오 객체 참조 분할 (Video Object Referring Segmentation)]]
비디오 객체 참조 분할은 언어 설명을 기반으로 비디오의 특정 객체를 분할하는 작업입니다. 참조된 객체를 프레임 전반에 걸쳐 정확하게 식별하고 분리합니다.
#### [[Spatiotemporal Grounding|시공간적 그라운딩 (Spatiotemporal Grounding)]]
시공간적 그라운딩은 주어진 쿼리를 기반으로 비디오의 공간 및 시간 차원 내에서 특정 객체나 이벤트를 식별하고 지역화하는 것을 목표로 합니다.

---

## **Section III. Vid-LLMs**

---

### **Vid-LLMs 분류 체계 (Taxonomy)**

논문은 비디오 입력 처리 방식에 따라 Vid-LLM을 크게 세 가지 유형으로 분류하고, LLM의 역할에 따라 세부 유형을 나눕니다.

#### **1. 비디오 분석기 $\times$ LLM (Video Analyzer $\times$ LLM)**
비디오 분석기(Video Analyzer)가 비디오를 텍스트(캡션, 객체 추적 결과, 자막 등)로 변환하고, 이 텍스트를 LLM에 입력하는 방식입니다.
*   **특징:** 비디오 정보를 텍스트로 변환하므로 LLM이 직접 비디오를 처리하지 않습니다.
*   **LLM의 역할에 따른 하위 분류:**
    *   **요약가(Summarizer)로서의 LLM:** 분석기가 생성한 텍스트 정보를 요약하거나 질문에 답하는 데 사용합니다. 정보의 흐름이 단방향입니다. (예: LaViLa, VLog)
    *   **관리자(Manager)로서의 LLM:** 시스템 전반을 조정합니다. LLM이 도구(Tool)를 호출하거나, 분석기와 여러 번 상호작용하여 결과를 도출합니다. (예: ViperGPT, Video ChatCaptioner)

#### **2. 비디오 임베더 $\times$ LLM (Video Embedder $\times$ LLM)**
비디오 임베더(예: ViT, CLIP)가 비디오를 벡터(임베딩)로 변환하고, 어댑터(Adapter)를 통해 이를 LLM이 이해할 수 있는 텍스트 의미 공간으로 매핑하는 방식입니다.
*   **특징:** 시각적 정보를 벡터 형태로 LLM에 직접 주입합니다.
*   **LLM의 역할에 따른 하위 분류:**
    *   **텍스트 디코더(Text Decoder)로서의 LLM:** 비디오 임베딩을 입력받아 일반적인 텍스트(답변, 캡션)를 생성합니다. 정밀한 시공간적 위치 파악보다는 일반적인 이해에 초점을 둡니다. (예: Video-LLaMA, Video-ChatGPT)
    *   **회귀 분석기(Regressor)로서의 LLM:** 텍스트뿐만 아니라 연속적인 값(타임스탬프, 바운딩 박스 좌표 등)을 직접 예측하여 출력합니다. (예: TimeChat, SeViLA)
    *   **은닉층(Hidden Layer)으로서의 LLM:** 비디오 임베딩을 입력받지만 텍스트를 직접 출력하지 않고, LLM을 거친 특징(feature)을 별도의 작업별 헤드(task-specific head)로 보내 회귀 작업 등을 수행합니다. (예: GPT4Video, OneLLM)

#### **3. (분석기 + 임베더) $\times$ LLM ((Analyzer + Embedder) $\times$ LLM)**
비디오 분석기가 생성한 텍스트 분석 정보와 비디오 임베더가 생성한 임베딩을 동시에 LLM에 입력하는 하이브리드 방식입니다. (예: VideoChat, Vid2Seq)

---

### **Vid-LLMs 학습 전략 (Training Strategies)**

#### **1. 훈련이 필요 없는 방식 (Training-free)**
*   주로 **비디오 분석기 $\times$ LLM** 유형에서 사용됩니다.
*   비디오 정보가 이미 텍스트로 변환되었기 때문에, 강력한 성능을 가진 기존 LLM(예: GPT-4)의 제로샷(Zero-shot) 또는 인컨텍스트 러닝(In-context learning) 능력을 그대로 활용합니다. 별도의 파라미터 업데이트가 없습니다.

#### **2. 파인튜닝 방식 (Fine-tuning)**
*   주로 **비디오 임베더 $\times$ LLM** 유형에서 사용됩니다.
*   어댑터(Adapter)의 사용 방식에 따라 네 가지로 나뉩니다.
    *   **LLM 전체 파인튜닝 (LLM Fully Fine-tuning):** 어댑터 없이 LLM의 모든 파라미터를 업데이트합니다. 성능은 좋을 수 있으나 계산 비용이 크고 LLM 본연의 능력이 저하될 수 있습니다.
    *   **연결 어댑터 파인튜닝 (Connective Adapter Fine-tuning):** 시각 정보와 텍스트 정보를 연결하는 외부 모듈(예: Q-former, Linear Layer)만 학습시키고, LLM과 비디오 인코더는 동결(Freeze)합니다. LLM의 기본 동작을 바꾸지 않습니다.
    *   **삽입 어댑터 파인튜닝 (Insertive Adapter Fine-tuning):** LLM 내부에 어댑터(예: LoRA)를 삽입하여 학습합니다. LLM의 동작 방식(예: 좌표 예측 등)을 변경해야 할 때 주로 사용됩니다.
    *   **하이브리드 어댑터 파인튜닝 (Hybrid Adapters):** 연결 어댑터와 삽입 어댑터를 조합하여 사용합니다. 보통 다단계 학습(1단계: 정렬, 2단계: 과제 학습)을 통해 진행됩니다.
---

## **Section V. APPLICATIONS AND FUTURE DIRECTIONS**

#### 1. 응용 시나리오 (Application Scenarios)

Vid-LLM(비디오 이해를 위한 대규모 언어 모델)은 다양한 산업 분야에서 혁신적인 기능을 제공하고 있습니다.

*   **미디어 및 엔터테인먼트 (Media and Entertainment)**
    *   **온라인 플랫폼:** 검색 알고리즘 개선, 문맥 인식 비디오 추천, 자막 생성 및 번역 기능 향상.
    *   **편집:** 비디오 콘텐츠의 핵심 기능을 분석하여 요약본 생성, 광고 편집 및 일반적인 비디오 편집 보조.
    *   **멀티미디어:** 음악, 아바타, 장면 생성 등 다양한 멀티미디어 분야와 결합.

*   **대화형 및 사용자 중심 시스템 (Interactive and User-Centric Systems)**
    *   **교육 및 접근성:** 교육용 비디오 분석을 통한 가상 튜터 역할, 수화를 텍스트나 음성으로 변환하여 청각 장애인의 접근성 향상.
    *   **게임 및 가상 환경:** 게임 내 다이내믹한 대화 및 스토리라인 생성, NPC 퀘스트 생성, 고객 서비스 챗봇, AR/VR 내 몰입형 내러티브 생성.
    *   **로봇 및 HCI:** 사용자의 비디오를 분석하여 맞춤형 지원 제공, 로봇이 3D 장면을 이해하고 복잡한 공간을 탐색(SayPlan 등)하도록 지원.

*   **헬스케어 및 보안 (Healthcare and Security)**
    *   **헬스케어:** 의료 문헌 분석 및 진단 보조, 환자 상담용 챗봇을 통한 증상 평가.
    *   **보안 및 감시:** 잠재적 위협 분석, 이상 행동 감지(CCTV), 사이버 보안(피싱 시도 식별), 포렌식 분석.
    *   **자율주행:** 도로 표지판 및 지침 이해, 차량 제어 시스템을 위한 사용자 인터페이스 개선.

*   **기타 응용 분야:** 비디오 생성 모델의 프롬프트 구체화 및 평가, 엣지 컴퓨팅 환경에서의 활용, 연합 학습(Federated Learning)을 통한 프라이버시 보호 시스템 강화.

#### 2. 향후 연구 방향 및 과제 (Future Directions)

Vid-LLM은 발전하고 있지만, 여전히 해결해야 할 몇 가지 중요한 과제들이 남아 있습니다.

*   **세밀한 비디오 이해 (More Fine-grained Video Understanding):** 프레임 단위의 분석은 계산 비용이 높으며, 감정이나 장면의 역학 관계 같은 깊은 의미를 파악하는 것은 여전히 어렵습니다.
*   **긴 형식의 비디오 이해 (Long-form Video Understanding):** 긴 영상에서 주요 이벤트를 식별하고 주의(attention)를 유지하는 것이 어렵습니다. 복잡한 플롯을 이해하기 위한 효과적인 메커니즘이 필요합니다.
*   **멀티모달 비디오 이해 (Multimodal Video Understanding):** 시각, 오디오, 텍스트 데이터를 통합하고 시간/공간적으로 동기화(alignment)하는 연구와 데이터셋이 부족합니다.
*   **할루시네이션 문제 (Hallucination in Video LLMs):** 모델이 비디오 내용과 무관한 응답을 생성하는 현상입니다. 도메인 차이, 문맥 영향 등으로 발생하며, 이를 완화하기 위한 학습 전략과 협업 모델이 필요합니다.
*   **산업적 배포 및 확장성 (Industrial Deployment and Scalability):** 실제 산업 현장에 적용하기 위해 모델 압축, 효율적인 캐싱, 토큰 병합(token merging) 등을 통해 성능과 효율성의 균형을 맞춰야 합니다.

#### 3. 윤리적 영향 (Ethical Implications)

*   **프라이버시 및 데이터 보안:** 비디오 데이터에 포함된 민감한 정보가 동의 없이 노출될 위험이 있습니다.
*   **오남용 및 편향:** 감시 목적으로 오남용되거나 오해의 소지가 있는 콘텐츠를 생성할 수 있으며, 훈련 데이터의 다양성 부족으로 인한 편향(bias) 문제가 발생할 수 있습니다. 이를 해결하기 위한 데이터 거버넌스와 윤리적 배포 전략이 필요합니다.
---

## 데이터셋 흐름 (요약)
- 초기: KTH, UCF101, HMDB51
- 중기: Sports-1M, ActivityNet, Kinetics
- 최근: Something-Something, AVA, Charades, Ego4D 등

## 관련 노트
- [[Two-Stream Network]]
- [[3D-CNN]]
- [[I3D]]
- [[Temporal Segment Networks]]
- [[20_Tasks/VideoUnderstanding/Abstract/Video Action Recognition]]
- [[Zero-shot and Few-shot Learning]]
