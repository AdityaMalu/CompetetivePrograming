import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random


def main():
    T = int(input())
    for _ in range(T):
        n, x, y = map(int, input().split())
        s = input()
        
        ap = [(0, 0)]
        sx, sy = 0, 0
        
        for i in range(n):
            if s[i] == 'U':
                sy += 1
            elif s[i] == 'D':
                sy -= 1
            elif s[i] == 'L':
                sx -= 1
            elif s[i] == 'R':
                sx += 1
            ap.append((sx, sy))
        
        bw = False
        for i in range(len(ap)):
            t = abs(x - ap[i][0]) + abs(y - ap[i][1])
            if t == i:
                bw = True
                break
        
        print("YES" if bw else "NO")

if __name__ == "__main__":
    main()
