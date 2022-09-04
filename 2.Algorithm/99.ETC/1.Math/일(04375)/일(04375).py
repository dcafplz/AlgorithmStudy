# https://www.acmicpc.net/problem/4375

import sys

def solution(N):
    ones = int(len(str(N)) * '1')
    while ones % N != 0:
        ones = ones * 10 + 1
    print(len(str(ones)))

try:
    while True:
        N = int(sys.stdin.readline())
        solution(N)
except:
    sys.exit()