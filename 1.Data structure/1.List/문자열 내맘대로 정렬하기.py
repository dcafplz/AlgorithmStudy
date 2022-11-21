def solution(strings, n):
    for i in range(0,len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()
    return [x[1:] for x in strings]