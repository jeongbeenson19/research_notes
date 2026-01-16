
# NumPy

#numpy #python #data-science #library

NumPy(Numerical Python)는 파이썬에서 과학적 계산을 위한 핵심 라이브러리입니다. 강력한 N차원 배열 객체인 `ndarray`를 제공하며, 이를 기반으로 고성능의 수치 연산 및 데이터 처리를 지원합니다.

데이터 사이언스 분야에서 Pandas, Matplotlib, Scikit-learn 등 대부분의 주요 라이브러리들이 NumPy를 기반으로 구축되었기 때문에, NumPy에 대한 이해는 데이터 분석 및 머신러닝 작업을 위한 필수 요소입니다.

> **NumPy의 장점**
> - 파이썬 리스트보다 훨씬 빠르고 메모리 효율적인 다차원 배열(`ndarray`) 제공
> - 벡터화된 연산을 통해 반복문 없이 전체 배열에 대한 빠른 작업 가능
> - 광범위한 고성능 수학 함수, 선형대수, 푸리에 변환 및 난수 기능 지원

---

## 1. NumPy 배열 생성 (Array Creation)

데이터를 `ndarray` 형태로 변환하거나 특정 형태의 배열을 새로 생성합니다.

### `np.array()`
파이썬의 리스트, 튜플 등의 자료구조를 `ndarray`로 변환합니다.
```python
import numpy as np

# 1차원 배열
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
# 출력: [1 2 3 4 5]

# 2차원 배열 (행렬)
list2 = [[1, 2, 3], [4, 5, 6]]
arr2 = np.array(list2)
print(arr2)
# 출력:
# [[1 2 3]
#  [4 5 6]]
```

### `np.zeros()`, `np.ones()`, `np.full()`
특정 값으로 채워진 배열을 생성합니다.
```python
# 0으로 채워진 2x3 배열
zeros_arr = np.zeros((2, 3))
print(zeros_arr)
# 출력:
# [[0. 0. 0.]
#  [0. 0. 0.]]

# 1로 채워진 3x2 배열
ones_arr = np.ones((3, 2))
print(ones_arr)
# 출력:
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]

# 7로 채워진 2x2 배열
full_arr = np.full((2, 2), 7)
print(full_arr)
# 출력:
# [[7 7]
#  [7 7]]
```

### `np.arange()`
파이썬의 `range()`와 유사하지만, 정수뿐만 아니라 실수 단위로도 생성이 가능합니다.
```python
# 0부터 9까지의 1차원 배열
range_arr = np.arange(10)
print(range_arr)
# 출력: [0 1 2 3 4 5 6 7 8 9]

# 0부터 1까지 0.2 간격의 배열
step_arr = np.arange(0, 1, 0.2)
print(step_arr)
# 출력: [0.  0.2 0.4 0.6 0.8]
```

### `np.linspace()`
지정된 범위 내에서 균등한 간격의 숫자들을 포함하는 배열을 생성합니다.
```python
# 0과 10 사이를 5개의 균등한 간격으로 나눈 배열
linspace_arr = np.linspace(0, 10, 5)
print(linspace_arr)
# 출력: [ 0.   2.5  5.   7.5 10. ]
```

---

## 2. 배열 속성 (Array Attributes)

배열의 기본 정보를 확인합니다.

- `arr.ndim`: 배열의 차원 수
- `arr.shape`: 배열의 각 차원의 크기를 나타내는 튜플
- `arr.size`: 배열의 전체 요소 수
- `arr.dtype`: 배열 요소의 데이터 타입

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(f"차원: {arr.ndim}")       # 출력: 2
print(f"형태: {arr.shape}")     # 출력: (2, 3)
print(f"전체 요소 수: {arr.size}") # 출력: 6
print(f"데이터 타입: {arr.dtype}") # 출력: int64
```

---

## 3. 인덱싱과 슬라이싱 (Indexing and Slicing)

배열의 특정 부분에 접근하거나 수정합니다.

### 기본 인덱싱 및 슬라이싱
파이썬 리스트와 유사하지만, 다차원 배열에 대해 더 강력한 기능을 제공합니다.
```python
arr = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]

# 단일 요소 접근
print(arr[5])  # 출력: 5

# 슬라이싱 (start:stop:step)
print(arr[2:8:2])  # 출력: [2 4 6]

# 2차원 배열 슬라이싱
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[1:, :2])
# 출력:
# [[4 5]
#  [7 8]]
```

### 불리언 인덱싱 (Boolean Indexing)
조건을 만족하는 요소만 선택하는 방식. 데이터 정제나 필터링에 매우 유용합니다.
```python
arr = np.array([10, 20, 30, 40, 50])
bool_idx = np.array([True, False, True, False, True])

print(arr[bool_idx])  # 출력: [10 30 50]

# 조건을 직접 사용
print(arr[arr > 25])  # 출력: [30 40 50]
```

---

## 4. 배열 형태 변경 (Array Manipulation)

### `reshape()`
배열의 차원과 형태를 변경합니다. 단, 전체 요소의 수는 동일해야 합니다.
```python
arr = np.arange(12)  # [0, 1, ..., 11]

# 1차원 배열을 3x4 2차원 배열로 변경
reshaped_arr = arr.reshape(3, 4)
print(reshaped_arr)
# 출력:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
```

### `concatenate()`, `vstack()`, `hstack()`
여러 배열을 하나로 결합합니다.
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# 수직으로 결합 (vstack)
v_concat = np.vstack((a, b))
print(v_concat)
# 출력:
# [[1 2]
#  [3 4]
#  [5 6]]

# 수평으로 결합 (hstack) - 형태가 맞아야 함
c = np.array([[5], [6]])
h_concat = np.hstack((a, c))
print(h_concat)
# 출력:
# [[1 2 5]
#  [3 4 6]]
```

---

## 5. 유니버설 함수 (Universal Functions, ufuncs)

배열의 모든 요소에 대해 반복문 없이 연산을 수행하는 함수입니다. 이는 NumPy의 핵심적인 성능 우위 요소입니다.

### 요소별 산술 연산
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # 출력: [5 7 9]
print(a * 2)  # 출력: [2 4 6]
```

### 수학 함수
`np.sqrt()`, `np.exp()`, `np.log()`, `np.sin()` 등 다양한 함수가 제공됩니다.
```python
arr = np.array([1, 4, 9])
print(np.sqrt(arr))  # 출력: [1. 2. 3.]
```

---

## 6. 집계 함수 (Aggregation Functions)

배열 전체 또는 특정 축(axis)을 기준으로 통계량을 계산합니다.

- `np.sum()`: 합계
- `np.mean()`: 평균
- `np.std()`: 표준편차
- `np.min()` / `np.max()`: 최소값 / 최대값
- `np.argmin()` / `np.argmax()`: 최소값 / 최대값의 인덱스

`axis` 매개변수가 중요합니다.
- `axis=0`: 열(column) 방향으로 연산
- `axis=1`: 행(row) 방향으로 연산

```python
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print(f"전체 합계: {np.sum(arr2d)}")          # 출력: 21
print(f"열(세로) 기준 합계: {np.sum(arr2d, axis=0)}") # 출력: [5 7 9]
print(f"행(가로) 기준 합계: {np.sum(arr2d, axis=1)}") # 출력: [ 6 15]
```

---

## 7. 브로드캐스팅 (Broadcasting)

서로 다른 형태(shape)를 가진 배열 간의 산술 연산을 가능하게 하는 NumPy의 강력한 기능입니다. 특정 조건 하에서 작은 배열이 큰 배열의 형태에 맞춰 자동으로 확장되어 연산이 수행됩니다.

```python
a = np.array([[1, 2, 3], [4, 5, 6]])  # (2, 3)
b = np.array([10, 20, 30])             # (3,)

# b가 a의 각 행에 더해짐
result = a + b
print(result)
# 출력:
# [[11 22 33]
#  [14 25 36]]
```

---

## 8. 선형대수 (Linear Algebra)

NumPy는 `np.linalg` 서브모듈을 통해 강력한 선형대수 기능을 제공합니다.

- `np.dot(a, b)` 또는 `a @ b`: 행렬 곱
- `np.linalg.inv(a)`: 역행렬
- `np.linalg.eig(a)`: 고유값(eigenvalue)과 고유벡터(eigenvector)

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 행렬 곱
dot_product = np.dot(A, B)
print(dot_product)
# 출력:
# [[19 22]
#  [43 50]]
```

---

## 9. 난수 생성 (Random Number Generation)

`np.random` 모듈은 다양한 종류의 난수를 생성하는 함수를 제공합니다.

- `np.random.rand(d0, d1, ...)`: `[0, 1)` 범위에서 균등 분포를 따르는 난수 생성
- `np.random.randn(d0, d1, ...)`: 표준 정규 분포(평균 0, 표준편차 1)를 따르는 난수 생성
- `np.random.randint(low, high, size)`: `[low, high)` 범위의 정수 난수 생성
- `np.random.seed(num)`: 난수 생성을 위한 시드(seed) 설정. 재현성을 보장합니다.

```python
# 재현성을 위해 시드 설정
np.random.seed(42)

# 2x3 형태의 난수 배열 생성
rand_arr = np.random.rand(2, 3)
print(rand_arr)
# 출력:
# [[0.37454012 0.95071431 0.73199394]
#  [0.59865848 0.15601864 0.15599452]]
```
