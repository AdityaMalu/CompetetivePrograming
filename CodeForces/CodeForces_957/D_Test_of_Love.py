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
        n, m, k = map(int, input().split())
        a = input().strip()

        temp1 = m - 1
        temp2 = 0
        temp3 = 0
        
        for c in a:
            if c == 'W':
                temp2 += 0 if temp1 >= 1 else 1
            elif c == 'L':
                temp1 = m
            else:
                temp3 += 0 if temp1 >= 1 else 1
            temp1 -= 1
        
        temp3 += 1 if temp2 > k else 0
        if temp3 == 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
