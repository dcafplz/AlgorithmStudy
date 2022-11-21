def solution(s):
    temp = ""
    answer = ""
    numbers = {"zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"}
    for i in s:
        try:
            answer += str(int(i))
        except:
            temp += i
            try:
                answer += numbers[temp]
                temp = ""
            except:
                pass
    return int(answer)