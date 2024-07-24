import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def solve():
    n = int(input())
    str = input()
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = (str[i - 1] == '1')
    
    cost = [0] * (n + 1)
    for i in range(n, 0, -1):
        for j in range(i, n + 1, i):
            if a[j]:
                break
            cost[j] = i
    
    
    print(sum(cost))

def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()