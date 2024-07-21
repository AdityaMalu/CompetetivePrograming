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
        cnt_arr = set()
        for i in range(n):
            cnt_arr.add(arr.count(arr[i]))
   
        for i in cnt_arr:
            if i % 2 == 1:
                print("YES")
                break
        else:
            print("NO")     



if __name__ == "__main__":
    main()