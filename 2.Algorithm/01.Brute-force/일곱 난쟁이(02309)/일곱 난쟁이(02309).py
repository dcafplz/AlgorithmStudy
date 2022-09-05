# https://www.acmicpc.net/problem/2309

import sys
from itertools import combinations
s = sum(arr:= sorted([int(sys.stdin.readline()) for _ in range(9)]))
for a, b in combinations(arr, 2):
    if s - a - b == 100:
        print('\n'.join([str(x) for x in arr if x != b and x != a]))
        break
