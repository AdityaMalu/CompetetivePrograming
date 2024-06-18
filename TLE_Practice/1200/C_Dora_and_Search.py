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
        n = int(input())
        arr = list(map(int, input().split()))
        l,r = 0,n-1
        mini,maxi = 1,n
        while l<r:
                if arr[l] == maxi:
                    l+=1
                    maxi-=1
                if arr[r] == maxi:
                    r-=1
                    maxi-=1
                if arr[l] == mini:
                    l+=1
                    mini+=1
                if arr[r] == mini:
                    r-=1
                    mini+=1
                if arr[l] != maxi and arr[l] != mini and arr[r] != maxi and arr[r] != mini:
                    break
        if (r-l)>1:
            print(l+1,r+1)
        else:
            print(-1)
            
if __name__ == "__main__":
    main()