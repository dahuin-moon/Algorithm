# SWEA(5658)::Simulation
T = int(input())
n,k = 0,0
t_box = []
t_box_num = set()

def initialize():
    global n,k,t_box,t_box_num
    n, k = map(int, input().split())
    t_box = list(map(str, input()))
    t_box_num = set()

def rotate():
    # CW 방향으로 한 칸씩 shift
    tmp = t_box[n-1]
    for i in range(n-1,0,-1):
        t_box[i] = t_box[i-1]
    t_box[0] = tmp

def extract():
    # 한 변에 해당하는 배열로부터 str 추출
    # ''.join(list) 형태를 사용했으면 더 편했을 것 !
    for i in range(4):
        a = '0x'
        for j in range(n//4):
            a += t_box[i*(n//4)+j]
        # hex로 변환(hex to int)
        t_box_num.add(int(a,16))
        
for test_case in range(1, T + 1):
    initialize()
    extract()
    for _ in range(n//4):
        rotate()
        extract()
    tmp = sorted(list(t_box_num), reverse=True)
    print('#{0} {1}'.format(test_case,tmp[k-1]))
