# https://school.programmers.co.kr/learn/courses/30/lessons/150370

import re

def solution(today, terms, privacies):
    date = [28 * 12, 28, 1]
    today = sum([int(x) * y for x, y in zip(re.findall("\w+", today), date)])
    terms_dict = {}
    answer = []

    for term in terms:
        a, b = re.findall("\w+", term)
        terms_dict[a] = int(b) * date[1]

    for idx, privacy in enumerate(privacies):
        y, m, d, term = re.findall("\w+", privacy)
        if today >= (int(y) * date[0] + (int(m)) * date[1] + int(d) + terms_dict[term]):
            answer.append(idx+1)

    return answer
