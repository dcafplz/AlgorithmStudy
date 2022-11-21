# https://www.acmicpc.net/submit/12865/48628379

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
dp = [{0:0}]

for i in range(N):
    k, v = tuple(map(int, sys.stdin.readline().rstrip().split()))
    if k <= K:
        now = dp[-1]
        dic = dp[-1].copy()
        for k1 in now:
            if k+k1 <= K:
                dic[k+k1] = max(now.get(k+k1, 0), v + now[k1])
        dic[k] = max(now.get(k, 0), v)
        dp.append(dic)

print(max(dp[-1].values()))