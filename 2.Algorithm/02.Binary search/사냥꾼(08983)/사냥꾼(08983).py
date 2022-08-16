# https://www.acmicpc.net/problem/8983

import sys
m, n, l = map(int,sys.stdin.readline().rstrip().split())
sd = sorted(list(map(int,sys.stdin.readline().rstrip().split())))
cnt = 0
for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    lower_bound, upper_bound = a+b-l, a-b+l
    if lower_bound <= upper_bound:
        bot, top = 0, m-1
        while bot <= top:
            now = (top+bot)//2
            if lower_bound <= sd[now] <= upper_bound:
                cnt += 1
                break
            elif sd[now] < lower_bound:
                bot = now+1
            else:
                top = now-1
print(cnt)
