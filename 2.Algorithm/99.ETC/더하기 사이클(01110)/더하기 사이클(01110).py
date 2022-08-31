# https://www.acmicpc.net/problem/1110

n = int(input())
n2, cnt = n, 0
while True:
    cnt += 1
    d, m = divmod(n2, 10)
    n2 = m * 10 + (d + m)%10
    if n == n2: break
print(cnt)