---
tags: [algorithm, graph, bfs, dfs, python]
aliases: [그래프 탐색, Graph Search]
---

# 그래프 탐색 (Graph Search) 알고리즘

그래프 탐색은 코딩 테스트에서 가장 빈번하게 출제되는 유형 중 하나입니다. 정점(Vertex/Node)과 간선(Edge)으로 구성된 그래프 자료구조를 특정 순서에 따라 방문하고 탐색하는 알고리즘으로, 다양한 문제 해결의 기반이 됩니다.

---

### **1. 그래프의 표현**

파이썬으로 그래프를 표현하는 방법은 주로 두 가지가 사용됩니다.

#### **1.1. 인접 리스트 (Adjacency List)**

-   **설명**: 각 정점이 어떤 다른 정점들과 연결되어 있는지를 리스트나 딕셔너리로 표현하는 방식입니다. 대부분의 경우 인접 행렬보다 효율적입니다.
-   **구현**: `defaultdict(list)`를 사용하면 편리합니다.

```python
from collections import defaultdict

graph = defaultdict(list)
graph['A'].append('B')
graph['A'].append('C')
graph['B'].append('D')

# graph -> {'A': ['B', 'C'], 'B': ['D']}
```

#### **1.2. 인접 행렬 (Adjacency Matrix)**

-   **설명**: 2차원 배열을 사용하여 `matrix[i][j]`가 1(또는 가중치)이면 정점 i와 j가 연결되었음을 의미합니다. 정점의 수가 적고 간선이 많을 때(Dense Graph) 유용합니다.
-   **구현**: `[[0] * N for _ in range(N)]` 형태로 구현합니다.

```python
N = 4 # 정점의 수
graph = [[0] * N for _ in range(N)]
graph[0][1] = 1 # 0 -> 1
graph[0][2] = 1 # 0 -> 2
graph[1][3] = 1 # 1 -> 3
```

> **코딩 테스트에서는 대부분 인접 리스트 방식이 메모리와 시간 효율성 면에서 유리합니다.**

---

### **2. 너비 우선 탐색 (Breadth-First Search, BFS)**

BFS는 시작 정점에서 가까운 정점부터 순서대로 탐색하는 알고리즘입니다. 마치 물결이 퍼져나가는 모습과 같습니다.

-   **핵심 원리**: 큐(Queue) 자료구조를 사용하여, 현재 정점에서 갈 수 있는 모든 이웃 정점을 큐에 넣고, 큐에서 순서대로 정점을 꺼내 방문합니다.
-   **주요 특징**:
    -   최단 경로 찾기(가중치가 없는 그래프에서)에 사용됩니다.
    -   FIFO(First-In, First-Out) 순서로 탐색합니다.
    -   방문 여부를 체크하는 배열이 반드시 필요합니다.

#### **Python3 BFS 구현**

```python
from collections import deque

def bfs(graph, start_node):
    # 방문한 노드를 기록하기 위한 집합(set)
    visited = set()
    # 탐색할 노드를 저장하는 큐
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        # 큐에서 노드를 하나 꺼냄
        node = queue.popleft()
        print(node, end=' ') # 현재 노드 방문 처리

        # 현재 노드와 연결된 다른 노드를 확인
        for neighbor in graph[node]:
            if neighbor not in visited:
                # 방문하지 않은 노드이면 큐에 추가하고 방문 처리
                queue.append(neighbor)
                visited.add(neighbor)

# 예제 그래프 (인접 리스트)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 'A'에서 BFS 시작
# 출력: A B C D E F
bfs(graph, 'A')
```

---

### **3. 깊이 우선 탐색 (Depth-First Search, DFS)**

DFS는 한 방향으로 갈 수 있을 때까지 최대한 깊게 탐색한 후, 더 이상 갈 곳이 없으면 뒤로 돌아와 다른 방향으로 탐색을 계속하는 알고리즘입니다.

-   **핵심 원리**: 스택(Stack) 자료구조 또는 재귀 함수를 사용하여 구현합니다. 한 정점에서 연결된 다음 정점으로 즉시 이동합니다.
-   **주요 특징**:
    -   모든 노드를 방문해야 하는 경우에 유용합니다. (예: 연결 요소 찾기, 사이클 탐지)
    -   LIFO(Last-In, First-Out) 순서로 탐색합니다.
    -   경로의 특징을 저장해야 하는 문제에 효과적입니다.

#### **Python3 DFS 구현 (재귀)**

```python
def dfs_recursive(graph, node, visited):
    # 현재 노드를 방문 처리
    visited.add(node)
    print(node, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# 예제 그래프 (위와 동일)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited_set = set()
# 'A'에서 DFS 시작
# 출력 예시: A B D E F C (탐색 순서는 인접 리스트 순서에 따라 달라질 수 있음)
dfs_recursive(graph, 'A', visited_set)
```

#### **Python3 DFS 구현 (스택)**

```python
def dfs_iterative(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')

            # 스택에 넣을 때는 역순으로 넣어주어야
            # 재귀 방식과 비슷한 순서로 방문 가능
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# 'A'에서 DFS 시작
# 출력 예시: A B D E F C 
dfs_iterative(graph, 'A')
```

---

### **4. BFS vs DFS: 언제 무엇을 쓸까?**

| 구분 | BFS (너비 우선 탐색) | DFS (깊이 우선 탐색) |
| :--- | :--- | :--- |
| **자료구조** | 큐 (Queue) | 스택 (Stack) 또는 재귀 |
| **속도** | 두 방식 모두 모든 노드와 간선을 한 번씩 방문하므로 시간 복잡도는 O(V+E)로 동일 (V: 정점 수, E: 간선 수) | 동일 |
| **메모리** | 인접한 정점이 많을수록 큐의 크기가 커짐 | 경로가 길어질수록 스택(또는 재귀 깊이)이 깊어짐 |
| **주요 용도** | **최단 경로** (가중치 없는 그래프), 너비가 넓은 그래프 탐색 | **모든 노드 방문**, 경로 탐색, 사이클 탐지, 연결 요소 찾기, 깊이가 깊은 그래프 탐색 |
| **답이 있는 경로가 여러 개일 때** | 최단 경로를 먼저 찾음 | 경로의 깊이에 따라 다름. 해가 깊은 곳에 있으면 빠르지만, 얕은 곳에 있어도 깊이 탐색 후 찾을 수 있음 |
