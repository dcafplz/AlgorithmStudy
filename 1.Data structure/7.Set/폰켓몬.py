def solution(nums):
    k = len(nums)/2
    nums = list(set(nums))
    return min(len(nums),k)