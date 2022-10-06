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
    # 오른쪽으로 한 칸씩 Shift
    tmp = t_box[n-1]
    for i in range(n-1,0,-1):
        t_box[i] = t_box[i-1]
    t_box[0] = tmp

def extract():
    # ''.join(list) 를 알았으면 더 유용했을 것!

    # 4개의 변 모두
    for i in range(4):
        a = '0x'
        # 각 변의 문자 합침
        for j in range(n//4):
            a += t_box[i*(n//4)+j]
        # 16진수를 10진수로 변환
        t_box_num.add(int(a,16))

for test_case in range(1, T + 1):
    initialize()
    extract()
    for _ in range(n//4):
        rotate()
        extract()
    tmp = sorted(list(t_box_num), reverse=True)
    print('#{0} {1}'.format(test_case,tmp[k-1]))
