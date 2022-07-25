def solution(n):
    a = [4, 1, 2]
    answer = ""
    while n > 0:
        temp = n % 3
        answer = str(a[temp]) + answer
        n //= 3
        if temp == 0:
            n -= 1
    return answer