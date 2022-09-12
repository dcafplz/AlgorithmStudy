# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    board = [list(s) for s in board]
    move = ((0, 0), (0, 1), (1, 0), (1, 1))
    answer = 0
    def delete():
        for i in range(m-1):
            for j in range(n-1):
                if len({board[i+k1][j+k2] for k1, k2 in move}) == 1:
                    for m1, m2 in move:
                        arr[i+m1][j+m2] = True
    while True:
        arr = [[False] * n for _ in range(m)]
        delete()
        for j in range(n):
            now = m-1
            for i in range(m-1, -1, -1):
                if not arr[i][j]:
                    board[now][j] = board[i][j]
                    now -= 1
            for i in range(now+1):
                board[i][j] = False
        temp = sum((True for j in range(n) for i in range(m) if arr[i][j] or not board[i][j]))
        if answer != temp:
            answer = temp
        else:
            return answer


# refactoring 한 코드, pop_set을 쓴다는 아이디어가 너무 좋아 가져다 쓰고 복잡했던 부분 정리함

def remove_blocks(m, n, board):
    move = ((0, 0), (0, 1), (1, 0), (1, 1))
    pop_set = set()
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] and len({board[i+m1][j+m2] for m1, m2 in move}) == 1:
                for m1, m2 in move:
                    pop_set |= {(i+m1,j+m2)}
    
    for j in range(n):
        now = m-1
        for i in range(m-1, -1, -1):
            if (i, j) not in pop_set:
                board[now][j] = board[i][j]
                now -= 1
        for i in range(now+1):
            board[i][j] = False

    return len(pop_set)
    
def solution(m, n, board):
    board = [list(s) for s in board]
    answer = 0

    while True:
        temp = remove_blocks(m, n, board)
        if temp != 0:
            answer += temp
        else:
            return answer