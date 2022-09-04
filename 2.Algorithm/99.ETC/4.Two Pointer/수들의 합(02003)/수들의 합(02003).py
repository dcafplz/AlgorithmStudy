# https://www.acmicpc.net/problem/2003

import sys

def solution(N, M, arr):
    m, s, e, cnt = 0, 0, 0, 0

    while e <= N:
        if m >= M:
            m -= arr[s]
            s += 1
        else:
            m += arr[e]
            e += 1
        if m == M:
            cnt += 1
    return cnt

N, M = map(int, sys.stdin.readline().rstrip().split())
print(solution(N, M, tuple(map(int, sys.stdin.readline().rstrip().split()))+(0,)))