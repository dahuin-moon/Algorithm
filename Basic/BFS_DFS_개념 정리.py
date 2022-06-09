#BFS/DFS

# 중요한 점은
# 1. visited로 얼마나 탐색 공간을 잘 제한하고
# 2. visited를 대체할 수 있는 자료형을 만드는가

# graph는 1~8로 구성된 노드 중 연결된 노드만을 나타낸 것.
# 0은 비어있음(1~8)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

def dfs(graph, v, visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

from collections import deque
def bfs(graph, start, visited):
    # 초기 위치를 넣어주고 while문 내에서 pop!
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

# DFS는 1 2 7 6 8 3 4 5 순으로 탐색
visited = [False]*len(graph)   
dfs(graph, 1, visited)

print()

# BFS는 1 2 3 8 7 4 5 6 순으로 탐색
visited = [False]*len(graph)
bfs(graph, 1, visited)

