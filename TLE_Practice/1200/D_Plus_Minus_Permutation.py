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
        n,a,b = map(int,input().split())
        cut = math.lcm(a,b)
        r1 = n//a - n//cut
        r2 = n//b - n//cut
        ans = 0
        total = n*(n+1)//2
        t1 = n-r1
        total1 = total - t1*(t1+1)//2
        total2 = r2*(r2+1)//2
        ans = total1-total2
        print(ans)


if __name__ == "__main__":
    main()