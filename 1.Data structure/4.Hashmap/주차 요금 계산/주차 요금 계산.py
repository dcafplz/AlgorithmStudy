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