# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

def solution(classes):
	for c in classes:
		case1 = c[1]/c[0]*100
		if case1 >= c[2]:
			return 0
		if c[4] >= min(c[5:]):
			return 0
	return 1

t = int(sys.stdin.readline())
print(solution([list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(t)]))