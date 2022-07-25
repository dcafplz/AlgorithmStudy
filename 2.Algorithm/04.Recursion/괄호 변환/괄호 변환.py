def ss(p):
    answer = 0
    for i in range(len(p)):
        if p[i] == "(":
            answer += 1
            if answer == 0:
                return ss("(" + ss(p[i+1:])  + ")" + p[1:i].replace("(","k").replace(")","(").replace("k",")")) 
        else:
            answer -= 1
            if answer == 0:
                return p[0:i+1] + ss(p[i+1:])
    return ""

def solution(p):
    return ss(p)