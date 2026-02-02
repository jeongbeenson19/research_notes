
# Seaborn

#seaborn #python #data-visualization #library

Seaborn은 Matplotlib을 기반으로 만들어진 파이썬 데이터 시각화 라이브러리입니다. [[Matplotlib]]보다 더 간결한 코드로 더 아름답고 통계적으로 의미 있는 그래프를 생성하는 것을 목표로 합니다.

특히 Pandas DataFrame과의 통합이 뛰어나 데이터프레임의 컬럼 이름을 직접 사용하여 복잡한 시각화를 손쉽게 구현할 수 있습니다.

> **Seaborn의 장점**
> - Matplotlib을 기반으로 하여 세부적인 조정이 가능하면서도, 기본적으로 더 미려한 스타일 제공
> - 통계적 정보(신뢰 구간, 분포 등)를 시각화하는 데 특화된 다양한 플롯 제공
> - Pandas DataFrame과 완벽하게 호환되어 데이터 조작과 시각화가 자연스럽게 연결됨
> - 복잡한 다변량 데이터의 관계를 파악할 수 있는 고수준의 함수 지원 (e.g., `pairplot`, `heatmap`)

---

## 1. Seaborn 시작하기

Seaborn은 일반적으로 `sns`라는 별칭으로 임포트하며, 내장된 테마와 스타일을 설정하여 그래프의 전반적인 미관을 향상시킬 수 있습니다.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn의 기본 스타일과 색상 팔레트 설정
sns.set_theme(style="whitegrid", palette="muted")

# Seaborn에 내장된 'tips' 데이터셋 로드
tips = sns.load_dataset("tips")

# 데이터셋 미리보기
# print(tips.head())
```

---

## 2. 관계 시각화 (Relational Plots)

두 변수 간의 관계를 탐색하는 데 사용됩니다.

### `sns.scatterplot()`
두 수치형 변수 간의 관계를 점으로 나타냅니다. `hue` 매개변수를 사용하여 세 번째 범주형 변수를 색상으로 표현할 수 있습니다.

```python
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")
plt.title("Tip amount vs. Total Bill")
plt.show()
```

### `sns.lineplot()`
주로 시간의 흐름에 따른 데이터의 변화(시계열)나 연속적인 변수 간의 관계를 선으로 표현합니다. 기본적으로 신뢰구간(confidence interval)을 함께 표시합니다.

```python
flights = sns.load_dataset("flights")

sns.lineplot(data=flights, x="year", y="passengers")
plt.title("Yearly Passengers Growth")
plt.show()
```

---

## 3. 분포 시각화 (Distribution Plots)

단일 변수의 분포나 변수 간의 결합 분포를 시각화합니다.

### `sns.histplot()` & `sns.kdeplot()`
- **histplot**: 데이터의 분포를 막대그래프(히스토그램)로 나타냅니다.
- **kdeplot**: Kernel Density Estimation을 통해 데이터의 분포를 부드러운 곡선으로 나타냅니다.

```python
sns.histplot(data=tips, x="total_bill", kde=True, bins=20)
plt.title("Distribution of Total Bill")
plt.show()
```

### `sns.boxplot()` & `sns.violinplot()`
- **boxplot**: 데이터의 사분위수와 이상치를 시각화하여 범주별 데이터 분포를 비교하는 데 유용합니다.
- **violinplot**: boxplot과 kdeplot을 결합한 형태로, 데이터의 전체적인 분포 형태까지 함께 보여줍니다.

```python
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Box Plot")

plt.subplot(1, 2, 2)
sns.violinplot(data=tips, x="day", y="total_bill")
plt.title("Violin Plot")

plt.tight_layout()
plt.show()
```

---

## 4. 범주형 데이터 시각화 (Categorical Plots)

하나 이상의 변수가 범주형일 때 사용하는 플롯입니다.

### `sns.countplot()`
범주별 데이터의 개수를 막대그래프로 보여줍니다.

```python
sns.countplot(data=tips, x="day", hue="sex")
plt.title("Count of Customers by Day and Sex")
plt.show()
```

### `sns.barplot()`
범주별 데이터의 평균과 신뢰구간을 막대그래프로 보여줍니다. `countplot`이 단순 개수를 세는 반면, `barplot`은 특정 수치형 변수의 통계량을 계산합니다.

```python
sns.barplot(data=tips, x="day", y="total_bill", hue="smoker")
plt.title("Average Total Bill by Day and Smoker Status")
plt.show()
```

---

## 5. 행렬 시각화 (Matrix Plots)

2차원 데이터를 색상을 이용해 시각화합니다.

### `sns.heatmap()`
데이터 행렬의 각 셀 값을 색상으로 표현합니다. 변수 간의 상관계수 행렬을 시각화하는 데 매우 유용합니다.

```python
# 수치형 데이터만 선택하여 상관계수 계산
numeric_cols = tips.select_dtypes(include=np.number)
correlation_matrix = numeric_cols.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix of Tips Dataset")
plt.show()
```

---

## 6. 다중 플롯 그리드 (Multi-plot Grids)

데이터셋의 다양한 측면을 한 번에 탐색하기 위해 여러 플롯을 격자 형태로 배열합니다.

### `sns.pairplot()`
데이터프레임의 모든 수치형 변수 쌍에 대해 스캐터 플롯을, 대각선에는 각 변수의 분포(히스토그램 또는 KDE)를 그립니다. 데이터셋 전체의 관계를 조망하는 데 가장 강력한 도구 중 하나입니다.

```python
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
plt.suptitle("Pair Plot of Iris Dataset", y=1.02)
plt.show()
```

### `sns.jointplot()`
두 변수에 대한 스캐터 플롯과 각 변수의 히스토그램/KDE를 함께 보여줍니다. 두 변수의 관계와 각 변수의 분포를 동시에 파악할 수 있습니다.

```python
sns.jointplot(data=tips, x="total_bill", y="tip", kind="hex") # kind: scatter, reg, kde, hex
plt.suptitle("Joint Plot of Total Bill and Tip", y=1.02)
plt.show()
```

---

## 7. Seaborn 내장 데이터셋 활용

Seaborn은 예제와 학습을 위해 몇 가지 유명한 데이터셋을 내장하고 있습니다. `sns.load_dataset()` 함수를 사용하여 손쉽게 Pandas DataFrame으로 불러올 수 있습니다.

- **사용법**: `sns.load_dataset("dataset_name")`
- **주요 데이터셋**: `tips`, `iris`, `titanic`, `flights`, `penguins` 등

### `iris` 데이터셋이란?

분류(Classification) 문제의 "Hello, World!"와 같은 고전적인 데이터셋입니다. 통계학자 피셔(Fisher)가 소개했으며, 붓꽃(iris)의 세 가지 품종을 꽃받침(sepal)과 꽃잎(petal)의 길이와 너비를 이용해 분류하는 문제를 다룹니다.

- **Features (독립 변수, 수치형)**:
    - `sepal_length`: 꽃받침 길이
    - `sepal_width`: 꽃받침 너비
    - `petal_length`: 꽃잎 길이
    - `petal_width`: 꽃잎 너비
- **Target (종속 변수, 범주형)**:
    - `species`: 붓꽃의 품종 (`setosa`, `versicolor`, `virginica`)

```python
import seaborn as sns
import numpy as np

# iris 데이터셋 로드
iris = sns.load_dataset("iris")

# 데이터셋 정보 확인
print("---", "Iris Dataset Info", "---")
iris.info()

# 데이터셋 상위 5개 행 출력
print("\n---", "First 5 Rows", "---")
print(iris.head())

# 품종별 데이터 개수 확인
print("\n---", "Species Count", "---")
print(iris['species'].value_counts())
```