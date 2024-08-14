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
        points = []
        for _ in range(n):
            points.append(list(map(int, input().split())))
        x1, y1, x2, y2 = list(map(int, input().split()))
        s1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        s2 = 10 ** 20
        for i in range(0, n):
            s2 = min(s2, (points[i][0] - x2) ** 2 + (points[i][1] - y2) ** 2)
        if s1 < s2:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
