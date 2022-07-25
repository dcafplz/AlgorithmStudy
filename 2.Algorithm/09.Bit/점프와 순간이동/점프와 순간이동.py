def solution(n):
    return str(bin(n)).count("1")


# def solution(n):
#     answer = 1
#     while n > 1:
#         answer = answer + (n%2)
#         n //= 2
#     return answer