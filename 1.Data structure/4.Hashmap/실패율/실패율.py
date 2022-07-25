def solution(N, stages):
    counts = {i:0 for i in range(1,N+2)}
    for i in stages:
        counts[i] += 1
    k = len(stages)
    for j in counts:
        try:
            k -= counts[j]
            counts[j] = counts[j]/(k+counts[j])
        except:
            0
    del(counts[N+1])
    return sorted(counts, key=lambda x: counts[x], reverse=True)