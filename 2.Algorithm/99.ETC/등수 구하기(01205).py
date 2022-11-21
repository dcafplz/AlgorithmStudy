# https://www.acmicpc.net/problem/1205

import sys

N, T, P = map(int, sys.stdin.readline().rstrip().split())
if N:
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    if N == P and arr[-1] >= T:
        print(-1)
    else:
        i = 0
        while i < N and arr[i] > T :
            i += 1
        print(i+1)
else:
    print(1)
