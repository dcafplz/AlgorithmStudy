# https://www.acmicpc.net/problem/2178

from collections import deque
import sys

def maze(maps):
    paths = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    search = deque([[0, 0, 1]])
    while search:
        x, y, cnt = search.popleft()
        for i in range(4):
            nx, ny = x+paths[i][0], y+paths[i][1]
            if nx == N-1 and ny == M-1:
                return cnt+1
            elif 0 <= nx < N and 0 <= ny < M and maps[nx][ny]:
                search.append([nx, ny, cnt+1])
                maps[nx][ny] = False    

N, M = map(int, sys.stdin.readline().rstrip().split())
print(maze([list(map(bool, map(int, list(sys.stdin.readline().rstrip())))) for _ in range(N)]))