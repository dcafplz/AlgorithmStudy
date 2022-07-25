def solution(n):
    answer = 1
    for i in range(1,int(n/2)+1):
        k,j = 0,0
        while k < n:
            k += (i+j)
            j+=1
            if k == n:
                answer +=1
                break
    return answer