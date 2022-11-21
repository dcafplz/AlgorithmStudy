from itertools import combinations_with_replacement

def solution(n, info):
    score_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    answer = [-1]
    max_score = 0
    for i in combinations_with_replacement(score_array,n):
        temp = [0] * 11
        a_score = 0
        r_score = 0
        for k in i:
            temp[k] += 1
        for k in range(len(temp)):
            if temp[k] > info[k]:
                r_score += score_array[k]
            elif temp[k] <= info[k] and info[k] > 0:
                a_score += score_array[k]
        if max_score < (r_score - a_score):
            max_score = r_score - a_score
            answer = temp.copy()
    return answer


# refactoring, 비교도 안되게 빠름


from collections import deque

def solution(n, info):
    info.reverse()
    q = deque([(10, 0, n, [0] * 11)])
    max_diff = [0, [-1]]

    while q:
        i, score_diff, left_arrows, arrows = q.popleft()
        if i and left_arrows:
            q.append((i-1, score_diff-(i if info[i]>0 else 0), left_arrows, arrows.copy()))
            if left_arrows > info[i]:
                arrows[i] = info[i]+1
                q.append((i-1, score_diff+i, left_arrows-arrows[i], arrows.copy()))
        else:
            score_diff -= sum([x for x in range(1, i+1) if info[x]])
            if max_diff[0] <= score_diff:
                arrows[0] = left_arrows
                max_diff = [score_diff, arrows.copy()]

    return [-1] if max_diff[0] == 0 else max_diff[1][::-1]