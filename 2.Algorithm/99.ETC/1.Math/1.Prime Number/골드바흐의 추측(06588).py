# https://www.acmicpc.net/problem/6588

import sys
arr = []
max_value = 0

while (n:= int(sys.stdin.readline())) != 0:
    arr.append(n)
    if max_value < n: max_value = n

def prime_list(n):
    sieve = [True] * n

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
                
    return {i:True for i in range(2, n) if sieve[i] == True}

primes = prime_list(max_value)

for i in arr:
    s, e = 0, -1
    for p in primes:
        if i-p in primes:
            print(f'{i} = {min(p, i-p)} + {max(p, i-p)}')
            break
    else:
        print('Goldbach\'s conjecture is wrong.')


# --------------------------


import sys
arr = []
max_value = 0

while (n:= int(sys.stdin.readline())) != 0:
    arr.append(n)
    if max_value < n: max_value = n

def prime_list(n):
    sieve = [True] * n

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return sieve

primes = prime_list(max_value)

for i in arr:
    for a in range(3, i, 2):
        if primes[a]:
            b=i-a
            if primes[b]:
                print(f'{i} = {a} + {b}')
                break
    else:
        print('Goldbach\'s conjecture is wrong.')