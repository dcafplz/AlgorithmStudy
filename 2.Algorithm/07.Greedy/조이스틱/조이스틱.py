# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    dic = {chr(x):min(x-65,91-x) for x in range(65,91)}
    l = len(name)
    def move_cnt(a):
        is_first, cnt = True, 0
        for i in range(l-1,0,-1):
            if is_first and name[a[i]] == 'A': continue
            b, s = max(a[i], a[i-1]), min(a[i], a[i-1])
            cnt += min(b-s, l-b+s)
            is_first = False
        return cnt
    min_value = 100 if len(name) > 1 else 0
    arr = list(range(1,l))
    for i in range(1, l-1):
        min_value = min(min_value, move_cnt([0]+ arr[0:i] + arr[-1:i-l:-1]), move_cnt([0]+ arr[-1:i-l:-1] + arr[0:i]))
    return min_value + sum([dic[x] for x in name])