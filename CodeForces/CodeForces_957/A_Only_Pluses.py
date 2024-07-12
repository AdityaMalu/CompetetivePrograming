#If input array is sorted then
#- Binary search
#- Two pointers

#If asked for all permutations/subsets then
#- Backtracking

#If given a tree then
#- DFS
#- BFS

#If given a graph then
#- DFS
#- BFS

#If given a linked list then
#- Two pointers

#If recursion is banned then
#- Stack

#If must solve in-place then
#- Swap corresponding values
#- Store one or more different values in the same pointer

#If asked for maximum/minimum subarray/subset/options then
#Dynamic programming

#If asked for top/least K items then
#- Heap
#- QuickSelect

#If asked for common strings then
#- Map

#Else
#- Map/Set for O(1) time & O(n) space
#- Sort input for O(nlogn) time and O(1) space
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
        a,b,c = map(int, input().strip().split())
        prev_a,prev_b,prev_c = a,b,c
        multi  = a*b*c
        for i in range(5):
            multi = max(multi,(a+1)*b*c,(b+1)*a*c,(c+1)*a*b)
            if multi == (a+1)*b*c:
                a += 1
            elif multi == (b+1)*a*c:
                b += 1
            elif multi == (c+1)*a*b:
                c += 1
        print(a*b*c)

        

if __name__ == "__main__":
    main()