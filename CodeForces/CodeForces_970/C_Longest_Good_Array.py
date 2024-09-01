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
        l, r = map(int, input().split())
        diff = r - l
        print(int((1 + math.sqrt(1 + 8 * diff)) // 2))

if __name__ == "__main__":
    main()
