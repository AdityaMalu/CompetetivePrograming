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
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        if a == b or a == b[::-1]:
            print("Bob")
        else:
            print("Alice")

if __name__ == "__main__":
    main()