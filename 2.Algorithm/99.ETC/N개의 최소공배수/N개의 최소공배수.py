def solution(arr):
    answer = 1
    arr.sort()
    for i in arr:
        for j in range(i,0,-1):
            if answer % j == 0 and i % j ==0:
                answer = i*answer/j
                break
    return answer