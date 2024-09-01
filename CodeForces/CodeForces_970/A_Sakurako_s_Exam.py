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
        a, b = map(int,input().split())
        if (a == 0):
            print("YES") if b%2 ==0 else print("NO")
        elif (b == 0):
            print("YES") if a%2 ==0 else print("NO")
        else:
            print("YES") if (a+2*b)%2 ==0 else print("NO")

if __name__ == "__main__":
    main()