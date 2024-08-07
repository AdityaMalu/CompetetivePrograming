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
        n, s, m = map(int, input().split())
        
        cnt = 0
        flag = False
        
        for _ in range(n):
            f, e = map(int, input().split())
            
            if (f - cnt) >= s:
                flag = True
            
            cnt = e
        
        if (m - cnt) >= s:
            flag = True
        
        if flag:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()