# https://school.programmers.co.kr/learn/courses/30/lessons/12936

def fac(n):
    if n <= 1: return 1
    return n * fac(n-1)

def solution(n, k):
    l = [x+1 for x in range(0,n)]
    answer = []
    for i in range(1,n):
        f = fac(n-i)
        answer.append(l.pop((k-1)//f))
        k %= f
    answer.append(l[0])
    return answer