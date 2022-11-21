# https://school.programmers.co.kr/learn/courses/30/lessons/77885
def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i+1)
        else:
            temp, n = i, 1
            while temp % 2 != 0:
                n *= 2
                temp //= 2
            answer.append(i+(n/2))
    return answer