import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        if n % 2 == 0:
            print(-1)
            continue
        
        odd = n // 2 + 1
        even = n // 2
        ans = [-1] * n
        
        for i in range(n):
            if i % 2 == 0:
                ans[i] = odd
                odd += 1
            else:
                ans[i] = even
                even -= 1
        
        print(*ans)

if __name__ == "__main__":
    main()
