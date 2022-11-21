# https://www.acmicpc.net/problem/1931
import sys
n = int(input())
meetings = sorted([tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)], key=lambda x: (x[1],x[0]))

cnt = 0
end_time = 0
for start, end in meetings:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)