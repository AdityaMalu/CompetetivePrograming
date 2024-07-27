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
        n, x = map(int, input().split())
        count = 0
        for a in range(1, x - 1):
            for b in range(1, x - a):
                if a * b > n:
                    break
                max_c = min(x - a - b, (n - a * b) // (a + b))
                if max_c > 0:
                    count += max_c
        print(count)


if __name__ == "__main__":
    main()
