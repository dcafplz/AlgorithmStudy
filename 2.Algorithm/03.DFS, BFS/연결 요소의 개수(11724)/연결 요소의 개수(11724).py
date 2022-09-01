# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10000)
N, M = map(int, sys.stdin.readline().rstrip().split())
visited = [0] * N
nord = [[False] * N for i in range(N)]
for i in range(M):
    t1, t2 = map(int, sys.stdin.readline().rstrip().split())
    nord[t1-1][t2-1], nord[t2-1][t1-1] = True, True
def dfs(v, k):
    visited[v] = k
    for i in range(k-1, N):
        if nord[v][i] and not visited[i]: dfs(i, k)
for i in range(N):
    if not visited[i]: dfs(i, i+1)
print(len(set(visited)))