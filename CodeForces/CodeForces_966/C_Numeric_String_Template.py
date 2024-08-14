import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        m = int(input())
        strings = [input().strip() for _ in range(m)]
        for s in strings:
            if len(s) != n:
                print("NO")
                continue
            
            mcn = {}
            mnc = {}
            match = True
            
            for i in range(n):
                c = s[i]
                num = a[i]
                
                if c in mcn:
                    if mcn[c] != num:
                        match = False
                        break
                else:
                    mcn[c] = num
                
                if num in mnc:
                    if mnc[num] != c:
                        match = False
                        break
                else:
                    mnc[num] = c
            
            if match:
                print("YES")
            else:
                print("NO")
        

if __name__ == "__main__":
    main()