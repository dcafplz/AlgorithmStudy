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