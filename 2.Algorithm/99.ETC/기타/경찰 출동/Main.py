# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from sys import stdin

dic = {}

for line in stdin:
	n, m = line.rstrip().split(' ')
	dic[m] = dic.get(m, 0) + 1
print(sum([min(2, dic[k]//2) for k, v in dic.items()]))

