def solution(n):
    cnt = str(bin(n)).count("1")
    while 1:
        n += 1
        if cnt == str(bin(n)).count("1"):
            return n