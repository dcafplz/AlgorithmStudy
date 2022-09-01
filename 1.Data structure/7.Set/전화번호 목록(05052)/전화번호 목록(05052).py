# https://www.acmicpc.net/problem/5052

import sys

def yes_no(arr):
    for k in arr:
        temp = ''
        for i in range(len(k)-1):
            temp += k[i]
            if temp in arr:
                return 'NO'
    return 'YES'

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    arr = {sys.stdin.readline().rstrip() for _ in range(N)}
    print(yes_no(arr))