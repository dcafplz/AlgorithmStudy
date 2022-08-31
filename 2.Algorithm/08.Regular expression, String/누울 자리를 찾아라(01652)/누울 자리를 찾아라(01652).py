# https://www.acmicpc.net/problem/1652

import sys
import re
arr = [sys.stdin.readline().rstrip() for _ in range(int(input()))]
p = re.compile('[\.]{2,}')
print(str(sum([len(p.findall(i)) for i in arr])) + ' ' + str(sum([len(p.findall(''.join(j))) for j in zip(*arr)])))