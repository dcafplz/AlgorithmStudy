# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    dict = {str(i):[0, 0] for i in range(9, -1, -1)}
    for x in X:
        dict[x][0] += 1
    for y in Y:
        dict[y][1] += 1
    answer = ''
    for k in dict:
        if answer == '' and k == '0':
            if min(dict['0']):
                return '0'
            else:
                return '-1'
        else:
            answer += (k * min(dict[k]))
    return answer

# dictionary 보다 counter 사용시 더 빠름
# 다른사람 풀이

def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer