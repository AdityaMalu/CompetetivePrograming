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
        if (101 < n <= 109 or 1010 <= n <= 1099):
            print("YES")
        else:
            print("NO") 
        


if __name__ == "__main__":
    main()