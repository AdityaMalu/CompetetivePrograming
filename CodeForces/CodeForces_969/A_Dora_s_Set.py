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
            o = 0
            e = 0
            if l % 2 and r % 2:
                o = (r - l) // 2 + 1
                e = (r - l) // 2
            elif l % 2 == 0 and r % 2 == 0:
                e = (r - l) // 2 + 1
                o = (r - l) // 2
            else:
                e = (r - l) // 2 + 1
                o = (r - l) // 2 + 1
            print(min(e, o // 2))

if __name__ == "__main__":
    main()


