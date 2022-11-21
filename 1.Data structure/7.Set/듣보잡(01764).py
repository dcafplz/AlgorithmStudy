# https://www.acmicpc.net/problem/1764

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
inter = list({sys.stdin.readline().rstrip() for _ in range(N)} & {sys.stdin.readline().rstrip() for _ in range(M)})
print(len(inter))
for i in sorted(inter):
    print(i)