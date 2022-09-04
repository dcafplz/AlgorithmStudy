# https://www.acmicpc.net/problem/1929

import sys
s, e = map(int, sys.stdin.readline().rstrip().split())

num = set(range(2,e+1))

for i in range(2,e+1):
    if i in num:
        if i >= s: print(i)
        num -= set(range(2*i,e+1,i))