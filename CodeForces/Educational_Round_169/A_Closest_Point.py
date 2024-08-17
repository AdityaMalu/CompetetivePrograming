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
        if n>2:
            print("NO")
        else:
            if abs(arr[0]-arr[1])>1:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()