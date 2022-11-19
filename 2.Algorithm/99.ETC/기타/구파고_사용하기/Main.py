# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
print(sorted(arr, key=lambda x: (len(x), x))[k-1])
