def rcur(triangle, i, j, dp):
    if dp[i][j] == -1:
      dp[i][j] = triangle[i][j] + (max(rcur(triangle, i+1, j, dp), rcur(triangle, i+1, j+1, dp)) if i < (len(triangle) - 1) else 0)
    return dp[i][j]

def solution(triangle):
    n = len(triangle)
    dp = [[-1] * (x+1) for x in range(n)]
    for i in range(n):
        dp[n-1][i] = triangle[n-1][i] 
    return rcur(triangle, 0, 0, dp)