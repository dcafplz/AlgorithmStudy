# https://www.acmicpc.net/problem/1476

import sys
esm = (15, 28, 19)
ESM = tuple(0 if I == i else I for I, i in zip(map(int, sys.stdin.readline().rstrip().split()), esm))
n = 0
while True:
    n += 1
    if ESM == (n%esm[0], n%esm[1], n%esm[2]):
        print(n)
        break