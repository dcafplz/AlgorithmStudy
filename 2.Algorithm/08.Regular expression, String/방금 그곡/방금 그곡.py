# https://school.programmers.co.kr/learn/courses/30/lessons/17683#

import re

def solution(m, musicinfos):
    p = re.compile(".#{0,1}")
    answer = ["(None)", 0]
    ml = len(m.replace("#",""))
    for i in musicinfos:
        temp = i.split(",")
        start, end  = temp[0].split(":"), temp[1].split(":")
        time = (int(end[0]) - int(start[0]))* 60 + int(end[1]) - int(start[1])
        if time <= answer[1]: continue
        t = p.findall(temp[3])
        for j in range(0, min(len(t), time)):
            now = ''.join([t[x%len(t)] for x in range(j,j+ml)])
            if m == now:
                answer = [temp[2], time]
                break
    return answer[0]