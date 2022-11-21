import sys
from collections import deque

moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
n, m = map(int, sys.stdin.readline().rstrip().split())
nord = [[temp:=list(str(sys.stdin.readline().rstrip())), temp.copy()] for _ in range(n)]
q = deque([(0, 0, 1, 0)])

while q:
    y, x, cnt, broken = q.popleft()
    if y == n-1 and x == m-1:
        print(cnt)
        exit()
    for dy, dx in moves:
        dy, dx = dy + y, dx + x
        if 0 <= dy < n and 0 <= dx < m:
            if nord[dy][broken][dx] == '0':
                nord[dy][broken][dx] = False
                q.append((dy, dx, cnt+1, broken))
            elif nord[dy][0][dx] == '1' and not broken:
                nord[dy][1][dx] = False
                q.append((dy, dx, cnt+1, 1))
print(-1)