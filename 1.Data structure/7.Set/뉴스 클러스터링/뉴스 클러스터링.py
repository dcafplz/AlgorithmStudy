# https://school.programmers.co.kr/learn/courses/30/lessons/17677
import re

p = re.compile('[a-z]{2}')

def to_dic(arr):
    dic = {}
    for i in arr:
        if p.match(i): dic[i] = dic.get(i, 0) + 1
    return dic

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    dic1 = to_dic([str1[x:x+2] for x in range(len(str1)-1)])
    dic2 = to_dic([str2[x:x+2] for x in range(len(str2)-1)])
    x, y = 0, 0
    for k in set(list(dic1.keys()) + list(dic2.keys())):
        x += min(dic1.get(k, 0), dic2.get(k, 0))
        y += max(dic1.get(k, 0), dic2.get(k, 0))
    return int(x/y * 65536) if y != 0 else 65536
