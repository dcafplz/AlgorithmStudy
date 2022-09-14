# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def cross(stones, k, mid):
    cnt = 0
    for s in stones:
        if s <= mid:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True

def solution(stones, k):
    low, high = 1, 200000000 #max(stones)로 해도 큰차이 보이지 않음
    while low <= high:
        mid = (low+high)//2
        if cross(stones, k, mid):
            low = mid + 1
        else:
            high = mid - 1
    return low