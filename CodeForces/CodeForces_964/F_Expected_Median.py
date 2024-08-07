import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random


MOD = 10**9 + 7

def pre(max_n, mod):
    fact = [1] * (max_n + 1)
    ifact = [1] * (max_n + 1)
    
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % mod
    
    ifact[max_n] = pow(fact[max_n], mod - 2, mod)
    for i in range(max_n - 1, 0, -1):
        ifact[i] = ifact[i + 1] * (i + 1) % mod
    
    return fact, ifact

def binomial_coefficient(n, k, fact, ifact, mod):
    if k > n or k < 0:
        return 0
    return fact[n] * ifact[k] % mod * ifact[n - k] % mod

def solve(t, tc):
    max_n = max(c[0][0] for c in tc)
    fact, ifact = pre(max_n, MOD)
    
    results = []
    for c in tc:
        n, k = c[0]
        a = c[1]
        cn1 = sum(a)
        cn0 = n - cn1

        mp = k // 2
        solve = 0

        for i in range(mp + 1, k + 1):
            if i > cn1:
                break
            solve += binomial_coefficient(cn1, i, fact, ifact, MOD) * binomial_coefficient(cn0, k - i, fact, ifact, MOD)
            solve %= MOD

        results.append(solve)
    
    return results

def main():
    t = int(input())
    tc = []
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        tc.append(((n, k), a))
    
    results = solve(t, tc)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
