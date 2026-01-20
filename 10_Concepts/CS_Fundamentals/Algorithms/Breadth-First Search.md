
## ✅ 1. BFS란 무엇인가?

- **그래프 탐색 알고리즘**의 하나로, **가까운(너비) 노드부터 차례로 탐색**하는 방법입니다.
    
- 한 노드에서 출발해 **인접한 모든 노드를 먼저 방문**한 뒤,  
    그다음에 다시 그 노드들의 인접 노드를 방문하는 방식으로 탐색합니다.
    
- **큐(queue)** 자료구조를 사용하며, **선입선출(FIFO)** 구조로 동작합니다.
    

---

## ✅ 2. BFS의 작동 원리

### 🔁 단계별 작동 방식

1. 시작 노드를 큐에 삽입 → 방문 처리
    
2. 큐가 빌 때까지 반복:
    
    - 큐에서 노드를 꺼냄 (popleft)
        
    - 꺼낸 노드의 **인접 노드들 중 방문하지 않은 노드를 전부 큐에 삽입** → 방문 처리
        

즉, **가까운 노드부터 순차적으로 방문**합니다.

---

### 🔄 간단한 흐름도

```
BFS(노드):
    큐에 시작 노드 삽입
    방문 처리
    while 큐가 비지 않음:
        현재 노드를 큐에서 꺼냄
        인접 노드 중 방문 안 한 노드를 큐에 넣고 방문 처리
```

---

## ✅ 3. BFS 예시

### 🖼️ 그래프 예제

```
1 - 2 - 4
|   |
3 - 5
```

### 🧠 BFS 탐색 순서 (시작: 1)

1. 시작 노드 `1` 방문 → 큐: `[1]`
    
2. `1` 꺼내고, 인접한 `2`, `3` 방문 → 큐: `[2, 3]`
    
3. `2` 꺼내고, 인접한 `4`, `5` 방문 → 큐: `[3, 4, 5]`
    
4. `3` 꺼냄 → 이미 인접 노드는 방문됨
    
5. `4` 꺼냄 → 인접 없음
    
6. `5` 꺼냄 → 인접 없음
    

탐색 순서: **1 → 2 → 3 → 4 → 5**

---

## ✅ 4. BFS 파이썬 구현

```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
```

---

## ✅ 5. BFS의 시간 복잡도

- 모든 노드를 한 번씩 방문, 간선도 한 번씩 확인  
    → **O(V + E)** (V: 노드 수, E: 간선 수)  
    DFS와 동일하지만, BFS는 **메모리 사용이 큼**(큐에 많은 노드가 들어갈 수 있음).
    

---

## ✅ 6. BFS vs DFS 비교

|항목|BFS|DFS|
|---|---|---|
|탐색 순서|**너비(가까운 노드)** 우선|**깊이(먼 노드)** 우선|
|자료구조|큐(FIFO)|스택(LIFO) 또는 재귀|
|주요 활용|**최단 거리 탐색** (가중치 없는 그래프)|백트래킹, 연결 요소 탐색|
|메모리 사용|큐에 많은 노드 저장 → 메모리 ↑|경로 깊이만큼 스택 사용 → 메모리 ↓|
|구현 난이도|비교적 간단|재귀 사용 시 더 간단|

---

## ✅ 7. BFS의 대표적 활용

✔ **최단 거리 탐색 (미로 탐색, 최소 이동 횟수 문제)**  
✔ **2차원 배열(격자) 탐색 (예: 유기농 배추, 토마토 문제)**  
✔ 네트워크 최단 연결 탐색

---

## ✅ 8. `유기농 배추 문제`에서 BFS 동작 방식 (간단 설명)

1. **배추(1) 위치를 찾으면 BFS 실행**
    
2. 큐에 배추 위치 삽입, 방문 처리
    
3. 큐에서 꺼내면서 상하좌우의 연결된 배추를 큐에 추가
    
4. 큐가 빌 때까지 반복 → **한 번의 BFS가 하나의 배추 묶음을 전부 탐색**
    

이 과정을 모든 배추밭에 대해 반복 → BFS 호출 횟수 = 필요한 지렁이 수

---

### 🔁 `유기농 배추` BFS 코드 예시

```python
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if field[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
```

---
# 1) BFS가 뭔데, 언제 쓰나

- **정의:** 시작점에서 가까운 정점(혹은 칸)부터 레벨(거리) 순서대로 탐색하는 알고리즘.
    
- **언제 쓰나:**
    
    - **무가중치 그래프/격자에서 최단 거리** 구할 때 (간선 비용이 전부 1일 때)
        
    - **최소 이동 횟수/단계**(ex. 최소 시간, 최소 문 열기 횟수 등)
        
    - **범위 확산/감염 전파** 시뮬레이션 (토마토, 불 번짐, 물 차오름)
        
    - **이분 그래프 판정**, **연결 요소 개수**, **트리 지름**(2번 BFS) 등
        

> 가중치가 있으면 Dijkstra(양의 가중치), 0/1 가중치면 **0-1 BFS**, 음수 가중치 있으면 Bellman-Ford.

# 2) BFS 문제를 푸는 사고 절차 (모델링 포맷)

1. **상태(state) 정의:**
    
    - 그래프: 정점 번호
        
    - 격자: (y, x)
        
    - 상태 확장형: (y, x, 열쇠비트마스크), (y, x, 벽부순횟수), (노드, 사용한 쿠폰 수) 처럼 “추가 변수”를 포함
        
2. **시작 상태/들:**
    
    - 단일 시작점 or **다중 시작점**(multi-source, ex. 모든 불의 위치)
        
3. **전이 규칙:**
    
    - 인접 정점/4방향·8방향 이동, 문/벽/물 같은 제약 반영
        
4. **방문/거리 기록:**
    
    - `visited` 또는 `dist` 배열(혹은 딕셔너리)
        
    - **큐에 넣을 때 방문표시**(중복 방지 핵심)
        
5. **종료 조건:**
    
    - 목표 도달 시 **즉시 반환(early exit)** 가능한가? (최단 경로면 가능)
        
6. **정답 구성:**
    
    - `dist[target]`, `sum(dist)`, 도달 불가 시 -1, 전체 최소값 등
        

# 3) 구현 템플릿

## 3-1. 일반 그래프 BFS (무가중치 최단거리)

```python
from collections import deque

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    q = deque([start])
    dist[start] = 0
    
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return dist  # dist[i]가 start→i 최단거리, 미도달은 -1
```

## 3-2. 격자 BFS (4방향)

```python
from collections import deque

def grid_bfs(board):
    n, m = len(board), len(board[0])
    dist = [[-1]*m for _ in range(n)]
    q = deque()
    # 시작점 예시: (sy, sx)
    sy, sx = 0, 0
    q.append((sy, sx))
    dist[sy][sx] = 0
    
    for_yx = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        y, x = q.popleft()
        for dy, dx in for_yx:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != '#' and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
    return dist
```

## 3-3. **다중 시작점 BFS (multi-source)**

“가장 가까운 **여러 출발지**로부터의 거리”를 한 번에 구함. 감염/불/물 퍼짐에 필수.

```python
def multi_source_bfs(starts, graph, n):
    from collections import deque
    dist = [-1]*(n+1)
    q = deque()
    for s in starts:
        dist[s] = 0
        q.append(s)
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return dist
```

## 3-4. **상태 확장형 BFS** (비트마스크/카운트 포함)

- 방문 배열 차원에 “추가 상태”를 포함해야 함.
    

```python
# 예: 벽을 K번까지 부술 수 있음 → dist[y][x][broken]
from collections import deque

def bfs_with_state(board, K):
    n, m = len(board), len(board[0])
    INF = 10**9
    dist = [[[INF]*(K+1) for _ in range(m)] for __ in range(n)]
    q = deque()
    dist[0][0][0] = 0
    q.append((0,0,0))  # y, x, broken
    
    for_yx = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        y, x, b = q.popleft()
        for dy, dx in for_yx:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < m:
                nb = b + (board[ny][nx] == 1)  # 벽이면 +1
                if nb <= K and dist[ny][nx][nb] == INF:
                    dist[ny][nx][nb] = dist[y][x][b] + 1
                    q.append((ny, nx, nb))
    return min(dist[n-1][m-1])  # 도착지까지 최소
```

## 3-5. **양방향 BFS**(Bidirectional)

- 시작점과 목표점에서 동시에 확장 → **깊이 d의 최단거리**를 **b^(d/2)** 수준으로 줄임.
    
- 그래프가 크고 목표가 단일할 때 유리.
    
- 구현 포인트: 양쪽 `visited`/`dist`를 따로 들고가다 **frontier가 만나는 시점**에 답을 조립.
    

# 4) BFS로 풀 수 있는 전형 패턴들

- **최단 거리(무가중치)**: 단일/다중 시작점, 격자/그래프 공통.
    
- **연결 요소 개수**: 방문 안 한 노드에서 BFS 한 번 → 컴포넌트 +1.
    
- **이분 그래프 판정**: BFS로 색칠(0/1)하며 확인.
    
- **사이클 판정(무방향)**: BFS 중 ‘부모가 아닌 방문 이웃’ 발견 시 사이클.
    
- **트리 지름**: 임의 노드 A에서 BFS → 가장 먼 B 찾기, B에서 BFS → 가장 먼 거리 = 지름.
    
- **최소 시간/동시 전파**: multi-source로 시작(불/바이러스/물). 레벨이 곧 ‘시간’.
    
- **최솟값 합 비교**: 모든 정점에서 BFS를 돌려 거리합 비교(= 1389번).
    

# 5) 성능/구현 디테일 (파이썬)

- **반드시 `deque`** 쓰기 (`list.pop(0)`는 O(N)이라 TLE 유발).
    
- **큐에 넣을 때 방문 처리**(enque 시 visited=1) → 중복 삽입 폭발 방지.
    
- **인접 리스트** 권장(간선 수가 많아도 메모리/시간 유리).
    
- **빠른 입력**: `input = sys.stdin.readline`.
    
- **조기 종료**: 목표 도달하면 바로 `return dist[target]`.
    
- **visited 재사용 주의**: 시작점 바꿀 땐 배열 초기화 or 재사용 시 타임스탬프 기법.
    
- **격자 경계 체크**: 인덱스 에러 방지, 장애물 조건 먼저 거르기.
    
- **미도달 처리**: `-1`, `INF`를 명확히 구분하고 합산 시 주의.
    

# 6) BFS vs 다른 알고리즘 선택 기준

- **간선 가중치 전부 1**: BFS
    
- **가중치 0/1**: **0-1 BFS**(deque에 0이면 appendleft, 1이면 append)
    
- **양의 임의 가중치**: Dijkstra (우선순위 큐)
    
- **음수 가중치 존재**: Bellman-Ford
    
- **모든 쌍 최단거리**: N이 작으면 Floyd–Warshall / 크면 각 정점에서 BFS/Dijkstra 반복
    

# 7) 디버깅 체크리스트

- 시작점 `dist[start]=0` 했나?
    
- **큐에 넣을 때 방문/거리 설정**했나? (꺼낼 때 X)
    
- 경계/장애물 조건 순서가 맞나?
    
- 상태 확장형이면 **방문 차원**이 상태를 모두 포함하나?
    
- 다중 시작점은 큐에 전부 넣고 `dist=0`으로 시작했나?
    
- 도달 불가(-1/INF) 처리를 빼먹지 않았나?
    

---


