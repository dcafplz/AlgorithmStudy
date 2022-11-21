# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    dic = {chr(x):x-64 for x in range(65,91)}
    answer = []
    cnt = 27
    index = 0
    while index < len(msg):
        i = 1
        while index + i <= len(msg) and dic.get(msg[index:index+i],0):
            i += 1
        answer.append(dic[msg[index:index+i-1]])
        dic[msg[index:index+i]] = cnt
        cnt += 1
        index = index+i-1
    return answer