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


#

s = {'C#':'c', 'D#':'d', 'F#':'f', 'G#':'g', 'A#':'a'}

def to_min(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def change(code):
    for i in s:
        code = code.replace(i, s[i])
    return code

def solution(m, musicinfos):

    answer = ["(None)", 0]
    m = change(m)
    
    for musicinfo in musicinfos:
        start, end, title, code = musicinfo.split(",")
        time = to_min(end) - to_min(start)
        if time <= answer[1]: continue
        
        code = change(code)
        if m in (code * (1 + time//len(code)))[:time] and time > answer[1]:
            answer = [title, time]
        
    return answer[0]