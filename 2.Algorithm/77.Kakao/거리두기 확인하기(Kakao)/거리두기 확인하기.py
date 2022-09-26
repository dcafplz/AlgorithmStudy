# https://school.programmers.co.kr/learn/courses/30/lessons/81302?language=python3

def social_distancing(place):
    arr = [[False for _ in range(7)] for _ in range(7)]
    moves = ((0, 1), (1, 0), (1, 1), (2, 1), (1, 2))
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                for move in moves:
                    if arr[i+move[0]][j+move[1]] and place[i+move[0]-1][j+move[1]-1] != 'X':
                        return 0
                    else:
                        arr[i+move[0]][j+move[1]] = True
            elif place[i][j] == 'X':
                arr[i+1][j+1] = False
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(social_distancing(place))
    return answer