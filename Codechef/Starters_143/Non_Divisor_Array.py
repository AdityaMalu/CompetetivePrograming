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
        ans = []
        temp = n>>1
        num  =1
        while(n >0):
            for i in range(temp+1,n+1):
                ans.append(num)
            num+=1
            n = temp
            temp = n>>1
        print(ans[-1])
        print(*reversed(ans))
        


if __name__ == "__main__":
    main()