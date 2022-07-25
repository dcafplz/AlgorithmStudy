def solution(n, words):
    first = False
    for i in range(1,len(words)):
        if words.count(words[i]) >= 2:
            if first or i == len(words)-1:
                return [(i%n)+1,(i//n)+1]
            else:
                first = True
        elif words[i-1][-1:] != words[i][0]:
            return [(i%n)+1,(i//n)+1]
    return [0,0]