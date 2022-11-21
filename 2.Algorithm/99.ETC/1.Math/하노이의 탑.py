def hanoi(n, start, to, other, answer):
    
    if n == 1:
        answer.append([start, to])

    else:
        hanoi(n-1, start, other, to, answer)
        answer.append([start, to])
        hanoi(n-1, other, to, start, answer)
    
    return answer
    
def solution(n):
    answer = []
    return hanoi(n, 1, 3, 2, answer)