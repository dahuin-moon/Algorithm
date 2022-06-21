# 백준(14888)::BFS/DFS
# itertools를 사용하지 않는 permutation 사용은 시간 초과!

n = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))

# 초기화 방법 확인 (1e)
minimum = 1e9
maximum = -1e9

def dfs(res, num, operate, count):
    global minimum, maximum
    if sum(operate) == 0:
        maximum = max(maximum, res)
        minimum = min(minimum, res)
        return
    
    # Back Tracking
    # 함수 인자를 각 연산자 별로 따로 넣어주는 형식을 취하면(ex. oper[i]-1)
    # 굳이 다시 더하는 과정을 거치지 않아도 됨

    if opers[0] > 0:
        opers[0] -= 1
        dfs(res+num[count], num, opers, count+1)
        opers[0] += 1
    if opers[1] > 0:
        opers[1] -= 1
        dfs(res-num[count], num, opers, count+1)
        opers[1] += 1
    if opers[2] > 0:
        opers[2] -= 1
        dfs(res*num[count], num, opers, count+1)
        opers[2] += 1
    if opers[3] > 0:
        opers[3] -= 1
        dfs(int(res/num[count]), num, opers, count+1)
        opers[3] += 1

# 초기값이 numbers[0]이므로 카운트를 1 추가하고 시작
dfs(numbers[0], numbers, opers, 1)

# sep = seperator 라는 의미!
print(maximum, minimum, sep='\n')