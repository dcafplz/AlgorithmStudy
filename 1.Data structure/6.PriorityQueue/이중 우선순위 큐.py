def solution(operations):
    answer = []
    for i in operations:
        temp = i.split(" ")
        if temp[0] == "I":
            answer.append(int(temp[1]))
        elif temp[0] == "D" and len(answer) > 0:
            answer.sort()
            if temp[1] == "-1":
                answer.pop(0)
            else:
                answer.pop()
    answer.sort()
    print(answer)
    return [answer[len(answer)-1] if len(answer)>0 else 0,answer[0] if len(answer)>0 else 0]