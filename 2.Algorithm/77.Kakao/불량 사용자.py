# https://school.programmers.co.kr/learn/courses/30/lessons/64064?language=python3

import re
from collections import deque

def is_match(user_id, banned_id):
    
    # 정규표현식 리스트형태로 아예 반환
    for i in range(len(banned_id)):
        p = re.compile(banned_id[i].replace('*', '\w'))
        banned_id[i] = []
        for u in user_id:
            temp = p.match(u) 
            if temp and temp.end() == len(u):
                banned_id[i].append(u)
    return banned_id

    # 일반 반복문
    # 반복은 solution에서 돌리고 여기서는 체크만
    # if len(u) == len(now):
    #     for s1, s2 in zip(u, now):
    #         if s1 == s2 or s2 == '*':
    #             continue
    #         return False
    # else:
    #     return False
    # return True

def solution(user_id, banned_id):
    banned_id = is_match(user_id, banned_id)
    q = deque([set()])
    answer_set = set()
    while q:
        now = q.popleft()
        i = len(now)
        if i < len(banned_id):
            for a in banned_id[i]:
                if a not in now:
                    now.add(a)
                    q.append(now.copy())
                    now.remove(a)
        else:
            answer_set.add(tuple(sorted(list(now))))

    return len(answer_set)