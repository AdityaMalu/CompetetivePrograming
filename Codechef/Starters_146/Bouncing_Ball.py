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
        
        pre_sum = [0] * (n + 1)
        suff_sum = [0] * (n + 1)
        ans = 0
        
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + arr[i - 1]
        
        for i in range(n - 1, -1, -1):
            suff_sum[i] = suff_sum[i + 1] + arr[i]
  
        for i in range(n):
            if arr[i] == 0:
                if abs(pre_sum[i] - suff_sum[i + 1]) == 1:
                    ans += 1
                if abs(pre_sum[i] - suff_sum[i + 1]) == 0:
                    ans += 2
        
        print(ans)

if __name__ == "__main__":
    main()
