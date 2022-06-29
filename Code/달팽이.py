# 백준(1913)::Simulation

dy = [0,1,0,-1]
dx = [-1,0,1,0]

n = int(input())
key = int(input())

area = [[0]*n for _ in range(n)]
x,y = n//2,n//2
def outside(num, key):
    global x, y
    
    dir = 0
    cnt = 1
    area[x][y] = cnt
    pos = [x,y]
    
    for rotate in range(1,num//2+1):
        while dir<=4:    
            nx = x+dx[dir%4]
            ny = y+dy[dir%4]
            if num//2-rotate <= nx <= num//2+rotate and num//2-rotate <= ny <= num//2+rotate:
                cnt+=1
                x = nx
                y = ny
                area[x][y] = cnt
                if cnt == key:
                    pos[0], pos[1] = x,y
            else:
                dir +=1
        dir = 0

    return pos


x, y = outside(n,key)
ans_x, ans_y = 0,0
for i in range(n):
    for j in range(n):
        print(area[i][j], end=' ')
    print()

print(x+1,y+1,sep=' ')
