# https://codeforces.com/contest/1980/problem/A

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
        n,m = map(int, input().split())
        s = input()
        ans = 0
        arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        dicta = defaultdict(int)
        for i in range(7):
            dicta[arr[i]] = 0
        for i in s:
            dicta[i] += 1
        for v in dicta.values():
            ans+=max(0,m-v)
        print(ans)
        


if __name__ == "__main__":
    main()