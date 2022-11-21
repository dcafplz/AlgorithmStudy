def solution(arr1, arr2):
    answer = []
    arr2 =  [[x[y] for x in arr2] for y in range(len(arr2[0]))]
    for i in range(len(arr1)):
        try:
            temp = []
            for j in range(len(arr2)):
                temp.append(sum([x*y for x,y in zip(arr1[i],arr2[j])]))
            answer.append(temp)
        except:
            print(i,j)
    return answer