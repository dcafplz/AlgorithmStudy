def solution(land):
    for i in range(len(land)-2,-1,-1):
        for j in range(0,4):
            m = max([land[i+1][x] for x in range(0,4) if x != j])
            land[i][j] += m

    return max(land[0])