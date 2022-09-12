# https://school.programmers.co.kr/learn/courses/30/lessons/67257
# eval, 괄호까지는 생각했는데 그 이상 구현하지 못하여 정답 참조함

def solution(expression):
    answer = 0
    for sign in ['+-*','+*-','-+*','-*+','*+-','*-+']:
        f, s = sign[0], sign[1]
        answer = max(answer, abs(eval(f.join([f'({s.join([f"({i})" for i in e.split(s)])})' for e in expression.split(f)]))))
    return answer

