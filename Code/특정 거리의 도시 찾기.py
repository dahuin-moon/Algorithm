#백준(18352): 특정 거리의 도시 찾기

from collections import defaultdict, deque

n,m,k,x = map(int, input().split())
area = defaultdict(list)
res = [-1]*(n+1)
res[x] = 0
ans = set()
for i in range(m):
    start, end = map(int, input().split())
    area[start].append(end)

def bfs(graph, start):
    queue = deque([start])
    while queue:
        start = queue.popleft()
        for end in graph[start]:
            # 처음 방문하는 노드일 때에만
            # -> 나중에 방문하면 무조건 cost가 더 높음
            if res[end] == -1:
                res[end] = res[start]+1
                # 도로가 존재하는 노드만 추가
                if end in graph.keys():
                    queue.append(end)

bfs(area, x)

sig = False
for i in range(1,n+1):
    if res[i] == k:
        print(i)
        sig = True
if not sig:
    print(-1)