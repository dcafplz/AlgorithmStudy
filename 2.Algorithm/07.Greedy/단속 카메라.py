# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    routes.sort(key=lambda x:x[1])
    cnt, i = 0, 0
    while i < len(routes):
        cnt += 1
        now = routes[i]
        while i+1 < len(routes) and min(routes[i+1]) <= now[1]:
            i += 1
        i += 1
    return cnt

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))