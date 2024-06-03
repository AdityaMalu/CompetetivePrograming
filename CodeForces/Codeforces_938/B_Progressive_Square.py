#Link : https://codeforces.com/contest/1955/problem/B

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
        n,c,d = map(int, input().split())
        arr = list(map(int, input().split()))
        a11 = min(arr)
        actual = []
        for i in range(n):
            for j in range(n):
                actual.append(a11 + c*i + d*j)       
        if (sorted(arr)==sorted(actual)):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()