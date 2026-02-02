
# 데이터 전처리 (Data Preprocessing)

#data-preprocessing #machine-learning #feature-engineering

데이터 전처리는 머신러닝 모델의 성능을 극대화하기 위해 원본 데이터(raw data)를 모델에 적합한 형태로 가공하는 과정입니다. "Garbage In, Garbage Out"이라는 말처럼, 데이터의 품질은 모델의 품질과 직결됩니다.

이 문서에서는 머신러닝에서 가장 기본적이고 필수적인 전처리 기법인 **범주형 데이터 인코딩**과 **피처 스케일링**에 대해 자세히 다룹니다.

- **범주형 데이터 인코딩**: 문자열 데이터를 모델이 이해할 수 있는 숫자형으로 변환합니다.
    - [[#1. 레이블 인코딩 (Label Encoding)]]
    - [[#2. 원-핫 인코딩 (One-Hot Encoding)]]
- **피처 스케일링**: 각 피처(변수)의 값의 범위를 일정하게 조정하여 모델의 학습을 안정화시킵니다.
    - [[#3. Min-Max 스케일링 (Min-Max Scaling)]]
    - [[#4. 표준화 (Standardization | Z-score Scaling)]]

---

## 1. 레이블 인코딩 (Label Encoding)

레이블 인코딩은 n개의 범주형 데이터를 0부터 n-1까지의 정수 값으로 변환하는 기법입니다.

예를 들어, 'Red', 'Green', 'Blue'라는 세 가지 범주가 있다면 각각 0, 1, 2와 같이 맵핑됩니다.

### 장점
- 구현이 간단하고, 차원을 늘리지 않아 계산 비용이 저렴합니다.

### 단점
- **순서의 특성**이 없는 범주형 데이터에 적용할 경우, 모델이 값의 크기에 따라 **잘못된 가중치**를 부여할 수 있습니다. 예를 들어, `Red(0) < Green(1) < Blue(2)` 와 같은 순서 관계가 없는데도 모델은 이를 학습할 수 있습니다.
- 따라서, 'Small', 'Medium', 'Large'와 같이 명확한 순서가 있는 데이터(Ordinal data)에 사용하는 것이 가장 적합합니다.

### Scikit-learn 예제

`sklearn.preprocessing.LabelEncoder`를 사용하여 레이블 인코딩을 수행할 수 있습니다.

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 예제 데이터
df = pd.DataFrame({'color': ['Red', 'Green', 'Blue', 'Green', 'Red']})

# LabelEncoder 객체 생성 및 학습/변환
encoder = LabelEncoder()
df['color_encoded'] = encoder.fit_transform(df['color'])

print(df)
# classes_ 속성으로 인코딩된 클래스 확인 가능
print("인코딩 클래스:", encoder.classes_)
```
**출력:**
```
   color  color_encoded
0    Red              2
1  Green              1
2   Blue              0
3  Green              1
4    Red              2
인코딩 클래스: ['Blue' 'Green' 'Red']
```

---

## 2. 원-핫 인코딩 (One-Hot Encoding)

원-핫 인코딩은 범주형 데이터를 0과 1로만 이루어진 벡터로 변환하는 기법입니다. 각 범주를 새로운 피처(컬럼)로 만들고, 해당 범주에 속하는 데이터는 1로, 나머지는 0으로 표시합니다.

예를 들어, 'Red', 'Green', 'Blue' 범주가 있다면, 3개의 새로운 컬럼 `is_Red`, `is_Green`, `is_Blue`가 생성됩니다. 'Green' 데이터는 `[0, 1, 0]` 벡터로 표현됩니다.

### 장점
- 범주 간의 순서 관계가 없으므로, 모델이 값의 크기에 따른 잘못된 해석을 하는 것을 방지합니다.
- 선형 모델이나 SVM과 같이 거리 기반 알고리즘에서 성능 저하를 막을 수 있습니다.

### 단점
- 범주의 개수가 많아지면 피처의 수가 급격히 늘어나 **차원의 저주(Curse of Dimensionality)** 를 유발할 수 있습니다.
- 이로 인해 계산 비용이 증가하고, 모델의 복잡도가 높아져 과적합의 위험이 생길 수 있습니다.

### Scikit-learn 예제

`sklearn.preprocessing.OneHotEncoder` 또는 `pandas.get_dummies`를 사용하여 원-핫 인코딩을 수행할 수 있습니다.

#### `pandas.get_dummies` 사용 (더 간편함)
```python
import pandas as pd

# 예제 데이터
df = pd.DataFrame({'color': ['Red', 'Green', 'Blue', 'Green', 'Red']})

# get_dummies 함수로 원-핫 인코딩
one_hot_df = pd.get_dummies(df['color'], prefix='color')

# 원본 데이터프레임과 병합
df = pd.concat([df, one_hot_df], axis=1)

print(df)
```
**출력:**
```
   color  color_Blue  color_Green  color_Red
0    Red           0            0          1
1  Green           0            1          0
2   Blue           1            0          0
3  Green           0            1          0
4    Red           0            0          1
```

---

## 3. Min-Max 스케일링 (Min-Max Scaling)

Min-Max 스케일링은 데이터의 모든 피처 값을 **0과 1 사이의 범위**로 변환하는 기법입니다. 각 피처의 최소값은 0으로, 최대값은 1로 맵핑됩니다. **정규화(Normalization)**라고도 불립니다.

### 수식

피처 $x$의 각 값은 다음 수식에 의해 변환됩니다.

$$ 
x_{scaled} = \frac{x - x_{min}}{x_{max} - x_{min}} 
$$

- $x$: 원본 데이터 포인트
- $x_{min}$: 해당 피처의 최소값
- $x_{max}$: 해당 피처의 최대값

### 장점
- 모든 피처를 동일한 스케일로 만들어주므로, 거리 기반 알고리즘(KNN, SVM)이나 경사 하강법 기반 알고리즘(선형 회귀, 로지스틱 회귀, 신경망)에서 성능을 향상시킵니다.
- 데이터의 분포를 유지하면서 스케일만 조정합니다.

### 단점
- **이상치(Outlier)에 매우 민감**합니다. 만약 아주 큰 값이나 아주 작은 값이 이상치로 존재한다면, 대부분의 데이터가 매우 좁은 범위에 압축될 수 있습니다.

### Scikit-learn 예제

`sklearn.preprocessing.MinMaxScaler`를 사용합니다.

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 예제 데이터
data = {'value': [10, 20, 50, 100, -10]}
df = pd.DataFrame(data)

# MinMaxScaler 객체 생성 및 학습/변환
scaler = MinMaxScaler()
df['value_scaled'] = scaler.fit_transform(df[['value']])

print(df)
```
**출력:**
```
   value  value_scaled
0     10      0.181818
1     20      0.272727
2     50      0.545455
3    100      1.000000
4    -10      0.000000
```

---

## 4. 표준화 (Standardization | Z-score Scaling)

표준화는 각 피처의 평균을 0, 표준편차를 1로 변환하는 기법입니다. 변환된 데이터는 **표준 정규분포**와 유사한 형태를 갖게 됩니다.

### 수식

피처 $x$의 각 값은 다음 수식에 의해 변환됩니다. (Z-score 계산과 동일)

$$ 
x_{scaled} = \frac{x - \mu}{\sigma} 
$$

- $x$: 원본 데이터 포인트
- $\mu$: 해당 피처의 평균
- $\sigma$: 해당 피처의 표준편차

### 장점
- **이상치에 상대적으로 덜 민감**합니다. Min-Max 스케일링과 달리 이상치가 전체 데이터의 스케일링에 미치는 영향이 적습니다.
- 데이터가 정규분포를 따른다고 가정하는 많은 알고리즘에서 좋은 성능을 보입니다.

### 단점
- 변환된 값의 범위가 특정 구간으로 제한되지 않습니다. 대부분의 값이 -3과 3 사이에 분포하지만, 더 크거나 작은 값도 나타날 수 있습니다.

### Scikit-learn 예제

`sklearn.preprocessing.StandardScaler`를 사용합니다.

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# 예제 데이터
data = {'value': [10, 20, 50, 100, -10]}
df = pd.DataFrame(data)

# StandardScaler 객체 생성 및 학습/변환
scaler = StandardScaler()
df['value_scaled'] = scaler.fit_transform(df[['value']])

print(df)
print(f"\n평균: {df['value_scaled'].mean():.2f}")
print(f"표준편차: {df['value_scaled'].std():.2f}")
```
**출력:**
```
   value  value_scaled
0     10     -0.566139
1     20     -0.314521
2     50      0.439330
3    100      1.886124
4    -10     -1.444804

평균: 0.00
표준편차: 1.12
```
