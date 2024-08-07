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
        ans = 0
        while(n > 0):
            ans += n%10
            n = n//10
        print(ans)

if __name__ == "__main__":
    main()