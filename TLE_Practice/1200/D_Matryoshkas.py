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
        arr = list(map(int,input().split()))
        arr.sort()
        ans = 0
        dict1 = defaultdict(int)
        for i in arr:
            if len(dict1) == 0:
                dict1[i+1] = 1
            else:
                if dict1[i] > 0:
                    dict1[i] -= 1
                    dict1[i+1] += 1
                else:
                    dict1[i+1] += 1
        
        for i,j in dict1.items():
            if i > 0:
                ans += j
        print(ans)
            

if __name__ == "__main__":
    main()