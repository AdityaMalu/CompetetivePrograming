import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def count_wins(a1, a2, b1, b2):
    wins = 0
    mtc = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]
    
    for (sa1, sb1, sa2, sb2) in mtc:
        suw = 0
        slw = 0
        if sa1 > sb1:
            suw += 1
        elif sa1 < sb1:
            slw += 1
        
        if sa2 > sb2:
            suw += 1
        elif sa2 < sb2:
            slw += 1
        
        if suw > slw:
            wins += 1
    
    return wins

t = int(input().strip())
results = []
for _ in range(t):
    a1, a2, b1, b2 = map(int, input().strip().split())
    results.append(count_wins(a1, a2, b1, b2))

for result in results:
    print(result)

        