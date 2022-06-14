def permutation(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutation(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next

def combination(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combination(array[i+1:], r-1):
                yield [array[i]] + next

print(list(combination('AABC',2)))

#reference: https://juhee-maeng.tistory.com/91
