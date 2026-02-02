# LOOM (Latent Object-Oriented Memory)

**LOOM (Latent Object-Oriented Memory)** 은 [[Out of Sight, Still in Mind]] 논문에서 DOOM과 함께 제안된 메모리 모델 구현체입니다.

## 핵심 특징

- **표현 방식**: LOOM은 [[객체 지향 메모리]]를 구현하기 위해 **잠재 공간 인코딩(latent space encoding)** 을 사용합니다.
- **역할**: DOOM이 객체의 3D 포인트 클라우드 정보를 직접 사용하는 것과 달리, LOOM은 객체의 시각적 정보를 저차원의 잠재 벡터(latent vector)로 압축하여 메모리에 저장합니다. 이 방식은 메모리 사용량을 줄이고 계산 효율성을 높일 수 있는 장점이 있습니다. 이 잠재 벡터를 통해 로봇은 가려진 객체에 대한 정보를 유지하고 추론합니다.

## 관련 논문

- [[Out of Sight, Still in Mind|Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models]]