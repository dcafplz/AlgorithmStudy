def is_prime(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return 0
    return 1 if n >= 2 else 0

def solution(n, k):
    s = ""
    answer = 0
    while n > 0:
        s = str(n%k) + s
        n //= k
    for i in filter(None, s.split("0")):
        answer += is_prime(int(i))
    return answer