n = int(input())
area = [[0]*n for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def outside(num):
    x,y = num//2, num//2
    cnt = 1
    area[x][y] = cnt

    for i in range(num//2+1):
        dir = 0
        while dir<=4:
            nx = x+dx[dir%4]
            ny = y+dy[dir%4]
            if abs(num//2-nx)<=i and abs(num//2-ny)<=i:
                if area[nx][ny]==0:
                    cnt+=1
                    x,y = nx,ny
                    area[x][y] = cnt
                else:
                    dir+=1
            else:
                dir+=1

def inside(num):
    cnt = 1
    x,y = 0,0
    area[x][y]=cnt
    for i in range(num//2+1):
        dir = 2
        while dir>=-1:
            nx = x+dx[dir%4]
            ny = y+dy[dir%4]
            if 0<=nx<num and 0<=ny<num:
                if area[nx][ny] == 0:
                    cnt+=1
                    x,y = nx,ny
                    area[x][y] = cnt
                else:
                    dir-=1
            else:
                dir-=1
            
outside(n)

for i in range(n):
    for j in range(n):
        print("{0:2d}".format(area[i][j]), end=' ')
    print()