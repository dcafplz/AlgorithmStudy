# https://school.programmers.co.kr/learn/courses/30/lessons/17680?language=python3

def solution(cacheSize, cities):
    dic = {}
    answer = 0
    for i in cities:
        if i.lower() in dic:
            del(dic[i.lower()])
            answer += 1
        else:
            answer += 5
        dic[i.lower()] = True
        if len(dic) > cacheSize:
            for k in dic.keys():
                del(dic[k])
                break
    return answer