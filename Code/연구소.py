# 백준(14502)::BFS/DFS

# 1번째 풀이 time: 시간 초과
# 2번째 풀이 time: 37m 44s, 성공

from copy import deepcopy
from collections import deque
VOID = 0
WALL = 1
VIRUS = 2

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int, input().split())
lab = []
v = []
for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(m):
        if lab[i][j] == VIRUS:
            v.append([i,j])

def spread(lab, v):
    for i in v:
        queue = deque([i])
        visited  = [[False]*m for _ in range(n)]
        
        while queue:
            x,y = queue.popleft()
            visited[x][y] = True
            for j in range(4):
                nx = x+dx[j]
                ny = y+dy[j]
                if nx < 0 or nx>=n or ny < 0 or ny>=m:
                    continue
                if lab[nx][ny] == VOID and not visited[nx][ny]:
                    lab[nx][ny] = VIRUS
                    visited[nx][ny] = True
                    queue.append([nx, ny])
    count = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == VOID:
                count+=1
    return count

ans = 0
# 1. 구현 시 x, y 대신 x*10+y 형태로 주어졌다면 중복된 벽을 확실하게 제거할 수 있었을 것
# 현재는 i, j로 나눴기 때문에 행에 대해서만 검토할 수 있음 --> 행이 다른 경우, 열은 처음부터 검사해야 하므로
# (문제의 조건이 3 <= N, M<= 8 임을 이용)

# 2. lab은 인자로 받지 않아도 됨!
# 개선: makeWall(wall_cnt, x,y)
def makeWall(lab, wall_cnt, x, y):
    global ans
    if wall_cnt == 3:
        ans = max(ans, spread(deepcopy(lab), v))
    else:
        # 개선: for i in range(start, n*m):
        # 개선:     i, j = start//m, start%m
        for i in range(x, n):
            for j in range(m):
                if lab[i][j] == VOID:
                    lab[i][j] = WALL
                    makeWall(lab, wall_cnt+1, i, j)
                    #back tracking
                    lab[i][j] = VOID


makeWall(lab, 0, 0, 0)
print(ans)