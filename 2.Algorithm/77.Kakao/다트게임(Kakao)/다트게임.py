def solution(dartResult):
    dartResult = dartResult.replace("10", "k")
    bonuses = {"S":1,"D":2,"T":3}
    
    answer = [0]
    
    for i in dartResult:
        try:
            answer[len(answer)-1] **= bonuses[i] 
        except:
            if i == "*":
                answer[len(answer)-1] *= 2
                answer[len(answer)-2] *= 2
            elif i == "#":
                answer[len(answer)-1] *= -1
            elif i == "k":
                answer.append(10)
            else:
                answer.append(int(i))
    return sum(answer)


import re

def solution(dartResult):
    answer = [0]
    
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'*':2, '#':-1}
    
    for i in re.findall('[0-9]+|[SDT]|[\*\#]', dartResult):
        if i.isdigit():
            answer.append(int(i))
        elif i.isalpha():
            answer[-1] = pow(answer[-1], bonus[i])
        else:
            answer[-1] *= option[i]
            if i == '*':
                answer[-2] *= option[i]
    return sum(answer)


import re

def solution(dartResult):
    answer = [0]
    
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'*':2, '#':-1, '':1}
    
    for s, b, o in re.findall('([0-9]+)([SDT])([*#]?)', dartResult):
        if o == '*':
            answer[-1] *= 2
        answer.append(int(s) ** bonus[b] * option[o])
    return sum(answer)