from collections import defaultdict, deque

n = int(input())
picture = []
g_score = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
groups = defaultdict(list)

for i in range(n):
    picture.append(list(map(int, input().split())))

def bfs(x, y, visited, idx):
    visited[x][y] = True
    queue = deque([[x,y]])
    groups[idx].append([x,y])
    ele = picture[x][y]

    # BFS
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny] and picture[nx][ny] == ele:
                visited[nx][ny] = True
                queue.append([nx,ny])
                groups[idx].append([nx, ny])
    

def findGroup():
    visited =[[False]*n for _ in range(n)]
    idx = -1

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                idx += 1
                bfs(i,j,visited, idx)
    return

def boundary(A, B):
    count = 0

    if len(A) > len(B):
        main = B
        sub = A
    else:
        main = A
        sub = B

    for i in range(len(main)):
        x, y = main[i][0], main[i][1]
        
        for j in range(4):
            nx, ny = x+dx[j], y+dy[j]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            # 경계에 있고(서로 다른 값), 해당 경계가 sub과의 비교가 맞으면
            if picture[nx][ny] != picture[x][y] and [nx,ny] in sub:
                count+=1
    return count

def harmony(A, B):
    x1, y1 = A[0][0], A[0][1]
    x2, y2 = B[0][0], B[0][1]
    return (len(A)+len(B))*picture[x1][y1]*picture[x2][y2]*boundary(A,B)

def calScore():
    score = 0
    for i in range(len(groups)):
        for j in range(i+1, len(groups)):
            score += harmony(groups[i], groups[j])
    return score

def rotateCW():
    mid = n//2
    startset = [[0,0], [0,mid+1],[mid+1,0],[mid+1,mid+1]]
    
    for start in startset:
        for base in range(0,mid//2):
            temp = picture[start[0]+base][mid-1-base]
            temp2 = picture[mid-1-base][mid-1-base]
            temp3 = picture[mid-1-base][start[1]+base]
            temp4 = picture[start[0]+base][start[1]+base]
            # 끝에서부터 넣어야 shift 편리
            for i in range(mid-1-base, 0, -1):
                picture[start[0]+base][i] = picture[start[0]+base][i-1]
                picture[i][mid-1-base] = picture[i-1][mid-1-base]
                
            for i in range(0, mid-1-base):
                picture[mid-1-base][i] = picture[mid-1-base][i+1]
                picture[i][start[1]+base] = picture[i+1][start[1]+base]

            picture[start[0]+1+base][mid-1-base] = temp
            picture[mid-1-base][mid-1-1-base] = temp2
            picture[mid-1-1-base][start[1]+base] = temp3
            picture[start[0]+base][start[1]+1+base] = temp4
    return
def rotateCCW():
    row, col = [], []

    # 가로 <-> 세로 처리
    for i in range(n):
        col.append(picture[n//2][n-i-1])
        row.append(picture[i][n//2])
    
    # 치환
    for i in range(n):
        picture[n//2][i] = row[i]
        picture[i][n//2] = col[i]
    return

def rotate():
    rotateCCW()
    rotateCW()
    return

def simulate():
    global g_score
    for i in range(4):
        groups.clear()
        findGroup()
        if i != 0:
            rotate()
        g_score += calScore()
    print(g_score)
    return

#simulate()
rotateCW()

from pprint import pprint
pprint(picture)
