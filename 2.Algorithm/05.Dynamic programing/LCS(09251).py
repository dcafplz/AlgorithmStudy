# https://www.acmicpc.net/problem/9251

import sys

a, b = sys.stdin.readline().strip(), sys.stdin.readline().strip()
la, lb = len(a)+1, len(b)+1
dp = [[0] * lb for _ in range(la)]
for i1 in range(1, la):
    for i2 in range(1, lb):
        if a[i1-1] == b[i2-1]:
            dp[i1][i2] = dp[i1-1][i2-1] + 1
        else:
            dp[i1][i2] = max(dp[i1][i2-1], dp[i1-1][i2])
print(dp[-1][-1])