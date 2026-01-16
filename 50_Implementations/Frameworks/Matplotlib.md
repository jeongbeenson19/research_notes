
# Matplotlib

#matplotlib #python #data-visualization #library

Matplotlib는 파이썬에서 데이터를 시각화하기 위한 가장 대표적인 라이브러리입니다. 라인 플롯, 바 차트, 히스토그램, 스캐터 플롯 등 다양한 종류의 그래프를 손쉽게 생성할 수 있으며, 출판 품질의 그림을 만드는 데 필요한 모든 기능을 제공합니다.

NumPy와 함께 데이터 분석 결과를 시각적으로 탐색하고 표현하는 데 필수적인 도구로 사용됩니다.

> **Matplotlib의 두 가지 인터페이스**
> 1.  **State-based (절차적) 인터페이스**: `matplotlib.pyplot` 모듈을 `plt`로 임포트하여 사용하는 방식입니다. 간단한 플롯을 빠르게 생성할 때 유용합니다.
> 2.  **Object-oriented (객체 지향) 인터페이스**: `Figure`와 `Axes` 객체를 명시적으로 생성하고, 이 객체의 메서드를 호출하여 플롯을 그리는 방식입니다. 더 복잡하고 세밀한 제어가 필요할 때 권장됩니다.

---

## 1. 기본 플롯 생성

`matplotlib.pyplot` 모듈을 사용하여 기본적인 그래프를 생성하는 방법입니다.

### `plt.plot()` - 라인 플롯
가장 기본적인 플롯으로, 데이터 포인트들을 선으로 연결하여 시계열 데이터나 연속적인 값의 변화를 보여주는 데 적합합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 준비
x = np.linspace(0, 10, 100) # 0부터 10까지 100개의 점
y = np.sin(x)

# 플롯 생성
plt.plot(x, y)

# 그래프 제목 및 축 레이블 설정
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 그리드 추가
plt.grid(True)

# 그래프 보여주기
plt.show()
```

---

## 2. 주요 구성 요소 (Anatomy of a Plot)

Matplotlib 그래프는 여러 요소로 구성되며, 각 요소를 개별적으로 제어할 수 있습니다.

- **Figure**: 전체 그래프가 그려지는 캔버스(창 또는 페이지).
- **Axes**: 실제 데이터가 그려지는 영역. 하나의 Figure 안에 여러 개의 Axes를 가질 수 있습니다.
- **Title**: 그래프의 제목.
- **X/Y-axis Label**: X축과 Y축에 대한 설명.
- **Legend (범례)**: 여러 개의 데이터를 한 번에 표시할 때 각 데이터가 무엇을 의미하는지 나타냅니다.

```python
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")

plt.title("Sine and Cosine Waves")
plt.xlabel("Radian")
plt.ylabel("Value")
plt.legend() # label을 표시하기 위해 필수
plt.grid(True)
plt.show()
```

---

## 3. 데이터 사이언스에서 자주 사용되는 플롯

데이터의 종류와 분석 목적에 따라 다양한 종류의 플롯을 사용합니다.

### `plt.bar()` - 바 차트
범주형 데이터의 빈도나 값을 비교할 때 사용됩니다.
```python
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 55, 19]

plt.bar(categories, values)
plt.title("Bar Chart Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()
```

### `plt.hist()` - 히스토그램
수치형 데이터의 분포를 시각화합니다. 데이터가 어떤 구간에 얼마나 집중되어 있는지 확인할 수 있습니다.
```python
# 정규분포를 따르는 데이터 1000개 생성
data = np.random.randn(1000)

plt.hist(data, bins=30, alpha=0.7) # bins: 막대의 개수
plt.title("Histogram of Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

### `plt.scatter()` - 스캐터 플롯
두 변수 간의 관계를 파악하는 데 사용됩니다. 변수들이 어떤 상관관계를 갖는지 시각적으로 확인할 수 있습니다.
```python
x = np.random.rand(50)
y = 2 * x + 1 + np.random.randn(50) * 0.2 # y = 2x + 1 + noise

plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel("X variable")
plt.ylabel("Y variable")
plt.show()
```

### `plt.boxplot()` - 박스 플롯
데이터의 사분위수(quartiles)를 시각화하여 데이터의 분포와 이상치(outlier)를 파악하는 데 유용합니다.
```python
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(1, 2, 100)
data = [data1, data2]

plt.boxplot(data, labels=['Data 1', 'Data 2'])
plt.title("Box Plot Example")
plt.ylabel("Value")
plt.show()
```

---

## 4. 플롯 꾸미기 (Customization)

플롯의 가독성을 높이기 위해 색상, 마커, 선 스타일 등을 변경할 수 있습니다.

```python
x = np.linspace(0, 10, 50)
y = x * 2

plt.plot(
    x, y,
    color='green',      # 선 색상
    linestyle='--',    # 선 스타일 ('-', '--', ':', '-.')
    marker='o',         # 데이터 포인트 마커 ('o', '^', 's', '*')
    label='y = 2x'
)

plt.title("Customized Plot")
plt.legend()
plt.show()
```

### `plt.figure(figsize=(width, height))`
그래프의 전체 크기를 조절합니다.
```python
plt.figure(figsize=(10, 5)) # 가로 10인치, 세로 5인치
plt.plot(x, y)
plt.title("Large Figure")
plt.show()
```

### `plt.savefig()`
생성된 그래프를 파일로 저장합니다.
```python
plt.plot(x, y)
plt.title("Sample Plot")
# plt.savefig('sample_plot.png', dpi=300) # png 파일로 해상도 300dpi로 저장
```

---

## 5. 여러 개의 플롯 그리기 (Subplots)

하나의 Figure 안에 여러 개의 Axes(서브플롯)를 배치하여 다양한 그래프를 한 번에 비교할 수 있습니다. 객체 지향 인터페이스를 사용하는 것이 일반적입니다.

### `plt.subplots()`
Figure 객체와 Axes 객체들의 배열을 반환합니다.

```python
# 1행 2열의 서브플롯 생성
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

x = np.linspace(0, 2 * np.pi, 100)

# 첫 번째 플롯 (axes[0])
axes[0].plot(x, np.sin(x), color='blue')
axes[0].set_title("Sine Wave")
axes[0].set_xlabel("Radian")
axes[0].set_ylabel("Value")
axes[0].grid(True)

# 두 번째 플롯 (axes[1])
axes[1].plot(x, np.cos(x), color='red')
axes[1].set_title("Cosine Wave")
axes[1].set_xlabel("Radian")
axes[1].grid(True)

# 전체 레이아웃 조정
plt.tight_layout()
plt.show()
```
