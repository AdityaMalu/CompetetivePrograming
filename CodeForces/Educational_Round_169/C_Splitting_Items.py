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
        arr = list(map(int, input().split()))
        arr.sort(reverse=True)
        tp = 0
        for i in range(0, n - 1, 2):
            tp += (arr[i] - arr[i + 1])

        ans = 0
        if n % 2 == 1:
            ans += arr[-1]

        if tp < k:
            print(ans)
        else:
            tp2 = (tp - k)
            ans += tp2
            print(ans)

if __name__ == "__main__":
    main()
