def solution(s):
    ntuple = list(map(int, s.replace("{","").replace("}","").split(",")))
    return sorted(list(set(ntuple)), key = lambda x : -ntuple.count(x))



# 시간복잡도 향상
import re

def solution(s):
    dic = {}
    for i in map(int, re.findall('[0-9]+',s)):
        dic[i] = dic.get(i, 0) + 1
    return sorted(dic.keys(), key=lambda x: -dic[x])