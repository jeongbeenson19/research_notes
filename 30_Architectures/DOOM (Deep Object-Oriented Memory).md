# DOOM (Deep Object-Oriented Memory)

**DOOM (Deep Object-Oriented Memory)** 은 [[Out of Sight, Still in Mind]] 논문에서 제안된 두 가지 메모리 모델 구현체 중 하나입니다.

## 핵심 특징

- **표현 방식**: DOOM은 [[객체 지향 메모리]]를 구현하기 위해 **포인트 클라우드 기반 인코딩(point cloud-based encoding)** 을 사용합니다.
- **역할**: 이 모델은 로봇이 관찰한 객체들의 이력(history)을 명시적으로 관리하고 저장합니다. 특히 [[UVOS (Unsupervised Video Object Segmentation)]]를 통해 추적된 객체들의 3D 포인트 클라우드 정보를 직접 메모리에 인코딩하여, 객체가 시야에서 가려진 후에도 그 형태와 위치를 기억하고 추론하는 데 사용됩니다.

## 관련 논문

- [[Out of Sight, Still in Mind|Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models]]