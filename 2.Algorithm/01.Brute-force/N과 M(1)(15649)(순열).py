# https://www.acmicpc.net/problem/15649

import sys

def permutations2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations2(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next

N, M = map(int, sys.stdin.readline().rstrip().split())
for i in permutations2(list(map(str, range(1, N+1))), M):
    print(' '.join(i))