#이것이 코딩테스트다 - 미로 탈출

VOID = 1
MONSTER = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]
x, y = 0, 0

n,m = map(int, input().split())
maze = []

for i in range(n):
    maze.append(list(map(int, input())))

from collections import deque
def bfs(maze, x, y):
    queue = deque([[x,y]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 다음에 탐색할 곳이 미로를 벗어지 않고 빈 공간인 경우
            if 0<=nx<n and 0<=ny<m:
                if maze[nx][ny] == VOID:
                    maze[nx][ny] += maze[x][y]
                    queue.append([nx, ny])
            if (nx, ny) == (n-1, m-1):
                return


def dfs(maze, x, y, cost):
    if x<0 or x>=n or y<0 or y>=m:
        return
    if maze[x][y] != VOID:
        return
    maze[x][y] += cost
    for i in range(4):
        dfs(maze, x+dx[i], y+dy[i], maze[x][y])

#bfs(maze, 0,0)
dfs(maze, 0, 0, 0)
print(maze[n-1][m-1])