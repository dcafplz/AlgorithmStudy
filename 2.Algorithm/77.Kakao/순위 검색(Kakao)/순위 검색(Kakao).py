# from itertools import product

def solution(info, query):
    dic = {}
    answer = []
    
    # product 사용시 시간복잡도 더 높음, 왜그런지는 의문
    # for i in info:
    #     i = i.split(' ')
    #     for j in product((i[0],'-'), (i[1],'-'), (i[2],'-'), (i[3],'-')):
    #         dic[j] = dic.get(j, []) + [int(i[4])]

    
    for lang in ['cpp', 'java', 'python', "-"]:
        for job in ['backend', 'frontend', "-"]:
            for career in ['junior', 'senior', "-"]:
                for food in ['chicken', 'pizza', "-"]:
                    dic[lang + job + career + food] = []

    for i in info:
        i = i.split(" ")
        for lang in [i[0], "-"]:
            for job in [i[1], "-"]:
                for career in [i[2], "-"]:
                    for food in [i[3], "-"]:
                        dic[lang + job + career + food].append(int(i[4]))
            
    for k in dic.keys():
         dic[k].sort()
    
    for q in query:
        s = q.split(' ')
        i = int(s[7])
        s = ''.join([s[0], s[2], s[4], s[6]])
        scores = dic.get(s, [])
        top, bot = len(scores)-1, 0
        while top >= bot:
            mid = (top+bot)//2
            if scores[mid] >= int(i):
                top = mid - 1
            else:
                bot = mid + 1
        answer.append(len(scores)-bot)
        
    return answer
        