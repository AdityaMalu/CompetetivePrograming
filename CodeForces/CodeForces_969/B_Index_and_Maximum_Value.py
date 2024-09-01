import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random


def main():
    T = int(input())
    ans = []
    
    for _ in range(T):
        n, q = map(int, input().split())
        
        a = list(map(int, input().split()))
        a.sort()
        maxi = a[-1]
        res = []
        
        for _ in range(q):
            c, l, r = input().split()
            l, r = int(l), int(r)
            
            if c == '+':
                if maxi >= l and maxi <= r:
                    maxi += 1
            else:
                if maxi >= l and maxi <= r:
                    maxi -= 1
            res.append(maxi)
        
        ans.append(res)
    
    for an in ans:
        print(*an)

if __name__ == "__main__":
    main()