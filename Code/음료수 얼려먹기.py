#이것이 코딩 테스트다 - 음료수 얼려먹기 BFS
from collections import deque

n,m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(graph, x, y):
    queue = deque([[x,y]])
    graph[x][y] = -1
    while queue:
        cx, cy = queue.popleft()
        for t in range(4):
            nx = cx+dx[t]
            ny = cy+dy[t]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = -1
                    queue.append([nx, ny])

result = 0
for i in range(n):
    for j in range(m):
        if area[i][j] == 0:
            bfs(area,i,j)
            result += 1
print(result)
