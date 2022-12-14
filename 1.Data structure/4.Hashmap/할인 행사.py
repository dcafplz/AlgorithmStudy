# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    discount_dict = {k:v for k, v in zip(want, number)}
    cnt = 0
    for i in range(0, 10):
        discount_dict[discount[i]] = discount_dict.get(discount[i], 0) - 1
    for now in range(0, len(discount)-9):
        if now - 1 >= 0:
            discount_dict[discount[now-1]] = discount_dict.get(discount[now-1], 0) + 1
            discount_dict[discount[now+9]] = discount_dict.get(discount[now+9], 0) - 1
        for k in discount_dict:
            if discount_dict[k] > 0:
                break
        else:
            cnt += 1
    return cnt