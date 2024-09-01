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
        n, x, y = map(int, input().split())
        arr = list(map(int, input().split()))
        
        gcd_val = math.gcd(x, y)
        mod_vals = [(val % gcd_val) for val in arr]
        
        mod_vals.sort(reverse=True)
        ans = mod_vals[0] - mod_vals[-1]
        mod_vals.reverse()
        
        for i in range(1, n):
            if mod_vals[i] == mod_vals[i-1]:
                continue
            else:
                ans = min(ans, (gcd_val + mod_vals[i-1] - mod_vals[i]))
        
        print(ans)

if __name__ == "__main__":
    main()


