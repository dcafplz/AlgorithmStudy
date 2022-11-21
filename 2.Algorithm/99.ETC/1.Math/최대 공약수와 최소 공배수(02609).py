# https://www.acmicpc.net/problem/2609

import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
a, b = max(A, B), min(A, B)
while a % b != 0:
    a, b = b, a % b
print(b, A * B // b, sep='\n')