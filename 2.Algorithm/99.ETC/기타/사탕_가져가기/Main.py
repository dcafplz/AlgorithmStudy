# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
n = int(sys.stdin.readline())
f, s = 0, 0
for num in sys.stdin.readline().rstrip().split():
	num = int(num)
	if num % 2 == 0:
		f += 1
	else:
		s += 1

print('tie' if s == f else max(s, f))