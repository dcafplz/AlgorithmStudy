# https://www.acmicpc.net/problem/9095

import sys
answer = [0, 1, 2, 4]
for i in range(4, 11):
	answer.append(answer[i-1] + answer[i-2] + answer[i-3])
for _ in range(int(sys.stdin.readline())):
	print(answer[int(sys.stdin.readline())])