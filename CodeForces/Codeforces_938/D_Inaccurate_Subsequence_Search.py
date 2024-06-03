# Link : https://codeforces.com/contest/1955/problem/D

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
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        dicta = defaultdict(int)
        dictb = defaultdict(int)
        
        for i in b:
            dictb[i] += 1
            
        for i in range(m):
            dicta[a[i]] += 1
            
        ans = 0
        c = 0
        
        for key in dictb:
            c += min(dicta[key], dictb[key])
            
        if c >= k:
            ans += 1
            
        for i in range(m, n):
            dicta[a[i - m]] -= 1
            if dictb[a[i - m]] > dicta[a[i - m]]:
                c -= 1
            dicta[a[i]] += 1
            if dictb[a[i]] >= dicta[a[i]]:
                c += 1
            if c >= k:
                ans += 1
                
        print(ans)


if __name__ == "__main__":
    main()