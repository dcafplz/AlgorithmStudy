def solution(record):
    answer = []
    msgdic = {"Enter":"님이 들어왔습니다.",
              "Leave":"님이 나갔습니다."}
    dic = {}
    
    for i in record:
        temp = i.split(" ")
        if temp[0] != "Change":
            answer.append([temp[1],temp[0]])
        if temp[0] != "Leave":
            dic[temp[1]] = temp[2]
    return [dic[x[0]]+msgdic[x[1]] for x in answer]