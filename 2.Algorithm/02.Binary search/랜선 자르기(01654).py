# https://www.acmicpc.net/problem/1654
import sys
k, n = map(int,sys.stdin.readline().rstrip().split())
lens = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
upper_bound = sum(lens)//n
lower_bound = 1
while upper_bound >= lower_bound:
    sum = 0
    now = (upper_bound+lower_bound)//2
    for v in lens:
        sum += v//now
    if sum >= n:
        answer = now
        lower_bound = now+1
    else:
        upper_bound = now-1
print(answer)