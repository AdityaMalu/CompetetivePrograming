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
        p = list(map(int, input().split()))
        s = input().strip()
        
        visited = [False] * n
        F = [0] * n
        
        for i in range(n):
            if not visited[i]:
                cycle = []
                x = i
                while not visited[x]:
                    visited[x] = True
                    cycle.append(x)
                    x = p[x] - 1
                
                black_count = sum(1 for idx in cycle if s[idx] == '0')
                for idx in cycle:
                    F[idx] = black_count
        
        print(*F)
            
        

if __name__ == "__main__":
    main()

