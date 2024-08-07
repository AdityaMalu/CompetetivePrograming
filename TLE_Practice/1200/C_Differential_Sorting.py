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
    
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        
        if a[-2] > a[-1]:
            print("-1")
        elif a[-1] < 0:
            print("0" if a == sorted(a) else "-1")
        else:
            print(n - 2)
            for i in range(1, n - 1):
                print(i, n - 1, n)
              

if __name__ == "__main__":
    main()