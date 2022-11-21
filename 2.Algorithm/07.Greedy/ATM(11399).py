# https://www.acmicpc.net/problem/11399

import sys

n = int(sys.stdin.readline())
print(sum([(n-idx) * x for idx, x in enumerate(sorted(list(map(int, sys.stdin.readline().rstrip().split()))))]))