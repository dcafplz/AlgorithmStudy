#https://www.acmicpc.net/problem/14562

from collections import deque

def t(i):
    q = deque([i+[0]])
    while q:
        a, b, cnt = q.popleft()
        if a == b:
            return cnt
        elif a*2 <= b+3:
            q.append([a*2,b+3,cnt+1])
        q.append([a+1,b,cnt+1])

n = int(input())
for i in range(n):
    print(t(list(map(int, input().split()))))