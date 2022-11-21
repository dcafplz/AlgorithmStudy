# https://school.programmers.co.kr/learn/courses/30/lessons/131701
# 효율성 통과는 했는데 더 효율적인 방법이 있을듯

def solution(elements):
    l = len(elements)
    elements = elements + elements 
    answer = set()
    for i in range(1, l+1):
        for j in range(0, l):
            answer.add(sum(elements[j:j+i]))
    return len(answer)