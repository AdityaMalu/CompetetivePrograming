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
        a = list(map(int, input().split()))
        ans = 0
        for i in range(0,n,2):
            ans = max(ans,a[i])
        print(ans)

if __name__ == "__main__":
    main()