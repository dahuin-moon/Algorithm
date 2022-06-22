# 백준(16234)::BFS/DFS
# 1번째 풀이 time: 시간 초과
# - BFS의 visited 추가 위치 주의!

from collections import deque

n,l,r = map(int, input().split())
a  = []
for i in range(n):
    a.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(area, x, y):
    queue = deque([[x,y]])
    nation = []
    nation.append([x,y])
    visited[x][y] = True
    people = area[x][y]
    cnt = 1
    
    while queue:
        cx, cy = queue.popleft()
        # 이 위치에 visited/people/cnt 연산이 추가되는 경우, 중복된 x,y가 추가될 수 있음
        # visited==True가 배제된 아래 위치에서 연산이 수행되어야 함!

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif l > abs(area[cx][cy]-area[nx][ny]) or abs(area[cx][cy]-area[nx][ny]) > r or visited[nx][ny] == True:
                continue
            queue.append([nx, ny])
            visited[nx][ny] = True
            nation.append([nx, ny])
            people += area[nx][ny]
            cnt += 1

    if cnt == 1:
        return False
    for i,j in nation:
            a[i][j] = people//cnt
    return True

count = 0
while True:
    visited = [[False]*n for _ in range(n)]
    t = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                if bfs(a, i, j):
                    t += 1
    # 한 번도 인구 이동이 일어나지 않은 경우 탈출
    if t == 0:
        break
    count += 1
print(count)

