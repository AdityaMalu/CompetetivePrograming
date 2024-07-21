import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def main():
    n, k = map(int, input().split())
    if k == 1:
        print(n)
        return
    ans = 1
    while ans < n:
        ans = ans * 2 + 1
    print(ans)
       

if __name__ == "__main__":
    main()