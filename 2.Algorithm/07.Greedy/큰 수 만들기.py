def solution(number, k):
    answer = []
    for s in number:
        while k > 0 and answer and answer[-1] < s:
            k-=1
            answer.pop()
        answer.append(s)
    return ''.join(answer[:len(answer)-k])
