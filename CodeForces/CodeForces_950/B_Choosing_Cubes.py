# https://codeforces.com/contest/1980/problem/B

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
        n,f,k = map(int, input().split())
        arr = list(map(int, input().split()))
        fav = arr[f-1]
        arr.sort(reverse=True)

        if (n == 1) or (k == n) :
            print("YES")
            continue

        k = k-1
        f = f-1

        if arr[k] < fav:
            print("YES")
        elif arr[k] > fav:
            print("NO")
        else:
            if arr[k+1] < fav:
                print("YES")
            else:
                print("MAYBE")


if __name__ == "__main__":
    main()