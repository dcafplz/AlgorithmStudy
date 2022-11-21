# https://www.acmicpc.net/problem/6064

import sys

def gcd(A, B):
    a, b = max(A, B), min(A, B)
    while a % b != 0:
        a, b = b, a % b
    return A * B // b

def s(M, N, x, y):
    g = gcd(M, N)
    for i in range(x, g+1, M):
        now = N if (i % N) == 0 else (i % N)
        if now == y:
            return i
    return -1        

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().rstrip().split())
    print(s(M, N, x, y))