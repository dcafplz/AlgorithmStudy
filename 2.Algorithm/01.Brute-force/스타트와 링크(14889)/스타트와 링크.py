# https://www.acmicpc.net/problem/14889

def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [array[i]] + next

n = int(input())
nord = [list(map(int, input().split())) for _ in range(n)]
sum = []
for idx,i in enumerate(combinations(list(range(n)),n//2)):
    sum.append(0)
    for j, k in combinations(i,2):
        sum[idx] += nord[j][k] + nord[k][j]
print(min([abs(sum[x]-sum[-x-1]) for x in range(len(sum)//2)]))