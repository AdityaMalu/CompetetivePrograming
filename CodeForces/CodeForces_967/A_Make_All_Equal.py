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
        n = int(input())
        arr = list(map(int, input().split()))
        dict1 = dict()
        for i in range(n):
            if arr[i] in dict1:
                dict1[arr[i]] += 1
            else:
                dict1[arr[i]] = 1
        
        maxi = 0
        for i in dict1:
            maxi = max(maxi, dict1[i])

        print(n-maxi)

if __name__ == "__main__":
    main()