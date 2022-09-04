def solution(s):
    s = "0b" + s
    answer = [0, 0]
    while s != "0b1":
        answer[0] += 1
        answer[1] += s.count("0")-1
        s = bin(s.count("1"))
    return answer