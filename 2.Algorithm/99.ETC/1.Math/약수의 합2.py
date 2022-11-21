# https://www.acmicpc.net/problem/17427

import sys

sum = 0
for i in range(1, (N:=int(sys.stdin.readline()))+1):
    sum += (N // i) * i
print(sum)