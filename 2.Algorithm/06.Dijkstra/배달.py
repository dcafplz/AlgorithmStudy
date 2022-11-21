def solution(N, road, K):
    answer = {x:500001 for x in range(1,N+1)}
    visited = [False for x in range(0,N+1)]
    answer[1] = 0
    visited[0] = True
    start = 1
    while False in visited:
        temp = {y:answer[y] for y in  list(filter(lambda x: visited[x]==False, answer.keys()))}
        start = min(temp,key=temp.get)
        visited[start] = True
        for i in road:
            if i[0] == start and visited[i[1]] == False:
                answer[i[1]] = min(answer[i[1]], answer[start] + i[2])
            if i[1] == start and visited[i[0]] == False:
                answer[i[0]] = min(answer[i[0]], answer[start] + i[2])
    return [1 if x <= K else 0 for x in answer.values()].count(1)