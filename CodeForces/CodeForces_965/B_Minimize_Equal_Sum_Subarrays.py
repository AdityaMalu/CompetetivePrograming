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
        p = list(map(int, input().split()))
        ans = []
        for i in range(n):
            ans.append(p[i]%n +1)
        print(*ans)

if __name__ == "__main__":
    main()