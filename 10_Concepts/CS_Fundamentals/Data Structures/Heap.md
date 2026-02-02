
`heap`(힙)은 **특정한 규칙을 만족하는 이진트리 기반의 자료구조**로, 우선순위 큐(priority queue)를 구현할 때 자주 사용됩니다. 주로 **최댓값 또는 최솟값을 빠르게 찾기 위한 자료구조**입니다.

---

### 📌 힙의 종류

1. **최소 힙 (Min-Heap)**
    
    - 부모 노드 ≤ 자식 노드
        
    - 루트 노드에 **최솟값**이 위치
        
2. **최대 힙 (Max-Heap)**
    
    - 부모 노드 ≥ 자식 노드
        
    - 루트 노드에 **최댓값**이 위치
        

---

### 📌 힙의 특징

- **완전 이진 트리**의 성질을 가짐  
    (왼쪽부터 차례로 채워지는 이진 트리)
    
- 평균 및 최악 시간복잡도:
    
    - 삽입 `O(log N)`
        
    - 삭제(루트 제거) `O(log N)`
        
    - 최솟값/최댓값 확인 `O(1)`
        

---

### 📌 Python에서의 힙: `heapq` 모듈

파이썬의 `heapq` 모듈은 **최소 힙(min-heap)**만 지원합니다.

#### ✅ 최소 힙 예시

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

print(heapq.heappop(heap))  # 출력: 1 (최소값)
```

#### ✅ 최대 힙 만들기 (음수로 변환)

```python
heap = []
heapq.heappush(heap, -3)
heapq.heappush(heap, -1)
heapq.heappush(heap, -5)

print(-heapq.heappop(heap))  # 출력: 5 (최대값)
```

---

### 📌 힙의 주요 사용 예

- **우선순위 큐**
    
- **다익스트라 알고리즘**
    
- **K번째 최소/최대 원소 구하기**
    
- **스케줄링 문제**
    

---

필요하다면 직접 힙을 구현하는 방법이나, 다익스트라 등에서의 활용 예시도 제공해줄 수 있어요. 추가로 궁금한 부분 있을까요?