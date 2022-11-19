# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
n = int(sys.stdin.readline())
wmin, wmax, hmin, hmax = n, 0, n, 0
scars = [sys.stdin.readline().rstrip().split(' ') for _ in range(n)]
for idx1, scar in enumerate(scars):
	for idx2, s in enumerate(scar):
		if s == '1':
			wmin = min(wmin, idx2)
			wmax = max(wmax, idx2)
			hmin = min(hmin, idx1)
			hmax = max(hmax, idx1)
band = (wmax - wmin + 1) * (hmax - hmin + 1)
print(band if band >= 0 else 0)
