import sys
from collections import defaultdict, deque
from heapq import heappop, heappush

import math
import bisect
import itertools
import functools
import random

def main():
    n = int(input())
    ans = [-1]*(n+1)
    check = [False]*(n+1)
    mappy = defaultdict(list)
    for i in range(n,0,-1):
        if check[i]:
            continue
        dig = math.log2(i)+1
        maxi = (1<<int(dig))-1
        curr = i^maxi
        mappy[curr] = i
        mappy[i] = curr
        check[i] = True
        check[curr] = True

    for i in range(0,n+1):
        if check[i]:
            ans[i] = mappy[i]
        else:
            ans[0] = i
    print(n*(n+1))
    print(*ans)

if __name__ == "__main__":
    main()