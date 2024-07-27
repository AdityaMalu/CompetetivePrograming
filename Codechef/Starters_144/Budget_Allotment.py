
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
        n,x = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        count = 0
        ans = 0
        for i in range(n):
            if a[i]>=x:
                count+=a[i]-x
                ans+=1
        if count == 0:
            print(ans)
            continue
        for i in range(n):
            if a[i] < x:
                count  = count -(x-a[i])
                ans += 1
                if count == 0:
                    break
                elif count < 0:
                    ans-=1
        print(ans)
                    

if __name__ == "__main__":
    main()