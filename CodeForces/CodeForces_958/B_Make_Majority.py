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
        s = input()
        arr = list(s)
        for i in range(n):
            arr[i] = int(arr[i])
        new_arr = []
        zero = 0
        for i in range(n):
            if arr[i] == 0:
                zero += 1
            else:
                if zero > 0:
                    new_arr.append(0)
                    zero = 0
                new_arr.append(arr[i])
        if zero > 0:
            new_arr.append(0)
        if new_arr.count(0) >= new_arr.count(1):
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()