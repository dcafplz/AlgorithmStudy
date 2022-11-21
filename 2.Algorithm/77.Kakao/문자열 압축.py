def solution(s):
    m = len(s)
    for i in range(1, int(len(s)/2)+1):
        now = s[0:i]
        cnt = len(s)
        match = 0
        for j in range(i, len(s)-i+1, i):

            if(now == s[j:j+i]):
                match += 1
            
            else:
                now = s[j:j+i]
                cnt = cnt - match * i + (0 if match == 0 else len(str(match+1)))
                match = 0

        cnt = cnt - match * i + (0 if match == 0 else len(str(match+1)))
        m = min(cnt, m)
    return m