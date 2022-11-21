# https://school.programmers.co.kr/learn/courses/30/lessons/42890?language=python3

from itertools import combinations

def solution(relation):
    n = len(relation[0])
    visited = set()
    
    def to_set(com):
        s = set()
        for k in relation:
            temp = ''.join([k[x] for x in com])
            if temp in s: return False
            s.add(temp)
        return True
    
    answer = 0
    for i in range(1, n+1):
        temp_visited = set()
        for j in combinations([x for x in range(n) if x not in visited], i):
            if to_set(j) and not sum([set(x).issubset(set(j)) for x in visited]):
                answer += 1
                visited.add(j)
    return answer