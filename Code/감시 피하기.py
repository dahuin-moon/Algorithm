# 백준(18428)::BFS/DFS
# 1번째 풀이 time: 시간초과, 틀렸습니다.(80%)

# 같은 행이나 열을 가지는 선생/학생의 비어있는 공간을 check로 설정
# check 위주로만 장애물을 설치
# 단, len(check) < 3 인 경우 check인 공간에 모두 장애물을 세우고 결과를 확인 !!! <- 놓쳤던 부분

n = int(input())
area = []
teachers = []
students = []
for i in range(n):
    area.append(list(input().split()))
    for j in range(n):
        if area[i][j] == 'T':
            teachers.append((i, j))
        elif area[i][j] == 'S':
            students.append((i,j))

check = []
for t in teachers:
    for s in students:
        temp = 0
        mini = 0
        maxi = 0
        if t[0] == s[0] or t[1] == s[1]:
            if t[0] == s[0]:
                temp = 1
            mini = s[temp] if t[temp] > s[temp] else t[temp]
            maxi = s[temp] if t[temp] < s[temp] else t[temp]
            for i in range(mini+1,maxi):
                if temp == 1 and (t[0],i) not in check:
                    check.append((t[0],i))
                elif temp == 0 and (i,t[1]) not in check:
                    check.append((i, t[1]))


def bare(teachers, students, area):
    for t in teachers:
        for s in students:
            temp = 0
            mini = 0
            maxi = 0
            if t[0] == s[0] or t[1] == s[1]:
                if t[0] == s[0]:
                    temp = 1
                mini = s[temp] if t[temp] > s[temp] else t[temp]
                maxi = s[temp] if t[temp] < s[temp] else t[temp]
                sig = False
                for i in range(mini+1,maxi):
                    if temp == 1:
                        if area[t[0]][i] == 'O':
                            sig = True
                            break
                    else:
                        if area[i][t[1]] == 'O':
                            sig = True
                            break
                if sig == False:
                    return False
    return True

res = False
def dfs(check, area, depth):
    if depth == 3:
        if bare(teachers, students, area):
            return True
    # 중요!!!!!
    elif len(check)<3:
        for c in check:
            area[c[0]][c[1]] = 'O'
        if bare(teachers, students, area):
            return True
        else:
            return False
    else:
        for i in range(len(check)):
            area[check[i][0]][check[i][1]] = 'O'
            if dfs(check[i+1:],area, depth+1):
                return True
            else:
                area[check[i][0]][check[i][1]] = 'X'

    return False

res = 'YES' if dfs(check, area, 0) else 'NO'
print(res)
