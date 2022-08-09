# https://school.programmers.co.kr/learn/courses/30/lessons/87377

def solution(line):
    star = []
    INF = float('inf')
    xy_range = [-INF,INF,-INF,INF]
    for i in range(0,len(line)-1):
        a, b, e = line[i]
        for j in range(i+1,len(line)):
            c, d, f = line[j]
            try:
                bot = (a*d - b*c)
                x = ((b*f) - (e*d))/bot
                y = ((e*c) - (a*f))/bot
                if x == int(x) and y == int(y):
                    x, y = int(x), int(y)
                    star.append([x,y])
                    xy_range[0], xy_range[1], xy_range[2], xy_range[3] =  max(xy_range[0], x), min(xy_range[1], x), max(xy_range[2], y), min(xy_range[3], y)
            except: 0
    answer = [["." for col in range(-1, xy_range[0] - xy_range[1])] for row in range(-1, xy_range[2]-xy_range[3])]
    for x,y in star:
        answer[(y-xy_range[2])*-1][x-xy_range[1]] = "*"
    return [''.join(x) for x in answer]