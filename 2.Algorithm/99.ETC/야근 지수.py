# https://school.programmers.co.kr/learn/courses/30/lessons/12927
# heap을 사용한 풀이보다 시간복잡도가 더 나은것으로 판단됨
def solution(n, works):
    works_dict = {}
    m = 0
    for work in works:
        if m < work: m = work
        works_dict[work] = works_dict.get(work, 0) + 1
    for i in range(m, 0, -1):
        temp = works_dict.get(i, 0)
        if temp != 0:
            if temp < n:
                del(works_dict[i])
                works_dict[i-1] = works_dict.get(i-1, 0) + temp
                n -= temp
            else:
                works_dict[i] -= n
                works_dict[i-1] = works_dict.get(i-1, 0) + n
                return sum([(k ** 2 * works_dict[k]) for k in works_dict])
        print(works_dict, n)

print(solution(3, [1, 1]))