# https://www.acmicpc.net/problem/1759

import sys
mos = {'a', 'e', 'i', 'o', 'u'}
n, m = map(int, sys.stdin.readline().rstrip().split())
l = sorted(sys.stdin.readline().rstrip().split())
answer = []
def com(idx, list, a):
	if len(list) == n:
		if 1 <= a <= len(list) - 2:
			answer.append(''.join(list[:]))
		return

	for i in range(idx, m):
		com(i+1 , list+[l[i]], a + (1 if l[i] in mos else 0))
		
com(0, [], 0)

print('\n'.join(answer))