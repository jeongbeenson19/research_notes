
# Scikit-learn

#scikit-learn #python #machine-learning #library

Scikit-learn(사이킷런)은 파이썬을 위한 가장 대표적이고 포괄적인 머신러닝 라이브러리입니다. 분류, 회귀, 클러스터링, 차원 축소 등 다양한 머신러닝 알고리즘을 제공하며, [[Numpy]], [[Pandas]], [[Matplotlib]] 등 다른 과학 컴퓨팅 라이브러리와 완벽하게 연동됩니다.

Scikit-learn은 일관된 API 설계를 통해 다양한 모델을 동일한 방식으로 사용할 수 있도록 하여, 머신러닝 모델의 실험과 배포를 매우 용이하게 만듭니다.

> **Scikit-learn의 장점**
> - 분류, 회귀, 클러스터링 등 광범위한 머신러닝 알고리즘을 포함
> - `fit()`, `predict()`, `transform()`으로 통일된 직관적이고 일관된 API 제공
> - 데이터 분할, 전처리, 모델 평가, 하이퍼파라미터 튜닝 등 모델링 전 과정을 지원하는 풍부한 유틸리티
> - 상세한 공식 문서와 풍부한 예제로 높은 학습 편의성

---

## 1. Scikit-learn의 핵심 API: Estimator

Scikit-learn의 모든 알고리즘은 **Estimator**라는 공통된 인터페이스를 따릅니다. 이 덕분에 모델을 교체하더라도 코드의 구조를 거의 변경할 필요가 없습니다.

- **`fit(X, y)`**: 모델을 학습시키는 메서드. `X`는 학습 데이터(피처), `y`는 타겟 데이터(레이블)입니다.
- **`predict(X)`**: 학습된 모델을 사용하여 새로운 데이터 `X`의 결과를 예측합니다. (분류, 회귀 등)
- **`transform(X)`**: 데이터를 변환합니다. (주로 전처리나 차원 축소에 사용)
- **`fit_transform(X, y)`**: `fit()`과 `transform()`을 한 번에 수행하여 코드를 간결하게 만듭니다.

---

## 2. 머신러닝 워크플로우 예시

Scikit-learn을 사용한 일반적인 머신러닝 작업 흐름입니다.

1.  **데이터 로드 및 준비**: [[Pandas]] DataFrame으로 데이터를 불러오고 피처(X)와 타겟(y)으로 분리합니다.
2.  **데이터 분할**: `train_test_split`을 사용하여 학습용 데이터와 테스트용 데이터로 나눕니다.
3.  **모델 선택 및 초기화**: 사용할 머신러닝 모델(Estimator)을 선택하고 객체를 생성합니다.
4.  **모델 학습**: `fit()` 메서드를 사용하여 학습용 데이터로 모델을 학습시킵니다.
5.  **예측**: `predict()` 메서드를 사용하여 테스트용 데이터로 예측을 수행합니다.
6.  **모델 평가**: 예측 결과와 실제 값을 비교하여 모델의 성능을 평가합니다.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. 데이터 준비 (예시)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# 2. 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 모델 선택 및 초기화
model = LinearRegression()

# 4. 모델 학습
model.fit(X_train, y_train)

# 5. 예측
y_pred = model.predict(X_test)

# 6. 모델 평가
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
```

---

## 3. 지도 학습 (Supervised Learning)

정답(label)이 있는 데이터를 사용하여 모델을 학습시키는 방법입니다.

### 분류 (Classification)
데이터를 주어진 클래스(범주) 중 하나로 예측하는 문제입니다.
- **`LogisticRegression`**: 선형 모델을 사용한 이진 또는 다중 클래스 분류.
- **`SVC` (Support Vector Classification)**: 서포트 벡터 머신을 사용한 분류.
- **`DecisionTreeClassifier`**: 결정 트리 기반 분류.
- **`RandomForestClassifier`**: 여러 결정 트리를 결합한 앙상블 모델.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
```

### 회귀 (Regression)
연속적인 값을 예측하는 문제입니다.
- **`LinearRegression`**: 가장 기본적인 선형 회귀 모델.
- **`Ridge`, `Lasso`**: 규제(Regularization)가 추가된 선형 회귀 모델.
- **`SVR` (Support Vector Regression)**: 서포트 벡터 머신을 사용한 회귀.
- **`RandomForestRegressor`**: 랜덤 포레스트 기반 회귀.

---

## 4. 비지도 학습 (Unsupervised Learning)

정답(label)이 없는 데이터를 사용하여 데이터 자체의 숨겨진 구조나 패턴을 찾는 방법입니다.

### 클러스터링 (Clustering)
비슷한 특성을 가진 데이터들을 그룹으로 묶는 기법입니다.
- **`KMeans`**: 데이터를 K개의 클러스터로 묶는 가장 대표적인 알고리즘.
- **`DBSCAN`**: 밀도 기반 클러스터링 알고리즘.

```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 2차원 데이터 생성 (예시)
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.title("K-Means Clustering")
plt.show()
```

### 차원 축소 (Dimensionality Reduction)
데이터의 특성(feature) 수를 줄이면서 정보 손실을 최소화하는 기법입니다.
- **`PCA` (Principal Component Analysis)**: 주성분 분석. 데이터의 분산을 가장 잘 설명하는 새로운 축을 찾아 차원을 축소합니다.

---

## 5. 데이터 전처리 및 파이프라인

머신러닝 모델의 성능을 높이기 위해 데이터를 적절히 가공하는 과정입니다.

### 데이터 스케일링
피처의 단위를 통일시켜 모델이 더 잘 학습되도록 합니다.
- **`StandardScaler`**: 각 피처의 평균을 0, 분산을 1로 조정합니다.
- **`MinMaxScaler`**: 각 피처의 값이 0과 1 사이에 오도록 조정합니다.

```python
from sklearn.preprocessing import StandardScaler

# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X_train)
```

### 파이프라인 (`Pipeline`)
데이터 전처리 과정과 모델 학습을 하나로 묶어주는 기능입니다. 코드의 가독성을 높이고 실수할 가능성을 줄여줍니다.

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC())
])

pipe.fit(X_train, y_train)
print(f"Pipeline Score: {pipe.score(X_test, y_test)}")
```

---

## 6. 모델 선택 및 평가

### 교차 검증 (`cross_val_score`)
데이터를 여러 번 나누어 학습과 평가를 반복함으로써 모델의 일반화 성능을 더 안정적으로 측정하는 방법입니다.

### 하이퍼파라미터 튜닝 (`GridSearchCV`)
모델의 성능을 최적화하기 위해 최적의 하이퍼파라미터 조합을 찾는 과정입니다. 지정된 파라미터 조합을 모두 시도하여 가장 좋은 성능을 내는 조합을 찾습니다.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)


param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30]
}

grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Score: {grid_search.best_score_}")
```