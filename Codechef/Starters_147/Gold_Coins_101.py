import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def main():
    # t = int(input())
    # for _ in range(t):
        a,b,x,y = map(int, input().split())
        if x > y:
            print(max(a,b))
        else:
            print(min(a,b))

if __name__ == "__main__":
    main()