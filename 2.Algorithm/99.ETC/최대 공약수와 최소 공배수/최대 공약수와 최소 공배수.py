def solution(n, m):
    for i in range((n if n <= m else m),0,-1):
        if n % i == 0 and m % i == 0:
            return [i,n*m/i]