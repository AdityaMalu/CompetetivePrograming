
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
        n  =int(input())
        a = list(map(int, input().split()))
        vis = set()
        valid = True
        for i in range(n):
            if i > 0:
                if not ((a[i] - 1 in vis) or (a[i] + 1 in vis)):
                    valid = False
                    break
            vis.add(a[i])
        
        if valid:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()

