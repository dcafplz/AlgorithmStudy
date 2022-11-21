def solution(citations):
    for i in range(max(citations),0,-1):
        hindex = sum([1 if i<=x else 0 for x in citations])
        if hindex >= i:
            return min(hindex,i)
    return 0