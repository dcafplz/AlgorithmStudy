def solution(n):
    fi1 = 0
    fi2 = 1
    for i in range(2,n+1):
        fi1, fi2 = fi2, (fi2+fi1)
    return fi2%1234567