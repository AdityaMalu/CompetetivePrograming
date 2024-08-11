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
        x, y, k = map(int, input().split())
        if k % 2 == 1:
            print(x, y)
            k -= 1
        
        for i in range(k // 2):
            j = i + 1
            print(x - j, y - j)
            print(x + j, y + j)

if __name__ == "__main__":
    main()