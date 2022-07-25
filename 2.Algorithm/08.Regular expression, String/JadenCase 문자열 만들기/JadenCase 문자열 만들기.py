def solution(s):
    s = s.lower()
    a = [s[0].upper()]
    for i in range(1,len(s)):
        if s[i-1] == " ":
            a.append(s[i].upper())
        else:
            a.append(s[i])
    return ''.join(a)