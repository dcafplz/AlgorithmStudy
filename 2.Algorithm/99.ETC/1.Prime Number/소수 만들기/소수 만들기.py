from itertools import *

def solution(nums):
    answer = []
    nums.sort()
    sieve = [True] * (sum(nums[-3:])+1)
    m = int((sum(nums)+1) ** 0.5)    

    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, (sum(nums[-3:])+1), i): 
                sieve[j] = False

    prime = [i for i in range(2, (sum(nums[-3:])+1)) if sieve[i] == True]

    for j in list(combinations(nums,3)):
        if sum(j) in prime:
            answer.append(sum(j))

    return len(answer)