# https://www.acmicpc.net/problem/1946

import sys

def f(ranks):
    t = ranks[0][1]
    cnt = 1
    for i in range(1, len(ranks)):
        if ranks[i][1] < t:
            t = ranks[i][1]
            cnt += 1
    return cnt
    
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    print(f(sorted([tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(int(sys.stdin.readline().rstrip()))])))