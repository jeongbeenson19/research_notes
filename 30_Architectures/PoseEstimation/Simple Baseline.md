
## **📄 Simple Baselines for Human Pose Estimation and Tracking (2018)**

  

### **1. 개요**

- **목표**: 사람 자세 추정(Human Pose Estimation)과 추적(Pose Tracking)을 위한 단순하지만 강력한 기준선(baseline) 제시

- **발표 논문**: [[Simple Baselines for Human Pose Estimation  and Tracking]]
    
- **핵심 아이디어**:
    
    - ResNet 백본 + Deconvolution Head를 이용한 단순 구조
        
    - Optical Flow 기반 joint propagation + [[Object Keypoint Similarity|flow-based pose similarity]]를 활용한 추적
        
    
- **성과**: COCO, PoseTrack에서 SOTA 달성
    

---

### **2. Pose Estimation**

  

#### **2.1 네트워크 구조**

- **백본**: ResNet-50 / 101 / 152
    
- **헤드 구조**:
    
    - Deconv × 3, kernel 4×4, stride 2, 채널 256
        
    - BatchNorm + ReLU
        
    - 마지막 1×1 Conv로 k개 키포인트 히트맵 생성
        
    
- **손실**: GT 히트맵과 예측 히트맵 간 MSE
    
- **GT 히트맵 생성**: 각 GT 키포인트를 중심으로 2D Gaussian 적용
    

  

#### **2.2 기존 구조와 비교**

- **Hourglass**: skip connection + multi-stage bottom-up/top-down
    
- **CPN**: skip connection + [[Online Hard Keypoints Mining|OHKM]]
    
- **본 방법**: skip connection 없이 deconv에서 업샘플링+컨볼루션 동시 처리
    

---

### **3. Pose Tracking**

  

#### **3.1 전체 파이프라인**

1. 이전 프레임 포즈를 Optical Flow로 현재 프레임으로 전파 (joint propagation)
    
2. 사람 탐지 박스 + 전파된 박스 → [[Greedy Non-maximum Suppression|NMS]]로 통합
    
3. 통합 박스에서 포즈 추정
    
4. 이전 프레임 큐(Q)와 현재 프레임 포즈 간 유사도 계산
    
5. Greedy Matching으로 ID 부여
    

  

#### **3.2 핵심 기법**

- **Joint Propagation**:
    
    - Optical Flow $F_{k-1 \to k}$로 이전 프레임 관절 좌표 전파
        
    - 바운딩 박스 계산 후 15% 확장하여 후보 박스 생성
        
    
- **Flow-based Pose Similarity**:
    
    - OKS(전파된 관절, 현재 관절)
        
    - Multi-frame propagation(SMulti-Flow)로 occlusion 후 재등장 추적 가능
        
    

---

### **4. 실험 결과**

  

#### **4.1 COCO (Pose Estimation)**

- **Ablation 주요 결과**:
    
    - Deconv 3층 > 2층 (AP +2.5)
        
    - Kernel size 4 권장
        
    - 깊은 백본일수록 성능 ↑
        
    - 해상도 ↑ → 성능 ↑, 연산량 ↑
        
    
- **COCO test-dev**:
    
    - ResNet-152, 384×288: AP 73.7 (CPN+ 대비 우위)
        
    

  

#### **4.2 PoseTrack (Pose Estimation + Tracking)**

- **Joint Propagation**: R-FCN 사용 시 +4.3% mAP, +3.8% MOTA
    
- **Flow-based Similarity**: Bounding box similarity 대비 MOTA ↑
    
- **리더보드 성과**:
    
    - mAP 74.6, MOTA 57.8 (기존 대비 대폭 향상)
        
    

---

### **5. 결론**

- 복잡한 구조 없이도 강력한 성능 달성 가능
    
- 추후 연구의 **재현성 높은 출발점** 제공
    
- Optical Flow와 간단한 디컨볼루션 설계만으로도 SOTA 가능함
    

---

**참고 논문**:

Bin Xiao, Haiping Wu, Yichen Wei, _Simple Baselines for Human Pose Estimation and Tracking_, ECCV 2018.

[GitHub Repo](https://github.com/leoxiaobin/pose.pytorch)

---

원하시면 제가 이 내용을 옵시디언 마크다운 구조에 맞춰서 **폴더·링크·태그 포함 버전**으로 만들어 드릴까요?

그렇게 하면 관련 논문, 개념, 코드까지 연동해서 관리할 수 있습니다.