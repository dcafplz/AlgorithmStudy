from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        dic = {}
        m = 2
        for menu in orders:
            for j in combinations(sorted(menu), i):
                dic[j] = dic.get(j, 0) + 1
                m = max(m, dic[j])
        answer += [''.join(k) for k in dic if dic[k] >= m]
    return sorted(answer)
