# https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=python3

from collections import deque

def solution(begin, target, words):
    v = [0 for x in range(len(words)+1)]
    q, length = deque([[len(words),0]]), len(begin)
    words.append(begin)
    while q:
        now, cnt = q.popleft()
        v[now] = 1
        for i, s in enumerate(words):
            if sum([s[x]==words[now][x] for x in range(length)]) >= length-1:
                if s == target: return cnt+1
                elif not v[i]: q.append([i, cnt+1])
    return 0