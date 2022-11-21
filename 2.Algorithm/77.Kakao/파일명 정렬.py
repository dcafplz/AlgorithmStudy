# https://school.programmers.co.kr/learn/courses/30/lessons/17686?language=python3

import re

def solution(files):
    return [''.join(k) for k in sorted([re.findall('[^0-9]+|[0-9]+', x) for x in files], key=lambda x: (x[0].lower(), int(x[1])))]