# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    cola = 0
    while n:
        t = n // a * b
        cola += t
        n = t + n % a
        print(t, cola, n)

print(solution(2, 1, 20))