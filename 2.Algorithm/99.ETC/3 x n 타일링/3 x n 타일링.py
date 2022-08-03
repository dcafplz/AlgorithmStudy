# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/12902
# 참고한 것 https://school.programmers.co.kr/questions/32019

def solution(n):
    p, k = 3, 1
    while n > 2:
        p, k = (p * 4 - k)%1000000007, p %1000000007
        n -= 2
    return p