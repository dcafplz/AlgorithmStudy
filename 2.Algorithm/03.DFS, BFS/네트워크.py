# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
def solution(n, computers):
    visited = [0 for x in range(n)]
    def dfs(v, k):
        visited[v] = k
        for i in range(k-1,n):
            if computers[v][i] and not visited[i]: dfs(i, k)
    for i in range(n):
        if not visited[i]: dfs(i, i+1)
    return len(set(visited))