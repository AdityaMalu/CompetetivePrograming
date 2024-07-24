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
        x = list(map(int, input().split()))
        y = list(map(int, input().split()))
        
        dif = [(y[i] - x[i], i) for i in range(n)]
        dif.sort(reverse=True)
        
        j = n - 1
        cnt = 0
        
        for i in range(n):
            while j > i and dif[i][0] + dif[j][0] < 0:
                j -= 1
            if j <= i:
                break
            cnt += 1
            j -= 1
        
        print(cnt)
                 


if __name__ == "__main__":
    main()