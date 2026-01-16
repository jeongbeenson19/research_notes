
## ✅ 1. DropConnect란?

**DropConnect**는 **신경망의 가중치(weight)** 에 **랜덤한 마스킹(masking)** 을 적용하여 **과적합을 방지하는 정규화 기법**입니다.

> 🔎 **핵심 아이디어**: Dropout이 뉴런을 랜덤하게 제거하는 것이라면, **DropConnect는 뉴런 간의 연결선(=가중치)을 랜덤하게 제거**합니다.

---

## ✅ 2. Dropout vs DropConnect: 비교

| 항목       | **Dropout**        | **DropConnect**                      |
| -------- | ------------------ | ------------------------------------ |
| 마스킹 대상   | 뉴런의 출력값            | **가중치 (weight matrix)**              |
| 동작 방식    | 출력값을 확률적으로 0으로 만듦  | weight를 확률적으로 0으로 만듦                 |
| 수식 적용 위치 | 활성값 $a = f(Wx)$ 이후 | 선형변환 $z = Wx$ 계산 시 $W$에 적용           |
| 계산 비용    | 상대적으로 적음           | 더 큼 (Weight-level mask 필요)           |
| 일반화 효과   | 있음                 | 더 강력할 수 있음 (실제로 더 regularization이 됨) |

---

## ✅ 3. 수학적 정의

신경망의 한 층에서 선형 변환은 다음과 같이 표현됩니다:

$$
z = W x$
$$

여기서 DropConnect는 weight matrix $W$에 대해 element-wise binary mask $M$을 곱해 다음과 같이 수정합니다:

$$
z = (W \odot M) x
$$
- $M_{ij} \sim \text{Bernoulli}(p)$: 각 weight $W_{ij}$에 대해 확률 $p$로 유지, $1 - p$로 제거
    
- $\odot$: element-wise 곱
    

즉, DropConnect는 학습 과정에서 **각 forward pass마다 가중치의 일부를 0으로 만들어 네트워크를 무작위로 희소하게** 만듭니다.

---

## ✅ 4. 직관적 이해

- **Dropout**은 "이 뉴런은 아예 작동하지 마!"
    
- **DropConnect**는 "이 뉴런은 작동은 하되, **연결선 일부는 끊어놓자**."
    

이로 인해 DropConnect는 훨씬 **세밀하게 구조를 무작위화**합니다.

---

## ✅ 5. 예시: Fully Connected Layer에 적용

기존 FC layer:

$$
z_i = \sum_j W_{ij} x_j
$$

DropConnect 적용 후:

$$
z_i = \sum_j (W_{ij} \cdot M_{ij}) x_j
$$

이 때 $M_{ij} \in \{0, 1\}$는 매 학습 배치에서 랜덤하게 재샘플됩니다.

---

## ✅ 6. 장점

|장점|설명|
|---|---|
|✅ 더 강력한 정규화|Dropout보다 더 높은 일반화 성능 가능|
|✅ 파라미터 단위의 제어|뉴런 전체가 아닌 가중치 단위에서의 sparsity|
|✅ 다른 정규화와 병행 가능|BatchNorm, MaxNorm과 병행 사용 가능|

---

## ✅ 7. 단점

|단점|설명|
|---|---|
|❌ 계산 비용 증가|각 weight에 대해 mask 연산 필요|
|❌ 학습 속도 느림|Dropout보다 구현이 복잡하고 느릴 수 있음|
|❌ Conv Layer에 바로 적용은 어려움|CNN에서는 weight sharing 구조 때문에 변형 필요|

---

## ✅ 8. DropConnect를 제안한 논문

**Wan et al. (2013)**

- 논문 제목: _Regularization of Neural Networks using DropConnect_
    
- 발표: ICML 2013
    
- 링크: [https://proceedings.mlr.press/v28/wan13.html](https://proceedings.mlr.press/v28/wan13.html)
    

> 🔍 결과: DropConnect는 MNIST에서 Dropout보다 더 나은 성능을 보였고, 다양한 신경망 구조에서도 regularization 효과가 입증됨.

---

## ✅ 9. 현대적 활용 예시: **EfficientNet → DropConnect의 변형 사용**

- EfficientNet에서는 **Stochastic Depth (DropPath)**라는 변형 기법을 사용했는데,  
    이는 Residual 연결에서 **레이어 전체를 드랍**하는 방식입니다.
    
- 이는 DropConnect의 아이디어와 유사하게 **경로를 랜덤하게 줄여 일반화 성능을 높이는 기법**입니다.
    

---

## ✅ 10. DropConnect 구현 예시 (PyTorch)

```python
class DropConnectLinear(nn.Linear):
    def __init__(self, in_features, out_features, bias=True, drop_prob=0.5):
        super().__init__(in_features, out_features, bias)
        self.drop_prob = drop_prob

    def forward(self, x):
        if self.training:
            # DropConnect mask on weight
            mask = torch.bernoulli(torch.ones_like(self.weight) * (1 - self.drop_prob))
            weight = self.weight * mask
        else:
            weight = self.weight * (1 - self.drop_prob)  # expectation during inference
        return F.linear(x, weight, self.bias)
```

---

## ✅ 11. 요약

|항목|내용|
|---|---|
|정의|뉴런 간 연결선(가중치)를 무작위로 제거하는 정규화 기법|
|목적|과적합 방지 및 일반화 성능 향상|
|Dropout과 차이|Dropout은 뉴런 제거, DropConnect는 연결 제거|
|한계|계산량 증가, Conv 구조에 직접 적용 어려움|
|활용|EfficientNet(Stochastic Depth), RNN/LSTM 일반화 등|

---
