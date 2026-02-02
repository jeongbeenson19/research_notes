
스택(Stack)은 **자료구조(Data Structure)** 의 한 종류로, **LIFO(Last In, First Out, 후입선출)** 원칙을 따릅니다. 즉, **마지막에 들어간 데이터가 가장 먼저 나온다**는 특징을 가집니다. 스택은 알고리즘, 컴퓨터 구조, 프로그램 실행 원리 등 다양한 분야에서 사용됩니다.

---

## 1. **스택의 기본 개념**

- **구조**: 한쪽 끝(top)에서만 데이터를 삽입(push)하거나 삭제(pop)할 수 있는 선형 자료구조
    
- **작동 방식**:
    
    ```
    [Bottom]  A  B  C  D [Top]
               ↑
         가장 마지막에 들어온 D가 먼저 나감 (pop)
    ```
    
- **주요 용도**:
    
    - **수식 계산 및 괄호 검사** (예: 후위 표기식, 괄호 짝 검사)
        
    - **재귀 함수 호출** (시스템 콜 스택)
        
    - **백트래킹(DFS)** (예: 미로 탐색)
        
    - **웹 브라우저의 뒤로가기 / 앞으로가기**
        
    - **언두(Undo) 기능** 등
        

---

## 2. **주요 연산**

|연산|설명|시간 복잡도|
|---|---|---|
|**push(item)**|스택의 맨 위(top)에 데이터를 삽입|O(1)|
|**pop()**|스택의 맨 위(top)에 있는 데이터를 제거하고 반환|O(1)|
|**peek()** (또는 top())|스택의 맨 위 데이터를 반환(삭제하지 않음)|O(1)|
|**isEmpty()**|스택이 비어 있는지 확인|O(1)|
|**size()**|스택의 요소 개수 반환|O(1)|

---

## 3. **스택의 시각적 예시**

초기 스택: `[]` (빈 상태)

1. `push(10)` → `[10]`
    
2. `push(20)` → `[10, 20]`
    
3. `push(30)` → `[10, 20, 30]`
    
4. `pop()` → `30` 제거 → `[10, 20]`
    
5. `peek()` → `20` 반환 (스택 변화 없음)
    

---

## 4. **파이썬에서 스택 구현**

### ✅ **(1) list를 이용한 기본 구현**

```python
stack = []

# push
stack.append(10)
stack.append(20)
stack.append(30)

# pop
print(stack.pop())  # 30 (마지막 요소 제거 및 반환)
print(stack)        # [10, 20]

# peek
print(stack[-1])    # 20 (삭제되지 않음)

# isEmpty
print(len(stack) == 0)  # False
```

---

### ✅ **(2) collections.deque를 이용한 구현 (추천)**

`deque`는 양방향 큐이지만, 스택처럼 사용하면 `list`보다 효율적입니다.

```python
from collections import deque

stack = deque()

# push
stack.append(10)
stack.append(20)
stack.append(30)

# pop
print(stack.pop())  # 30
print(stack)        # deque([10, 20])

# peek
print(stack[-1])    # 20
```

**왜 deque가 list보다 좋은가?**

- `list`는 pop()이나 append()가 끝에서만 빠르지만, 중간이나 앞쪽에서 삽입/삭제가 느립니다.
    
- `deque`는 양쪽 끝에서 O(1)로 삽입/삭제가 가능하므로 스택 용도로는 더 안정적입니다.
    

---

### ✅ **(3) 직접 클래스 구현 (학습용)**

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("스택이 비어 있습니다.")
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# 사용 예시
s = Stack()
s.push(10)
s.push(20)
print(s.pop())  # 20
print(s.peek()) # 10
```

---

## 5. **스택의 장점과 단점**

### ✅ 장점

- 구현이 간단하며 빠름
    
- 후입선출(LIFO) 작업에 적합
    

### ❌ 단점

- 중간 데이터 접근이 불가능 (오직 top에서만 접근 가능)
    
- 선입선출(FIFO) 구조에는 부적합 (→ 이건 큐가 적합)
    

---

## 6. **스택과 관련된 대표 문제 유형**

- **괄호의 유효성 검사** (예: 백준 9012)
    
- **수식 변환 (중위 → 후위 표기식)**
    
- **재귀 호출 함수 구현**
    
- **DFS (깊이 우선 탐색)**
    

---
