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
        o,g,w = map(int, input().split())
        maxi = max(o,g,w)
        if maxi <= (o+g+w+1)//2:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()