# https://school.programmers.co.kr/learn/courses/30/lessons/67259

# dfs를 이용한 풀이, 방향에 따라 오답이 될 수 있음, 엄밀하게 틀린 풀이임
def solution(board):
    # moves를 ((1, 0), (0, 1), (-1, 0), (0, -1))로 할시 테스트 케이스 통과 못함
    moves = ((-1, 0), (0, -1), (1, 0), (0, 1))
    n = len(board)-1
    board[0][0] = -500
    stack = [(0, 0, 4)]
    while stack:
        y, x, last_move = stack.pop()
        money = board[y][x] 
        for i, move in enumerate(moves):
            ny, nx = y + move[0], x + move[1]
            if 0 <= ny <= n and 0 <= nx <= n:
                cost = (100 if i == last_move else 600) 
                if (board[ny][nx] != 1 and (board[ny][nx] >= money+cost or board[ny][nx] == 0)):
                    stack.append((ny, nx, i))
                    board[ny][nx] = money + cost
    return board[-1][-1]

# 3차원 dp를 통한 풀이
from collections import deque

def solution(board):
    n = len(board)
    dp = [[[10000000] * 4 for x in range(n)] for _ in range(n)]
    dp[0][0][0], dp[0][0][1], dp[0][0][2], dp[0][0][3] = -500, -500, -500, -500
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    q = deque([(0, 0, -1)])
    while q:
        y, x, last_move = q.popleft()
        money = dp[y][x][last_move]
        for i, move in enumerate(moves):
            ny, nx = y + move[0], x + move[1]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                c = (100 if i == last_move else 600)
                if money + c < dp[ny][nx][i]:
                    q.append((ny, nx, i))
                    dp[ny][nx][i] = money + c
    return min(dp[-1][-1][0], dp[-1][-1][1], dp[-1][-1][2], dp[-1][-1][3])