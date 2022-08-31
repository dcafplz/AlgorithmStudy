# https://www.acmicpc.net/problem/8979

# 기존 풀이
import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    if temp[0] == K:
        target = temp
    arr.append(temp)
rank = 1
for i in arr:
    if i[1] > target[1] or (i[1] == target[1] and i[2] > target[2]) or (i[1] == target[1] and i[2] == target[2] and i[3] > target[3]):
         rank += 1
print(rank) 

# 배열간 대소비교가 가능함을 알고 난 풀이
import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    if temp[0] == K:
        target = temp[1:]
    else:
        arr.append(temp[1:])
print(len([x for x in arr if x > target])+1)