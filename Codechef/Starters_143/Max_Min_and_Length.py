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
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if max(arr[i:j])-min(arr[i:j]) == abs(j-i+1):
                    ans += 1
        print(ans)

if __name__ == "__main__":
    main()
