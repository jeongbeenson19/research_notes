## CVPR 2025
---

### Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation

> VFM + VLM 결합 모델
> Multi Modalities 성능 향상을 위해 MTEnhancer 도입
> 시각적 특징(VFM + VLM) 간의 융합을 위해 MVFuser 도입
> 도메인 일반화 성능을 위해 synthetic-to-real, real-to-real 설정으로 학습

단순히 멀티모달 데이터를 처리하는 것을 넘어, **"비전 모델의 세밀함"** 과 **"언어 모델의 일반화 능력"** 을 **Mamba**라는 효율적인 구조를 통해 연결(Bridge)함으로써, 보지 못한 환경(Unseen Domain)에서도 잘 작동하는 세그멘테이션 모델을 만드는 것이 목적입니다.

###  ReWind: Understanding Long Videos with Instructed Learnable Memory

> VLM (VQA + Temporal Grounding)
> 2-stage 구조 - 동적 학습 메모리(read-perceive-write cycle)를 이용한 시각 정보 저장 및 업데이트 + adaptive frame selection mechanism을 이용한 key moment 규명

**핵심 맥락은 압축하여 메모리 뱅크(M)에 저장**하여 긴 비디오를 효율적으로 다루고, **상세 정보는 특징 버퍼에 남겨두어** 필요시 다시 꺼내 쓸 수 있도록 하는 이중 전략을 사용

