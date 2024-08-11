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
        n, m = map(int, input().split())

        adj = [[] for _ in range(n + 1)]

        for __ in range(m):
            u, v = map(int, input().split())
            adj[u].append(v)
        
        time = [float('inf')] * (n + 1)
        time[1] = 0

        ans = ['1'] * (n - 1)
        j = 2

        for i in range(1, n):
            j = max(j, i + 1)
            time[i] = min(time[i], time[i - 1] + 1)

            for v in adj[i]:
                time[v] = min(time[v], time[i] + 1)
                while j < v - time[i] - 1:
                    ans[j - 1] = '0'
                    j += 1

        print(''.join(ans))

if __name__ == "__main__":
    main()
