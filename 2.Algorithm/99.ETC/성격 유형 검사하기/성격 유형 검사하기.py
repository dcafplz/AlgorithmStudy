# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    POINT = {x:x-4 for x in range(1,8)}
    dic = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    for s, c in zip(survey, choices):
        if s in dic:
            dic[s] -= POINT[c]
        else: 
            dic[s[::-1]] += POINT[c]
    return ''.join([x[0] if dic[x] >= 0 else x[1] for x in dic])