import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random


N = int(1e7) + 15
arr = [-1] * N


def pre_com():
    res = 0
    arr[0] = 0
    arr[1] = 1
    for i in range(2, N):
        if arr[i] == -1:
            res += 1
            if i == 2:
                res = 0
            if i == 3:
                res = 2
            for j in range(i, N, i):
                if arr[j] == -1:
                    arr[j] = res
        if arr[i] == -1:
            res += 1


def main():
    pre_com()
    t = int(input())
    for _ in range(t):
        n = int(input())
        v = list(map(int, input().split()))
        chc = 0
        for num in v:
            chc ^= arr[num]
        if chc == 0:
            print("Bob")
        else:
            print("Alice")

if __name__ == "__main__":
    main()
