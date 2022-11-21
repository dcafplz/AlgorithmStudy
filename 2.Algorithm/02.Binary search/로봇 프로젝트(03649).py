# https://www.acmicpc.net/problem/3649

import sys

def block(blocks, N):
    start, end = 0, N-1
    while start < end:
        s = blocks[start] + blocks[end]
        if s == target:
            return (f'yes {blocks[start]} {blocks[end]}')
        elif s > target:
            end -= 1
        else:
            start += 1
    return 'danger'

while True:
    try:
        target, N = int(sys.stdin.readline())*10000000, int(sys.stdin.readline())
        print(block(sorted([int(sys.stdin.readline()) for _ in range(N)]), N))
    except:
        break