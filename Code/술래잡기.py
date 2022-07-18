# CodeTree::삼성 2022(상) 오전 기출

n, m, h, k = map(int, input().split())

hiders, trees = [], []
next_cw_dir = [[0]*n for _ in range(n)]
next_ccw_dir = [[0]*n for _ in range(n)]
pos_x, pos_y = n//2, n//2
forward = True
score = 0
dx, dy = [-1,0,1,0], [0,1,0,-1] # N E S W

for i in range(m):
    x, y, d = map(int, input().split())
    hiders.append([x-1,y-1,d])
for i in range(h):
    x, y = map(int, input().split())
    trees.append([x-1,y-1])

def calDistance(x,y):
    return abs(pos_x-x)+abs(pos_y-y)

def hiderMove(hider):    
    nx = hider[0]+dx[hider[2]]
    ny = hider[1]+dy[hider[2]]
    # 격자 이내일 때
    if 0<=nx<n and 0<=ny<n:
        # 술래와 다른 위치일때만
        if (nx, ny) != (pos_x, pos_y):
            hider[0], hider[1] = nx, ny
    # 격자 이외일 때
    else:
        hider[2] = (hider[2]+2)%4
        hiderMove(hider)

def hiderMoveAll():
    for i in range(len(hiders)):
        if calDistance(hiders[i][0], hiders[i][1]) > 3:
            continue
        hiderMove(hiders[i])
    return

def seekerDir():
    if forward:
        dir = next_cw_dir[pos_x][pos_y]
    else:
        dir = next_ccw_dir[pos_x][pos_y]
    return dir

def seekerMove():
    global forward, pos_x, pos_y
    
    dir = seekerDir()
    pos_x, pos_y = pos_x+dx[dir], pos_y+dy[dir]

    if not pos_x and not pos_y and forward:
        forward = False
    elif (pos_x, pos_y) == (n//2, n//2) and not forward:
        forward = True
    return

def calScore():
    global pos_x, pos_y
    res = 0
    dir = seekerDir()

    for i in range(3):
        nx, ny = pos_x+dx[dir]*i, pos_y+dy[dir]*i
        if 0<=nx<n and 0<=ny<n and not ([nx, ny] in trees):
            length = len(hiders)
            cnt, index = 1, 0
            while cnt <= length:
                if [nx, ny] == hiders[index][:2]:
                    res+=1
                    del hiders[index]
                else:
                    index+=1
                cnt+=1
    return res

def simulator():
    global score

    for i in range(k):
        hiderMoveAll()
        seekerMove()
        score += calScore()*(i+1)

def initializer():
    x,y = n//2, n//2
    dir = 0
    cnt = 1
    while x or y:
        for _ in range(cnt):
            next_cw_dir[x][y] = dir
            x,y = x+dx[dir], y+dy[dir]
            next_ccw_dir[x][y] = (dir+2)%4
            if not x and not y:
                break
        
        dir = (dir+1)%4
        # 북/남쪽인 경우 카운트를 늘려감
        if dir == 0 or dir == 2:
            cnt+=1

initializer()
simulator()
print(score)