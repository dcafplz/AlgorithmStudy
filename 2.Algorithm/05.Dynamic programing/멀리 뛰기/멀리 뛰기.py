#팩토리얼을 통한 중복값 순열로 구하려 했으나 도중에 피보나치 수열인걸 확인하고 적용함.

def solution(n):
    f1, f2 = 0, 1
    for i in range(1,n+1):
        f1, f2 = f2, f2 + f1
    return f2%1234567