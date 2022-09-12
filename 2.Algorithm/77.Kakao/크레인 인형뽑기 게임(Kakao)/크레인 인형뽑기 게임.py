def solution(board, moves):
    answer = [0]
    cnt = 0
    for i in moves:
        for j in range(0,len(board)):
            if board[j][i-1] != 0:
                if board[j][i-1] == answer[len(answer)-1]:
                    answer.pop()
                    cnt += 2
                else:
                    answer.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return cnt