# https://www.acmicpc.net/problem/10825
import sys

n = int(sys.stdin.readline())
for v in sorted([list(sys.stdin.readline().rstrip().split()) for _ in range(n)], key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0])):
    print(v[0])