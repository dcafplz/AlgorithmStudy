def solution(s):
    sl = []

    for i in s:
        if len(sl) > 0 and sl[-1] == i:
            sl.pop()
        else:
            sl.append(i)
    
    return 0 if len(sl) > 0 else 1 