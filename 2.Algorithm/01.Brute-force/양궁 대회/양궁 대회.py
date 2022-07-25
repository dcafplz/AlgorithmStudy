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