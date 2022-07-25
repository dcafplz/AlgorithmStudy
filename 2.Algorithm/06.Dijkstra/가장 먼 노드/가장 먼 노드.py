from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for i in edge:
        graph[i[0]].append([i[1]])
        graph[i[1]].append([i[0]])
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        i = q.popleft()
        for j in graph[i]:
            if visited[j[0]] == 0:
                q.append(j[0])
                visited[j[0]] = visited[i] + 1
    return visited.count(max(visited))