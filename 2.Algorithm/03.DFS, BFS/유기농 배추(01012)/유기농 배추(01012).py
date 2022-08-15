# https://www.acmicpc.net/problem/1012

import sys
from collections import deque

near = ((0, 1), (1, 0), (-1, 0), (0, -1))
t = int(sys.stdin.readline())

for _ in range(t):
    m, n, be = map(int, sys.stdin.readline().rstrip().split())
    visited = [0 for _ in range(be)]
    nord = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(be)]
    search = deque()
    for j in range(be):
        if not visited[j]:
            search.append([j,j+1])
            visited[j] = j+1
        while search:
            idx1, k = search.popleft()
            nears = [(nord[idx1][0]+i[0], nord[idx1][1]+i[1]) for i in near]
            for idx2, v in enumerate(nord):
                if not visited[idx2] and v in nears:
                    search.append([idx2,k])
                    visited[idx2] = k
    print(len(set(visited)))

# 재귀함수 1000초과 오류
# near = ((0, 1), (1, 0), (-1, 0), (0, -1))
# t = int(sys.stdin.readline())

# for _ in range(t):
#     m, n, be = map(int, sys.stdin.readline().rstrip().split())
#     visited = [0 for _ in range(be)]
#     nord = []
#     for _ in range(be):
#         nord.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
#     def dfs(v, k):
#         nears = [(nord[v][0]+x[0], nord[v][1]+x[1]) for x in near]
#         for idx, v in enumerate(nord):
#             if not visited[idx] and v in nears:
#                 visited[idx] = k
#                 dfs(idx, k)
#     for i in range(be):
#         if not visited[i]:
#             visited[i] = i+1
#             dfs(i, i+1)
#     print(len(set(visited)))

