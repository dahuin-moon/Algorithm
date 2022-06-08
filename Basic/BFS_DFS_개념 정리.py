#BFS/DFS

# 중요한 점은
# 1. visited로 얼마나 탐색 공간을 잘 제한하고
# 2. visited를 대체할 수 있는 자료형을 만드는가

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
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

visited = [False]*len(graph)   
dfs(graph, 1, visited)

print()

visited = [False]*len(graph)
bfs(graph, 1, visited)

