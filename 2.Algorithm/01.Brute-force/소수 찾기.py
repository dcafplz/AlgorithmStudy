import itertools

def solution(numbers):
    a = []
    for i in range(0,len(numbers)):
        a += list(map(int,map(''.join, itertools.permutations(numbers, i+1))))
    a = sorted(list(set(a)))
    answer = len(a)
    for i in a:
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                answer -=1
                break
    return answer - sum([1 if x == 1 or x == 0 else 0 for x in a])