def solution(answers):
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]    
    answer = [0,0,0]
    for i in range(len(answers)):
        answer[0] += (a1[i%5] == answers[i])
        answer[1] += (a2[i%8] == answers[i])
        answer[2] += (a3[i%10] == answers[i])
    return [i+1 for i in list(filter(lambda x: answer[x] == max(answer), range(len(answer))))]