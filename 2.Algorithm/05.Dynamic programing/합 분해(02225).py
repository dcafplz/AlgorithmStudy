# https://www.acmicpc.net/problem/2225

import sys
sys.setrecursionlimit(1000000)
dic = {}

def solution(n, k):
    if (n, k) in dic:
        return dic[(n, k)]
    elif k == 1 or n == 0:
        return 1
    elif k == 2:
        return n+1
    else:
        dic[(n, k)] = sum([solution(x,k-1) for x in range(n+1)])%1000000000
        return dic[(n, k)]

N, K = map(int, sys.stdin.readline().rstrip().split())
print(solution(N, K))