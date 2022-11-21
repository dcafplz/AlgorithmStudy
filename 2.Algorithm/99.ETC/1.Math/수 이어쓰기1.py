# https://www.acmicpc.net/problem/1748

import sys
n = int(sys.stdin.readline())
l = len(str(n))
answer = 0 
while l:
	cnt = 10 ** (l-1)
	temp = n - cnt + 1
	n -= temp
	answer += temp * l
	l -= 1
print(answer)