
## **📄 Transformer 개요**

- **발표 논문**: [[Attention Is All You Need|Attention Is All You Need_ (Vaswani et al., NIPS 2017)]]
    
- **핵심 아이디어**:
    
    순환(RNN)과 합성곱(CNN) 없이 **전적으로 [[Self-Attention|자기-주의(Self-Attention)]]** 만을 사용한 시퀀스 변환 모델.
    
- **주요 성과**:
    
    - WMT 2014 영어→독일어: 28.4 BLEU (기존 최고 성능 대비 +2 BLEU)
        
    - WMT 2014 영어→프랑스어: 41.8 BLEU (단일 모델 기준 최고 성능)
        
    - 기존 모델 대비 **더 적은 학습 시간과 비용**으로 SOTA 달성.
        
    

---

## **🏗 아키텍처 개요**

  

Transformer는 **인코더(Encoder)** 와 **디코더(Decoder)** 로 구성된 전형적인 시퀀스-투-시퀀스 구조를 따른다.

단, 모든 계층이 **[[Multi-Head Attention|다중 헤드 자기-주의(Multi-Head Self-Attention)]]** 와 **위치별 완전연결 네트워크(Position-wise Feed-Forward Network)** 로 이루어져 있음.

### **0. 기호/차원**
- 시퀀스 길이: $n$, 모델 차원: $d_{model}$
- 헤드 수: $h$, 헤드 차원: $d_k = d_v = d_{model}/h$
- 입력 임베딩: $X \in \mathbb{R}^{n \times d_{model}}$

  

### **1. 인코더(Encoder)**

- **구성**: 동일한 6개 층의 스택
    
- 각 층:
    
    1. **[[Multi-Head Attention|다중 헤드 자기-주의]]**
        
    2. **위치별 완전연결 네트워크**
        
    
- **잔차 연결 + 층 정규화** 적용
    
- 출력 차원: $d_{model} = 512$
    

  

### **2. 디코더(Decoder)**

- **구성**: 동일한 6개 층의 스택
    
- 각 층:
    
    1. 마스킹된 [[Self-Attention|자기-주의]] (미래 토큰 참조 방지)
        
    2. 인코더 출력에 대한 [[Cross-Attention|다중 헤드 교차 어텐션]]
        
    3. 위치별 완전연결 네트워크
        
    
- **잔차 연결 + 층 정규화** 적용

### **3. 서브레이어 수식 요약**
- **Multi-Head Attention**:
  - $\\mathrm{head}_i = \\mathrm{Attention}(QW_i^Q, KW_i^K, VW_i^V)$
  - $\\mathrm{MHA}(Q,K,V) = \\mathrm{Concat}(\\mathrm{head}_1,\\ldots,\\mathrm{head}_h)W^O$
- **Position-wise FFN**:
  - $\\mathrm{FFN}(x)=W_2\\,\\sigma(W_1 x + b_1)+b_2$ (ReLU)
- **Residual + LayerNorm(논문 기준)**:
  - $\\mathrm{LayerNorm}(x + \\mathrm{Sublayer}(x))$

---

## **🎯 주요 구성 요소**

  

### **1. [[Scaled Dot-Product Attention|스케일드 닷-프로덕트 어텐션]]**

- 입력: Query(Q), Key(K), Value(V)
    
- 연산:
    
    $$\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{QK^T}{\sqrt{d_k}} \right) V$$
    
- 스케일링$(\sqrt{d_k})$으로 학습 안정성 확보
    

  

### **2. [[Multi-Head Attention|다중 헤드 어텐션(Multi-Head Attention)]]**

- Q, K, V를 $h$개로 분할하여 병렬 연산
    
- 다양한 표현 하위공간에서 정보 추출
    
- 본 논문: $h=8, d_k = d_v = 64$
    

  

### **3. 위치별 완전연결 네트워크**

- 각 위치에 독립적으로 적용되는 2층 FFN
    
- 내부 차원: $d_{ff} = 2048$
    

  

### **4. 임베딩 & 위치 인코딩**

- **입출력 임베딩**과 **softmax 이전 선형변환**의 가중치 공유
    
- 위치 인코딩(Positional Encoding):
    
    - 사인/코사인 함수 기반
        
    - 다양한 파장으로 절대·상대적 위치 정보 제공
        
    - 수식:
      - $PE_{(pos,2i)}=\\sin(pos/10000^{2i/d_{model}})$
      - $PE_{(pos,2i+1)}=\\cos(pos/10000^{2i/d_{model}})$
    

---

## **⚖️ Self-Attention vs RNN/CNN**

| **비교 항목** | **Self-Attention** | **RNN**   | **CNN**       |
| --------- | ------------------ | --------- | ------------- |
| **병렬성**   | $O(1)$ 순차 연산       | $O(n)$    | $O(1)$        |
| **경로 길이** | $O(1)$             | $O(n)$    | $O(log_k(n))$ |
| **복잡도**   | $O(n^2 d)$         | $O(nd^2)$ | $O(knd^2)$    |

- Self-Attention은 경로 길이가 짧고 병렬화가 쉬움 → 장기 의존성 학습에 유리
    

---

## **🧠 디코딩(추론)**
- **오토리그레시브**: 이전 토큰까지의 출력만 참고하도록 마스킹.
- **출력 분포**: $p(y_t|y_{<t},x)$를 softmax로 계산.
- **디코딩 기법**: 그리디, 빔서치, 길이 패널티 등 사용.

---

## **⚙️ 학습 설정**

- **데이터셋**:
    
    - WMT14 EN-DE (4.5M 문장, BPE 37K)
        
    - WMT14 EN-FR (36M 문장, WordPiece 32K)
        
    
- **하드웨어**: 8 × NVIDIA P100 GPU
    
- **학습 시간**:
    
    - Base: 100K step (~12h)
        
    - Big: 300K step (~3.5일)
        
    
- **옵티마이저**: Adam(β1=0.9, β2=0.98, ε=1e-9)
    
- **학습률 스케줄**:
    
    Warmup 4K step → 이후 step^-0.5 감소
    
- **정규화**:
    
    - 드롭아웃(P=0.1~0.3)
        
    - 레이블 스무딩(ε=0.1)
        
    

---

## **⚠️ 한계**
- $O(n^2)$ 어텐션으로 긴 시퀀스에서 메모리/시간 부담.
- 입력 길이 증가 시 학습/추론 비용 급증.

---

## **📊 주요 실험 결과**

  

### **번역 성능 (BLEU)**

|**모델**|**EN-DE**|**EN-FR**|
|---|---|---|
|ByteNet|23.75|-|
|ConvS2S|25.16|40.46|
|GNMT+RL|24.6|39.92|
|Transformer(Base)|27.3|38.1|
|**Transformer(Big)**|**28.4**|**41.8**|

### **영어 구문 분석(WSJ)**

- WSJ only: 91.3 F1 (기존 대부분 모델 초과)
    
- Semi-supervised: 92.7 F1 (SOTA 달성)
    

---

## **🔮 향후 연구 방향**

- 다양한 모달리티(이미지, 오디오, 비디오)에 적용
    
- 국소·제한적 주의로 대규모 입력 처리
    
- 생성 과정의 비순차성 완화
    

---

## **🔗 관련 링크**
- [[Attention]]
- [[Self-Attention]]
- [[Cross-Attention]]
- [[Multi-Head Attention]]
- [[Bahdanau Attention]]
- [[Vision Transformer]]

## **📌 참고 링크**

- **논문 원문**: [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)
    
- **코드**: [https://github.com/tensorflow/tensor2tensor](https://github.com/tensorflow/tensor2tensor)
    

---
