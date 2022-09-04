# https://www.acmicpc.net/problem/1978

import sys
_ = sys.stdin.readline()
arr = tuple(map(int, sys.stdin.readline().rstrip().split()))
big = max(arr)+1
num = set(range(2,big))

for i in range(2,big):
    if i in num:
        num -= set(range(2*i,big,i))
        
print(sum([True for x in arr if x in num]))