# https://www.acmicpc.net/problem/15650

def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [array[i]] + next

from itertools import combinations
n, m = map(int, input().split())
for i in combinations([x for x in range(1, n+1)], m):
    print(*i, sep=' ')