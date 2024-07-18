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
        n,m = map(int,input().split())
        matrix = []
        for i in range(n):
            matrix.append(list(map(int,input().split())))
        ans = []
        for i in range(n):
            ans.append([-1]*m)
       
        if n == 1 and m == 1:
            print(-1)
        else:
            for i in range(n):
                for j in range(m):
                    temp = (matrix[i][j] + n*m - 1) % (n*m)
                    if temp == 0:
                        temp = n*m
                    ans[i][j] = temp
     
            for i in range(n):
                print(*ans[i]) 
            


if __name__ == "__main__":
    main()