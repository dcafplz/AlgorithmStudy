# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer, length = len(s), len(s)
    s += s
    stack = []
    dic = {"{":(1,0), "}":(0,0), "(":(1,1), ")":(0,1), "[":(1,2), "]":(0,2)}
    for i in range(length):
        t = 0
        for st in s[i:i+length]:
            temp = dic[st]
            if temp[0]:
                stack.append(st)
            elif not stack or dic[stack.pop()][1] != temp[1]:
                t = -1
                break
        if stack: t = -1
        answer += t
    return answer

# "{([})]" 통과 못하는 코드
# def solution(s):
#    answer, length = len(s), len(s)
#    dic = {"{":(1,0), "}":(-1,0), "(":(1,1), ")":(-1,1), "[":(1,2), "]":(-1,2)}
#    s += s
#    for i in range(length):
#        a = [0,0,0]
#        k = 0
#        for st in s[i:i+length]:
#            temp = dic[st]
#            if temp[0] + a[temp[1]] < 0:
#                k = -1
#                break
#            a[temp[1]] += temp[0]
#        if max(a) > 0: k = -1
#        answer += k
#    return answer
