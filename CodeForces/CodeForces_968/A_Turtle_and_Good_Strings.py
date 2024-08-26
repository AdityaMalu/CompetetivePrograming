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
        if(n == 1):
            print("NO")
        else:
            if s[0] == s[-1]:
                print("NO")
            else:
                print("YES")

if __name__ == "__main__":
    main()