import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def can_form_subsequence(s, t):
    i, j = 0, 0
    s = list(s)  
    
    while i < len(s) and j < len(t):
        if s[i] == '?':
            s[i] = t[j]
            j += 1
        elif s[i] == t[j]:
            j += 1
        i += 1
    
    if j == len(t):
        s = ''.join(c if c != '?' else 'a' for c in s)
        return "YES", s
    else:
        return "NO", None
    
def main():
    t = int(input())
    for _ in range(t):
        s1 = list(input())
        s2 = list(input())
        bul,ans = can_form_subsequence(s1,s2)
        print(bul)
        if bul == "YES":
            print(ans)

          


if __name__ == "__main__":
    main()