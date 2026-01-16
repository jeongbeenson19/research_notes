
## **📄 [[U-Net Convolutional Networks for Biomedical  Image Segmentation]]**

**저자**: Olaf Ronneberger, Philipp Fischer, Thomas Brox
**발표 연도**: 2015
**링크**: [[U-Net]]

---

### **1. 개요**

- **목적**: 적은 수의 주석 데이터로도 정밀한 생의학 영상 분할 가능
    
- **핵심 특징**
    
    - **U자형 대칭 구조** (Contracting path ↔ Expansive path)
        
    - **Fully Convolutional Network(FCN)** 기반 확장
        
    - **Elastic deformation** 기반의 강력한 데이터 증강
        
    - 접촉 객체 분리를 위한 **가중 손실(weighted loss)**
        
    - GPU에서 빠른 추론 속도 (512×512 이미지 < 1초)
        
    

---

### **2. 아키텍처**

- **Contracting Path**
    
    - 3×3 무패딩 합성곱 + ReLU × 2
        
    - 2×2 Max pooling(stride 2)
        
    - 다운샘플 시 채널 수 2배 증가
        
    
- **Expansive Path**
    
    - 업샘플링 + 2×2 업-합성곱 (채널 수 절반 감소)
        
    - Contracting path에서 크롭한 피처맵과 concat
        
    - 3×3 합성곱 + ReLU × 2
        
    
- **최종 출력**
    
    - 1×1 합성곱으로 클래스 수 매핑
        
    
- **총 23개의 합성곱 층**
    

---

### **3. 학습 전략**

- **손실 함수**: 픽셀 단위 softmax + Cross-Entropy
    
    $$E = \sum_{x \in \Omega} w(x) \log(p_{\ell(x)}(x))$$
    
- **가중치 맵(weight map)**: 클래스 불균형 보정 + 경계 강조
    
    $$w(x) = w_c(x) + w_0 \cdot \exp\left(-\frac{(d_1 + d_2)^2}{2\sigma^2}\right)$$
    
- **가중치 초기화**: He Initialization $(\sqrt{2/N})$
    
- **데이터 증강**:
    
    - 무작위 탄성 변형(3×3 grid, Gaussian std=10px, bicubic interpolation)
        
    - 회전, 이동, 명암 변환
        
    - Contracting path 끝에 Dropout
        
    

---

### **4. 실험 결과**

- **EM Segmentation Challenge 2012**
    
    - Warping error: 0.000353 (최고 성능)
        
    - Rand error: 0.0382
        
    
- **ISBI Cell Tracking Challenge 2015**
    
    - PhC-U373: IOU 92% (2위 대비 +9%)
        
    - DIC-HeLa: IOU 77.5% (2위 대비 +31.5%)
        
    

---

### **5. 결론**

- 적은 주석 데이터로도 높은 성능
    
- 다양한 생의학 영상에 적용 가능
    
- 공개된 구현(Caffe)과 pretrained 모델 존재
    
- 빠른 추론과 효율적인 메모리 사용
    

---

### **📂 관련 키워드**

#U-Net #BiomedicalSegmentation #FCN #DataAugmentation #WeightedLoss #ElasticDeformation

---
