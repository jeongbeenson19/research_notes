
네, 이번에는 **큐(Queue)** 에 대해 자세히 설명드리겠습니다. 스택과 달리 큐는 **FIFO(First In, First Out, 선입선출)** 원칙을 따르는 자료구조입니다. 즉, **먼저 들어온 데이터가 먼저 나간다**는 특징이 있습니다.

---

## 1. **큐의 기본 개념**

- **구조**: 한쪽 끝(rear)에서는 삽입만 가능하고, 반대쪽 끝(front)에서는 삭제만 가능한 선형 자료구조
    
- **작동 방식**:
    
    ```
    Front → [A, B, C, D] ← Rear
    (A가 먼저 들어왔으므로 A가 가장 먼저 나감)
    ```
    
- **주요 용도**:
    
    - **프린터 대기열 관리**
        
    - **프로세스 스케줄링 (운영체제)**
        
    - **네트워크 패킷 처리**
        
    - **BFS(너비 우선 탐색)**, 다익스트라 등 그래프 알고리즘
        
    - **실시간 데이터 스트리밍 버퍼**
        

---

## 2. **큐의 주요 연산**

|연산|설명|시간 복잡도|
|---|---|---|
|**enqueue(item)**|큐의 맨 뒤(rear)에 요소 삽입|O(1)|
|**dequeue()**|큐의 맨 앞(front)에서 요소 제거 및 반환|O(1)|
|**peek()** (또는 front())|큐의 맨 앞(front) 요소를 반환(삭제하지 않음)|O(1)|
|**isEmpty()**|큐가 비어 있는지 확인|O(1)|
|**size()**|큐의 요소 개수 반환|O(1)|

---

## 3. **큐의 시각적 예시**

초기 큐: `[]` (빈 상태)

1. `enqueue(10)` → `[10]`
    
2. `enqueue(20)` → `[10, 20]`
    
3. `enqueue(30)` → `[10, 20, 30]`
    
4. `dequeue()` → `10` 제거 → `[20, 30]`
    
5. `peek()` → `20` 반환 (큐 변화 없음)
    

---

## 4. **파이썬에서 큐 구현**

### ✅ **(1) list를 이용한 기본 구현 (비추천)**

```python
queue = []

# enqueue
queue.append(10)
queue.append(20)
queue.append(30)

# dequeue
print(queue.pop(0))  # 10
print(queue)         # [20, 30]

# peek
print(queue[0])      # 20
```

**⚠️ 단점**: `pop(0)`은 O(n) 시간복잡도를 가지므로 데이터가 많을 때 비효율적입니다.

---

### ✅ **(2) collections.deque를 이용한 구현 (추천)**

`deque`는 양쪽 끝에서 O(1)로 삽입/삭제 가능하므로 큐 구현에 최적화되어 있습니다.

```python
from collections import deque

queue = deque()

# enqueue
queue.append(10)
queue.append(20)
queue.append(30)

# dequeue
print(queue.popleft())  # 10
print(queue)            # deque([20, 30])

# peek
print(queue[0])         # 20
```

---

### ✅ **(3) 직접 클래스 구현 (학습용)**

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("큐가 비어 있습니다.")
        return self.items.popleft()

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# 사용 예시
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  # 10
print(q.peek())     # 20
```

---

## 5. **큐의 종류**

1. **일반 큐 (FIFO)** – 지금까지 설명한 기본 큐
    
2. **원형 큐 (Circular Queue)** – 메모리 재사용을 위해 원형 형태로 구현
    
3. **우선순위 큐 (Priority Queue)** – 먼저 들어온 순서가 아닌 **우선순위**에 따라 처리 (`heapq` 사용)
    
4. **이중 큐 (Deque)** – 양쪽에서 삽입/삭제 모두 가능
    

---

## 6. **큐의 장점과 단점**

### ✅ 장점

- 선입선출이 필요한 상황에서 자연스럽게 동작
    
- 단순하고 효율적(O(1) 연산)
    

### ❌ 단점

- 임의 접근이 불가능 (가장 앞/뒤 요소만 접근 가능)
    
- 일반 리스트 기반 구현 시 비효율적(pop(0)이 O(n))
    

---

## 7. **스택과의 비교**

|구분|스택(Stack)|큐(Queue)|
|---|---|---|
|원칙|LIFO (후입선출)|FIFO (선입선출)|
|입출력 위치|한쪽(top)에서만|양쪽(삽입: rear, 삭제: front)|
|주요 활용|재귀, 수식 계산, DFS|프로세스 관리, BFS, 대기열|

---
 