from collections import deque

def solution(numbers, target):
    i = 1
    q = deque()
    q.append(numbers[0])
    q.append(-numbers[0])
    while i < len(numbers):
        temp = q.popleft()
        q.append(temp+numbers[i])
        q.append(temp-numbers[i])
        if len(q) == 2 ** (i+1):
            i += 1
    return q.count(target)