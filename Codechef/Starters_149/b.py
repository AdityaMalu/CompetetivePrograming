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
        arr = list(map(int, input().split()))

        mini = float('inf')

        no = 0
        ans = 0

        for i in arr:
            mini = min(mini,abs(i))
            if i  < 0:
                no += 1
        
            ans += abs(i)
        
        if no%2 != 0:
            ans -= 2*mini
                
        print(ans)


if __name__ == "__main__":
    main()