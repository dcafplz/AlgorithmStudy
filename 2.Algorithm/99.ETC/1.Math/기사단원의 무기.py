# https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=python3

def solution(number, limit, power):
    counts = [0, 1] + [2] * (number-1)
    for i in range(2, int(number ** 0.5) + 1):
        for j in range(i+i, int(number ** 0.5) + 1, i):
            counts[j] += 2
    return sum([x if x <= limit else power for x in counts])

    # answer = 0
    # for num in range(1, number+1):
    #     cnt = 2
    #     for i in range(2, int(num**0.5)+1):
    #         if num % i == 0:
    #             cnt += 2
    #     if num ** 0.5 == int(num**0.5): cnt -= 1
    #     answer += cnt if cnt <= limit else power
    # return answer