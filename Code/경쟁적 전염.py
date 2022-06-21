# 백준(18405)::BFS/DFS

# 1번째 풀이 time: 24m 25s

from collections import defaultdict
n, k = map(int, input().split())
area = []
virus = defaultdict(list)
for i in range(n):
    area.append(list(map(int, input().split())))
    for j in range(n):
        if area[i][j] > 0:
            virus[area[i][j]].append([i,j])
s, x, y = map(int, input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(area, depth):
    global virus
    if depth == k+1:
        return
    temp = []
    for v in virus[depth]:
        for i in range(4):
            c_x = v[0]+dx[i]
            c_y = v[1]+dy[i]
            if c_x < 0 or c_x>=n or c_y < 0 or c_y >=n:
                continue
            elif area[c_x][c_y] != 0:
                continue
            area[c_x][c_y] = depth
            temp.append([c_x, c_y])

    # 기존의 list는 이미 사방으로 확산하여 더 확산할 공간이 없으므로 새로 추가된 list로 대체함
    virus[depth] = temp
    # dfs니까 n번 바이러스에 대한 확산이 끝나면 n+1에 대한 확산 수행
    dfs(area, depth+1)
        
for i in range(s):
    dfs(area, 1)
print(area[x-1][y-1])