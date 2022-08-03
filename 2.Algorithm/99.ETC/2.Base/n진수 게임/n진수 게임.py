# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/17687

def to_base(i, n):
    dic = {10: "A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    re = ""
    while i > 0:
        re = dic.get(i%n, str(i%n)) + re
        i //= n
    return re

def solution(n, t, m, p):
    answer = "0"
    i = 1
    while len(answer) < t*m-1:
        answer += to_base(i, n)
        i += 1
    return ''.join([answer[x] for x in range(p-1,len(answer),m)][:t])