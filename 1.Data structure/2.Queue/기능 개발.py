def solution(progresses, speeds):
    answer = []
    cnt = 1
    for i in range(0,len(progresses)):
        speeds[i] = -((progresses[i]-100)//speeds[i])
        if i >= 1 and max(speeds[:i]) >= speeds[i]:
            cnt+=1
        elif i != 0:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer



# def solution(progresses, speeds):
#     answer = [0]
#     index = 0
#     while min(progresses) < 100:
#         for i in range(index,len(speeds)):
#             progresses[i] += speeds[i]
#         while progresses[index] >= 100:
#             index += 1
#             if index >= len(speeds):
#                 break
#         answer.append(index)
#     answer = sorted(list(set(answer)))
#     return [answer[x+1]-answer[x] for x in range(0,len(answer)-1)]