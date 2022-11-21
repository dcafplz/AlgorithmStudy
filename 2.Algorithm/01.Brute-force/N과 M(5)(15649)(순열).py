# https://www.acmicpc.net/problem/15654

import sys

def permutations2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield (array[i],)
        else:
            for next in permutations2(array[:i] + array[i+1:], r-1):
                yield (array[i],) + next

N, M = map(int, sys.stdin.readline().rstrip().split())
s = set()
for i in permutations2(tuple(map(str, sorted(map(int, sys.stdin.readline().rstrip().split())))), M):
    if i not in s:
        print(' '.join(i))
        s.add(i)