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

# 

change = {'(':')', ')':'('}

def f(str):
    cnt = 0
    cor = True
    for i in range(len(str)):
        if str[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0: cor = False
            
        if cnt == 0:
            return i+1, cor

def solution(p):
    if not p: return ''
    index, cor = f(p)
    u = p[:index]
    v = p[index:]
    if cor:
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + ''.join([change[u[x]] for x in range(1,len(u)-1)])