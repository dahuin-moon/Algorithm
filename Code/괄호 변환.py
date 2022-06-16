#Programmers(60058)::BFS/DFS

def balanced(p):
    u = ''
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count+=1
        else:
            count-=1
        u+=p[i]
        if count == 0:
            break
    return i          

def right(p):
    count = 0
    for i in p:
        if i == '(':
            count+=1
        else:
            if count <= 0:
                return False
            count-=1
    if count == 0:
        return True
    else:
        return False

def solution(p):
    if len(p) == 0:
        return p
    
    answer = ''
    length = len(p)
    while length != len(answer):
        i = balanced(p)
        u = p[:i+1]
        v = p[i+1:]
        if right(u):
            answer += u
            p = v
        else:
            def reverse(str):
                ret = ''
                for i in str:
                    if i=='(':
                        ret+=')'
                    else:
                        ret+='('
                return ret
                    
            temp = '('+solution(v)+')'+reverse(u[1:len(u)-1])
            answer+=temp
    
    return answer

print(solution('()))((()'))