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
        arr = [0]*n 
        first_half  = n//2

        fir = []
        sec = []
        for i in range(1,first_half+1):
            fir.append(i)
        for i in range(first_half+1,n+1):
            sec.append(i)
        
        for i in range(n):
            if i%2 == 0:
                arr[i] = sec.pop()
            else:
                arr[i] = fir.pop()
        if n%2==0:
            for i in range(0,n,2):
                arr[i],arr[i+1] = arr[i+1],arr[i]
        print(*arr[::-1]) 

if __name__ == "__main__":
    main()