# https://www.acmicpc.net/problem/13305

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
answer = price[0] * distance[0]
now = price[0]
for i in range(1, n-1):
    if price[i] < now:
        now = price[i]
    answer += now * distance[i]
print(answer)