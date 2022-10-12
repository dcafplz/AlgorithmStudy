# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
n = int(sys.stdin.readline())
answer_list = [1, 2, 3]
if n <= 3:
	print(answer_list[n-1])
else:
	for i in range(3, n+1):
		if i % 2 == 0:
			answer_list.append(i + answer_list[-1])
			
		else:
			answer_list.append(answer_list[i-3])
			
	print(answer_list[-1])