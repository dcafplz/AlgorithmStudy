def solution(N, number):
    dic = {}
    if N == number:
        return 1
    dic[1] = set([N])
    for i in range(2, 9):
        temp = set([int(str(N)*i)])
        for j in range(1, i):
            for x in dic[j]:
                for y in dic[i-j]:
                    temp.add(x+y)
                    temp.add(x*y)
                    temp.add(x-y)
                    if y != 0:
                        temp.add(x//y)
        for j in temp:
            if j == number: return i
        dic[i] = temp
    return -1