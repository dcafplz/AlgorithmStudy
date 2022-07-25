def solution(clothes):
    answer = 1
    clothes_dic = {x[1]:0 for x in clothes}
    for i in clothes:
        clothes_dic[i[1]] +=1
    for j in clothes_dic.values():
        answer *= (j+1)
    return answer - 1