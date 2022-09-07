# https://www.acmicpc.net/problem/15652

import sys

def combinations2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations2(array[i:], r-1):
                yield [array[i]] + next

N, M = map(int, sys.stdin.readline().rstrip().split())
for i in combinations2([str(x+1) for x in range(N)], M):
    print(' '.join(i))
