import itertools

def solution(k, dungeons):
    bf = list(itertools.permutations(dungeons))
    answer = 0
    for x in bf:
        kk = k
        cnt = 0
        for i in x:
            if kk >= i[0] and kk >= i[1]:
                kk -= i[1]
                cnt += 1
        answer = max(answer, cnt)
                
    return answer