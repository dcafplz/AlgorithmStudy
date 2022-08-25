# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 정답 참조함

def solution(numbers):
    return str(int(''.join(sorted([str(x) for x in numbers], key=lambda x: (x*4)[:4], reverse=True))))
