
# Pandas

#pandas #python #data-analysis #library

Pandas는 파이썬에서 데이터 분석과 조작을 위한 가장 핵심적인 라이브러리입니다. R의 `data.frame`에 영감을 받아 설계된, **Series**와 **DataFrame**이라는 강력하고 유연한 데이터 구조를 제공합니다.

Pandas를 사용하면 정형 데이터를 손쉽게 불러오고, 정제하며, 분석하고, 시각화 전 단계까지 처리할 수 있습니다. [[Numpy]]가 수치 연산에 중점을 둔다면, Pandas는 테이블 형태의 데이터를 다루는 데 특화되어 있습니다.

> **Pandas의 장점**
> - 빠르고 효율적인 **DataFrame** 객체를 통해 대규모 데이터를 유연하게 처리
> - CSV, Excel, SQL 데이터베이스 등 다양한 포맷의 데이터를 읽고 쓰는 기능 제공
> - 데이터 정렬, 누락값 처리, 필터링, 선택 등 데이터 정제 및 준비를 위한 풍부한 기능
> - 강력한 `groupby` 기능을 통한 데이터 집계 및 변환
> - 시계열 데이터 처리에 특화된 기능 지원

---

## 1. Pandas의 핵심 자료구조

### `pd.Series`
1차원 배열과 유사한 구조로, 각 데이터 값에 **인덱스(index)**를 부여할 수 있습니다. 모든 데이터 타입을 저장할 수 있습니다.

```python
import pandas as pd

# 리스트로부터 Series 생성
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# 출력:
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64
```

### `pd.DataFrame`
2차원 테이블 형태의 자료구조로, 여러 개의 Series가 모여 구성됩니다. 각 열(column)은 서로 다른 데이터 타입을 가질 수 있으며, 행과 열에 모두 인덱스가 있습니다. 데이터 분석 작업의 대부분은 DataFrame을 대상으로 이루어집니다.

```python
import pandas as pd
import numpy as np

# 딕셔너리로부터 DataFrame 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}
df = pd.DataFrame(data)
print(df)
# 출력:
#       Name  Age       City
# 0    Alice   25   New York
# 1      Bob   30      Paris
# 2  Charlie   35     London
# 3    David   28      Tokyo
```

---

## 2. 데이터 확인하기 (Inspecting Data)

DataFrame의 기본적인 정보를 파악하는 메서드들입니다.

- `df.head(n)`: 처음 n개의 행을 보여줍니다. (기본값: 5)
- `df.tail(n)`: 마지막 n개의 행을 보여줍니다. (기본값: 5)
- `df.info()`: DataFrame의 인덱스, 컬럼, 데이터 타입, 메모리 사용량 등 요약 정보를 제공합니다.
- `df.describe()`: 수치형 컬럼에 대한 주요 통계량(개수, 평균, 표준편차, 최소/최대값, 사분위수)을 요약합니다.
- `df.shape`: DataFrame의 형태(행의 수, 열의 수)를 튜플로 반환합니다.
- `df.columns`: 컬럼명을 반환합니다.
- `df.index`: 인덱스 정보를 반환합니다.

```python
# df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Name    4 non-null      object
#  1   Age     4 non-null      int64
#  2   City    4 non-null      object
# dtypes: int64(1), object(2)
# memory usage: 224.0+ bytes

# df.describe()
#              Age
# count   4.000000
# mean   29.500000
# std     4.203173
# min    25.000000
# 25%    27.250000
# 50%    29.000000
# 75%    31.250000
# max    35.000000
```

---

## 3. 데이터 선택 및 필터링 (Selection & Filtering)

DataFrame에서 원하는 데이터를 추출하는 것은 매우 중요합니다.

### 컬럼 선택
- `df['ColumnName']`: 하나의 컬럼을 Series 형태로 선택합니다.
- `df[['Col1', 'Col2']]`: 여러 개의 컬럼을 DataFrame 형태로 선택합니다.

```python
# 'Name' 컬럼 선택
print(df['Name'])

# 'Name'과 'City' 컬럼 선택
print(df[['Name', 'City']])
```

### 행 선택: `loc`와 `iloc`
- **`df.loc[]` (Label-based)**: 인덱스 이름(label)을 기준으로 행과 열을 선택합니다.
- **`df.iloc[]` (Integer-based)**: 정수 인덱스(0부터 시작하는 위치)를 기준으로 행과 열을 선택합니다.

```python
# 인덱스 레이블이 1인 행 선택
print(df.loc[1])

# 0번, 2번 행과 'Name', 'Age' 컬럼 선택
print(df.loc[[0, 2], ['Name', 'Age']])

# 2번째 행(정수 위치) 선택
print(df.iloc[2])

# 첫 3개 행과 첫 2개 컬럼 선택
print(df.iloc[:3, :2])
```

### 불리언 인덱싱 (Boolean Indexing)
조건을 만족하는 행만 필터링하는 가장 일반적이고 강력한 방법입니다.

```python
# 나이가 30세 이상인 데이터 필터링
print(df[df['Age'] >= 30])
# 출력:
#       Name  Age    City
# 1      Bob   30   Paris
# 2  Charlie   35  London

# 도시가 'New York' 또는 'Tokyo'인 데이터 필터링
print(df[df['City'].isin(['New York', 'Tokyo'])])
```

---

## 4. 데이터 조작 (Data Manipulation)

### 정렬
- `df.sort_values(by='ColumnName', ascending=True)`: 특정 컬럼을 기준으로 데이터를 정렬합니다.

```python
# 나이를 기준으로 내림차순 정렬
df_sorted = df.sort_values(by='Age', ascending=False)
print(df_sorted)
```

### 컬럼 추가 및 삭제
- `df['NewColumn'] = values`: 새로운 컬럼을 추가합니다.
- `df.drop('ColumnName', axis=1)`: 컬럼을 삭제합니다. `axis=1`은 컬럼을 의미합니다.

```python
# 'Age_Group' 컬럼 추가
df['Age_Group'] = df['Age'] // 10 * 10
print(df)

# 'City' 컬럼 삭제
df_dropped = df.drop('City', axis=1)
print(df_dropped)
```

### 결측치 처리 (Handling Missing Data)
- `df.isnull()`: 결측치(NaN) 여부를 boolean 마스크로 반환합니다.
- `df.dropna()`: 결측치가 포함된 행 또는 열을 제거합니다.
- `df.fillna(value)`: 결측치를 특정 값으로 채웁니다.

```python
data_with_nan = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]}
df_nan = pd.DataFrame(data_with_nan)

# 결측치 제거
print(df_nan.dropna())

# 결측치를 평균값으로 채우기
mean_A = df_nan['A'].mean()
print(df_nan.fillna(value={'A': mean_A}))
```

---

## 5. GroupBy: 데이터 집계 및 그룹 연산

데이터를 특정 기준으로 그룹화하여 각 그룹에 대해 집계 함수(sum, mean, count 등)를 적용하는 강력한 기능입니다. **Split-Apply-Combine** 전략을 따릅니다.

1.  **Split**: 특정 기준(컬럼)에 따라 데이터를 여러 그룹으로 분할합니다.
2.  **Apply**: 각 그룹에 대해 함수(e.g., `sum`, `mean`)를 독립적으로 적용합니다.
3.  **Combine**: Apply된 결과들을 하나의 DataFrame으로 결합합니다.

```python
# 'tips' 데이터셋 로드
tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

# 요일(day)별 팁(tip)의 평균 계산
day_tip_mean = tips.groupby('day')['tip'].mean()
print(day_tip_mean)
# 출력:
# day
# Fri     2.734737
# Sat     2.993103
# Sun     3.255132
# Thur    2.771452
# Name: tip, dtype: float64

# 성별(sex)과 흡연여부(smoker)에 따라 total_bill과 tip의 평균 계산
grouped_stats = tips.groupby(['sex', 'smoker'])[['total_bill', 'tip']].mean()
print(grouped_stats)
```

---

## 6. 데이터 병합 및 연결 (Merge, Join, Concat)

여러 개의 DataFrame을 하나로 합치는 방법입니다.

### `pd.concat()`
단순히 DataFrame을 수직 또는 수평으로 이어 붙입니다.

```python
df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})

# 수직으로 연결
result = pd.concat([df1, df2])
print(result)
```

### `pd.merge()`
SQL의 `JOIN`과 같이 특정 공통 컬럼(key)을 기준으로 두 DataFrame을 병합합니다.

```python
left = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K3'], 'B': ['B0', 'B1', 'B3']})

# 'key' 컬럼을 기준으로 병합 (inner join이 기본값)
merged = pd.merge(left, right, on='key', how='inner')
print(merged)
# 출력:
#   key   A   B
# 0  K0  A0  B0
# 1  K1  A1  B1
```
- `how` 옵션: `inner`, `outer`, `left`, `right` 등 다양한 조인 방식을 지정할 수 있습니다.

---

## 7. 파일 입출력 (File I/O)

Pandas는 다양한 데이터 소스를 손쉽게 DataFrame으로 변환할 수 있습니다.

- `pd.read_csv('file.csv')`: CSV 파일을 읽어 DataFrame으로 만듭니다.
- `pd.read_excel('file.xlsx')`: Excel 파일을 읽습니다.
- `df.to_csv('output.csv', index=False)`: DataFrame을 CSV 파일로 저장합니다. `index=False`는 인덱스를 파일에 쓰지 않는 옵션입니다.

```python
# CSV 파일 읽기
# tips_df = pd.read_csv('tips.csv')

# DataFrame을 CSV 파일로 저장하기
# df.to_csv('my_dataframe.csv', index=False)
```
