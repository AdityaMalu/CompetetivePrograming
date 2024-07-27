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
        ans = n//4
        n -= ans*4
        ans += n//2
        print(ans)
            
    

if __name__ == "__main__":
    main()