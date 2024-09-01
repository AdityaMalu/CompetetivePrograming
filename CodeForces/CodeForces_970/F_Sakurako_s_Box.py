import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

MOD = 10**9 + 7

def mi(x, mod):
    return pow(x, mod - 2, mod)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        
        total = sum(arr) % MOD
        squ_sum = sum(x * x for x in arr) % MOD
        
        num = (total * total - squ_sum) % MOD
        den = (n * (n - 1)) % MOD
        
        print((num * mi(den, MOD)) % MOD)

if __name__ == "__main__":
    main()