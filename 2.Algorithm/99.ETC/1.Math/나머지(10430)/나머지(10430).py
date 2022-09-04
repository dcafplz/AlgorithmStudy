import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())
for i in [(A+B)%C,  ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C]: print(i)