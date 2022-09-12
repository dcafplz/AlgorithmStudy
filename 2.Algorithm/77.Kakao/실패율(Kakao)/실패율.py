def solution(N, stages):
    counts = {i:0 for i in range(1,N+2)}
    for i in stages:
        counts[i] += 1
    del(counts[N+1])
    
    total = len(stages)
    for j in counts:
        total -= counts[j]
        if total:
            counts[j] = counts[j]/(total+counts[j])
        
    return sorted(counts, key=lambda x: -counts[x])


def solution(N, stages):
    counts = [0 for _ in range(N+1)]
    answer = []
    for i in stages:
        counts[i-1] += 1
    counts.pop()
    total = len(stages)
    for i in range(N):
        answer.append((i+1, counts[i]/total if total > 0 else 0))
        total -= counts[i]
    
    return list(map(lambda x: x[0], sorted(answer, key=lambda x: (-x[1], x[0]))))