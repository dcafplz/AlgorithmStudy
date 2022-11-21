import sys

def dynamic(lst, i, n):
    if i + lst[i][0] < n:
        return max(lst[i][1] + dynamic(lst, i+lst[i][0], n), dynamic(lst, i+1, n))
    elif i + lst[i][0] == n:
        return max(lst[i][1], dynamic(lst, i+1, n) if i+1 < n else 0)
    elif i + 1 < n:
        return dynamic(lst, i+1, n)
    return 0

n = int(sys.stdin.readline())
lst = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
print(dynamic(lst, 0, n))