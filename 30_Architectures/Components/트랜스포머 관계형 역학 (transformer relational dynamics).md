# 트랜스포머 관계형 역학 (Transformer Relational Dynamics)

**트랜스포머 관계형 역학(Transformer Relational Dynamics)** 은 [[Out of Sight, Still in Mind]] 논문에서 객체들의 시간적, 공간적 관계와 그 변화(dynamics)를 모델링하기 위해 사용된 핵심 컴포넌트입니다.

## 핵심 특징

- **기반 모델**: 이 컴포넌트는 [[Transformer|트랜스포머]] 아키텍처, 특히 셀프 어텐션(self-attention) 메커니즘을 기반으로 합니다.
- **역할**:
    1.  **관계 모델링**: 씬(scene)에 존재하는 여러 객체들의 표현(representations)을 입력으로 받아, 셀프 어텐션을 통해 모든 객체 쌍 간의 상호 관계를 계산합니다. 이를 통해 "어떤 객체가 다른 객체에 영향을 미치는지"를 학습합니다.
    2.  **동역학 예측**: 현재 객체들의 상태와 로봇의 행동(action)이 주어졌을 때, 다음 시점(timestep)에 객체들의 상태가 어떻게 변할지를 예측합니다. 즉, 물리적 상호작용의 결과를 예측하는 역학 모델(dynamics model)의 역할을 수행합니다.
- **장점**: 트랜스포머를 사용함으로써, 모델은 씬에 있는 객체의 수가 변하더라도 유연하게 처리할 수 있으며, 객체 간의 복잡하고 장기적인 의존성을 효과적으로 포착할 수 있습니다.

## 관련 논문

- [[Out of Sight, Still in Mind|Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models]]

## 관련 링크
- [[Transformer]]
- [[Relational Reasoning]]
- [[Dynamics Model]]