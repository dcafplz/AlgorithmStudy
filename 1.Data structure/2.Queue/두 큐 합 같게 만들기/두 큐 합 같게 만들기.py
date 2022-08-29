# https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3

from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    s1, l = sum(queue1), len(queue1)
    target = (s1 + sum(queue2))//2
    cnt = 0
    while queue1 and queue2 and cnt <= l*2+2:
        if s1 > target:
            t = queue1.popleft()
            queue2.append(t)
            s1 -= t
        elif s1 < target:
            t = queue2.popleft()
            queue1.append(t)
            s1 += t
        else:
            return cnt
        cnt += 1
    return -1