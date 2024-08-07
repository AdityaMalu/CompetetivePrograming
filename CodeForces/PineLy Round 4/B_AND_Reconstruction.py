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
        b = list(map(int, input().split()))
        a = [0]*(n)

        a[0] = b[0]

        for i in range(1,n-1):
            a[i] = b[i] | b[i-1]
        
        a[n-1] = b[n-2]

        for i in range(n-1):
            if a[i] & a[i+1] != b[i]:
                print(-1)
                break
        else:
            print(*a)

if __name__ == "__main__":
    main()