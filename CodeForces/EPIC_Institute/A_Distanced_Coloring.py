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
        a,b,k =  map(int, input().split())
        if k*k < min(k*a,k*b,a*b):
            print(k*k)
        else:
            print(min(k*a,k*b,a*b))

if __name__ == "__main__":
    main()