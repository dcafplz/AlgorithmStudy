def solution(fees, records):
    answer = {}
    for r in records:
        temp = r.split(" ")
        t = temp[0].split(":")
        if temp[2] == "IN":
            answer[temp[1]] = answer.get(temp[1], 0) - int(t[0])*60 - int(t[1])
        else:
            answer[temp[1]] = answer[temp[1]] + int(t[0])*60 + int(t[1])
    for i in answer:
        if answer[i] <= 0: answer[i] += 1439
        if answer[i] <= fees[0]:
            answer[i] = fees[1]
        else:
            answer[i] = -(-(answer[i] - fees[0]) // fees[2]) * fees[3] + fees[1]
    return [x[1] for x in sorted(answer.items(), key=lambda x: x[0])]


# refactoring

def to_min(time):
    hh, mm = time.split(':')
    return int(hh) * 60 + int(mm)

def solution(fees, records):
    answer = {}
    for r in records:
        time, num, in_out = r.split(' ')
        if in_out == "IN":
            answer[num] = answer.get(num, 0) - to_min(time)
        else:
            answer[num] = answer[num] + to_min(time)
            
    result = []
    for i in sorted(answer):
        time = answer[i] + 1439 if answer[i] <= 0 else answer[i] 
        if time <= fees[0]:
            result.append(fees[1])
        else:
            result.append(-(-(time - fees[0]) // fees[2]) * fees[3] + fees[1])
            
    return result