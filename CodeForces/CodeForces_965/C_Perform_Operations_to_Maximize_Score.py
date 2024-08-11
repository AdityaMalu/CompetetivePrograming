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
        n, k = map(int, input().split())
        a = []
        aa = []
        ba = []

        aa = list(map(int, input().split()))
        ba = list(map(int, input().split()))
        for i in range(n):
            a.append([aa[i], ba[i]])
            
        a.sort()
        lo, hi, ans = 0, int(2e9), a[n - 1][0]
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            req = (n - 1) // 2 + 2
            rem = k
            for i in range(n - 1, -1, -1):
                if a[i][0] >= mid:
                    req -= 1
                elif a[i][1] == 1:
                    if mid - a[i][0] <= rem:
                        rem -= mid - a[i][0]
                        req -= 1
            if req <= 0:
                ans = max(ans, a[n - 1][0] + mid)
                lo = mid + 1
            else:
                hi = mid - 1
        
        j = -1
        for i in range(n - 1, -1, -1):
            if a[i][1] == 1:
                j = i
                break
        
        if j == -1:
            print(ans)
        else:
            if j <= n // 2 - 1:
                ans = max(ans, a[n // 2][0] + a[j][0] + k)
            else:
                ans = max(ans, a[n // 2 - 1][0] + a[j][0] + k)
            
            print(ans)

if __name__ == "__main__":
    main()