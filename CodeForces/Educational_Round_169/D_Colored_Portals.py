import sys
from collections import defaultdict, deque
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right

import math
import bisect
import itertools
import functools
import random




def main():
    n, q = map(int, input().split())
    a = input().split()  
    
    vec = ["BG", "BR", "BY", "GR", "GY", "RY"]
    mp = [[] for _ in range(6)]
    
    for i, color in enumerate(a):
        for j, vec_color in enumerate(vec):
            if color == vec_color:
                mp[j].append(i)
                break
    
    for _ in range(q):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        
        stt = set(a[i] + a[j])
        if len(stt) < 4:
            print(abs(i - j))
            continue
        
        if j < i:
            i, j = j, i
        
        l, r = -1, n
        for k in range(6):
            if vec[k] == a[i] or vec[k] == a[j]:
                continue
            
            it = bisect_left(mp[k], i)
            if it > 0:
                l = max(l, mp[k][it - 1])
            
            it = bisect_right(mp[k], i)
            if it < len(mp[k]):
                r = min(r, mp[k][it])
        
        if l == -1 and r == n:
            print("-1")
        elif l == -1:
            print(abs(i - r) + abs(j - r))
        elif r == n:
            print(abs(i - l) + abs(j - l))
        else:
            ans = min(abs(i - l) + abs(j - l), abs(i - r) + abs(j - r))
            print(ans)


t = int(input())
for _ in range(t):
    main()