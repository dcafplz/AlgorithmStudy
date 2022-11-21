# stack 사용 
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(0,len(prices)):
        while stack != [] and stack[-1][0] > prices[i]:
            temp = stack.pop()[1]
            answer[temp] = i-temp
        else:
            stack.append([prices[i],i])
    for i in stack:
        answer[i[1]] = len(prices) - i[1]-1
    return answer

# 원래 코드, 테스트 3 222.59, 19.3mb
    # answer =[]
    # for i in range(0,len(prices)-1):
    #     k = i
    #     while prices[i] <= prices[k]:
    #         k +=1
    #         if k >= len(prices)-1:
    #             break
    #     answer.append(k-i)
    # answer.append(0)