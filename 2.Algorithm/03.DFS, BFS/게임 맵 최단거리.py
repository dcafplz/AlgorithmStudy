# https://school.programmers.co.kr/questions/16215
# 효율성 통과 못한 코드이나 가독성 좋은 코드라 참고
# maps[x][y] = 0 -> maps[nx][ny] = 0 만 변경 후 성공

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    news = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    search = deque([[0, 0, 1]])
    while search:
        x, y, cnt = search.popleft()
        for i in range(4):
            nx, ny = x+news[i][0], y+news[i][1]
            if nx == n-1 and ny == m-1:
                return cnt + 1
            elif 0 <= nx < n and 0 <= ny < m and maps[nx][ny]:
                search.append([nx, ny, cnt+1])
                maps[nx][ny] = 0
    return -1


# 다른사람 코드 보기전 참고한 코드
# maps에 거리를 누적하였는데 어떤 오류가 발생한것인지 확인하지 못함

# from collections import deque

# def solution(maps):
#     q = deque()
#     end = [len(maps)-1, len(maps[0])-1]
#     q.append([0,0])
#     maps[0][0] = 1
#     while q:
#         now = q.popleft()
#         if end == now:
#             return maps[now[0]][now[1]] - 1
#         nex = [[now[0]-1, now[1]], [now[0]-1, now[1]], [now[0]+1, now[1]], [now[0], now[1]+1]]
#         for i in nex:
#             if i == end:
#                 return maps[now[0]][now[1]] + 1
#             elif 0 <= i[0] <= end[0] and 0 <= i[1] <= end[1]:
#                 if maps[i[0]][i[1]] == 1:
#                     q.append(i)
#                     maps[i[0]][i[1]] = maps[now[0]][now[1]] + 1
#     return -1