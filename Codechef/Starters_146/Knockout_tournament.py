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
        arr = list(map(int,input().split()))
        dict1 = {}
        for i in range(len(arr)):
            dict1[arr[i]] = i
        dict1 = dict(sorted(dict1.items()))
        
        ind = 1

        for i in dict1:
            if ind == 1:
                dict1[i] = 0
            elif ind > 1 and ind <= 3:
                dict1[i] = 1
            elif ind >3 and ind <=7:
                dict1[i] = 2
            elif ind >7 and ind <=15:
                dict1[i] = 3
            else:
                dict1[i] = 4
            ind += 1
        
        for i in arr:
            print(dict1[i],end=" ")
        print()



if __name__ == "__main__":
    main()