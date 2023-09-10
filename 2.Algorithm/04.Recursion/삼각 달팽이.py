def solution(n):
    answer = [(x+1)*[0] for x in range(n)]
    
    def recur(x, y, m, now):
        for i in range(m):
            answer[y+i][x] = now
            now += 1
        for i in range(1,m):
            answer[y+m-1][x+i] = now
            now += 1
        for i in range(m-2, 0, -1):
            answer[y+i][x+i] = now
            now += 1
        if m - 3 > 0:
            recur(x+i, y+i+1, m-3, now)
    recur(0, 0, n, 1)

    return [x for y in answer for x in y]