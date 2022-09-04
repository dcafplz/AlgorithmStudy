# https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    f1, f2 = 0, 1
    for i in range(1,n+1):
        f1, f2 = f2%1000000007, (f2 + f1)%1000000007
    return f2