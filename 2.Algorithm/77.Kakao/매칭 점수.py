# https://school.programmers.co.kr/learn/courses/30/lessons/42893

import re

def solution(word, pages):
    dic = {}
    word = word.lower()
    score = re.compile('[a-z]+')
    meta = re.compile('<meta.+ content=\"(.*)\"/>')
    out = re.compile('<a href=\"(\S*)\">')

    for page in pages:
        page = page.lower()
        dic[meta.findall(page)[0]] = [len([x for x in score.findall(page) if x == word]), [out.findall(page)][0], 0]
    cnt = -1

    for k in dic:
        cnt += 1
        for link in dic[k][1]:
            if link in dic:
                dic[link][2] += (dic[k][0]/len(dic[k][1]))

    score = [x[0]+x[2] for x in list(dic.values())]
    return [x for x in range(len(score)) if max(score) == score[x]][0]


#

import re

def solution(word, pages):
    dic = {}
    word = word.lower()

    for page in pages:
        page = page.lower()
        meta = re.findall('<meta.+ content="(.*)"/>', page)[0]
        score = len([x for x in re.findall('[a-z]+', page) if x == word])
        out = re.findall('<a href="(\S*)">', page)
        dic[meta] = [score, 0, out]
        
    for k in dic:
        for link in dic[k][2]:
            if link in dic:
                dic[link][1] += (dic[k][0]/len(dic[k][2]))

    score = [x[0]+x[1] for x in list(dic.values())]
    return [x for x in range(len(score)) if max(score) == score[x]][0] 