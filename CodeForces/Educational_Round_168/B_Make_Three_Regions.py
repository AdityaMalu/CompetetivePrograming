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
        a = []
        for _ in range(2):
            a.append(list(input()))
        
        ans = 0
        i = 0
        if(n < 3):
            print(0)
            continue
        while(i < n-2):
            if a[0][i] == 'x' and a[0][i+1] == '.' and a[0][i+2] == 'x' and a[1][i] == '.' and a[1][i+1] == '.' and a[1][i+2] == '.':
                ans += 1
            elif a[0][i] == '.' and a[0][i+1] == '.' and a[0][i+2] == '.' and a[1][i] == 'x' and a[1][i+1] == '.' and a[1][i+2] == 'x':
                ans += 1
            i+=1
        print(ans)



if __name__ == "__main__":
    main()