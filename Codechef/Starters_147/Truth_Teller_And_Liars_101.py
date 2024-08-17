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
        t,l = map(int, input().split())
        if 2*l + 1 <= (l+t):
            print(2*l+1)
        else:
            print(-1)

if __name__ == "__main__":
    main()