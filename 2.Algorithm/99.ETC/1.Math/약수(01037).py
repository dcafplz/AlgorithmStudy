# https://www.acmicpc.net/problem/1037

import sys

N = int(sys.stdin.readline())
print(max(arr:= tuple(map(int, sys.stdin.readline().rstrip().split()))) * min(arr))