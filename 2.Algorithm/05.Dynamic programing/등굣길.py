# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for puddle in puddles:
        arr[puddle[1]][puddle[0]] = -1
    arr[1][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if not arr[j][i]:
                arr[j][i] = (max(0, arr[j-1][i]) + max(arr[j][i-1], 0)) % 1000000007
    return arr[-1][-1] 