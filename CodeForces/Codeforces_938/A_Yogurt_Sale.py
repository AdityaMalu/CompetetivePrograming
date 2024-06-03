# Link: https://codeforces.com/contest/1955/problem/A

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
        n,a,b = map(int, input().split())
        if a*2 <= b:
            print(n*a)
        else:
            print((n//2)*b + (n%2)*a)

if __name__ == "__main__":
    main()