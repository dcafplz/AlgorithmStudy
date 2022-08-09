# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    def recur(n, row, col):
        if n == 0:
            return (1-arr[row][col], arr[row][col])
        else:
            c0, c1 = 0, 0
            for i in (recur(n//2, row, col), recur(n//2, row+n, col), recur(n//2, row, col+n), recur(n//2, row+n, col+n)):
                c0, c1 = c0+i[0], c1+i[1]
        return (1 if c1 == 0 else c0, 1 if c0 == 0 else c1) 
    return recur(len(arr[0])//2, 0, 0)