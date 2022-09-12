def solution(n, arr1, arr2):
    answer = [((" "*n)+str(bin(x | y)).replace("0"," ").replace("1", "#")[2:])[-n:] for x, y in zip(arr1,arr2)]
    return answer