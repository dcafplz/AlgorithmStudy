# https://school.programmers.co.kr/learn/courses/30/lessons/67258?language=python3

def solution(gems):
    dic = {}
    answer = [100000, [0, 0]]
    count = len(set(gems))
    for i, gem in enumerate(gems):
        if gem in dic:
            del(dic[gem])
        dic[gem] = i
        if len(dic) == count:
            for k in dic.keys():
                if i-dic[k] < answer[0]:
                    answer = [i-dic[k], [dic[k]+1, i+1]]
                break
    return answer[1]