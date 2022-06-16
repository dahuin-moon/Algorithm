#Programmers(60058)::재귀

def balanced(p):
    u = ''
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count+=1
        else:
            count-=1
        u+=p[i]
        # 아래와 같이 구문을 추가하면 u가 올바른 문장인지 또한 확인 가능
        # -> right 필요하지 않아짐!
        # if count < 0 : r = False
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
    
    i = balanced(p)
    u = p[:i+1]
    v = p[i+1:]
    if right(u):
        return u+solution(v)
    else:
        def reverse(str):
            ret = ''
            for i in str:
                if i=='(':
                    ret+=')'
                else:
                    ret+='('
            return ret
                
        return '('+solution(v)+')'+reverse(u[1:len(u)-1])

print(solution('()))((()'))