def solution(s, n):
    answer = ""
    for i in s:
        if i == " ":
            answer += " "
        elif (ord(i) >= 97 and ord(i)+n > 122) or (ord(i) <= 90 and ord(i) >= 65 and ord(i)+n > 90):
            answer += chr(ord(i)+n-26)
        else:
            answer += chr(ord(i)+n)
    return answer