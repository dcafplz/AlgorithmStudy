def solution(word):
    dic = {"A":0,"E":1,"I":2,"O":3,"U":4}
    i = 781
    answer = 0
    for s in word:
        answer += dic[s]*i + 1
        i = (i-1)/5
    return answer